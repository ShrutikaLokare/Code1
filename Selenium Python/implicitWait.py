#shop veggies and add to cart, apply coupon code

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#implicit wait = global wait
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

time.sleep(5)
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
#time.sleep(5)
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
#time.sleep(2)

#sum addition verification

prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for price in prices:
    sum = sum+ int(price.text)   #48+160+180
print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

#############
#to apply the coupon code as "rahulshettyacademy"
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(10)

#explicit wait, specifically for one line
#wait = WebDriverWait(driver,10)
#wait.until(expected.presence_of_elements_located(By.CSS_SELECTOR, ".promoInfo"))

#to print "code applied" and verify same message exits
var = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(var)
assert "Code applied" in var

#to verify discounted price is lower than the actual price

actual = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
discounted = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
#discounted = int(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

print(actual)
print(discounted)

assert actual < discounted