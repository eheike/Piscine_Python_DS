import sys

def stock_prices():
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
    my_key = sys.argv[1].capitalize()
    if my_key in COMPANIES:
        print (STOCKS[COMPANIES[my_key]])
    else:
        print ('Unknown company')
if __name__ == '__main__':
    stock_prices()