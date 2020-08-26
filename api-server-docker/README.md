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