
import requests
import json


API_KEY = "4b9b2e12-caac-4075-8c5b-8633b0163a1f"


def get_prices():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {
        "start": "1",
        "limit": "10",
        "convert": "USD",
    }
    response = requests.get(url, headers=headers, params=params)
    response_json = response.json()


    prices = {}
    for currency in response_json["data"]:
        symbol = currency["symbol"]
        price = currency["quote"]["USD"]["price"]
        prices[symbol] = price

    return prices


def find_arbitrage(prices):
    for symbol1 in prices:
        for symbol2 in prices:
            if symbol1 == symbol2:
                continue

            price1 = float(prices[symbol1])
            price2 = float(prices[symbol2])

            if price1 > price2:
                print(f"{symbol1} is trading higher than {symbol2}")
            elif price2 > price1:
                print(f"{symbol2} is trading higher than {symbol1}")


def main():
    prices = get_prices()

    find_arbitrage(prices)

if __name__ == "__main__":
    main()
