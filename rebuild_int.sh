#!/bin/bash
git pull
docker compose -p aequitas-int -f docker-compose-deploy.yml build
docker compose -p aequitas-int -f docker-compose-deploy.yml up -d
cat data.json | docker exec -i aequitas-test-app-1 python manage.py loaddata  --format=json -
