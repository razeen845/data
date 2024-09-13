import os
import requests
from bs4 import BeautifulSoup


url = 'https://www.msd.govt.nz/about-msd-and-our-work/publications-resources/statistics/benefit/index.html'  # Replace with the actual URL
response = requests.get(url)


download_folder = 'downloaded_files'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)


for link in soup.find_all('a', href=True):
    href = link['href']
    
    
    if href.endswith('.pdf') or href.endswith('.xls') or href.endswith('.xlsx'):
        file_url = href
        if not file_url.startswith('http'):  
            file_url = f"https://www.msd.govt.nz/about-msd-and-our-work/publications-resources/statistics/benefit/index.html{href}"  # Adjust to the correct base URL
        
        
        file_name = os.path.join(download_folder, file_url.split('/')[-1])
        print(f"Downloading {file_name}...")
        file_response = requests.get(file_url)
        
        with open(file_name, 'wb') as file:
            file.write(file_response.content)

print("All files downloaded.")
