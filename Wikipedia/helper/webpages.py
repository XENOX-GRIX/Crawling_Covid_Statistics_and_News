import os
from urllib.request import Request, urlopen

def download_webpage(url, category):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        webpage = urlopen(req).read()
        mydata = webpage.decode("utf8")
        page_name = url.split('/')[-1]
        filename = f"{page_name}.html".replace("%", "_").replace("/", "_").replace(":", "_")
        with open(filename, 'w+', encoding="utf-8") as f:
            f.write(mydata)

        if category == "timeline":
            with open('timeline.txt', 'a+', encoding="utf-8") as f:
                f.write(f"{page_name}.html\n")
        elif category == "responses":
            with open('responses.txt', 'a+', encoding="utf-8") as f:
                f.write(f"{page_name}.html\n")
                
        # print(f"Downloaded {page_name} saved to {filename} and logged in {category}.txt")
    except Exception as e:
        print(f"Error downloading {page_name}: {e}")

def categorize_and_download():
    base_url = 'https://en.wikipedia.org'
    if os.path.exists('extracted_link.txt'):
        with open('extracted_link.txt', 'r') as file:
            for url_suffix in file.readlines():
                full_url = base_url + url_suffix.strip()
                if "Timeline" in url_suffix:
                    category = "timeline"
                elif "Responses" in url_suffix:
                    category = "responses"
                else:
                    category = "unknown"
                download_webpage(full_url, category)
    else:
        print("extracted_link.txt file not found.")
