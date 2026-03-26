import ollama
import time

models = ["qwen3.5:0.8b", "qwen3.5:4b", "mistral"]
prompt = "Explain the difference between RAM and a hard drive in detail."
runs = 3

for model in models:
    times = []
    tokens = []
    print(f"\nTesting {model}...")
    for i in range(runs):
        start = time.time()
        response = ollama.generate(model=model, prompt=prompt)
        elapsed = time.time() - start
        tok = response["eval_count"]
        times.append(elapsed)
        tokens.append(tok / elapsed)
        print(f"  Run {i+1}: {elapsed:.2f}s — {tok/elapsed:.1f} tokens/sec")

    print(f"  Average: {sum(tokens)/len(tokens):.1f} tokens/sec")
