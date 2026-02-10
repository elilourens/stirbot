from urllib.parse import urldefrag
from .chroma_client import get_client


def _base_url(url):
    """Strip URL fragment to get the base page URL."""
    return urldefrag(url).url


def search(query, n_results=5, diverse=True):
    client = get_client()
    collection = client.get_or_create_collection("university_docs")

    # Over-fetch when enforcing diversity so we have enough unique pages
    fetch_count = n_results * 4 if diverse else n_results
    results = collection.query(query_texts=[query], n_results=fetch_count)

    context_parts = []
    seen_urls = set()

    for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
        base = _base_url(metadata['url'])

        if diverse and base in seen_urls:
            continue
        seen_urls.add(base)

        print(f"\nURL: {metadata['url']}")
        print(f"Text: {doc[:200]}...\n")
        context_parts.append(f"Source: {metadata['url']}\n{doc}")

        if len(context_parts) >= n_results:
            break

    return "\n\n".join(context_parts)

if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "undergraduate courses"
    search(query)
