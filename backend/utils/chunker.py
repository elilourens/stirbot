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
        url = page.get('url', '')
        accordions = page.get('accordions', [])

        # Add regular text chunks
        chunks = chunk_text(text, chunk_size)
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                'url': url,
                'title': title,
                'chunk_index': i,
                'text': f"{title}\n{chunk}" if title else chunk
            })

        # Add accordion sections as separate chunks
        for j, accordion in enumerate(accordions, start=len(chunks)):
            accordion_text = f"{accordion['title']}\n\n{accordion['text']}"
            all_chunks.append({
                'url': url,
                'title': title,
                'chunk_index': j,
                'text': f"{title}\n\n{accordion_text}" if title else accordion_text
            })

    return all_chunks
