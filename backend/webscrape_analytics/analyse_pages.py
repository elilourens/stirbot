#!/usr/bin/env python3
"""Simple analytics for chunked_data.json - streaming version for large files"""

import ijson
from collections import Counter
from urllib.parse import urlparse
import matplotlib.pyplot as plt

def main():
    # Stream data and collect stats
    urls = set()
    chunk_count = 0

    print("Streaming through chunked_data.json (this may take a while for large files)...")

    # ============================================================================
    # AI GENERATED CODE
    # Model: Claude Opus 4.5 (claude-opus-4-5-20251101)
    # Prompt: "The file is 20GB and getting killed when loading. Use ijson to
    #          stream the JSON file instead of loading it all at once."
    # ============================================================================
    with open('../chunked_data.json', 'rb') as f:
        for item in ijson.items(f, 'item'):
            chunk_count += 1
            urls.add(item['url'])
            if chunk_count % 100000 == 0:
                print(f"  Processed {chunk_count:,} chunks...")
    # ============================================================================

    print(f"  Done! Processing {len(urls):,} unique URLs...")

    # Count directories
    directories = Counter()
    subdirectories = {}

    for url in urls:
        path = urlparse(url).path.strip('/')
        parts = path.split('/') if path else []

        top_dir = '/' + parts[0] if parts else '/'
        directories[top_dir] += 1

        # Track subdirectories
        if len(parts) >= 2:
            sub_dir = '/' + '/'.join(parts[:2])
            if top_dir not in subdirectories:
                subdirectories[top_dir] = Counter()
            subdirectories[top_dir][sub_dir] += 1

    # Print stats
    print(f"\nTotal chunks: {chunk_count:,}")
    print(f"Unique pages: {len(urls):,}")
    print(f"Avg chunks/page: {chunk_count / len(urls):.1f}")
    print(f"\nTop 10 directories:")
    for dir_path, count in directories.most_common(10):
        print(f"  {dir_path:<25} {count:>5} pages")

    # Create figure with 2 charts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Chart 1: Top 10 directories
    top_10 = directories.most_common(10)
    dirs = [d[0] for d in top_10]
    counts = [d[1] for d in top_10]
    ax1.barh(dirs[::-1], counts[::-1], color='steelblue')
    ax1.set_xlabel('Number of Pages')
    ax1.set_title('Top 10 Directories')

    # Chart 2: Subdirectories of top 3 directories
    top_3 = directories.most_common(3)
    colors = ['#e74c3c', '#3498db', '#2ecc71']
    y_labels = []
    y_values = []
    y_colors = []

    for i, (top_dir, _) in enumerate(top_3):
        if top_dir in subdirectories:
            for sub_dir, count in subdirectories[top_dir].most_common(5):
                label = sub_dir.replace(top_dir, '').strip('/')
                y_labels.append(f"{top_dir}: {label}")
                y_values.append(count)
                y_colors.append(colors[i])

    ax2.barh(y_labels[::-1], y_values[::-1], color=y_colors[::-1])
    ax2.set_xlabel('Number of Pages')
    ax2.set_title('Top Subdirectories (of 3 largest directories)')

    plt.tight_layout()
    plt.savefig('page_analytics.png', dpi=100)
    print(f"\nChart saved to: page_analytics.png")

if __name__ == '__main__':
    main()
