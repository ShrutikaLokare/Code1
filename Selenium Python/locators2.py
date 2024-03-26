from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#driver.find_element(By.XPATH, "//input[@type ='email']").send_keys("demo@gmail.com")

#using CSS Locator with  parent child method
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(1) input").send_keys(("demo@gmail.com"))
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(4) button").click()

#using XPATH Locator with  parent child method
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys(("demo@gmail.com"))
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("12345")
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("12345")
driver.find_element(By.XPATH, "//form/div[4]/button").click()



