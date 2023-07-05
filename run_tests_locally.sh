#!/bin/bash

pytest -n 4 -rxXsva --alluredir=reports "$@"
