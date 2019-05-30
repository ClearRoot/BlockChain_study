from django.shortcuts import render
import os
import requests
import configparser # 설정값 관리하기, 내장모듈
from inspect import getcallargs
import base64
import hashlib
import hmac
import json
import time
import httplib2
# Create your views here.

access_token = os.getenv('access_token')
secret_key = os.getenv('secret_key')

ACCESS_TOKEN = str(access_token)
SECRET_KEY = bytes(str(secret_key), 'utf-8')


def get_encoded_payload(payload):
    payload['nonce'] = int(time.time() * 1000)

    dumped_json = json.dumps(payload)
    encoded_json = base64.b64encode(bytes(dumped_json, 'utf-8'))
    return encoded_json


def get_signature(encoded_payload):
    signature = hmac.new(SECRET_KEY, encoded_payload, hashlib.sha512)
    return signature.hexdigest()


def get_response(action, payload):
    url = '{}{}'.format('https://api.coinone.co.kr/', action)

    encoded_payload = get_encoded_payload(payload)

    headers = {
        'Content-type': 'application/json',
        'X-COINONE-PAYLOAD': encoded_payload,
        'X-COINONE-SIGNATURE': get_signature(encoded_payload),
    }

    http = httplib2.Http()
    response, content = http.request(url, 'POST', body=encoded_payload, headers=headers)

    return content


# balance
print(get_response(action='v2/account/balance', payload={
    'access_token': ACCESS_TOKEN,
}))

# # limit buy
# print(get_response(action='v2/order/limit_buy', payload={
#     'access_token': ACCESS_TOKEN,
#     'price': '4241000.0',
#     'qty': '0.1',
#     'currency': 'BTC',
# }))

# # limit sell
# print(get_response(action='v2/order/limit_sell', payload={
#     'access_token': ACCESS_TOKEN,
#     'price': '4241000.0',
#     'qty': '0.1',
#     'currency': 'BTC',
# }))

# limit order
print(get_response(action='v2/order/limit_orders', payload={
    'access_token': ACCESS_TOKEN,
    'currency': 'BTC',
}))


# cancel order
# print(get_response(action='v2/order/cancel', payload={
#     'access_token': ACCESS_TOKEN,
#     'order_id': 'eeee8cab-a35a-43e5-8c47-d3c79c20d808',
#     'price': '4241000.0',
#     'qty': '0.1',
#     'is_ask': '1',
#     'currency': 'BTC',
# }))


    
# https://docs.python.org/3/library/inspect.html
# https://wikidocs.net/12065

# exec $SHELL
# echo export 'token="<token>"' >> ~/.bashrc
# c9 ~/.bashrc