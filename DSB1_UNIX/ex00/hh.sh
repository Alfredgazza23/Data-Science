#!/bin/sh

if [ $# -eq 0 ]; then
  echo "Invalid request: please provide a vacancy name as an argument."
  echo "Example: ./hh.sh \"data scientist\""
  exit 1
fi

SEARCH="$*"

ENCODE=$(echo "$SEARCH" | sed 's/ /+/g')

if curl -s "https://api.hh.ru/vacancies?text=$ENCODE&per_page=20"| jq .  > hh.json; then
  echo "Saved in hh.json"
else
  echo "Request error during JSON processing"
  exit 1
fi
