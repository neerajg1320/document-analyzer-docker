# Install Docker Desktop on macOS


## For deploying production container
##

docker-compose -f docker-compose-deploy.yml up

# Api server on port 8000
# Jquery frontend server on port 4000
# Vuejs frontend server on port 3000


## Trouble Shooting
# Sometime an error happens due to delay in postgres start
# In case we get an error related to authtoken then do following
docker exec -it document-analyzer-docker_db_1 bash
psql -U postgres
drop database app;
#Restart the containers
docker-compose -f docker-compose-deploy.yml up



## For development environment
##

cd api-server-docker
docker-compose -f docker-compose-dev.yml  up
# api server on port 8000

cd frontend-jquery-docker
docker-compose -f docker-compose-dev.yml  up
# http://localhost:8070

cd frontend-vuejs-docker
docker-compose -f docker-compose-dev.yml  up
# http://localhost:8080



