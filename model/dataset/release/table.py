import requests
import json
from bs4 import BeautifulSoup

url = 'https://docs.accops.com/HyWorks34/content/release_notes/hyworks_known_issues/hylabs_known_issues.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find("table")

# Extract the data from the table rows
data_dict = {}
for row in table.find_all("tr"):
    columns = row.find_all("td")
    if len(columns) == 2:
        key = columns[0].find("strong").text
        value = columns[1].text.strip()
        data_dict[key] = value

# Print the resulting dictionary
print(data_dict)

json_data = []
for key, value in data_dict.items():
    json_obj = {"prompt": "Limitations and Issues of HyLabs "+ str(key), "completion": value}
    json_data.append(json_obj)

with open('model/dataset/release/data.json', 'w') as f:
    json.dump(json_data, f, indent=4)