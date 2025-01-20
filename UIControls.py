import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# checkboxes *********************************************************************************

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("Value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# Radio button *******************************************************************************

RadioButtons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
RadioButtons[1].click()
time.sleep(1)

# Is Displayed or Not ************************************************************************

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
time.sleep(1)
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
