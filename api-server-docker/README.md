
## For Developement process (docker-compose-dev.yml)
docker-compose -f docker-compose-dev.yml up --build
 - During development the code is not copied into the images
 - The code is mounted using volume
 - The database script is also mounted
 
## For creating production build (docker-compose.yml)
docker-compose up --build
docker commit api-server-docker_app_1
docker tag <hash> neeraj76/analyzer-api-server
docker push neeraj76/analyzer-api-server

 - The code is copied into the images
 - The database script is copied into the image
 - We create an image out of the container.
 - We upload the created image to docker hub.
 
## For using production build (docker-compose-deploy.yml)
docker-compose -f docker-compose-deploy.yml up --build
    - The image is directly downloaded from docker hub.
    


docker-compose -f docker-compose-dev.yml up --build
##
Two containers are created:
app:
    debian: 10 (buster)
    python: 3.7
    poppler: 20.08.0
    psql: 
    
db:
    postgres10
##


## Deployment
# Database: -p is required only if we want to access db from docker host.
# --env , -e, --env-file for providing environment variables to containers 

docker run -h db -p 5432:5432 \
    --env POSTGRES_DB=app \
    --env POSTGRES_USER=postgres \
    --env POSTGRES_PASSWORD=Postgres123 \
    postgres:10-alpine    


Api Server:

docker run -h app -p 8000:8000 \
    --env DB_HOST=db \
    --env DB_NAME=app \
    --env DB_USER=postgres \
    --env DB_PASS=Postgres123 \
    neeraj76/analyzer-api-server
      
##




