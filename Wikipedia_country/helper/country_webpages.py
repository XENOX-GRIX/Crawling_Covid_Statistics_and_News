import os
from urllib.request import Request, urlopen

def download_webpage(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        webpage = urlopen(req).read()
        mydata = webpage.decode("utf8")
        page_name = url.split('/')[-1]
        filename = f"{page_name}.html".replace("%", "_").replace("/", "_").replace(":", "_")
        with open(filename, 'w+', encoding="utf-8") as f:
            f.write(mydata)

        with open('extracted_country_data.txt', 'a+', encoding="utf-8") as f:
            f.write(f"{filename}\n")
        
    except Exception as e:
        print(f"Error downloading {page_name}: {e}")

def download_from_extracted_links():
    base_url = 'https://en.wikipedia.org'
    if os.path.exists('extracted_country_link.txt'):
        with open('extracted_country_link.txt', 'r', encoding="utf-8") as file:
            for url_suffix in file.readlines():
                full_url = base_url + url_suffix.strip()
                download_webpage(full_url)
    else:
        print("extracted_country_link.txt file not found.")
