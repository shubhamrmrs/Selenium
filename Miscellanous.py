import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors")

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(2)
driver.get_screenshot_as_file("screenshot.png")


