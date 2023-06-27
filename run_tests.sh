#!/bin/bash

docker_compose="docker-compose -f docker-compose.yaml"
nodes_number=4

put_dockers_down () {
  $docker_compose down --remove-orphans
}

build_dockers () {
  $docker_compose build
}

scale_and_run_grid () {
  $docker_compose up -d --scale chrome="$nodes_number"
  $docker_compose run --rm python sh -c /ta_framework/wait_for_grid.sh
}

run_test () {
  $docker_compose run --rm python sh -c "pytest /ta_framework/tests -n $nodes_number -v -ra --alluredir=reports"
}

put_dockers_down
build_dockers
scale_and_run_grid
run_test
put_dockers_down
