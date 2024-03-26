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

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles     #this gives list of all the windows opened by selenium
print(len(windowsOpened))                 #2 windows opened first is main parent and second is child

#to switch to the chile window
driver.switch_to.window(windowsOpened[1])   #to switch to window found from the list of windows and index 1 means second window)
driver.find_element(By.TAG_NAME, "h3").text
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()   #to close the child window

#to switch to parent main window again

driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
