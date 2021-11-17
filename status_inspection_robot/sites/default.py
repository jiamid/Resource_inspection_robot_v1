# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 15:17
@File     ：default.py
@Software ：PyCharm
"""
import requests
import random
from urllib import parse
import cloudscraper
from status_inspection_robot.config import SUPPORT_DOMAINS_SPECIAL
from status_inspection_robot.config import OFFILE_CONTENTS
from status_inspection_robot.config import OFFILE_CONTENTS_SPECIAL

sess_cf = cloudscraper.create_scraper()
DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
]
sess = requests.session()
sess.headers.update({'User-Agent': random.choice(DEFAULT_USER_AGENTS)})


def check_url(url, proxies, params):
    referer = params.get('referer', None)
    if referer:
        sess.headers.update({'Referer': referer})
    ret = parse.urlparse(url)
    domain = ".".join(ret[1].split('.')[-2:])
    try:
        resp = sess_cf.get(url, proxies=proxies, timeout=(15, 15))  # 部分链接使用cf sess会失败
    except:
        resp = sess.get(url, proxies=proxies, timeout=(15, 15))

    html = resp.text

    if ("We're sorry.  You can't access this item" in html) and 'google.com' in url:
        return 'google offline'

    if ('403 Forbidden' in html) or (resp.status_code == 403):
        raise ValueError(403, 'IPBlock')

    if ('Cache Access Denied' in html):
        raise ValueError(403, 'IPBlock-Cache Access Denied')

    result = None

    if domain in SUPPORT_DOMAINS_SPECIAL:
        contents = OFFILE_CONTENTS_SPECIAL
    else:
        contents = OFFILE_CONTENTS

    for ck in contents:
        if ck in html:
            result = ck
            break

    # ulozto.cz offline
    if 'hledej?q=' in resp.url:
        result = 'hledej?q='

    # print(html)
    if result:
        return result
    elif resp.status_code == 404:
        return 'http 404'
    else:
        return 0
