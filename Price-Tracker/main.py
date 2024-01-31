#!/usr/bin/python3
"""Track amazon price"""

from bs4 import BeautifulSoup
import requests
import lxml

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,de;q=0.7"
}

response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers=header)

soup = BeautifulSoup(markup=response.text, features="lxml")




#print(soup.prettify())
whole = soup.select_one(".a-price-whole").get_text()
dec = soup.select_one(".a-price-decimal").get_text()
frac = soup.select_one(".a-price-fraction").get_text()

val = f"{whole}{frac}"
print(val)
print(float(val))
