#!/bin/bash
git pull
docker compose -p aequitas-int -f docker-compose-deploy.yml build
docker compose -p aequitas-int -f docker-compose-deploy.yml up -d