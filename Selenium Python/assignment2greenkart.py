
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

ExpectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#implicit wait = global wait
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div/button").click()

print(actualList)
assert ExpectedList == actualList

