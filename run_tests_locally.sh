#!/bin/bash

pytest -n 4 -v -ra --alluredir=reports "$@"
