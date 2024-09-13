from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


chrome_driver_path = 'C:/chrome driver/chromedriver.exe'


options = Options()
download_directory = os.path.join(os.path.expanduser('~'), 'Downloads')
prefs = {"download.default_directory": download_directory}
options.add_experimental_option("prefs", prefs)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


url = 'https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads'


driver.get(url)
time.sleep(5)  



link = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div/div/ul[6]/li[2]/a').get_attribute('href')

response = requests.get(link, headers=headers)
file_name = os.path.join(download_directory, link.split('/')[-1])


with open(file_name, 'webs') as file:
    file.write(response.content)

print(f'{file_name} saved successfully')


driver.quit