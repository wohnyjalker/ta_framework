#!/bin/bash

docker-compose -f docker-compose.yaml build
docker-compose -f docker-compose.yaml up -d
docker-compose -f docker-compose.yaml run --rm python sh -c /ta_framework/wait_for_grid.sh
docker-compose -f docker-compose.yaml run --rm python sh -c pytest
docker-compose -f docker-compose.yaml down
