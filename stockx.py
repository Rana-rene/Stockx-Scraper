import requests
import json
import pandas as pd


def parser(data):
    dict = {}
    for doc in data:
        prod_id = data[doc]
        shoe_size = prod_id.get('shoeSize')
        lowest_ask = prod_id['market']['lowestAsk']
        dict[shoe_size] = lowest_ask
    return dict

# Set the URL of the shoe you want to scrape
def search(query):
    url = f'https://www.stockx.com/api/browse?_search={query}'

    # Set the headers to make it appear as a legitimate user
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'x-requested-with': 'XMLHttpRequest',
        'app-platform': 'Iron',
        'app-version': '2022.05.08.04',
        'referer': 'https://stockx.com/'
        }

    # Send a GET request to the URL with headers
    html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)
    return output['Products'][0]


def get_sizes(id):
    url = f'https://stockx.com/api/products/{id}?includes=market&currency=USD&country=US'

    # url = 'https://stockx.com/api/products/5e6a1e57-1c7d-435a-82bd-5666a13560fe?includes=market&currency=USD&country=US'
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'x-requested-with': 'XMLHttpRequest',
        'app-platform': 'Iron',
        'app-version': '2022.05.08.04',
        'referer': 'https://stockx.com/'
    }

    html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)


    children_data = output['Product']['children']

    final = parser(children_data)
    return final








# https://stockx.com/api/products/5e6a1e57-1c7d-435a-82bd-5666a13560fe?includes=market&currency=USD&country=US

