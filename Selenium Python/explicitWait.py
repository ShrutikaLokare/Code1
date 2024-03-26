

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#explicit wait, specifically for one line
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_elements_located(By.CSS_SELECTOR, ".promoInfo"))

WebDriverWait()
