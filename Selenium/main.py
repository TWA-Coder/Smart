from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
search_box2.send_keys('Mugabe Patrick')

search_box2 = driver.find_element(By.ID,'lbl_password')
search_box2.send_keys('Mugab@39')

next_button1 = driver.find_element(By.ID,'FormSubmit')
next_button1.click()
time.sleep(5)

wait = WebDriverWait(driver, 10)

try:

    css_selector = f'[data-value = "0"]'
    css_selector1 = f'[data-value = "accept"]'
    search_box3 = wait.until(EC.visibility_of_element_located((By.ID, "typing")))
    search_box3.click()
    

    search_box3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    search_box3.click()
    search_box3.click()
    search_box3.click()
    search_box3.click()

    search_box3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector1)))
    search_box3.click()

except Exception as e:
    print(f"Error: Element not found or not visible: {e}")

time.sleep(5)

next_button2 = driver.find_element(By.ID,'FormSubmit2')
next_button2.click()



time.sleep(60)

driver.quit()