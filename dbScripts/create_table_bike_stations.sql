CREATE TABLE bike_stations (
	object_id INT PRIMARY KEY,
	location VARCHAR(100),
	station_nr INT,
	bikes INT,
	stands INT,
	station_coordinates GEOGRAPHY(POINT,4326)
);

CREATE INDEX bike_stations_gix ON bike_stations USING GIST ( station_coordinates );