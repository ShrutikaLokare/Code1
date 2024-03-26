import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://www.snapdeal.com")
time.sleep(1)

driver.find_element(By.XPATH, "(//div[@class='accountInner'])").click()
time.sleep(2)
driver.find_element(By.TAG_NAME, "href = https://www.snapdeal.com/login")
time.sleep(3)