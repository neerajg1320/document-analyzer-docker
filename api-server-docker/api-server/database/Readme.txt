# To manually dump the database use following commands:

docker exec -it document-analyzer-docker_app_1 bash

# The postgres hostname is 'db'. We should be able to ping it
PGPASSWORD=Postgres123 pg_dump -h db -U postgres app > /database/postgres_database_dump.sql
