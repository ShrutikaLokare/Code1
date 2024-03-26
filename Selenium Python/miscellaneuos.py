#scroll down

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

chromeOptions = webdriver.ChromeOptions()                      #ChromeOptions() is a class use to use arguments like headless etc
chromeOptions.add_argument("headless")                         #to run chrome without opening it
chromeOptions.add_argument("--ignore-certificate-errors")      #to ignore all the certificate errors


service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chromeOptions)        #need to add all the objects here

#to open the web page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") #to scroll the page to the down using java scripts
driver.get_screenshot_as_file("screenshot.png")        #to take the screenshot of the scrolled down page
#time.sleep(4)