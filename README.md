# Stirbot - University Website Scraper

A Python-based web scraping project for extracting data from the university of Stirling website.

## Running the app

**Tester mode** (chatbot only — scraping and ingestion hidden) so testers cant remove db:
```bash
python app.py
```

**Admin mode** (all tabs visible, including Scrape and Ingest):
```bash
python app.py --admin
```

> **Warning:** Only run admin mode if you know what you're doing. Triggering a scrape or re-ingestion will overwrite the existing db.
