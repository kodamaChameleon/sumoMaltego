import requests
from bs4 import BeautifulSoup
import re

def format_phone_number(phone_number):

    # Remove any non-digit characters from the input
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Use the last 10 digits if there are more
    if len(cleaned_number) > 10:
        cleaned_number = cleaned_number[-10:]

    # Check if the cleaned number has 10 digits
    if len(cleaned_number) == 10:
        formatted_number = f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}"
        return formatted_number
    else:
        raise ValueError("Invalid Number Format")

class sumo:
    
    def __init__(self) -> None:
        self.phone_url_base = "https://sumosear.ch/phone/"
        self.image_url_base = "https://sumosear.ch/images/phone/"
        self.headers = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.cookies = None

    def phone_lookup(self, phone_number) -> list[str]:

        # Initialize variables
        search_results = []
        page = 1

        # Create loop for multiple pages of results
        while True:

            search_url = f"{self.phone_url_base}{format_phone_number(phone_number)}" + (f"/{page}" if page > 1 else "")

            response = requests.get(search_url, headers=self.headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all links with the class 'search-result-i__title-link'
                links = soup.find_all('a', class_='search-result-i__title-link')
                
                # Extract the href attribute of each link
                link_urls = [link['href'] for link in links]
                search_results.extend(link_urls)

                page += 1
            else:
                break

        return search_results
    
    def image_lookup(self, phone_number) -> list[str]:

        # Initialize variables
        search_results = []
        page = 1

        # Create loop for multiple pages of results
        while True:

            search_url = f"{self.image_url_base}{format_phone_number(phone_number)}" + (f"/{page}" if page > 1 else "")

            response = requests.get(search_url, headers=self.headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all links with the class 'search-result-i__title-link'
                links = soup.find_all('a', class_='img-res-item')
                
                # Extract the href attribute of each link
                link_urls = [link['href'] for link in links]
                search_results.extend(link_urls)

                page += 1
            else:
                break

        return search_results
        

# query_object = sumo()
# query_object.phone_lookup("470-673-0339") # Single page phone lookup
# query_object.phone_lookup("337-420-0436") # Multi page phone lookup
# query_object.image_lookup("337-420-0436")