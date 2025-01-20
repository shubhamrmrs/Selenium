import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)
# actions.double_click(driver.find_element(By.))
# actions.click_and_hold(driver.find_element(By.))
# actions.key_down()
# actions.key_up()
# actions.drag_and_drop(driver.find_element(By.), driver.find_element(By.))
actions.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# actions.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(2)