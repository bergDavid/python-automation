import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service

# initialize web drive
driver = webdriver.Firefox(service= Service(r"C:\Users\David\Documents\GitHub\python-automation\automation\geckodriver.exe"))
url = "https://www.techlistic.com/p/selenium-practice-form.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(8) #time.sleep(30)
#Enter Firstname
driver.find_element(By.NAME,"firstname").click()
driver.find_element(By.NAME,"firstname").send_keys("Tom")
driver.find_element(By.ID,"submit").click()