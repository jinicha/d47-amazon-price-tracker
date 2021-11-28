import requests
from bs4 import BeautifulSoup


PRODUCT_URL = "https://www.amazon.com/gp/product/B082TSD2W5/ref=ox_sc_saved_title_6?smid=ATVPDKIKX0DER&th=1"

headers = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").get_text().split('$')[1])
print(price)
