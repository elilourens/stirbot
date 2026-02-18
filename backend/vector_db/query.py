from urllib.parse import urldefrag
from .chroma_client import get_client


def _base_url(url):
    """Strip URL fragment to get the base page URL."""
    return urldefrag(url).url


def search_with_sources(query, n_results=5, diverse=True):
    """Search and return both the context string and a list of source dicts."""
    client = get_client()
    collection = client.get_or_create_collection("university_docs")

    fetch_count = n_results * 4 if diverse else n_results
    results = collection.query(query_texts=[query], n_results=fetch_count)

    context_parts = []
    sources = []
    seen_urls = set()

    for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
        base = _base_url(metadata['url'])

        if diverse and base in seen_urls:
            continue
        seen_urls.add(base)

        context_parts.append(f"Source: {metadata['url']}\n{doc}")
        sources.append({
            'url': metadata['url'],
            'title': metadata.get('title', ''),
            'snippet': doc[:200],
        })

        if len(context_parts) >= n_results:
            break

    context = "\n\n".join(context_parts)
    return context, sources


def search(query, n_results=5, diverse=True):
    """Search and return the context string (backwards-compatible)."""
    context, sources = search_with_sources(query, n_results, diverse)
    for s in sources:
        print(f"\nURL: {s['url']}")
        print(f"Text: {s['snippet']}...\n")
    return context

if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "undergraduate courses"
    search(query)
