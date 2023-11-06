from bs4 import BeautifulSoup
import requests
import re

url_cash = "https://minfin.com.ua/currency/"
url_bitcoin = "https://www.binance.com/ru-UA"


def find_curses():
    response = requests.get(url_cash)
    soup = BeautifulSoup(response.text, 'lxml')

    data_buy = soup.find_all('div', {'type': 'cash', 'class': 'sc-1x32wa2-9 bKmKjX'})
    pattern = re.compile(r'\b\d+,\d+\b')

    values = [float(pattern.search(item.text).group().replace(',', '.')) for item in data_buy if
              pattern.search(item.text)]

    dollar_buy = values[0]
    euro_buy = values[2]

    dollar_sale = values[1]
    euro_sale = values[3]

    return [dollar_buy, dollar_sale, euro_buy,  euro_sale]


def find_cripto():
    response = requests.get(url_bitcoin)
    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all('div', class_="css-1d6w3z5")
    values = [div.text.strip() for div in data]

    return [values[0], values[1]]


