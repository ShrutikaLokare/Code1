from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
#driver = webdriver.chrome(service = service_obj)

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)

