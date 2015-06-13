# ZPBD
Project for Advanced Database Problems - app downloading data about Veturilo bike stations from Warsaw Data API and storing them into PostGIS database.

Installation
-----------
Install Python 3.x, then run the following commands in bash terminal:
```sh
$ git clone git@github.com:mc-suchecki/ZPBD.git
$ cd ZPBD
$ chmod +x ./install.sh
$ ./install.sh
$ chmod +x ./setup_DB.sh
$ ./setup_DB.sh
$ python load_data.py
```

References
-----------
### database installation
http://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS21UbuntuPGSQL93Apt

#### API reference
https://api.um.warszawa.pl/
