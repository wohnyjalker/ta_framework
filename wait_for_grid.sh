#!/bin/bash

set -e

max_attempts=300
delay=1

for ((attempt=1; attempt<=max_attempts; attempt++))
do
  echo "Checking Selenium Grid readiness -> attempt number $attempt/$max_attempts"
  if curl -sSL "http://selenium-hub:4444/wd/hub/status" 2>&1 | grep '"ready":' | grep "true" > /dev/null;
  then
    echo "Selenium Grid is ready"
    exit 0
  fi
  echo "Waiting $delay sec for the next check"
  sleep $delay
done

echo "Maximum number of attempts reached -> exit 1"
exit 1
