from selenium import webdriver
import os
import time
import datetime
import shutil
from datetime import timedelta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# The code below allows the user to login and download the scheme utilization report of the previous day once run!


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://data.smartapplicationsgroup.com/ssp/login.jsp')

search_box = driver.find_element(By.ID, "language_select")

search_box.send_keys("English")

search_box2 = driver.find_element(By.ID,'lbl_country')
search_box2.send_keys('rwanda')

search_box2 = driver.find_element(By.ID,'lbl_username')
search_box2.send_keys('Mugabe Patrick')

search_box2 = driver.find_element(By.ID,'lbl_password')
search_box2.send_keys('Mugabep@39')

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
driver.maximize_window()
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
EMPTY_SELECTOR = f'[src="img/smartlogo.jpg"]'

try:
    date_input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, DATE_INPUT_SELECTOR))
            )
    date_input_field.click()
    date_input_field.send_keys(yesterday_formatted)
    #EMPTY_SELECTOR.click()

except:
    print(f"An error occurred while processing {yesterday_formatted}")

time.sleep(10)

#Empty click 1

empty_click1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"//label[@data-i18n='from']")))
empty_click1.click()

#Input to-date formmatted

try:
    date_input_field2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID,'txt_dateto'))
            )
    date_input_field2.click()
    date_input_field2.send_keys(today_formatted)
    #EMPTY_SELECTOR.click()

except:
    print(f"An error occurred while processing {today_formatted}")

#empty click 2
time.sleep(5)

try:
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']"))
)
    GENERATE_BUTTON= driver.find_element(By.XPATH, "//button[text()='Search']")
    GENERATE_BUTTON.click()
except:
    print("GENERATE_BUTTON is missing")

time.sleep(5)



try:
    EXPORT_BUTTON = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Export']"))
)
    EXPORT_BUTTON.click()
except:
    print("EXPORT_BUTTON  is missing")

time.sleep(5)


try:
    EXPORT_TO_EXCEL = driver.find_element(By.XPATH,"//a[@data-i18n='exporttoexcel']")
    EXPORT_TO_EXCEL.click()
except:
    print("EXPORT_TO_EXCEL  is missing")

time.sleep(10)

try:
    CLICK_HERE = driver.find_element(By.XPATH,"//a[text()='click here']")
    CLICK_HERE.click()
except:
    print("CLICK_HERE  is missing")

time.sleep(10)
try:
    DOWNLOAD_LAST = driver.find_element(By.XPATH,"//a[@data-i18n='download']")
    DOWNLOAD_LAST.click()
except:
    print("DOWNLOAD_LAST  is missing")

try:
    SEARCH_LAST = driver.find_element(By.XPATH,"//a[@data-i18n='search']")
    SEARCH_LAST.click()
    time.sleep(30)
    SEARCH_LAST.click()
    time.sleep(30)
    SEARCH_LAST.click()
except:
    print("SEARCH_LAST  is missing")

time.sleep(60)

try:
    FILE_LAST = driver.find_element(By.XPATH,"//a[contains(@href, 'download-report.jsp')]")
    FILE_LAST.click()
except:
    print("FILE_LAST  is missing")

time.sleep(3)

try:
    DOWNLOAD_POP = driver.find_element(By.XPATH,"//button[@id='download_btn']")
    DOWNLOAD_POP.click()
except:
    print("DOWNLOAD_POP  is missing")

time.sleep(10)

try:
    OPEN_FILE = driver.find_element(By.XPATH,"//button[@id='bot2-Msg1']")
    OPEN_FILE.click()
except:
    print("OPEN_FILE  is missing")




time.sleep(20)

# Direct the downloaded file to a specific folder

DEFAULT_DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
TARGET_DIR = r"C:\Users\Akaruretwa\OneDrive - Old Mutual Africa Regions\Documents\PowerBI_Data"   # 👈 your desired folder
os.makedirs(TARGET_DIR, exist_ok=True)

# === 2️⃣ Set up Chrome ===
chrome_options = Options()
prefs = {
    "download.default_directory": DEFAULT_DOWNLOAD_DIR,   # Chrome default path
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)


# === 3️⃣ Go to your site and trigger download ===
driver.get("https://example.com/your-download-page")

# Example: click a download button
# driver.find_element("xpath", "//button[contains(text(),'Download Excel')]").click()

# === 4️⃣ Wait for the download to finish ===
def wait_for_download(download_dir, timeout=60):
    """
    Wait until the latest .crdownload file disappears,
    meaning the download has finished.
    """
    seconds = 0
    while seconds < timeout:
        time.sleep(1)
        files = os.listdir(download_dir)
        # Check for unfinished downloads
        if not any(f.endswith('.crdownload') for f in files):
            return True
        seconds += 1
    return False

wait_for_download(DEFAULT_DOWNLOAD_DIR)
driver.quit()

# === 5️⃣ Move the Excel file to your target folder ===
def move_latest_excel(src_dir, dest_dir):
    excel_files = [f for f in os.listdir(src_dir) if f.endswith((".xlsx", ".xls"))]
    if not excel_files:
        print("❌ No Excel files found in downloads.")
        return None

    # Get the newest file
    latest_file = max(
        [os.path.join(src_dir, f) for f in excel_files],
        key=os.path.getmtime
    )

    dest_path = os.path.join(dest_dir, os.path.basename(latest_file))
    shutil.move(latest_file, dest_path)
    print(f"✅ Moved {os.path.basename(latest_file)} to {dest_dir}")
    return dest_path

move_latest_excel(DEFAULT_DOWNLOAD_DIR, TARGET_DIR)

driver.quit()