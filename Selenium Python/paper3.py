#Open a Browser (write the generic code such that by changing the parameter browser can be changed.)
#Navigate to https://flipkart.com website.
#Write a method to find the count (number of) links on the homepage of Flipkart.
#Write another method to print link text and URLs of all the links on the page of Flipkart.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://flipkart.com")
time.sleep(1)
print(driver.current_url)

element = 0
elements = driver.find_elements(By.TAG_NAME, 'a')
for element in elements:
    href = element.get_attribute('href')
    if href is not None:
        print(href)

time.sleep(5)