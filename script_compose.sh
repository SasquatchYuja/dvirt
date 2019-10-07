#!/bin/sh

# avoid copying too much files in the image
unalias rm
rm ./*~ ./*# ./src/*~ ./src/*# ./src/*.jpg ./src/*.png ./src/*.jpeg
rm -r ./__pycache__ ./src/__pycache__

# docker-compose -p histograme up [--no-start] [--force-recreate] -d
docker-compose -p histograme up -d

# docker image prune -f # delete dangling images (multi-stage build)
