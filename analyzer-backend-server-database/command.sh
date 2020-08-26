#!/usr/bin/env bash

pwd && cd \/database && pwd && ls &&        \
cd \/app && pwd && ls &&                    \
python manage.py wait_for_db &&             \
cd \/database && pwd &&                     \
.\/init_db.sh postgres Postgres123 db &&    \
cd \/app && pwd && ls &&                    \
python manage.py migrate --fake &&          \
python manage.py runserver 0.0.0.0:8000