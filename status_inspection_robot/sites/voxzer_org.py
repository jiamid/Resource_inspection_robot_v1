# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 16:25
@File     ：voxzer_org.py
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
    keyid = re.findall('/view/(\w+)', url)[0]
    api_url = 'https://player.voxzer.org/list/{}'.format(keyid)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55',
        'referer': url,
    }
    resp = sess.get(api_url, proxies=proxies, timeout=(15, 15), headers=headers)
    data = resp.json()
    try:
        download_url = data['link']
        if download_url:
            return 0
        else:
            return 'state:offline'
    except:
        return 'state:offline'