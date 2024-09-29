from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os

chrome_driver_path = 'C:/chrome driver/chromedriver.exe'  
options = Options()
download_directory = os.path.join(os.path.expanduser('~'), 'Downloads')
prefs = {'download.default_directory': download_directory}
options.add_experimental_option("prefs", prefs)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
url = 'https://www.stats.govt.nz/information-releases/labour-market-statistics-june-2024-quarter/'
driver.get(url)

xpaths = [
    '//*[@id="main"]/section/div/div/div[1]/article/div/div[3]/article/ul/li[1]/div/div/h3/a',
    '//*[@id="main"]/section/div/div/div[1]/article/div/div[3]/article/ul/li[2]/div/div/h3/a',
    '//*[@id="main"]/section/div/div/div[1]/article/div/div[3]/article/ul/li[3]/div/div/h3/a',
    '//*[@id="main"]/section/div/div/div[1]/article/div/div[3]/article/ul/li[4]/div/div/h3/a',
    '//*[@id="main"]/section/div/div/div[1]/article/div/div[3]/article/ul/li[5]/div/div/h3/a'
]

try:
    for i, xpath in enumerate(xpaths):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            link_element = driver.find_element(By.XPATH, xpath)
            download_link = link_element.get_attribute('href')
            file_name = os.path.join(download_directory, download_link.split('/')[-1])
            
            # Download the file
            try:
                response = requests.get(download_link, headers=headers, timeout=10)
                response.raise_for_status()  # Raise an error if the request was not successful
                
                with open(file_name, 'wb') as file:
                    file.write(response.content)
                    print(f'File {i + 1}: {file_name} downloaded successfully.')
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {download_link}: {e}")
                continue

        except Exception as e:
            print(f"Error in locating element for XPath {xpath}: {e}")
            continue

finally:
    driver.quit()
