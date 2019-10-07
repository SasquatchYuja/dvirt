#!/bin/sh

# avoid copying too much files in the image
unalias rm
rm ./*~ ./*# ./src/*~ ./src/*# ./src/*.jpg ./src/*.png ./src/*.jpeg
rm -r ./__pycache__ ./src/__pycache__

# docker build -t histograme [--no-cache=true] .
docker build -t histograme .

# docker image prune -f # delete dangling images (multi-stage build)
docker run --rm -p 5000:5000 -d -ti histograme
