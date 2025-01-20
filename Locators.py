import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("shubham")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(msg)
assert "Success" in msg

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello text box")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(1)


# ID, ClassName, name, linkText, Xpath, CSSSelector
#
# Xpath -> //tagname[@attribute='value']
# OR //ParentTagName/ChildTagName[Index]/chilTagName
# OR //TagName[text()='text value']
# OR //TagName[contains(@attribute,'part of value')]
#
# CSSSelector -> tagname[attribute='value']
# OR #ID
# OR .ClassName
# OR ParentTagName ChildTagName:nth-child(Index) childTagName..

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("Hello@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("99999")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("99999")
# driver.find_element(By.XPATH,"//form/div[4]/Button").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(2)

