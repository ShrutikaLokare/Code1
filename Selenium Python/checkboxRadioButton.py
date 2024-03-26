from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(4)
#RadioButton

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

#display boc

assert driver.find_element(By.ID, "displayed-text").is_displayed()      #to check whether box is displayed or not
driver.find_element(By.ID,"hide-textbox").click()                       #to click on hide
assert not driver.find_element(By.ID, "displayed-text").is_displayed()  #assert not is opposite of assert


