import sys

def main():
    if len(sys.argv)!=2:
        return

    stock_prices(sys.argv[1])

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

    temp=value.capitalize()

    if temp not in COMPANIES.keys():
        return print('Unknown company')

    temp=COMPANIES[temp]

    print(STOCKS[temp])

if __name__ == '__main__':
    main()
