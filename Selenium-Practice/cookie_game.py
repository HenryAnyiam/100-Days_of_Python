#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


score = driver.find_element(By.ID, "money")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")

def get_score():
    score = driver.find_element(By.ID, "money")
    score = score.text
    score = int(score.replace(",", ""))
    return score
sleep = 5
val = time()
check = time()
while (time() - val) <= 300:
    cookie.click()
    if (time() - check) >= sleep:
        store = driver.find_elements(By.CSS_SELECTOR, "#store div")
        length = len(store) -1
        for i in range(length, -1, -1):
            if store[i].get_attribute("class") != "grayed":
                store[i].click()
                break
        check = time()
        sleep += 5

score = driver.find_element(By.ID, "cps")
print(score.text)