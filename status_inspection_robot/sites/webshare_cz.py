# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 16:24
@File     ：webshare_cz.py
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
    keyid = re.search(r'/file/([^/]+)', url).group(1)
    api_url = 'https://en.webshare.cz/api/file_info/'
    p_data = {
        "ident": keyid,
        "maybe_removed": True,
        'wst': ''
    }
    resp = sess.post(api_url, proxies=proxies, timeout=(15, 15), data=p_data)
    html = resp.text
    # print html
    if ('403 Forbidden' in html) or (resp.status_code == 403):
        raise ValueError(403, 'IPBlock')

    if 'File not found' in html:
        return 'File not found'
    else:
        return 0
