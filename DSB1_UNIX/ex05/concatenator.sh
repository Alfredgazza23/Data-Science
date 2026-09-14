#!/bin/sh

OUTPUT="hh_concatenated.csv"

if [ -f "$OUTPUT" ]; then
  rm "$OUTPUT"
fi

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > "$OUTPUT"

for file in *.csv; do
  if [ "$file" != "$OUTPUT" ]; then
    tail -n +2 "$file" >> "$OUTPUT"
  fi
done

if [ $? -eq 0 ]; then
  echo "Concatenation completed successfully."
else
  echo "Error during concatenation."
  exit 1
fi
