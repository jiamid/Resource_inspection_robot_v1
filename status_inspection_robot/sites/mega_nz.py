# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 16:26
@File     ：mega_nz.py
@Software ：PyCharm
"""
import re
import requests
import random

DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
]
sess = requests.session()
sess.headers.update({'User-Agent': random.choice(DEFAULT_USER_AGENTS)})

def check_url(url, proxies, params):
    api_url = "https://g.api.mega.co.nz/cs?id=0&domain=meganz&v=2&lang=cn"
    ph = re.findall('#\!(\w+)\!', url)[0]
    payload = "[{\"a\":\"g\",\"p\":\"" + ph + "\"}]"
    resp = sess.post(api_url, data=payload, proxies=proxies, timeout=(15, 15))
    data = resp.json()
    try:
        if data[0]['err'] == -6:
            return 'state:offline'
        else:
            return 0
    except:
        return 0