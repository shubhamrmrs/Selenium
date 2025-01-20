import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

NewSortedList = []

# click on column header
driver.find_element(By.XPATH, "//th[1]").click()

# collect all veggie name -> BrowserSortedVeggieList
VeggieList = driver.find_elements(By.XPATH, "//tr/td[1]")
for veggie in VeggieList:
    NewSortedList.append(veggie.text)
BrowserSorted = NewSortedList.copy()

# Sort this BrowserSortedVeggieList -> NewSortedList
NewSortedList.sort()

# assert BrowserSortedVeggieList == NewSortedList
assert BrowserSorted == NewSortedList
