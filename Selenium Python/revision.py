import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome()

#service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
#service_obj = Service("C:/Users/adity/Downloads/chromedriver-win64(1)/chromedriver-win64/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.google.com/")
time.sleep(5)
driver.title
print(driver.title)
driver.current_url
print(driver.current_url)
driver.close()