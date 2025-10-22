# Summarizer

Web summarization project using OpenAI API.

# ⚠️ Web Scraping Disclaimer

This project uses basic web scraping techniques for **educational and research purposes only**.  

Please note that:

- Some websites **may not expose their full content** through static HTML.
- Modern sites often load data **dynamically with JavaScript** or employ **anti-scraping measures** that prevent direct access via libraries like `requests` and `BeautifulSoup`.
- If the scraper fails to extract content, consider using tools that **support JavaScript rendering**, such as:
  - `requests-html`
  - `Playwright`
  - `Selenium`

> ⚠️ Always review the website’s **robots.txt** and **terms of service** before scraping.  
> Respect legal and ethical boundaries when accessing external content.

## Setup Instructions
open your root folder and recreate the conda environment
```bash
conda env create -f environment.yml
```

activate the environment
```bash
conda activate summarizer
```

create a .env file based on the .env.example and add your OpenAI API key
```bash
cp .env.example .env
```

run the app
```bash
python main.py
```
