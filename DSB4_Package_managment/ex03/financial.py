#!/usr/bin/env python3

import sys
import time
import requests
from bs4 import BeautifulSoup

def get_page(ticker: str, field_name: str) -> tuple:

    ticker = ticker.upper()
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://finance.yahoo.com"
}


    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ConnectionError(f"Failed to access Yahoo Finance: {response.status_code}")

    time.sleep(5)

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("div", class_="tableBody")
    if not table:
        raise AttributeError("Could not find financial table on the page.")


    row_title = table.find("div", class_="rowTitle", title=field_name)
    if not row_title:
        raise AttributeError(f"Field '{field_name}' not found.")

    row_container = row_title.find_parent(class_="row")
    values = row_container.find_all("div", class_="column")

    return tuple([field_name] + [value.text.strip() for value in values[1:]])

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print(f"Usage: {sys.argv[0]} <TICKER> <FIELD>")
            sys.exit(1)

        ticker = sys.argv[1]
        field = sys.argv[2]

        result = get_page(ticker, field)
        print(result)

    except (AttributeError, ConnectionError, Exception) as e:
        print(f"Error: {e}")
        sys.exit(1)
