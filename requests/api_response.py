# -*- coding: utf-8 -*-

import requests

response = requests.get('https://api.github.com')
# response = requests.get('http://api.github.com')
print('>>> Response: ', response)
print('>>> DIR: ', dir(response))
print('>>> Status Code: ', response.status_code)
print('>>> Reason: ', response.reason)
print('>>> Headers: ', response.headers)
print('>>> URL: ', response.url)
print('>>> Redirect History: ', response.history)  # [<Response [301]>]
print('>>> Elapsed: ', response.elapsed)
print('>>> Request: ', response.request)
print('>>> Request Headers: ', response.request.headers)
print('>>> Request Method: ', response.request.method)

print('>>> Encoding: ', response.encoding)
print('>>> RAW Read: ', response.raw.read(10))
print('>>> Content(byte): ', response.content, type(response.content))
print('>>> Text(str): ', response.text, type(response.text))
print('>>> Json(dict): ', response.json(), type(response.json()))
print('>>> Team URL: ', response.json()['team_url'])
