import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_daily_report_generation(driver, start_date, num_days):
    """
    Automates the process of generating reports for a series of consecutive days.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        start_date (datetime.date): The first date for which to generate a report.
        num_days (int): The number of days to iterate and generate reports for.
    """
    # Define a CSS selector for the date input field.
    css_selector = f'[class ="icon-append fa fa-calendar"]'

    date_input = driver.find_element(By.CSS_SELECTOR, css_selector)
    date_input.click()
    DATE_INPUT_SELECTOR = f"[data-dateformat='yy-m-dd']"

    # Define a CSS selector for the report generation button.
    # You will need to inspect your webpage to find the correct selector.
    # Example: generate_button = driver.find_element(By.ID, "generate-report-button")
    GENERATE_BUTTON_SELECTOR = f'[data-i18n="search"]'

    #print(f"Starting report generation from {start_date} for {num_days} days...")

    # Iterate through the number of days specified.
    for i in range(num_days):
        # Calculate the current report date by adding a timedelta.
        # This is the core logic for your requirement.
        current_report_date = start_date + timedelta(days=i)

        # Format the date into a string that the web form will accept.
        # The common format for HTML5 date inputs is 'YYYY-MM-DD'.
        formatted_date = current_report_date.strftime('%Y-%m-%d')

        #print(f"\nProcessing report for date: {formatted_date}")

        try:
            # Wait for the date input field to be visible and interactable.
            # This prevents errors if the page takes time to load.
            date_input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, DATE_INPUT_SELECTOR))
            )

            # Clear any existing value in the date field.
            date_input_field.clear()

            # Input the formatted date into the field.
            date_input_field.send_keys(formatted_date)

            #print("Date entered successfully.")

            # Find and click the generate report button.
            generate_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, GENERATE_BUTTON_SELECTOR))
            )
            generate_button.click()

            #print("Report generation button clicked.")

            # --- Placeholder for report download/saving logic ---
            # At this point, you would add code to handle the report download.
            # This might involve waiting for a download to complete,
            # or clicking a link to save a PDF, CSV, etc.
            # The exact code depends on how the report is presented on the website.
            # For example:
            # WebDriverWait(driver, 60).until(EC.url_contains("download-complete"))
            # print("Report downloaded for {formatted_date}")

        except Exception as e:
            print(f"An error occurred while processing {formatted_date}: {e}")
            # You can add more robust error handling here, like taking a screenshot
            # or logging the error.
            continue # Continue to the next day even if one fails.

    #print("\nReport automation complete.")