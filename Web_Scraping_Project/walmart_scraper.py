from bs4 import BeautifulSoup
import requests
import json

walmart_url = "https://www.walmart.com/ip/Mainstays-Hillside-Diamond-Tufted-Upholstered-Queen-Platform-Bed-Gray/5035918436?classType=VARIANT&from=/search"

#supposed to make our web scraping algorithm look more human-like to the webpage that we're doing scraping on, otherwise will not
#   capture the script tag with the id "__NEXT_DATA__"
HEADERS = {
    "Accept": "*/*",
    "Accept-encoding": "gzip, deflate, br, zstd",
    "Accept-language": "en-US,en;q=0.9",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

response = requests.get(walmart_url, headers = HEADERS)

soup = BeautifulSoup(response.text, "html.parser")

script_tag = soup.find("script", id="__NEXT_DATA__")

data = json.loads(script_tag.string)

print(data['props']['pageProps'].keys())