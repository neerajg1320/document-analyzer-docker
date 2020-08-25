brew install poppler

python3 -m venv venv3
pip install -r requirements.txt

brew install postgresql
pg_ctl -D /usr/local/var/postgres start
psql postgres

# Import database
psql <databasename> < postgres_database_dump.sql

# Following commands are run on postgres shell
create user postgres with encrypted password 'Postgres123';
create database app;
grant all privileges on database app to postgres;
create database docminer;
grant all privileges on database docminer to postgres;

cd app/
# If running for first time
python manage.py makemigrations core
python manage.py migrate

python manage.py runserver
