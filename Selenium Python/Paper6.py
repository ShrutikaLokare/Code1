import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#to open gmail webpage
driver.get("https://www.gmail.com")
#time.sleep(1)

#to enter the email
driver.find_element(By.XPATH, "(//input[@type='email'])").send_keys("avantikawalke24@gmail.com")
#time.sleep(1)

#to click on next
driver.find_element(By.XPATH, "((//span[normalize-space()='Next'])[1])").click()
#time.sleep(2)

#to enter the password
driver.find_element(By.XPATH, "(//input[@name='Passwd'][1])").send_keys("Avantika@2021")
#to tick the checkbox
driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
#time.sleep(2)

#to click on next
driver.find_element(By.XPATH, "(//span[normalize-space()='Next'])[1]").click()
#time.sleep(6)

#to click on not now
#driver.find_element(By.XPATH, "(//span[normalize-space()='Not now'])[1]").click()
#time.sleep(5)

#to click on compose
driver.find_element(By.XPATH, "(//div[contains(text(),'Compose')])[1]").click()

#to enter the recepient
driver.find_element(By.XPATH, "(//div[@id=':o6'])[1]").send_keys("shrutikalokare03@gmail.com")
time.sleep(5)