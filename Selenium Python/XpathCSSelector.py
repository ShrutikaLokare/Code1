from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#locators - NAME, ID, XPATH, CSSselector, ClassName, lineText :: CSS and xpath can be constructed

driver.find_element(By.NAME, "email").send_keys("shrutikalokare03@gmail.com")    #send keys to enter any value
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")            #send keys to enter any value
driver.find_element(By.ID, "exampleCheck1").click()                              #click to just click and not sending any value
driver.find_element(By.CLASS_NAME, "form-check-label").click()

#XPATH - "//tagname[@attribute="value"]" - syntax to construct the XPATH locator
#CSSSelector - "tagname[attribute="value"]" -syntax to construct the CSS loactor


driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Rahul")
driver.find_element(By.XPATH, "//input[@type ='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.CSS_SELECTOR, "input[value ='option1']").click()

driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("helloagain")
