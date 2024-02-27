import requests
import os
import re

def fetch_save_page(url, filename, folder="countries"):
    # Create folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Construct file path
    file_path = os.path.join(folder, f"{filename}.html")
    
    # Fetch and save the page content
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
    else:
        print(f"Failed to fetch {url}")

# Example usage
main_url = "https://www.worldometers.info/coronavirus/"
fetch_save_page(main_url, "main_page.html")

def fetch_countries_pages(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Strip leading and trailing whitespace and check if line contains "-" or is empty
            country_name = line.strip()
            if "-" in country_name or not country_name:
                continue  # Skip this line
            if ":" in country_name:
                continue
            
            # Construct the country URL
            country_url = f"https://www.worldometers.info/coronavirus/country/{country_name}/"
            
            # Fetch and save the page
            fetch_save_page(country_url, country_name)

# Example usage
fetch_countries_pages("worldometers_countrylist.txt")

