#!/bin/sh

INPUT="../ex03/hh_positions.csv"
OUTPUT="hh_uniq_positions.csv"

if [ ! -f "$INPUT" ]; then
  echo "Error: $INPUT not found."
  exit 1
fi

echo "\"name\",\"count\"" > "$OUTPUT"

tail -n +2 "$INPUT" \
| awk -F ',' '{ print $3 }' \
| tr -d '"' \
| sort \
| uniq -c \
| sort -nr \
| awk '{ print "\"" $2 "\",\"" $1 "\"" }' \
>> "$OUTPUT"

if [ $? -eq 0 ]; then
  echo "Counting completed successfully."
else
  echo "Error: Counting failed."
  exit 1
fi
