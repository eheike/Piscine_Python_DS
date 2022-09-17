import sys

def ticker_sym():
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
    name = sys.argv[1].upper()
    my_key = ""
    for key, value in COMPANIES.items():
        if value==name:
            my_key = key
    if my_key=="":
        print ('Unknown ticker')
        return
    print (my_key, STOCKS[name])
if __name__ == '__main__':
    ticker_sym()