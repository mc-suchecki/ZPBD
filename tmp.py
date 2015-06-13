""" Python script that loads data about Veturilo stations from Warsaw public API."""
__author__ = 'mc'

import requests
import json


# constants for accessing the Warsaw Data API
API_URL = "https://api.um.warszawa.pl/api/action/wfsstore_get"
API_KEY = "d477ba05-8d49-4630-8d03-a4a8d24798bd"

# constants for building the request URL
STATIONS_MAP_ID = "a08136ec-1037-4029-9aa5-b0d0ee0b9d88"
ROADS_MAP_ID = "07f8275c-7ae5-4b74-a429-da94dbfa28bd"
FILTER_PREFIX = "<Filter><PropertyIsEqualTo><PropertyName>NR_STACJI</PropertyName><Literal>"
FILTER_SUFFIX = "</Literal></PropertyIsEqualTo></Filter>"
MIN_STATION_NR = 6300
MAX_STATION_NR = 6467

url = API_URL + "?id=" + ROADS_MAP_ID + "&limit=1" + "&apikey=" + API_KEY # + "&filter=" + FILTER_PREFIX + str(number) + FILTER_SUFFIX
response = json.loads(requests.get(url).text)
print json.dumps(response, indent=2, sort_keys=True)