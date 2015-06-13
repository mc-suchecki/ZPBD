""" Python script that loads data about Veturilo stations from Warsaw public API."""
__author__ = 'mc'

import requests
import psycopg2


# constants for accessing the Warsaw Data API
API_URL = "https://api.um.warszawa.pl/api/action/wfsstore_get"
API_KEY = "d477ba05-8d49-4630-8d03-a4a8d24798bd"

# constants for building the request URL
MAP_ID = "a08136ec-1037-4029-9aa5-b0d0ee0b9d88"
FILTER_PREFIX = "<Filter><PropertyIsEqualTo><PropertyName>NR_STACJI</PropertyName><Literal>"
FILTER_SUFFIX = "</Literal></PropertyIsEqualTo></Filter>"
MIN_STATION_NR = 6300
MAX_STATION_NR = 6467


def is_response_valid(response):
    """ checks if response from API is valid """
    if response.status_code != 200:
        return False
    if isinstance(response.json()["result"], dict):
        return True
    return False


def store_station_in_db(data, cursor, connection):
    """ stores station data in PostGIS database """
    object_id = data["featureMemberProperties"][0]["OBJECTID"]
    location = data["featureMemberProperties"][0]["LOKALIZACJA"]
    station_nr = data["featureMemberProperties"][0]["NR_STACJI"]
    bikes = data["featureMemberProperties"][0]["ROWERY"]
    stands = data["featureMemberProperties"][0]["STOJAKI"]
    latitude = data["featureMemberCoordinates"][0]["latitude"]
    longitude = data["featureMemberCoordinates"][0]["longitude"]
    sql = "INSERT INTO bike_stations (object_id, location, station_nr, bikes, stands, station_coordinates) "
    sql += "VALUES (%s, %s, %s, %s, %s, ST_GeographyFromText('SRID=4326;POINT(%s %s)') );"
    cursor.execute(sql, (object_id, location, station_nr, bikes, stands, latitude, longitude))
    connection.commit()
    print("OK")


# connect to the database and get cursor
connection = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
cursor = connection.cursor()

# load the bike stations
stations_loaded = 0
for number in range(MIN_STATION_NR, MAX_STATION_NR + 1):
    successful = False
    url = API_URL + "?id=" + MAP_ID + "&apikey=" + API_KEY + "&filter=" + FILTER_PREFIX + str(number) + FILTER_SUFFIX
    while not successful:
        print("Downloading data for station number " + str(number) + "... ", end="")
        response = requests.get(url)
        if is_response_valid(response):
            print("OK")
            print("Storing data for station number " + str(number) + "... ", end="")
            store_station_in_db(response.json()["result"], cursor, connection)
            stations_loaded += 1
            successful = True
        else:
            print("ERROR: ", end="")
            if response.status_code == 200:
                print(response.json()["result"])
            else:
                print(str(response.status_code))

print("Successfully loaded " + str(stations_loaded) + " stations.")

# close communication with the database
cursor.close()
connection.close()
