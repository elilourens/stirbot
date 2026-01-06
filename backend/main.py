from backend.webscrape import scraper
from backend.vector_db import load_data
from backend.vector_db import search

CHUNK_SIZE = 1000


def scrape():
    """Scrape the entire Stir University website and save chunked data."""
    scraper.main(chunk_size=CHUNK_SIZE)


def ingest():
    """Load scraped data into ChromaDB."""
    load_data("chunked_data.json")


if __name__ == "__main__":
    #scrape()
    #ingest()
    search("Library Opening times ")
