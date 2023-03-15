import requests
import json
from bs4 import BeautifulSoup

url = 'https://docs.accops.com/HyWorks34/content/installation/troubleshooting.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

h2_tags = soup.find_all('h2')

# Initialize an empty dictionary to store the extracted data
data_dict = {}

# Loop through each h2 tag
for h2_tag in h2_tags:
    # Get the text of the h2 tag as the key in the dictionary
    key = h2_tag.text
    
    # Get the next sibling of the h2 tag as the value
    value = h2_tag.find_next_sibling().text
    
    # Add the key-value pair to the dictionary
    data_dict[key] = value

# Convert the dictionary to JSON format and print it
# json_data = json.dumps(data_dict)
# print(json_data)

json_data = json.dumps(data_dict, indent=4)

# # Save the JSON data to a file
# with open('data.json', 'w') as f:
#     f.write(json_data)

json_data = []
for key, value in data_dict.items():
    json_obj = {"prompt": "Session Host " + key, "completion": value}
    json_data.append(json_obj)

with open('model/dataset/installation/data1.json', 'a') as f:
    json.dump(json_data, f, indent=4)
exit()
