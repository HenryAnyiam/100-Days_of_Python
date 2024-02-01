#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://secure-retreat-92358.herokuapp.com/")

firstname = driver.find_element(By.NAME, "fName")
firstname.send_keys("Lex")

lastname = driver.find_element(By.NAME, "lName")
lastname.send_keys("Louis")

email = driver.find_element(By.NAME, "email")
email.send_keys("emailemail@email.org")

submit = driver.find_element(By.CSS_SELECTOR, "form .btn")
