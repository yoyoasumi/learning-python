# -*- coding: utf-8 -*-

import requests


def get_key_info(response, *args, **kwargs):
    """callback
    """
    print(response.headers['Content-Type'])


def main():
    """main
    """
    requests.get('https://api.github.com', hooks=dict(response=get_key_info))


if __name__ == '__main__':
    main()
