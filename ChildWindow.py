import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# driver.find_element(By.LINK_TEXT,"Click Here").click()
#
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
#
# print(driver.find_element(By.TAG_NAME,"h3").text)
# time.sleep(1)
# driver.close()
#
# driver.switch_to.window(handles[0])
# print(driver.find_element(By.TAG_NAME,"h3").text)
# time.sleep(1)


driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])
text = driver.find_element(By.XPATH,"//div/p[2]").text
lst = text.split()
email = lst[4]
print(lst)
driver.close()
driver.switch_to.window(handles[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"signInBtn").click()
time.sleep(2)
