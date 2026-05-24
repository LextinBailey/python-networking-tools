import requests
from bs4 import BeautifulSoup

url = input("Enter a URL to scrape: ")

if not url.startswith("http"):
    print("Please include http:// or https://")
    exit()

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

headings = soup.find_all("h1")

for heading in headings:
    print(heading.text.strip())