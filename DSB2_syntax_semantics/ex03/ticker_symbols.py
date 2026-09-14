import sys

def main():
    if len(sys.argv)!=2:
        return

    print(stock_prices(sys.argv[1]))

def stock_prices(value: str):

    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    temp=value.upper()

    if temp not in STOCKS.keys():
        return 'Unknown company'

    nameComp=[k for k,v in COMPANIES.items() if v==temp]

    return f'{nameComp[0]} {STOCKS[temp]}'

if __name__ == '__main__':
    main()
