import os
import ijson
import time
from tqdm import tqdm

# Enable GPU for embeddings
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from .chroma_client import get_client, get_embedding_function

def load_data(json_file="chunked_data.json", batch_size=5000):
    start_time = time.time()
    client = get_client()
    embedding_fn = get_embedding_function()

    # Delete existing collection
    try:
        client.delete_collection("university_docs")
        print(" Wiped existing collection")
    except:
        pass

    # Create fresh collection with GPU embedding function
    collection = client.get_or_create_collection("university_docs", embedding_function=embedding_fn)

    # Count total chunks first for progress bar
    print(" Counting chunks...")
    total_count = 0
    with open(json_file, 'rb') as f:
        for _ in ijson.items(f, 'item'):
            total_count += 1

    # Stream chunks from JSON file instead of loading entire file into memory
    documents = []
    metadatas = []
    ids = []
    total_chunks = 0
    batch_count = 0

    with open(json_file, 'rb') as f:
        pbar = tqdm(ijson.items(f, 'item'), total=total_count, desc="Loading chunks", unit="chunk")
        for chunk in pbar:
            documents.append(chunk['text'])
            metadatas.append({'url': chunk['url'], 'title': chunk['title']})
            ids.append(f"{chunk['url']}_{chunk['chunk_index']}")
            total_chunks += 1

            # Add batch when we reach batch_size
            if len(documents) >= batch_size:
                collection.add(
                    documents=documents,
                    metadatas=metadatas,
                    ids=ids
                )
                batch_count += 1
                pbar.set_postfix({'batches': batch_count})
                documents = []
                metadatas = []
                ids = []

    # Add remaining chunks
    if documents:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        batch_count += 1

    total_vectors = collection.count()
    elapsed_time = time.time() - start_time
    print(f"\n Created {total_chunks} vectors in {batch_count} batches")
    print(f" Collection: '{collection.name}' now contains {total_vectors} total vectors")
    print(f" Total ingestion time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    load_data()
