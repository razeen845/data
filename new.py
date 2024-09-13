from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import requests
import os

# Set Chrome driver path
chrome_driver_path = 'C:/chrome driver/chromedriver.exe'

# Configure download directory
options = Options()
download_directory = os.path.join(os.path.expanduser('~'), 'Downloads')
prefs = {'download.default_directory': download_directory}
options.add_experimental_option('prefs', prefs)

# Create Chrome service and driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the webpage
url = 'https://www.msd.govt.nz/about-msd-and-our-work/publications-resources/statistics/benefit/index.html'
driver.get(url)

# Wait for the page to load completely
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'main-content')))

# Find all links to Excel files
excel_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.xlsx')]")

# Download each Excel file
for link in excel_links:
    file_url = link.get_attribute('href')
    file_name = file_url.split('/')[-1]

    # Download the file using Selenium (alternative method)
    driver.get(file_url)
    time.sleep(2)  # Adjust sleep time if needed

# Close the browser
driver.quit()

print(f"Downloaded {len(excel_links)} Excel files to {download_directory}")