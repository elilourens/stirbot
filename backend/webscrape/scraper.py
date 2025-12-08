import httpx
from bs4 import BeautifulSoup
import html5lib
from urllib.parse import urljoin
import time


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


if __name__ == "__main__":
    # Example usage
    with WebScraper() as scraper:
        
        
        found_urls = {"https://www.stir.ac.uk/"}
        urls_to_visit = ["https://www.stir.ac.uk/"]

        


        while(urls_to_visit):
            current_url = urls_to_visit.pop(0)
            print(f"\nVisiting: {current_url}")
            soup = scraper.scrape(current_url)
            if soup:
                links = soup.find_all('a', href=True)
                for link in links:
                    
                    absolute_url = urljoin(current_url, link['href'])

                    if absolute_url not in found_urls and absolute_url.startswith('https://www.stir.ac.uk'):
                        found_urls.add(absolute_url)
                        urls_to_visit.append(absolute_url)
            time.sleep(1)







        print(f"\nFound {len(found_urls)} links:")
