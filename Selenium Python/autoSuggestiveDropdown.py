import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")

time.sleep(5)

countries = driver.find_elements(By.CSS_SELECTOR,"li[class = 'ui-menu-item'] a")  # finding multiple elements with same tagname
print(len(countries))  # number of items found
for country in countries:              # for loop to iterate each item
    if country.text == "India":              # if text matches with India
        country.click()                     # click on it
        break                             # once we found india, no need to iterate ahead so break it

#driver.find_element(By.ID, "autosuggest").get_attribute("value")
#expected = print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
