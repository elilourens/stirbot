# Stirbot - University Website Scraper

A Python-based web scraping project for extracting data from university websites.

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your actual credentials and configuration
```

### 4. Run the Scraper

```bash
python backend/webscrape/scraper.py
```

## Project Structure

```
stirbot/
├── backend/
│   └── webscrape/
│       └── scraper.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Dependencies

- **requests**: HTTP library for making web requests
- **beautifulsoup4**: HTML/XML parsing
- **selenium**: Browser automation for dynamic content
- **scrapy**: Powerful scraping framework
- **pandas**: Data manipulation and export
- **python-dotenv**: Environment variable management

## Notes

- Never commit your `.env` file with real credentials
- Respect the university's robots.txt and terms of service
- Add delays between requests to avoid overloading servers
- Check if the website has an official API before scraping

## License

See [LICENSE](LICENSE) file for details.
