import httpx
import asyncio
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag
import time
import json

from utils.chunker import chunk_scraped_data


class WebScraper:
    def __init__(self, timeout=30.0):
        self.client = httpx.AsyncClient(timeout=timeout, follow_redirects=True)

    async def fetch_page(self, url):
        """Fetch HTML content from a URL."""
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.text
        except httpx.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def parse_html(self, html_content):
        """Parse HTML content using BeautifulSoup."""
        if html_content:
            return BeautifulSoup(html_content, 'lxml')
        return None

    def extract_accordion_sections(self, soup):
        """Extract accordion sections from a page."""
        accordions = []
        accordion_containers = soup.find_all('div', {'data-behaviour': 'accordion'})

        for container in accordion_containers:
            title = None
            content_div = None

            # Pattern 1: Button with role='region' (nested accordions)
            button = container.find('button', class_='stir-accordion--btn')
            if button:
                title = button.get_text(strip=True)
                content_div = button.find_parent().find_next('div', role='region')

            # Pattern 2: H3 title with c-wysiwyg-content (top-level accordions)
            if not title:
                h3 = container.find('h3')
                if h3:
                    title = h3.get_text(strip=True)
                    content_div = container.find('div', class_='c-wysiwyg-content')

            if title and content_div:
                text = re.sub(r'\s+', ' ', content_div.get_text(separator=' ', strip=True)).strip()
                if text:
                    accordions.append({
                        'title': title,
                        'text': text
                    })

        return accordions

    async def scrape(self, url):
        """Main scraping method: fetch and parse a URL."""
        html_content = await self.fetch_page(url)
        return self.parse_html(html_content)

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


async def process_url(scraper, url, semaphore, excluded_patterns, found_urls):
    """Process a single URL with semaphore-based rate limiting."""
    async with semaphore:
        # skip if URL matches excluded patterns
        if any(pattern in url for pattern in excluded_patterns):
            return None, []

        soup = await scraper.scrape(url)
        if soup:
            # Remove scripts/styles
            for script in soup(['script', 'style']):
                script.decompose()

            # Remove navigation, header, and footer boilerplate
            for element in soup.find_all(['nav', 'header', 'footer']):
                element.decompose()
            # Remove common boilerplate by role attributes
            for element in soup.find_all(attrs={'role': ['navigation', 'banner', 'contentinfo']}):
                element.decompose()
            # Remove skip-to-content links
            for element in soup.find_all('a', string=lambda s: s and 'skip to' in s.lower()):
                element.decompose()

            # Extract page data
            page_title = soup.find('title').get_text() if soup.find('title') else ''
            page_data = {
                'url': url,
                'title': page_title,
                'text': re.sub(r'\s+', ' ', soup.get_text(separator=' ', strip=True)).strip(),
                'headings': [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])],
                'accordions': scraper.extract_accordion_sections(soup)
            }

            # Extract links
            links = soup.find_all('a', href=True)
            new_urls = []
            for link in links:
                absolute_url = urldefrag(urljoin(url, link['href'])).url

                # Apply same filtering logic
                if absolute_url in found_urls:
                    continue
                if not absolute_url.startswith('https://www.stir.ac.uk'):
                    continue
                if any(pattern in absolute_url for pattern in excluded_patterns):
                    continue

                new_urls.append(absolute_url)

            return page_data, new_urls
        return None, []


async def main(chunk_size=1000, max_concurrent=10):
    start_time = time.time()

    excluded_patterns = [
        '/research/hub',
        '/news',
        # exclude binary/media files
        '.pdf',
        '.docx',
        '.doc',
        '.xlsx',
        '.xls',
        '.jpg',
        '.jpeg',
        '.png',
        '.gif',
        '.zip',
        '.mp4',
        '.mp3',
        '.exe',
    ]

    semaphore = asyncio.Semaphore(max_concurrent)
    active_tasks = {}

    async with WebScraper() as scraper:
        found_urls = {"https://www.stir.ac.uk/", "https://www.stir.ac.uk/sitemap/"}
        urls_to_visit = ["https://www.stir.ac.uk/", "https://www.stir.ac.uk/sitemap/"]
        scraped_data = []

        while urls_to_visit or active_tasks:
            # Launch new tasks up to limit
            while urls_to_visit and len(active_tasks) < max_concurrent:
                url = urls_to_visit.pop(0)
                print(f"\nLaunching task for: {url}")
                task = asyncio.create_task(process_url(scraper, url, semaphore, excluded_patterns, found_urls))
                active_tasks[task] = url

            # Wait for task completion
            if active_tasks:
                done, _ = await asyncio.wait(
                    active_tasks.keys(),
                    return_when=asyncio.FIRST_COMPLETED
                )

                # Process results
                for task in done:
                    try:
                        page_data, new_urls = await task
                        if page_data:
                            print(f"\nCompleted: {page_data['url']}")
                            scraped_data.append(page_data)

                        # Add new URLs to queue
                        for new_url in new_urls:
                            if new_url not in found_urls:
                                found_urls.add(new_url)
                                urls_to_visit.append(new_url)
                    except Exception as e:
                        print(f"Error processing task: {e}")

                    del active_tasks[task]

        chunked_data = chunk_scraped_data(scraped_data, chunk_size=chunk_size)
        """
        with open("scraped_data.json", "w", encoding="utf-8") as f:
            json.dump(scraped_data, f, indent=2, ensure_ascii=False)
        """
        with open("chunked_data.json", "w", encoding="utf-8") as f:
            json.dump(chunked_data, f, indent=2, ensure_ascii=False)

    elapsed_time = time.time() - start_time
    print(f"\nScraping complete.")
    print(f"Total pages visited: {len(scraped_data)}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
        
