#!/bin/sh

input="../ex01/hh.csv"
output="hh_sorted.csv"

if [ ! -f "$input" ]; then
  echo "Error: $input not found."
  exit 1
fi

head -n 1 "$input" > "$output"

tail -n +2 "$input" | sort -t ',' -k2,2 -k1,1 | cat >> "$output"

if [ $? -eq 0 ]; then
  echo "Sorting completed successfully."
else
  echo "Sorting failed."
  exit 1
fi
