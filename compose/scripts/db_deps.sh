#! /usr/bin/env bash

# PACKAGE
apk add --no-cache gcc make \
    python3-dev tzdata

# DATABASE 

if [[ $SQLALCHEMY_DATABASE_URI =~ ^mysql.* ]] || [ $MYSQL_SERVER ]
then
    echo "MYSQL DEPENDENCIES..."
    apk add --no-cache mariadb-dev build-base libffi-dev
fi
if [[ $SQLALCHEMY_DATABASE_URI =~ ^postgres.* ]] || [ $POSTGRES_SERVER ]
then 
    echo "POSTGRESQL DEPENDENCIES..."
    apk add --no-cache postgresql-dev musl-dev
fi
