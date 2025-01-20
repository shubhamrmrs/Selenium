import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

name = "Hello Shubham, share this practice page and share your knowledge"

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Shubham")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
alert.accept()
alert.dismiss()
print(alertText)

assert name in alertText
time.sleep(2)
alert.accept()
# alert.dismiss()


