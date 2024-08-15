#!/bin/bash

touch .env && . .env
[ -d .venv ] && echo "venv already exists" || python -m venv .venv
[ -n "$VIRTUAL_ENV" ] && echo "already in venv" || source .venv/bin/activate
python -m pip install -r requirements.txt
[ -n "$SECRET_KEY" ] && echo "secret key in environment already" || SECRET_KEY=$(tr -dc "A-Za-z0-9" </dev/urandom | head -c 30)
grep -q "SECRET_KEY=" .env && echo "key already in .env" || echo "export SECRET_KEY=$SECRET_KEY" >>.env

cd cnf
python manage.py migrate
