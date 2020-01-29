#!/usr/bin/env bash

docker stop mymdb
docker rm mymdb
docker build . -t mymdb:latest
docker run \
    --name mymdb \
    -e SOMEVAR=foo \
    -p 8031:80  \
    --network host \
    -e DJANGO_DB_HOST=db
    -e DJANGO_DB_PORT=5434
    -e DJANGO_DB_USER=postgres
    -e DJANGO_DB_NAME=moviedb05
    -e DJANGO_DB_PASSWORD=allN1ghtL0ng22
    mymdb:latest
#   --detach \
