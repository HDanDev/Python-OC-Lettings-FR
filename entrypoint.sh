#!/bin/bash
python manage.py collectstatic --noinput
./start.sh
