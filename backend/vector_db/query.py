from urllib.parse import urldefrag
from .chroma_client import get_client


def _base_url(url):
    """Strip URL fragment to get the base page URL."""
    return urldefrag(url).url


def search_with_sources(query, n_results=5, diversified=5):
    """
    Search and return both the context string and a list of source dicts.

    Args:
        query: search query
        n_results: number of top-K relevant results (can be from same page)
        diversified: number of additional diverse results from different pages

    Returns:
        (context_str, sources_list)
    """
    client = get_client()
    collection = client.get_or_create_collection("university_docs")

    context_parts = []
    sources = []
    seen_urls = set()

    # Step 1: Get top n_results without diversity constraint
    top_results = collection.query(query_texts=[query], n_results=n_results)

    for doc, metadata in zip(top_results['documents'][0], top_results['metadatas'][0]):
        context_parts.append(f"Source: {metadata['url']}\n{doc}")
        sources.append({
            'url': metadata['url'],
            'title': metadata.get('title', ''),
            'snippet': doc,
        })
        seen_urls.add(_base_url(metadata['url']))

    # Step 2: Get diversified results from different pages
    if diversified > 0:
        # Fetch enough to get diversified unique pages
        fetch_count = diversified * 4
        diverse_results = collection.query(query_texts=[query], n_results=fetch_count)

        for doc, metadata in zip(diverse_results['documents'][0], diverse_results['metadatas'][0]):
            base = _base_url(metadata['url'])

            # Skip if we've already included this page
            if base in seen_urls:
                continue

            context_parts.append(f"Source: {metadata['url']}\n{doc}")
            sources.append({
                'url': metadata['url'],
                'title': metadata.get('title', ''),
                'snippet': doc,
            })
            seen_urls.add(base)

            if len(sources) - n_results >= diversified:
                break

    context = "\n\n".join(context_parts)
    return context, sources


def search(query, n_results=5, diversified=5):
    """Search and return the context string (backwards-compatible)."""
    context, sources = search_with_sources(query, n_results, diversified)
    for s in sources:
        print(f"\nURL: {s['url']}")
        print(f"Text: {s['snippet']}...\n")
    return context

if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "undergraduate courses"
    search(query)
