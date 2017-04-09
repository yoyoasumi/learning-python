# -*- coding: utf-8 -*-

import json
import requests
from requests import exceptions
from requests import Request, Session

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    # response = requests.get(build_uri('users/imoocdemo'))
    response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'))
    print(better_print(response.text))


def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)


def json_request():
    # response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'),
    #                           json={'name': 'babymc89', 'email': 'hellowhat@imooc.com'})
    response = requests.post(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'),
                             json=['hellohello@hello.com'])
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)


def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        print(better_print(response.text))
        print(response.status_code)


def hard_requests():
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    request = Request('GET', build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), headers=headers)
    preparedReq = request.prepare()
    print(preparedReq.body)
    print(preparedReq.headers)

    try:
        response = s.send(preparedReq, timeout=5)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        print(response.status_code)
        print(response.reason)
        print(response.request.headers)
        print(better_print(response.text))


if __name__ == '__main__':
    # request_method()
    # params_request()
    # json_request()
    # timeout_request()
    hard_requests()
