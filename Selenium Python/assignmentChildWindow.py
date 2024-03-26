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

#to open the web page
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()  #click on the link
#time.sleep(10)
windowsOpened = driver.window_handles     #this gives list of all the windows opened by selenium
print(len(windowsOpened))

#to switch to chile window
driver.switch_to.window(windowsOpened[1])
WholeText = driver.find_element(By.XPATH,"//p[@class='im-para red']").text
print(WholeText)

#to trim left part till at
CutString = WholeText.split("at ")
newString = CutString[1]
print(newString)

#to trim right part till
CutString1 = newString.split(" with")
newString1 = CutString1[0]
print(newString1)

driver.close()   #to close the child window

#to switch to parent main window again
driver.switch_to.window(windowsOpened[0])
#to enter the username
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(newString1)
#time.sleep(2)
#to enter the password
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("12345")
#to tick on terms
driver.find_element(By.CSS_SELECTOR, "#terms").click()
#to click on sign in
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

time.sleep(10)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)