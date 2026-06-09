from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")

print(driver.title)

input("Press Enter to close...")

driver.quit()