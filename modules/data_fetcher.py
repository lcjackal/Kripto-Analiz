import requests

class DataFetcher:
    def __init__(self, coinmarketcap_key, coingecko_key):
        self.coinmarketcap_key = coinmarketcap_key
        self.coingecko_key = coingecko_key
        self.session = requests.Session()

    def fetch_coinmarketcap_data(self, query):
        url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/info"
        headers = {"X-CMC_PRO_API_KEY": self.coinmarketcap_key}
        params = {"symbol": query.upper()}
        response = self.session.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get(query.upper(), {})
        else:
            print(f"Error fetching CoinMarketCap data: {response.text}")
            return {}

    def fetch_coingecko_data(self, query):
        url = f"https://api.coingecko.com/api/v3/coins/{query.lower()}"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching CoinGecko data: {response.text}")
            return {}

    def get_coin_data(self, query):
        # Fetch data from both APIs and merge
        cmc_data = self.fetch_coinmarketcap_data(query)
        cg_data = self.fetch_coingecko_data(query)

        if cmc_data or cg_data:
            return {
                "name": cmc_data.get("name", cg_data.get("name")),
                "symbol": cmc_data.get("symbol", cg_data.get("symbol")),
                "logo": cmc_data.get("logo", cg_data.get("image", {}).get("large")),
                "price": cg_data.get("market_data", {}).get("current_price", {}).get("usd"),
                "contract": cg_data.get("platforms", {}).get("ethereum", ""),
                "network_logo": "https://etherscan.io/images/brandassets/etherscan-logo-circle.png" if "ethereum" in cg_data.get("platforms", {}) else ""
            }
        return {}