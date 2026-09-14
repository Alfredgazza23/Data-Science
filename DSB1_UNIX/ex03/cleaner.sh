#!/bin/sh

INPUT="../ex02/hh_sorted.csv"
OUTPUT="hh_positions.csv"

if [ ! -f "$INPUT" ]; then
  echo "Error: $INPUT not found."
  exit 1
fi

awk -F ',' '
BEGIN { OFS = "," }

NR == 1 {
  print $0
  next
}

{
  # Убираем кавычки из нужных полей
  gsub(/^"|"$/, "", $3)

  # Ищем позиции
  pos = "-"
  if (tolower($3) ~ /junior/) pos = "Junior"
  if (tolower($3) ~ /middle/) pos = (pos == "-" ? "Middle" : pos "/Middle")
  if (tolower($3) ~ /senior/) pos = (pos == "-" ? "Senior" : pos "/Senior")

  # Собираем новую строку
  print $1, $2, "\"" pos "\"", $4, $5
}
' "$INPUT" > "$OUTPUT"

echo "Cleaning completed successfully."
