import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#implicit wait = global wait
driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

# first switch to frames
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to perform automation")

#to get text present on the top on original content screen
driver.switch_to.default_content()         #first do  switch back to original default content
text3 = driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text
print(text3)