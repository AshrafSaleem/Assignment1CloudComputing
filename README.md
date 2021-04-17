To build a docket image with the name assignment1_fit5225

`docker build -t assignment1_fit5225 .`

To list out the images that have been build so far

`docker images`

To run the docker image of assignment1_fit5225 with the port set at 5000 and naming it object_detection

`docker run --name object_detection -p 5000:5000 assignment1_fit5225`