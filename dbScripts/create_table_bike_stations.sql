CREATE TABLE bike_stations (
	object_id INT PRIMARY KEY,
	location VARCHAR(100),
	station_nr INT,
	bikes VARCHAR(10),
	stands INT,
	station_coordinates GEOMETRY(POINT,2059)
);

CREATE INDEX bike_stations_gix ON bike_stations USING GIST ( station_coordinates );