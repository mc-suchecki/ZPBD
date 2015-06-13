#!/usr/bin/env bash

# install the database (Ubuntu only)
sudo apt-get install -y postgresql
sudo apt-get install -y pgadmin3
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >> /etc/apt/sources.list'
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y postgresql-9.4-postgis-2.1 pgadmin3 postgresql-contrib

# install the Python dependecies
sudo pip install -r requirements.txt
