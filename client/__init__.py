import requests

base_url = 'https://api.coincap.io/v2/'
base_payload = {}
base_headers = {}


def get_assets() -> str:
    """
    Returns a list of all assets
    TODO: add optional params
    """
    method = 'assets'
    url = base_url + method
    response = requests.get(url)
    return response.text


def get_asset(id: str) -> str:
    """
    Returns a specified asset
    """
    method = f'assets/{id}'
    url = base_url + method
    response = requests.get(url)
    return response.text


def get_asset_history(id: str, interval: str='d1', start: str=None, end: str=None) -> str:
    """
    Returns historicy of asset
    """
    method = f'assets/{id}/history?interval={interval}'
    url = base_url + method
    if start:
        method += f'&start={start}'
    if end:
        method += f'&end={end}'
    response = requests.get(url)
    return response.text


def get_asset_markets(id: str) -> str:
    """
    Returns markets associated with assets
    TODO: optional params
    """
    method = f'assets/{id}/markets'
    url = base_url + method
    response = requests.get(url)
    return response.text


def get_rates() -> str:
    """
    Returns rates 
    """
    method = 'rates'
    url = base_url + method
    response = requests.get(url)
    return response.text


def get_rate(id: str) -> str:
    """
    Returns rates by id
    """
    method = f'rates/{id}'
    url = base_url + method
    response = requests.get(url)
    return response.text


def get_exchanges() -> str:
    """
    Returns exchanges
    """
    method = f'exchanges'
    url = base_url + method
    response = requests.get(url)
    return response.text


def get_exchange(id: str) -> str:
    """
    Returns specified exchange
    """
    method = f'exchanges/{id}'
    url = base_url + method
    response = requests.get(url)
    return response.text


def get_markets() -> str:
    """
    Returns markets
    TODO: optional params
    """
    method = 'markets'
    url = base_url + method
    response = requests.get(url)
    return response.text


def get_candles(exchange: str, interval: str, base: str, quote: str) -> str:
    """
    Returns OHLCV candles for charting
    TODO: optional params
    """
    method = f'candles?exchange={exchange}&interval={interval}&baseId={base}&quoteId={quote}'
    url = base_url + method
    response = requests.get(url)
    return response.text
