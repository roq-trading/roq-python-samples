#!/usr/bin/env bash

echo -e "\033[1;34m--- ENV ---\033[0m"

env | sort

echo -e "\033[1;34m--- PIP ---\033[0m"

ls -ahl

$PYTHON -m pip install . -vvv

echo -e "\033[1;34m--- DONE ---\033[0m"
