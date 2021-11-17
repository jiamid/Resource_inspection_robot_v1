# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 16:26
@File     ：123moviesfree_ltd.py
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
    keyid = re.findall('id=(\w+)', url)[0]
    api_url = "https://player.fmoviess.cyou/{}".format(keyid)
    resp = sess.get(api_url, proxies=proxies, timeout=(15, 15))
    html = resp.text
    try:
        if '''If the player don't work please click on "SERVERS" and choose another Server To Watch this Movie. Thank You !''' in html:
            return 'state:offline'
        else:
            return 0
    except:
        return 0