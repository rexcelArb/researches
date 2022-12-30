
import requests
import json


API_KEY = "4b9b2e12-caac-4075-8c5b-8633b0163a1f"


def get_prices():
    url = "https://pro-api.coinmarketcap.com/v1/exchange/quotes/latest"
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {
        "id": "1,2,3,4,5,6,7,8,9,10",
        "symbol": "ETH",
        "convert": "USD",
    }
    response = requests.get(url, headers=headers, params=params)
    response_json = response.json()


    prices = {}
    for exchange in response_json["data"]:
        name = exchange["name"]
        price = exchange["quote"]["USD"]["price"]
        prices[name] = price

    return prices


def find_arbitrage(prices):

    table = PrettyTable()
    table.field_names = ["Exchange", "Price"]


    for exchange in prices:
        price = prices[exchange]
        table.add_row([exchange, price])


    print(table)


def main():

    prices = get_prices()


    find_arbitrage(prices)


if __name__ == "__main__":
    main()
