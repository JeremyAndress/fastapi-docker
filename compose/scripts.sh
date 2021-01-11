#! /usr/bin/env bash

# PACKAGE
apk add --no-cache gcc make \
    python3-dev tzdata

# DATABASE PACKAGE
if [ $MYSQL_SERVER ]
then
    echo "MYSQL DEPENDENCIES..."
    apk add --no-cache mariadb-dev build-base libffi-dev
elif [ $POSTGRES_SERVER ]
then 
    echo "POSTGRE DEPENDENCIES..."
    apk add --no-cache postgresql-dev musl-dev
fi
