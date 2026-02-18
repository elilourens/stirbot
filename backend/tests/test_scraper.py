import asyncio
import sys
import os
from datetime import datetime

# need to add parent dir to path so imports work
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from webscrape.scraper import WebScraper


async def test_url_extraction(url):
    """Test scraper on a specific URL and output results to file."""
    async with WebScraper() as scraper:
        print(f"Scraping: {url}")
        soup = await scraper.scrape(url)

        if not soup:
            print("Failed to fetch URL")
            return

        # Remove junk like scripts, styles, nav etc
        for script in soup(['script', 'style']):
            script.decompose()
        for element in soup.find_all(['nav', 'header', 'footer']):
            element.decompose()
        for element in soup.find_all(attrs={'role': ['navigation', 'banner', 'contentinfo']}):
            element.decompose()

        # get page data
        page_title = soup.find('title').get_text() if soup.find('title') else ''
        page_text = soup.get_text(separator=' ', strip=True)
        accordions = scraper.extract_accordion_sections(soup)

        # make output string with all the results
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = f"""
================================================================================
SCRAPER TEST RESULTS
================================================================================
Time: {timestamp}
URL: {url}
Title: {page_title}

================================================================================
PAGE TEXT
================================================================================
{page_text}

================================================================================
ACCORDIONS ({len(accordions)} found)
================================================================================
"""

        # add all the accordion sections to output
        for i, accordion in enumerate(accordions, 1):
            output += f"\n--- {i}. {accordion['title']} ---\n"
            output += accordion['text']
            output += "\n"

        # save it to a file with timestamp
        filename = f"test_extraction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(output)

        # tell user what happened
        print(f"\n✓ saved to: {filename}")
        print(f"✓ page: {page_title}")
        print(f"✓ found {len(accordions)} accordions:")
        for accordion in accordions:
            print(f"   {accordion['title']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_scraper.py <url>")
        print("Example: python test_scraper.py https://www.stir.ac.uk/courses/ug/accountancy/")
        print("\nthis script tests the scraper on a single page and outputs all the extracted text")
        sys.exit(1)

    url = sys.argv[1]
    asyncio.run(test_url_extraction(url))
