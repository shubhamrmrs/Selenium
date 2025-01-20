import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Static dropdown **********************************************************************************

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select[class='form-control']"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Teacher")
dropdown.select_by_value("consult")
time.sleep(3)

# Dynamic dropdown / AutoSuggestive dropdown ********************************************************

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(1)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        time.sleep(1)
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
