#!/bin/sh


if [ ! -f "../ex00/hh.json" ]; then
  echo "Error: hh.json not found in ../ex00/"
  exit 1
fi


jq -f filter.jq ../ex00/hh.json > hh.csv


if [ $? -eq 0 ]; then
  echo "Converted to CSV successfully."
else
  echo "Conversion failed."
  exit 1
fi
