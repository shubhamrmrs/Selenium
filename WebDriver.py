import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_obj = Service("D:\Software\IMP\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# OR

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)
