INSERT INTO bike_stations (object_id, location, station_nr, bikes, stands, station_coordinates)
VALUES (0,'asd',0,0,0, ST_GeographyFromText('SRID=4326;POINT(0 49)') );

SELECT * FROM bike_stations WHERE ST_DWithin(station_coordinates, ST_GeographyFromText('SRID=4326;POINT(52.1464422 21.0282027)'), 5000);