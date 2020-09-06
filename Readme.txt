# Install Docker Desktop on macOS


## For development environment
cd api-server-docker
docker-compose -f docker-compose-dev.yml  up

cd frontend-jquery-docker
docker-compose -f docker-compose-dev.yml  up
# http://localhost:8070

cd frontend-vuejs-docker
docker-compose -f docker-compose-dev.yml  up
# http://localhost:8080

## For production environment

docker-compose up

# Api server on port 8000

# Jquery frontend server on port 4000

# Vuejs frontend server on port 3000

