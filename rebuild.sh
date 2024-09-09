#!/bin/bash
git pull
docker compose -f docker-compose-deploy.yml build
docker compose -f docker-compose-deploy.yml up -d