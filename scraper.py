# # Product Scrapping from Flipkart using BeautifulSoup
# import csv
# import requests
# from bs4 import BeautifulSoup

# # Get user input for the product to search
# search = input("Enter the product you want to search: ")

# # Send a request to Flipkart and check if the response is successful
# try:
#     res = requests.get(f"https://www.flipkart.com/search?q={search}")
#     res.raise_for_status()  # Raise an exception for any HTTP error status codes

#     # Create a BeautifulSoup object from the response content
#     soup = BeautifulSoup(res.content, 'html.parser')

#     # Find all the product cards on the page
#     product_cards = soup.find_all('div', {'class': '_2kHMtA'})

#     # Create a CSV file and write headers
#     filename = f"flipkart_products_{search}.csv"
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['Product Name', 'Specifications', 'Price', 'MRP', 'Image URL'])

#         # Iterate over each product card and extract the required information
#         for card in product_cards:
#             try:
#                 # Extract item details, specifications, price, and MRP (if available)
#                 item_details = card.find('div', {'class': '_4rR01T'}).text.strip()
#                 ul_element = card.find('ul', class_='_1xgFaf')
#                 specifications = [li.text for li in ul_element.find_all('li')]
#                 price = card.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()
#                 mrp = card.find('div', {'class': '_3I9_wc _27UcVY'}).text.strip()
#             except AttributeError:
#                 # Handle the case when MRP is not available
#                 mrp = None

#             # Extract the image URL
#             url = card.find('img', {'class': '_396cs4'}).get('src')

#             # Write the data to the CSV file
#             writer.writerow([item_details, specifications, price, mrp, url])

#     print(f"Data scraped from Flipkart and saved to {filename} successfully.")

# except requests.RequestException as e:
#     print(f"An error occurred while requesting the page: {e}")
# except Exception as e:
#     print(f"An error occurred during scraping: {e}")
import csv
import requests
from bs4 import BeautifulSoup

search = input("Enter the product you want to search: ")
pages = int(input("Enter the number of pages to scrape: "))

# Create a CSV file and write headers
filename = f"flipkart_products_{search}.csv"
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product Name', 'Specifications', 'Price', 'MRP', 'Image URL', 'Rating'])

    for page in range(1, pages+1):
        try:
            url = f"https://www.flipkart.com/search?q={search}&page={page}"
            res = requests.get(url)
            if res.status_code == 200:
                soup = BeautifulSoup(res.content, 'html.parser')
                product_cards = soup.find_all('div', {'class': '_2kHMtA'})

                for card in product_cards:
                    item_details = card.find('div', {'class': '_4rR01T'}).text.strip()
                    ul_element = card.find('ul', class_='_1xgFaf')
                    specifications = [li.text for li in ul_element.find_all('li')]
                    price = card.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()
                    try:
                        mrp = card.find('div', {'class': '_3I9_wc _27UcVY'}).text.strip()
                    except:
                        mrp = None
                    url = card.find('img', {'class': '_396cs4'}).get('src')

                    rating = card.find('div', {'class':"_3LWZlK"}).text.strip()

                    writer.writerow([item_details, specifications, price, mrp, url, rating])
                print(f"Data scraped from Flipkart and saved to {filename} successfully.")
        except requests.RequestException as e:
            print(f"An error occurred while requesting the page: {e}") 
        except Exception as e:
            print(f"An error occurred during scraping: {e}")

