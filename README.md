# DVIRT Epita assignment

Dockerize a basic image processing (histogram) API using Flask,
trying to make the docker image as small as possible

Final image size: ~160MB

see: ./subject/*.html

Usage :
- script_compose.sh
Using docker-compose up

OR

- script_simple.sh
Using docker build and docker run

Run the following line after having started the docker container:
src/client.py imgs/img.jpg

* both scripts will run the built image with -d
* built image's name: histograme[_web] depending on which script is used
* some test images (jpg/png/...) are available at ./imgs/*

If filename not allowed (see src/app.py:HistograMe())
--> will return HTTP 500

Notes:
It is possible to drastically lower the image size by :
- using a smaller base image like alpine or busybox
requires to install all numpy dependencies by hand
- going FROM scratch
even worse
- not using Python
for instance, check: https://github.com/alexkirsz/dvirt that uses Rust
