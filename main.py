import requests
import hmac
import hashlib
import time
import base64
import json


#message = ''.join([timestamp, method, request_path, body])

def read_cfg():
    return(open("cbpro.cfg", 'r').read().splitlines())



def get_auth_headers(timestamp, message, api_key, secret_key, passphrase): #Taken from cbpro
    message = message.encode('ascii')
    hmac_key = base64.b64decode(secret_key)
    signature = hmac.new(hmac_key, message, hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
    return {
        'Content-Type': 'Application/JSON',
        'CB-ACCESS-SIGN': signature_b64,
        'CB-ACCESS-TIMESTAMP': timestamp,
        'CB-ACCESS-KEY': api_key,
        'CB-ACCESS-PASSPHRASE': passphrase
    }

def get_current_price(product_id):
    method = 'GET'
    endpoint = "/currencies/" + product_id
    body = ''

    message = ''.join([str(time.time()), method, endpoint, body])
    return([method, endpoint, message])

def get_all_currencies():
    method = 'GET'
    endpoint = '/currencies'
    body = ''
    message = ''.join([str(time.time()), method, endpoint, body])
    return([method, endpoint, message])

def get_price_history(product_id, granularity, start, end):
    return

def get_url(endpoint):
    base_url = 'https://api.exchange.coinbase.com'
    url = base_url + endpoint
    return(url)

def main():
    data = read_cfg()
    api_key = data[0]
    api_secret = data[1]
    api_passphrase = data[2]

    base_url = 'https://api.exchange.coinbase.com'

    timestamp = str(time.time())
    method = "GET"
    request_path = "/accounts"
    body = ''

    url = base_url + request_path





    message = ''.join([timestamp, method, request_path, body])
    headers = get_auth_headers(timestamp, message, api_key, api_secret, api_passphrase)
    response = requests.request(method, url, headers=headers)

    print(response.text)
    print("------------")



    #return([method, endpoint, message])

    call = get_all_currencies()
    method = call[0]
    full_url = base_url + call[1]
    message = call[2]


    headers = get_auth_headers(str(time.time()), message, api_key, api_secret, api_passphrase)

    response = requests.request(method, full_url, headers=headers)
    print(response.text)

    currencies = json.loads(response.text)
    print(currencies)

    for coin in currencies:
        print(coin)


if __name__ == "__main__":
    main()