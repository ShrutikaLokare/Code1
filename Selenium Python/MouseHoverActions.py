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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.click_and_hold(driver.find_element())     -to click and hold
#action.double_click(driver.find_element())       -to double click
#action.context_click(driver.find_element())       -to right click
#action.drag_and_drop(driver.find_element())       -to drag and drop

#to move to element option 1 and then double click on option 1
action.move_to_element(driver.find_element(By.ID, "checkBoxOption1")) .perform()
action.double_click(driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']")).perform()

time.sleep(5)

#to move to mouse hover and then right click on Top
#always use .perform() at the end whenever using actionchains()
action.move_to_element(driver.find_element(By.ID, "mousehover")) .perform()         #just to move to that element
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()