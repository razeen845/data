from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

# Path to your ChromeDriver
chrome_driver_path = 'C:/chrome driver/chromedriver.exe'

# Set up Chrome options to define the download directory
options = Options()
download_directory = os.path.join(os.path.expanduser('~'), 'Downloads')
prefs = {"download.default_directory": download_directory}
options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Headers for making requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# URL to the webpage
url = 'https://kaingaora.govt.nz/en_NZ/publications/oia-and-proactive-releases/housing-statistics/'

# Open the webpage
driver.get(url)
time.sleep(5)  # Wait for the page to load

# Locate the download link (e.g., PDF link)
# Adjust the XPath to the specific file you want to download
link = driver.find_element(By.XPATH, '//*[@id="e191"]/div/div/div/div/div/ul[1]/li[2]/a').get_attribute('href')

# Request the file and download it
response = requests.get(link, headers=headers)
file_name = os.path.join(download_directory, link.split('/')[-1])

# Save the file in the Downloads directory
with open(file_name, 'wb') as file:
    file.write(response.content)

print(f'{file_name} saved successfully')

# Close the driver
driver.quit()
