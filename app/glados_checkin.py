# -*- coding: utf-8 -*-
import logging
import requests
import os
result = b'success\n'
# url
url = "https://glados.rocks/api/user/checkin"
# cookie
cookie = ''

payload = "{\"token\":\"glados_network\"}"
headers = {
    'authority': 'glados.rocks',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://glados.rocks',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://glados.rocks/console/checkin',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': cookie
}


def main(COOKIE: str):
    global cookie
    cookie = COOKIE
    logger = logging.getLogger()
    response = requests.request("POST", url, headers=headers, data=payload)
    result = response.text
    logger.info(result)
    print(result)
    return result
