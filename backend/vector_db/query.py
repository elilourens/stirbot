from .chroma_client import get_client

def search(query, n_results=5):
    client = get_client()
    collection = client.get_or_create_collection("university_docs")
    results = collection.query(query_texts=[query], n_results=n_results)

    for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
        print(f"\nURL: {metadata['url']}")
        print(f"Text: {doc[:200]}...\n")

    return results

if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "undergraduate courses"
    search(query)
