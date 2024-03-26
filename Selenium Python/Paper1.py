#Question1:

#Open the Firefox browser.
#Maximize the browser window.
##Navigate to “http://qatechhub.com”.
#Write a method to print PASS if the title of the page matches with “QA Automation Tools Trainings and Tutorials | QA Tech Hub” else FAIL. (If you are familiar with TestNG or JUnit use assert statement like assert.assertequals(actual, expected) to give a verdict of the pass or fail status.
#Navigate to the Facebook page (https://www.facebook.com)
#Navigate back to the QA Tech Hub website.
#Print the URL of the current page.
#Navigate forward.
#Reload the page.
#Close the Browser.



import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = webdriver.Firefox()

driver.maximize_window()

driver.get("http://qatechhub.com")
time.sleep(2)

titleText = driver.title
print(titleText)
assert "QA Automation Tools Trainings and Tutorials | QA Tech Hub" in titleText
driver.close()

driver = webdriver.Firefox()
driver.get("http://www.google.com")
time.sleep(2)
driver.close()

driver = webdriver.Firefox()
driver.get("http://qatechhub.com")
time.sleep(2)
titleText = driver.title
print(titleText)

driver.forward()
driver.refresh()
driver.close()