# dvirt

Deployment & Virtualization Epita assignment

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
-> some test images (jpg/png/...) from [Unsplash](https://unsplash.com) and [Ephemere](https://club-ephemere.fr) are available at ./imgs/*

* both scripts will run the built image with -d (background)
* built image's name: histograme[_web] depending on which script is used

If filename not allowed (see src/app.py:HistograMe())  
--> will return HTTP 500 (Flask)

Notes:
It is possible to drastically lower the image size by :
- using a smaller base image like alpine or busybox  
requires to install all numpy dependencies by hand
- going FROM scratch  
even worse
- not using Python  
for instance, check: https://github.com/alexkirsz/dvirt that uses Rust
- use an executable packer like UPX
