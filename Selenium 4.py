import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
url = "https://demo.automationtesting.in/Register.html"
driver.get(url)

first_txt =driver.find_element(By.XPATH,'//input[@placeholder="First Name"]')

driver.find_element(locate_with(By.TAG_NAME,'input').to_right_of(first_txt)).send_keys("HELLLLO")
time.sleep(1)
right_txt = driver.find_element(locate_with(By.TAG_NAME,'label').to_left_of(first_txt)).text
print(right_txt)
time.sleep(1)
driver.find_element(locate_with(By.TAG_NAME,'textarea').below(first_txt)).send_keys("adddreesss")
time.sleep(1)
above_txt = driver.find_element(locate_with(By.TAG_NAME,'h2').above(first_txt)).text
print(above_txt)
time.sleep(1)
driver.find_element(locate_with(By.TAG_NAME,'input').near(first_txt)).send_keys("aa jao")
time.sleep(2)