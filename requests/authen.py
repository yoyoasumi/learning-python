# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase

BASE_URL = 'https://api.github.com'


def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])


def basic_auth():
    """basic auth
    """
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print(response.text)
    print(response.request.headers)


def basic_oauth():
    headers = {'Authorization': 'token dd6322fa6c57a548268453dc245cbcdc352a7811'}
    response = requests.get(construct_url('user/emails'), headers=headers)
    print(response.request.headers)
    print(response.text)
    print(response.status_code)


class GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = ''.join(['token', self.token])
        return r


def oauth_advanced():
    auth = GithubAuth('dd6322fa6c57a548268453dc245cbcdc352a7811')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print(response.text)


if __name__ == '__main__':
    # basic_auth()
    # basic_oauth()
    oauth_advanced()
