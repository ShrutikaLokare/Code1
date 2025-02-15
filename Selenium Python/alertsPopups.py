import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Rahul")
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert "Rahul" in alertText
alert.accept()