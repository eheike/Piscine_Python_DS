from bs4 import BeautifulSoup
import sys
import requests
import time

def parse_html_yahoo():
    if len(sys.argv) != 3:
        raise Exception("Incorrect data")
    time.sleep(5)
    html_yahoo = requests.get(f"https://finance.yahoo.com/quote/{sys.argv[1]}/financials", headers={'User-Agent' : 'Custom'})
    if html_yahoo.status_code != 200:
        raise Exception("Page is not found")
    soup = BeautifulSoup(html_yahoo.text, "html.parser")
    rows = soup.find_all('div', attrs={'data-test' : 'fin-row'})
    for i in rows:
        if i.find("div", attrs={'title' : sys.argv[2]}) is None:
            raise Exception("Statement name is not found")
        cols = i.find_all('div', {'data-test' : 'fin-col'})
        return tuple([sys.argv[2], *[j.text for j in cols]])
    

if __name__ == "__main__":
    try:
        fin_info = parse_html_yahoo()
    except Exception as err:
        print(err)
    else:
        print(fin_info)
