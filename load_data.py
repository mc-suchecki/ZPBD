__author__ = 'mc'

import requests

# constants for accessing the Warsaw Data API
API_URL = "https://api.um.warszawa.pl/api/action/wfsstore_get"
API_KEY = "d477ba05-8d49-4630-8d03-a4a8d24798bd"

# request example
map_id = "TODO"
url = API_URL + "?id=" + map_id + "&api_key=" + API_KEY
response = requests.get(url)

print(response.status_code)
print(response.json())
