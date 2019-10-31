# coincap-client
rest api wrapper for hitting the coincap.io api

API Documentation Here:
https://docs.coincap.io/?version=latest

## Installation
git clone this

## Usage
List of Function calls. Please see api docs for more information
```python
import client

assets = client.get_assets()
btc = client.get_asset('bitcoin')
btc_history = client.get_asset_history('bitcoin')
btc_markets = client.get_asset_markets('bitcoin')
rates = client.get_rates()
btc_rates = client.get_rate('bitcoin')
exchanges = client.get_exchanges()
kraken = client.get_exchange('kraken')
markets = client.get_markets()
btc_usd_candles = client.get_candles('kraken', 'd1', 'bitcoin', 'united-states-dollar')
```
## TODO
[] implement optional args on some api calls
[] json dictionary dump helper function
[] could build out functionality to be a full client, etc
