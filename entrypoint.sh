#!/bin/bash
python manage.py collectstatic --noinput
/app/start.sh
