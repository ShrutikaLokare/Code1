#Open a Chrome browser.
#Navigate to “http://www.fb.com”
#Verify that the page is redirected to “http://www.facebook.com”, by getting the current URL. (use if-else condition to verify this condition or use Assert.assertequals() in case you are familiar with TestNG or JUnit)
#Verify that there is a “Create an account” section on the page.
##Fill in the text boxes: First Name, Surname, Mobile Number or email address, “Re-enter mobile number”, new password.
#Update the date of birth in the drop-down.
#Select gender.
#Click on “Create an account”.
#Verify that the account is created successfully

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://www.fb.com")
time.sleep(0)

print(driver.current_url)

if driver.current_url == "https://www.facebook.com/":
    print("pass")
else:
    print("fail")

text1 = driver.find_element(By.LINK_TEXT, "Create new account").text
print(text1)

driver.find_element(By.LINK_TEXT, "Create new account").click()
time.sleep(2)

driver.find_element(By.NAME,"firstname").send_keys("Shrutika")
time.sleep(2)

#entering email id and re-entering email id
driver.find_element(By.NAME,"lastname").send_keys("Lokare")
driver.find_element(By.NAME,"reg_email__").send_keys("shrutikaditya@gmail.com")
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("shrutikaditya@gmail.com")
time.sleep(2)

#entering password
driver.find_element(By.XPATH,"//input[@id='password_step_input']").send_keys("Shru@Lok@1994")
time.sleep(2)

#selecting month
dropdown = Select(driver.find_element(By.XPATH,"//select[@id='month']"))
dropdown.select_by_index(8)
dropdown.select_by_visible_text("Sep")

#selecting date
dropdown = Select(driver.find_element(By.XPATH,"//select[@id='day']"))
dropdown.select_by_index(2)
dropdown.select_by_visible_text("3")

#selecting year
dropdown = Select(driver.find_element(By.XPATH,"//select[@id='year']"))
dropdown.select_by_visible_text("1994")
time.sleep(2)

#selecting gender
#driver.find_element(By.CSS_SELECTOR, "._5k_3").click()
driver.find_element(By.XPATH, "(//span[@class='_5k_2 _5dba'])[1]").click()
time.sleep(2)

#to click on submit
driver.find_element(By.NAME, "websubmit").click()
time.sleep(5)