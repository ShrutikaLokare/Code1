#problem statement
import time

#1- click on the column header
#2- collect all the veggies and save it in the #browserSortedList
#3- Sort the #browserSortedList using python methods and save it in the #sortedList
#4- assert whether #browserSortedList == #sortedList

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


browserSortedVeggies = []   #declare an empty list

service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()       #to click on colum header
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")               #colect all the veggies in column 1

for elements in veggieWebElements:                                    #use for loop to iterate throught he veggieWebElemnts
    browserSortedVeggies.append(elements.text)                       #store the iterated elements in browserSortedVeggie using append

OriginalBrowserSortedList = browserSortedVeggies.copy()          #to save original copy in OrginialBrowserSortedList
print(OriginalBrowserSortedList)                                 #to print OriginalBrowserSortedList

browserSortedVeggies.sort()
print(browserSortedVeggies)

assert OriginalBrowserSortedList == browserSortedVeggies