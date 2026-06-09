from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID,"user-name")

username.send_keys("standard_user")

input("Press Enter")