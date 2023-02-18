#!/bin/sh

if [ "$DATABASE" = "db" ]
then
    echo "Waiting for mysql..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "MYSQL started"
fi

exec "$@"