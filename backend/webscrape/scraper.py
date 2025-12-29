import httpx
from bs4 import BeautifulSoup
import html5lib
from urllib.parse import urljoin
import time
import json

from backend.utils.chunker import chunk_scraped_data


class WebScraper:
    def __init__(self, timeout=30.0):
        self.client = httpx.Client(timeout=timeout, follow_redirects=True)

    def fetch_page(self, url):
        """Fetch HTML content from a URL."""
        try:
            response = self.client.get(url)
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
            return BeautifulSoup(html_content, 'html5lib')
        return None

    def scrape(self, url):
        """Main scraping method: fetch and parse a URL."""
        html_content = self.fetch_page(url)
        return self.parse_html(html_content)

    def close(self):
        """Close the HTTP client."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def main(chunk_size=1000):
    with WebScraper() as scraper:
        found_urls = {"https://www.stir.ac.uk/"}
        urls_to_visit = ["https://www.stir.ac.uk/"]
        scraped_data = []

        while urls_to_visit:
            current_url = urls_to_visit.pop(0)
            print(f"\nVisiting: {current_url}")
            soup = scraper.scrape(current_url)
            if soup:
                links = soup.find_all('a', href=True)

                for script in soup(['script', 'style']):
                    script.decompose()

                page_data = {
                    'url': current_url,
                    'title': soup.find('title').get_text() if soup.find('title') else '',
                    'text': soup.get_text(separator=' ', strip=True),
                    'headings': [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
                }
                scraped_data.append(page_data)

                for link in links:
                    absolute_url = urljoin(current_url, link['href'])

                    if absolute_url not in found_urls and absolute_url.startswith('https://www.stir.ac.uk'):
                        if absolute_url.startswith(('https://www.stir.ac.uk/research', 'https://www.stir.ac.uk/media','https://www.stir.ac.uk/people','https://www.stir.ac.uk/news','https://www.stir.ac.uk/about/our-people','https://www.stir.ac.uk/student-stories','https://www.stir.ac.uk/about/professional-services','https://www.stir.ac.uk/about/university-collections','https://www.stir.ac.uk/staff-profiles','https://www.stir.ac.uk/events/','https://www.stir.ac.uk/scholarships','https://www.stir.ac.uk/expert')):
                            continue
                        if 'our-research' in absolute_url or 'research-groups' in absolute_url:
                            continue
                        found_urls.add(absolute_url)
                        urls_to_visit.append(absolute_url)

        chunked_data = chunk_scraped_data(scraped_data, chunk_size=chunk_size)
        """
        with open("scraped_data.json", "w", encoding="utf-8") as f:
            json.dump(scraped_data, f, indent=2, ensure_ascii=False)
        """
        with open("chunked_data.json", "w", encoding="utf-8") as f:
            json.dump(chunked_data, f, indent=2, ensure_ascii=False)

        #print(f"\nFound {len(found_urls)} links:")
        #print(f"Scraped {len(scraped_data)} pages")
        #print(f"Created {len(chunked_data)} chunks")


if __name__ == "__main__":
    main()
        
