#Project - Open a webpage, click on shop(child window), add items to cart, checkout,
# select address(dynamic dropdown) and place the order

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

#implicit wait = global wait
driver.implicitly_wait(5)
driver.maximize_window()

#to open the web page
driver.get("https://rahulshettyacademy.com/angularpractice/")

#to click on shop
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

#to get all 4 model info using common class
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button")



#to click on checkout
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()


#to click on checkout
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

#to enter ind in the blank space
driver.find_element(By.ID, "country").send_keys("ind")

#explicit wait until india appears on the screen
wait = WebDriverWait(driver,10)        #explicit wait
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
time.sleep(5)
#to click on checkBox
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

#to click on purchase
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

#to  get the success message
successMessage = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(successMessage)

assert "Success! Thank you!" in successMessage