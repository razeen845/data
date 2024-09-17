import requests
import pandas as pd

url = "https://production.infometrics.co.nz/api/qem/data/?area_id=northland-region&series=VEH_REG_NONCOM_Q"


response = requests.get(url)
data = response.json()


series_data = data['series'][0]['values']


df = pd.DataFrame(series_data)


cleaned_df = df[['year', 'month', 'quarterly_value', 'annualised_value', 'area_id', 'area_name']]
cleaned_df.rename(columns={
    'year': 'Year',
    'month': 'Month',
    'quarterly_value': 'Quarterly Value',
    'annualised_value': 'Annualised Value',
    'area_id': 'Area ID',
    'area_name': 'Area Name'
}, inplace=True)


cleaned_df.to_csv("cleaned_vehicle_data.csv", index=False)

print("Data has been downloaded and saved to 'cleaned_vehicle_data.csv'.")
