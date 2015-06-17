#!/usr/bin/env bash

# setup postgres
sudo service postgresql start
sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password 'password';"
echo 'local   all         postgres                          md5' >> /etc/postgresql/9.4/main/pg_hba.conf
sudo service postgresql restart

# create db
psql -U postgres postgres -f ./db/create_db.sql