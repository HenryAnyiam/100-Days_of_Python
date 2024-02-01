#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org")

time_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li time")
anchor_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li a")

length = len(time_elements)

data = {i : {"time": time_elements[i].text,
             "event": anchor_elements[i].text,
             "link": anchor_elements[i].get_attribute("href")}
             for i in range(length)}

print(data)

driver.close()
  