# -*- coding: utf-8 -*-

import requests


def download_image():
    """demo: Download Image, Text
    """
    url = "http://img5.imgtn.bdimg.com/it/u=4064076728,1079006275&fm=23&gp=0.jpg"

    # without HEADERS
    # response = requests.get(url)
    # print(response.status_code, response.reason)
    # print(response.headers)
    # print(response.content)

    # with HEADERS
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response = requests.get(url, headers=headers, stream=True)

    # print(response.status_code, response.reason)
    # print(response.headers)  # 'Content-Type': 'image/jpeg'
    # print(response.content)
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    """demo: Download Image
    """
    url = "http://img5.imgtn.bdimg.com/it/u=4064076728,1079006275&fm=23&gp=0.jpg"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        with open('demo1.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__ == '__main__':
    download_image_improved()
