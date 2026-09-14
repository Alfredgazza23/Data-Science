import sys

def main():
    if len(sys.argv)!=2:
        return

    temp=sys.argv[1].split(',')

    temp = [value.strip() for value in temp]

    if '' in temp:
        return

    all_stocks(temp)

def all_stocks(values: list):

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

    for value in values:
        if value.title() in COMPANIES.keys():
            print(f'{value.capitalize()} stock price is {STOCKS[COMPANIES[value.capitalize()]]}')
        elif value.upper() in STOCKS.keys():
            nameComp=[k for k,v in COMPANIES.items() if v==value.upper()]
            print(f'{value.upper()} is a ticker symbol for {nameComp[0]}')
        else:
            print(f'{value} is an unknown company or an unknown ticker symbol')

if __name__ == '__main__':
    main()
