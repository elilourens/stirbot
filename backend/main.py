from backend.webscrape import scraper
from backend.vector_db import load_data
from backend.vector_db import search
from backend.llm_interface import chat

CHUNK_SIZE = 1000
LLM_MODEL = "Mistral"


def scrape():
    """Scrape the entire Stir University website and save chunked data."""
    scraper.main(chunk_size=CHUNK_SIZE)


def ingest():
    """Load scraped data into ChromaDB."""
    load_data("chunked_data.json")

def chatbot():
    system_prompt = "You are a helpful chatbot that returns relevant appropriate answers for people interested in knowing more about stirling university." \
    " Give Citations about where you got your answers from."

    print("Stirling University Chatbot (type 'exit' to quit)")
    print("-" * 50)

    while True:
        user_query = input("\nYour question: ")

        if user_query.lower() in ['exit', 'quit', 'q']:
            print("Exited")
            break

        if not user_query.strip():
            continue

        context = search(user_query)
        response = chat(user_query, context, LLM_MODEL, system_prompt) 
        print(response)



if __name__ == "__main__":
    #scrape()
    #ingest()
    #search("Library Opening times ")
    chatbot()