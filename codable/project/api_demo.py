import requests 
from pprint import pprint

API_KEY = 'Q8oZ1WAdkXVpTint'
authentication = "vasp?API_KEY="+ API_KEY

# request_type, identifier, parameters
request_string = 'https://www.materialsproject.org/rest/v2/{}/{}/{}'
temp = requests.get(request_string.format('materials','mp-1234', authentication))
# print(request_string.format('materials','mp-1234', authentication))
temp_dict = temp.json()
pprint(temp_dict)