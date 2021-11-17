# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 16:25
@File     ：oboom_com.py
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
    keyid = re.search(r'oboom.com/(.*)', url).group(1)
    resp = sess.get(url, proxies=proxies, timeout=(15, 15))
    html = resp.text
    token = re.search(r'Token : \{Session : "(.*?)"', html).group(1)

    api_url = 'https://api.oboom.com/1/ls'
    p_data = {
        "token": token,
        "item": keyid,
        'http_errors': 0
    }
    resp = sess.post(api_url, proxies=proxies, timeout=(15, 15), data=p_data)
    html = resp.text
    # print html
    if ('403 Forbidden' in html) or (resp.status_code == 403):
        raise ValueError(403, 'IPBlock')

    if '"state":"online"' not in html:
        return 'state:offline'
    else:
        return 0