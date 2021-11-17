# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 16:27
@File     ：filmeserialegratis_org.py
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
    response = sess.get(url, proxies=proxies, timeout=(15, 15))
    html = response.text
    try:
        src = re.findall('<iframe src="(.*?)"', html)[0]
        if src:
            return 0
        else:
            return 'state:offline'
    except:
        return 'state:offline'