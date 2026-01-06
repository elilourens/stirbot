import json
from tqdm import tqdm
from .chroma_client import get_client

def load_data(json_file="chunked_data.json", batch_size=5000):
    client = get_client()

    # Delete existing collection
    try:
        client.delete_collection("university_docs")
        print(" Wiped existing collection")
    except:
        pass

    # Create fresh collection
    collection = client.get_or_create_collection("university_docs")

    with open(json_file, 'r', encoding='utf-8') as f:
        chunks = json.load(f)

    documents = [chunk['text'] for chunk in chunks]
    metadatas = [{'url': chunk['url'], 'title': chunk['title']} for chunk in chunks]
    ids = [f"{chunk['url']}_{chunk['chunk_index']}" for chunk in chunks]

    # Add in batches with progress bar
    total = len(documents)
    batches = range(0, total, batch_size)

    for i in tqdm(batches, desc="Loading vectors", unit="batch"):
        batch_end = min(i + batch_size, total)
        collection.add(
            documents=documents[i:batch_end],
            metadatas=metadatas[i:batch_end],
            ids=ids[i:batch_end]
        )

    total_vectors = collection.count()
    print(f" Created {total} vectors")
    print(f" Collection: '{collection.name}' now contains {total_vectors} total vectors")

if __name__ == "__main__":
    load_data()
