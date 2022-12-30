
def get_prices():
    url = "https://api.coinpaprika.com/v1/tickers"
    response = requests.get(url)
    response_json = response.json()

    for currency in response_json:
        symbol = currency["symbol"]
        if "price_usd" in currency:
            price = currency["price_usd"]
            prices[symbol] = price

    return prices

