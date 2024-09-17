import requests
import json
import csv
import time


area_ids = [f"area_{i}" for i in range(1, 61)]


base_url = "https://production.infometrics.co.nz/api/user_context/?app_type=QEM&area_id={}&compare_area_id=new-zealand&compare_area_id=rural-areas"

def download_area_data(area_id):
    url = base_url.format(area_id)
    
    try:
        
        response = requests.get(url)

        
        if response.status_code == 200:
            data = response.json()

            
            if 'compare_areas' in data:
                relevant_data = data['compare_areas']

                
                if isinstance(relevant_data, list) and relevant_data:
                    return relevant_data
                else:
                    print(f"No relevant data found for {area_id}.")
            else:
                print(f"Could not find the expected key in the JSON for {area_id}.")
        else:
            print(f"Failed to retrieve data for {area_id}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while processing {area_id}: {e}")
    
    return []


all_data = []
headers_written = False


with open('combined_areans_data.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    
    for area_id in area_ids:
        area_data = download_area_data(area_id)

        
        if area_data:
            
            if not headers_written:
                headers = area_data[0].keys()
                writer.writerow(headers)
                headers_written = True
            
            
            for item in area_data:
                writer.writerow(item.values())
        
        
        time.sleep(1)

print("Data for all areas successfully combined and saved to 'combined_areas_data.csv'.")
