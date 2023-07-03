# Flipkart Product Scraper

This Python script allows you to scrape product data from Flipkart's search results page. It fetches product details like name, specifications, price, MRP, and image URL and saves the data to a CSV file for further analysis.

## How to Use

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/pankajshakya627/flipkart_product_scraper.git
   cd flipkart_product_scraper
   ```

2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

3. Run the script and provide the product you want to search:
   ```bash
   python scraper.py
   ```

4. The script will prompt you to enter the product name. It will then scrape the data from Flipkart and save it to a CSV file named 'flipkart_products_search.csv', where 'search' is the product you searched for.

## Exception Handling

The script uses proper error handling to handle HTTP errors and gracefully continue execution. If any HTTP errors or other exceptions occur during the scraping process, appropriate error messages will be displayed.
