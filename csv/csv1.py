import requests
from bs4 import BeautifulSoup
import csv

url = 'https://infopark.in/companies/company/thrissur'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

h3_tags = soup.find_all('h3')


company_names = [tag.text.strip() for tag in h3_tags]

csv_file_path = 'company_names.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
  
    csv_writer = csv.writer(csvfile)

   
    csv_writer.writerow(['Company Name'])

   
    csv_writer.writerows([[name] for name in company_names])

print(f"Company names have been saved to {csv_file_path}")
