def chunk_text(text, size=1000):
    chunks = []
    for i in range(0, len(text), size):
        chunks.append(text[i:i + size])
    return chunks


def chunk_scraped_data(scraped_data, chunk_size=1000):
    all_chunks = []
    for page in scraped_data:
        title = page.get('title', '')
        text = page.get('text', '')
        chunks = chunk_text(text, chunk_size)
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                'url': page.get('url', ''),
                'title': title,
                'chunk_index': i,
                'text': f"{title}\n{chunk}" if title else chunk
            })
    return all_chunks
