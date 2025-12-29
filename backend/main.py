from backend.webscrape import scraper

CHUNK_SIZE = 1000


def scrape():
    """Scrape the entire Stir University website and save chunked data."""
    scraper.main(chunk_size=CHUNK_SIZE)


if __name__ == "__main__":
    scrape()
