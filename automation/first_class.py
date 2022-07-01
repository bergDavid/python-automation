import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service

# initialize web drive
driver = webdriver.Firefox(service= Service(r"C:\Users\David\Documents\GitHub\python-automation\automation\geckodriver.exe"))
url = "https://jqueryui.com/resources/demos/progressbar/download.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(8) #time.sleep(30)
my_element = driver.find_element(By.ID,'downloadButton')
#my_element = driver.find_element_by_id('downloadButton')
my_element.click()

WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,'progress-label'),# Element filtration
        "Complete!" # The expected text
    )
)