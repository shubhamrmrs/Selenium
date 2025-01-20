import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://jqueryui.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

for link in links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"broken link: {href}(Status code: {response.status_code})")

driver.quit()