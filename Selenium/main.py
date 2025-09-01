from selenium import webdriver
import time
import datetime
from datetime import timedelta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from input_date import automate_daily_report_generation

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



css_selector = f'[data-value = "0"]'
css_selector1 = f'[data-value = "accept"]'
search_box3 = wait.until(EC.visibility_of_element_located((By.ID, "typing")))
search_box3.click()

time.sleep(5)
try:
    search_box3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    for _ in range(4):
        search_box3.click()
        time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")



search_box3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector1)))
search_box3.click()



time.sleep(5)

next_button2 = driver.find_element(By.ID,'FormSubmit2')
next_button2.click()


time.sleep(10)

# Here We start the process of downloading the report
css_selector2 = f'[data-i18n="reports"]'
search_box4 = driver.find_element(By.CSS_SELECTOR, css_selector2)
search_box4.click()

# step 2
time.sleep(10)
css_selector3 = f'[data-i18n="claimsreports"]'
search_box5 = driver.find_element(By.CSS_SELECTOR, css_selector3)
search_box5.click()

# step 3

time.sleep(10)
css_selector4 = f'[data-i18n="scheme_utilization_report"]'
search_box6 = driver.find_element(By.CSS_SELECTOR, css_selector4)
search_box6.click()

# step 4
time.sleep(10)
search_box7 = driver.find_element(By.ID,'chk_datefrom')
search_box7.click()

# step 5
time.sleep(10)
today = datetime.date.today()
yesterday = datetime.date.today() - timedelta(days=1)
today_formatted = today.strftime('%Y-%m-%d')
yesterday_formatted = yesterday.strftime('%Y-%m-%d')

css_selector = f'[class ="icon-append fa fa-calendar"]'

date_input = driver.find_element(By.CSS_SELECTOR, css_selector)
date_input.click()
time.sleep(10)
DATE_INPUT_SELECTOR = f'[data-dateformat="yy-mm-dd"]'
EMPTY_SELECTOR = f'[data-i18n="from"]'

try:
    date_input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, DATE_INPUT_SELECTOR))
            )
    date_input_field.click()
    date_input_field.send_keys(yesterday_formatted)
    EMPTY_SELECTOR.click()

except:
    print(f"An error occurred while processing {yesterday_formatted}")
          
    





time.sleep(60)

driver.quit()