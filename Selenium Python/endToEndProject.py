#Project - Open a webpage, click on shop(child window), add items to cart, checkout,
# select address(dynamic dropdown) and place the order

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#implicit wait = global wait
driver.implicitly_wait(5)
driver.maximize_window()

#to open the web page
driver.get("https://rahulshettyacademy.com/angularpractice/")               #to open the web page
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()       #click on shop

windowsOpened = driver.window_handles                      #class is used to check no of windows opened
#print(len(windowsOpened))

#to switch to the chile window
driver.switch_to.window(windowsOpened[0])                   #to switch on child window
driver.find_elements(By.XPATH, "(//div[@class='card h-100'])/div[1]/h4")        #to get all the mobiles header

Models = driver.find_elements(By.XPATH, "(//div[@class='card h-100'])/div[1]/h4")
#print(driver.find_elements(By.XPATH, "(//div[@class='card h-100'])/div[1]/h4"))
for model in Models:
    if model.text == 'Blackberry':
        driver.find_element(By.XPATH,"(//button[@class='btn btn-info'][normalize-space()='Add'])[4]").click()
        break


#driver.find_element(By.XPATH, "//span[@class='navbar-toggler-icon']").click()
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

time.sleep(4)

driver.find_element(By.ID, "country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, "India"))

#countries = driver.find_elements((By.XPATH, "//div[@class='suggestions']"))
countries = driver.find_elements((By.XPATH, "//div[@class='suggestions']"))

print(len(countries))  # number of items found
for country in countries:
    if country.text == "India":
        country.click()
        break




time.sleep(10)

#driver.find_element(By.LINK_TEXT, "India").click()
#driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
#driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
#time.sleep(10)
#successText = driver.find_element(By.CLASS_NAME, "alert-success").text
#print(successText)
#assert "Success! Thank you!" in successText