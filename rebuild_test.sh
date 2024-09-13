#!/bin/bash
git pull
docker compose -p aequitas-test -f docker-compose-deploy.yml build
docker compose -p aequitas-test -f docker-compose-deploy.yml up -d