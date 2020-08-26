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




