"""RAG evaluation using RAGAS and Ollama."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from ragas.llms.base import BaseRagasLLM, LLMResult
from ragas.embeddings.base import Embeddings
from datasets import Dataset
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.outputs import Generation
from sentence_transformers import SentenceTransformer
from vector_db import search
from llm_interface import chat
from .test_data import get_test_dataset

## RAG Evaluation Script thingy RAGAS + Ollama + Sentence Transformers


class OllamaRagasLLM(BaseRagasLLM):
    """Wrapper to make ChatOllama compatible with RAGAS."""

    def __init__(self, model_name: str = "mistral"):
        super().__init__()
        self.llm = ChatOllama(model=model_name, temperature=0, timeout=30.0)

    def generate_text(self, prompt, **kwargs) -> LLMResult:
        """Generate text using Ollama."""
        # Handle StringPromptValue objects from RAGAS
        if hasattr(prompt, 'text'):
            prompt_text = prompt.text
        else:
            prompt_text = str(prompt)

        messages = [HumanMessage(content=prompt_text)]
        response = self.llm.invoke(messages)
        return LLMResult(generations=[[Generation(text=response.content)]])

    async def agenerate_text(self, prompt, **kwargs) -> LLMResult:
        """Async generate text using Ollama."""
        return self.generate_text(prompt, **kwargs)

    def is_finished(self, response):
        """Check if generation is finished."""
        return True


class SentenceTransformerEmbeddings(Embeddings):
    """Embeddings using sentence-transformers."""
    ##
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        super().__init__()
        self.model = SentenceTransformer(model_name)

    def embed_query(self, text: str):
        
        return self.model.encode(text, convert_to_numpy=True)

    def embed_documents(self, documents: list):
       
        return self.model.encode(documents, convert_to_numpy=True)

def get_rag_response(question: str, n_results: int = 5):
    """
    Get RAG response from the chatbot.
    ##
    Returns:
        tuple: (answer, context_list)
    """
    try:
        context = search(question, n_results=n_results)
        system_prompt = (
            "You are a helpful chatbot that returns relevant appropriate answers "
            "for people interested in knowing more about Stirling University. "
            "Give Citations about where you got your answers from."
        )
        response = chat(question, context, "Mistral", system_prompt)
        return response, context
    except Exception as e:
        print(f"Error getting response for '{question}': {e}")
        return "", ""

def run_evaluation():
    """Run RAGAS evaluation on the test dataset."""
    print("=" * 60)
    print("RAG Evaluation - Stirling University Chatbot")
    print("=" * 60)
    ##
    print("\nLoading test dataset...")
    test_dataset = get_test_dataset()
    print(f"Loaded {len(test_dataset)} questions\n")

    print("Generating RAG responses...")
    results = {
        "question": [],
        "answer": [],
        "contexts": [],
        "ground_truth": []
    }
    #
    for idx, (question, ground_truth) in enumerate(
        zip(test_dataset["question"], test_dataset["ground_truth"]), 1
    ):
        print(f"  [{idx}/{len(test_dataset)}] {question[:40]}...")
        answer, context = get_rag_response(question)

        results["question"].append(question)
        results["answer"].append(answer)
        results["contexts"].append([context])
        results["ground_truth"].append(ground_truth)

    eval_dataset = Dataset.from_dict(results)

    print("\nRunning evaluation metrics...")
    ollama_llm = OllamaRagasLLM(model_name="mistral")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    ragas_results = evaluate(
        eval_dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
        ],
        llm=ollama_llm,
        embeddings=embeddings,
    )

    # Display results
    print("\n" + "=" * 60)
    print("EVALUATION RESULTS")
    print("=" * 60)

    # Handle both scalar and list results from RAGAS
    def get_scalar_score(value):
        """Extract scalar from value, handling lists and numpy arrays."""
        if isinstance(value, list):
            return sum(value) / len(value) if value else 0
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    metrics = {
        "Faithfulness": get_scalar_score(ragas_results["faithfulness"]),
        "Answer Relevancy": get_scalar_score(ragas_results["answer_relevancy"]),
    }

    for metric_name, score in metrics.items():
        percentage = score * 100
        print(f"{metric_name:20s}: {score:.4f} ({percentage:.2f}%)")

    # Calculate overall score
    overall_score = sum(metrics.values()) / len(metrics)
    print("-" * 60)
    print(f"{'Overall Score':20s}: {overall_score:.4f} ({overall_score*100:.2f}%)")
    print("=" * 60)

    # Save results
    results_dir = Path(__file__).parent / "results"
    results_dir.mkdir(exist_ok=True)

    import json
    details = {
        "metrics_summary": metrics,
        "overall_score": overall_score,
        "test_cases": [
            {"question": q, "answer": a, "ground_truth": gt}
            for q, a, gt in zip(
                results["question"],
                results["answer"],
                results["ground_truth"]
            )
        ]
    }
    json_path = results_dir / "results.json"
    with open(json_path, "w") as f:
        json.dump(details, f, indent=2)
    print(f"\nResults saved to: {json_path}")

    print("\nMetrics:")
    print("  Faithfulness: answers grounded in context (higher = better)")
    print("  Answer Relevancy: answers address the question (higher = better)")

    return ragas_results

if __name__ == "__main__":
    run_evaluation()
