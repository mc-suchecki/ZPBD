INSERT INTO bike_stations (object_id, location, station_nr, bikes, stands, station_coordinates)
VALUES (0,'asd',0,0,0, ST_GeographyFromText('SRID=4326;POINT(0 49)') );

SELECT location FROM bike_stations WHERE ST_DWithin(station_coordinates, ST_GeographyFromText('SRID=4326;POINT(-110 29)'), 1000000);