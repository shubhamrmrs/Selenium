import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

# Comparing lists of veggies ******************************************************************

Lists = driver.find_elements(By.XPATH, "//div/h4")
for List in Lists:
    actualList.append(List.text)
assert actualList == expectedList


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

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert Sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").is_displayed()

# Compare discountAmount with totalAmount *******************************************************

discountAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert discountAmount < totalAmount
