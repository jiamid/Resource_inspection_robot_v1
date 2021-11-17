# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 14:18
@File     ：__init__.py.py
@Software ：PyCharm
"""
from status_inspection_robot.config.offile_contents import offile_contents, offile_contents_special
from status_inspection_robot.config.closed_site_name_domain import closed_site_name_domain
from status_inspection_robot.config.support_domains_normal import support_domains_normal
from status_inspection_robot.config.support_domains_special import support_domains_special
from status_inspection_robot.config.support_domains_script import support_domains_script
from status_inspection_robot.config.url_need_format_domain import url_need_format_domain

ALL_SUPPORT_DOMAINS = support_domains_normal + support_domains_special + url_need_format_domain + support_domains_script
OFFILE_CONTENTS = offile_contents
OFFILE_CONTENTS_SPECIAL = offile_contents_special
SUPPORT_DOMAINS_NORMAL = support_domains_normal
SUPPORT_DOMAINS_SPECIAL = support_domains_special
SUPPORT_DOMAINS_SCRIPT = support_domains_script
CLOSED_SITE_NAME_DOMAIN = closed_site_name_domain
URL_NEED_FORMAT_DOMAIN = url_need_format_domain

DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
]
