#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(article.text)



search_bar = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")

search_bar.send_keys("Beyonce", Keys.ENTER)

# search_button = driver.find_element(By.CLASS_NAME, "cdx-search-input__end-button")
# search_button.click()

driver.close()
