from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#locators - NAME, ID, XPATH, CSSselector, ClassName, lineText :: CSS and xpath can be constructed

driver.find_element(By.NAME, "email").send_keys("shrutikalokare03@gmail.com")    #send keys to enter any value
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")            #send keys to enter any value
driver.find_element(By.ID, "exampleCheck1").click()                              #click to just click and not sending any value

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
