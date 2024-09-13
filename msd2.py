import requests
from bs4 import BeautifulSoup
import os

# URL of the page containing the Excel download links
url = 'https://www.msd.govt.nz/about-msd-and-our-work/publications-resources/statistics/benefit/index.html'

# Headers for making the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Set up the download directory
download_directory = os.path.join(os.path.expanduser('~'), 'Downloads')

# Make a request to the page
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links that contain 'Excel' in their string (text) or href
excel_links = soup.find_all('a', href=True, string=lambda x: x and 'Excel' in x)

# Print the found links to verify
for link in excel_links:
    print(link['href'])

# Loop through each link and download the corresponding file
for link in excel_links:
    file_url = link['href']
    
    # Construct full URL if needed (some links might be relative)
    if not file_url.startswith('http'):
        file_url = 'https://www.msd.govt.nz' + file_url
    print(f'Downloading from: {file_url}')
    
    # Get the file name from the URL
    file_name = os.path.join(download_directory, file_url.split('/')[-1])
    
    # Download the file
    file_response = requests.get(file_url, headers=headers)
    
    # Check if the download was successful
    print(f'Response status code: {file_response.status_code}')
    
    if file_response.status_code == 200:
        # Save the file locally
        with open(file_name, 'wb') as file:
            file.write(file_response.content)
        print(f'{file_name} saved successfully')
    else:
        print(f'Failed to download {file_url}')

print("All files downloaded successfully.")
