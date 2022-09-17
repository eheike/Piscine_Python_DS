import sys

def all_stocks():
    if len(sys.argv) != 2:
        return
    
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
    PRICE_DICT = dict(zip(COMPANIES.keys(), STOCKS.values()))
    PRICE_DICT = {key.lower(): value for key, value in PRICE_DICT.items()}
    TICKERS_DICT = {key.lower(): value for value, key in COMPANIES.items()}
    expr = sys.argv[1].replace(" ", "").split(',')
    for i in expr:
        if not i:
            print()
            return
    for i in expr:
        i = i.lower()
        if i in PRICE_DICT.keys():
            print (f"{i.capitalize()} stock price is {PRICE_DICT[i]}")
        elif i in TICKERS_DICT.keys():
            print (f"{i.upper()} is a ticker symbol for {TICKERS_DICT[i]}")
        else:
            print (f"{i.capitalize()} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    all_stocks()