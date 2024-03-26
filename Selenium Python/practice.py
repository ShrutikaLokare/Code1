from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


browserSortedVeggies = []   #declare an empty list

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#oroginal list
originalList = driver.find_elements(By.XPATH,"//tr/td[1]")
print(originalList)