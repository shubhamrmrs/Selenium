import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
buttons = driver.find_elements(By.XPATH, "//div[@class='products']/div/div[3]/button")
for button in buttons:
    button.click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[@type='button']").click()

# SUM Validation **************************************************************************
Sum = 0
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")
for amount in amounts:
    Sum = Sum + int(amount.text)

print(Sum)

text = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert Sum == text

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").is_displayed()
