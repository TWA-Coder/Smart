from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://data.smartapplicationsgroup.com/ssp/login.jsp')

search_box = driver.find_element(By.ID, "language_select")

search_box.send_keys("English")

search_box2 = driver.find_element(By.ID,'lbl_country')
search_box2.send_keys('rwanda')

search_box2 = driver.find_element(By.ID,'lbl_username')
search_box2.send_keys('')

search_box2 = driver.find_element(By.ID,'lbl_password')
search_box2.send_keys('')

next_button = driver.find_element(By.ID,'FormSubmit')
next_button.click()


time.sleep(60)

driver.quit()