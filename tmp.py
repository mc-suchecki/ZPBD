""" Python script that loads data about Veturilo stations from Warsaw public API."""
__author__ = 'mc'

import requests
import json


# constants for accessing the Warsaw Data API
API_URL = "https://api.um.warszawa.pl/api/action/wfsstore_get"
API_KEY = "ba0152ab-ce64-4835-8d93-49d8f1f1f2dc"

# constants for building the request URL
STATIONS_MAP_ID = "a08136ec-1037-4029-9aa5-b0d0ee0b9d88"
ROADS_MAP_ID = "07f8275c-7ae5-4b74-a429-da94dbfa28bd"
PILKA_NOZNA_ID = "9317a2dc-d08a-41bc-874d-01cc2dc88006"
FILTER_PREFIX = "<Filter><PropertyIsEqualTo><PropertyName>NR_STACJI</PropertyName><Literal>"
FILTER_SUFFIX = "</Literal></PropertyIsEqualTo></Filter>"
MIN_STATION_NR = 6300
MAX_STATION_NR = 6467

url = API_URL + "?id=" + STATIONS_MAP_ID + "&apikey=" + API_KEY + "&filter=" + FILTER_PREFIX + str(6300) + FILTER_SUFFIX
response = json.loads(requests.get(url).text)
print json.dumps(response, indent=2, sort_keys=True)
url = API_URL + "?id=" + STATIONS_MAP_ID + "&apikey=" + API_KEY + "&filter=" + FILTER_PREFIX + str(6301) + FILTER_SUFFIX
response = json.loads(requests.get(url).text)
print json.dumps(response, indent=2, sort_keys=True)