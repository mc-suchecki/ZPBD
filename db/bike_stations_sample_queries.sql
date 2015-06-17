--wstawienie nowego wiersza
INSERT INTO bike_stations (object_id, location, station_nr, bikes, stands, station_coordinates)
VALUES (0,'asd',0,0,0, ST_Transform(ST_GeomFromText('POINT(52.1464422 21.0282027)',4326),2059) );

--Zapytanie 1: wyszukanie stacji w zasiegu 5000m od podanego punktu
SELECT * FROM bike_stations WHERE ST_DWithin(station_coordinates, ST_Transform(ST_GeomFromText('POINT(52.1464422 21.0282027)',4326),2059), 5000);

--Zapytanie 2: odleglosc pomiedzy dwoma stacjami
SELECT ST_Distance(
		(SELECT station_coordinates FROM public.bike_stations WHERE station_nr = 6300),
		(SELECT station_coordinates FROM public.bike_stations WHERE station_nr = 6301)
	)

--Zapytanie 3: znajdz stacje najblizsze dwom punktom
Select 'start' as label, object_id, location, station_nr, bikes, stands, minDist
From bike_stations
INNER JOIN (
	SELECT MIN(distance) minDist FROM (
		Select *, ST_Distance(station_coordinates,ST_Transform(ST_GeomFromText('POINT(52.1464422 21.0282027)',4326),2059)) distance
		From bike_stations
		) asd
) minTab ON ST_Distance(station_coordinates,ST_Transform(ST_GeomFromText('POINT(52.1464422 21.0282027)',4326),2059)) = minTab.minDist
UNION
Select 'end' as label, object_id, location, station_nr, bikes, stands, minDist
From bike_stations
INNER JOIN (
	SELECT MIN(distance) minDist FROM (
		Select *, ST_Distance(station_coordinates,ST_Transform(ST_GeomFromText('POINT(52.2773211 20.8567145)',4326),2059)) distance
		From bike_stations
		) asd
) minTab ON ST_Distance(station_coordinates,ST_Transform(ST_GeomFromText('POINT(52.2773211 20.8567145)',4326),2059)) = minTab.minDist
