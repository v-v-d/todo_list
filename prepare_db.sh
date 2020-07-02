#!/bin/sh

source config.sh

echo 'Uploading postgresql...'

sudo apt update -y
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql.service

echo 'Creating postgresql user and database...'

sudo -u postgres psql -c "CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD' SUPERUSER CREATEDB;"
sudo -u postgres createdb $POSTGRES_DB

echo 'DB is preparing'
