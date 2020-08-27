if [[ $# -lt 3 ]]
then
  echo "Usage: $0 <user> <password> <host>"
  exit 1
fi

PG_USER=$1
PG_PASSWORD=$2
PG_HOST=$3

export PGUSER=$PG_USER
export PGPASSWORD=$PG_PASSWORD

# The above variables ensure that we don't need to add the value in the command
# PGPASSWORD=Postgres123 psql -h db -U postgres app < /install/postgres_database_dump.sql

APP_DATABASE_FILE="./postgres_database_dump.sql"
APP_DATABASE_NAME="app"
DOCUMENTS_DATABASE_NAME="docminer"


# Command to list the remote databases
# PGPASSWORD=Postgres123 psql -h db -U postgres -c "\l"

APP_DATABASE_EXISTS=`PGPASSWORD=Postgres123 psql -h db -U postgres -c "\l" |grep $APP_DATABASE_NAME |wc -l`

echo "APP_DATABASE_EXISTS: $APP_DATABASE_EXISTS"

## If the database exists then delete it
FORCE_DELETE=0
if [[ $APP_DATABASE_EXISTS -gt 0  && $FORCE_DELETE -gt 0 ]]
then
    DELETE_DATABASE_COMMAND="'drop database $APP_DATABASE_NAME;'"
    SH_COMMAND="psql -h $PG_HOST -c $DELETE_DATABASE_COMMAND"
    echo "$SH_COMMAND"
    eval "$SH_COMMAND"

    DELETE_DATABASE_COMMAND="'drop database $DOCUMENTS_DATABASE_NAME;'"
    SH_COMMAND="psql -h $PG_HOST -c $DELETE_DATABASE_COMMAND"
    echo "$SH_COMMAND"
    eval "$SH_COMMAND"

    APP_DATABASE_EXISTS=0
fi

## Create the database if it does not exist
SUPPRESS_DATA_INITIALIZATION=0
if [[ $APP_DATABASE_EXISTS -lt 1 && $SUPPRESS_DATA_INITIALIZATION -lt 1 ]]
then

    CREATE_DATABASE_COMMAND="'create database $DOCUMENTS_DATABASE_NAME with owner $PG_USER;'"
    SH_COMMAND="psql -h $PG_HOST -c $CREATE_DATABASE_COMMAND"
    echo "$SH_COMMAND"
    eval "$SH_COMMAND"

    CREATE_DATABASE_COMMAND="'create database $APP_DATABASE_NAME with owner $PG_USER;'"
    SH_COMMAND="psql -h $PG_HOST -c $CREATE_DATABASE_COMMAND"
    echo "$SH_COMMAND"
    eval "$SH_COMMAND"

    psql -h $PG_HOST $APP_DATABASE_NAME < $APP_DATABASE_FILE
fi
