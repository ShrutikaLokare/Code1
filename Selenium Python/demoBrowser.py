#script will give command to chrome driver and then chrome driver will push those actions to chrome browser

from selenium import webdriver                           #webdriver is a class
from selenium.webdriver.chrome.service import Service    #Service is a class


#Service automatically installs the driver for  chrome
#service_obj = Service()           #Service is a class name, responsible for starting and stopping of webdriver
#driver = webdriver.Chrome(service=service_obj)

#driver.get("https://w3schools.com")
#driver.maximize_window()

#another way of directly setting up the driver of chrowm
#chrome
#service_obj = Service("C:/Users/adity/OneDrive/Documents/chromedriver.exe") #chromedriver is a driver for chrome
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://w3schools.com")

#same program with firefox
#firefox
#service_obj = Service("C:/Users/adity/OneDrive/Documents/geckodriver.exe")  #geckodriver is a driver for firefox
#driver = webdriver.Firefox(service=service_obj)
#driver.get("https://w3schools.com")

#microsoft

#service_obj = Service("C:/Users/adity/OneDrive/Documents/msedgedriver.exe")  #geckodriver is a driver for firefox
#driver = webdriver.Edge(service=service_obj)
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://w3schools.com")


print(driver.current_url)
print(driver.title)
driver.get("https://w3schools.com/html")
driver.back()
driver.back()
driver.refresh()
driver.minimize_window()
driver.back()
driver.close()