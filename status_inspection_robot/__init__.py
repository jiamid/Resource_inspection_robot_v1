# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/17 10:42
@File     ：__init__.py.py
@Software ：PyCharm
"""
import sys
import json
from urllib import parse
import status_inspection_robot.config
import importlib
from status_inspection_robot.filter_tools import url_filter


class InspectionRobot:
    CONFIG = config
    proxies = None
    proxy = ''

    def __init__(self, params: dict):
        self.params = params
        self.clip_url = params["clip_url"]
        self.url = params["clip_url"]
        if 'proxy' in params:
            proxy = params["proxy"]
            self.proxy = proxy
            self.proxies = {'http': proxy, 'https': proxy}
        ret = parse.urlparse(self.url)
        self.domain = ".".join(ret[1].split('.')[-2:])
        self.special_init()

    def special_init(self):
        if 'vidshare.tv' in self.url:
            self.params['referer'] = 'https://www.google.com'

    def get_content(self):
        try:
            py_name = self.domain.replace('.', '_')
            module = importlib.import_module(f'sites.{py_name}')
        except ModuleNotFoundError:
            module = importlib.import_module('status_inspection_robot.sites.default')
        default_func_name = 'check_url'
        func = getattr(module, default_func_name)
        content = func(self.url, self.proxies, self.params)
        return content

    def get_status(self):
        if self.domain in self.CONFIG.URL_NEED_FORMAT_DOMAIN:
            self.url = url_filter.format_url_filter(self.url)
            ret = parse.urlparse(self.url)
            self.domain = ".".join(ret[1].split('.')[-2:])
        if self.domain in self.CONFIG.ALL_SUPPORT_DOMAINS:
            try:
                content = self.get_content()
                if content == 0:
                    content = ''
                    error_code = 0
                else:
                    error_code = -2008
            except ValueError as e:
                content = str(e) + self.proxy
                error_code = -1003
            except Exception as e:
                content = str(e) + self.proxy
                error_code = -2004
        else:
            error_code = 2010
            content = 'Unsupported website'

        if self.domain == "data.hu":
            content = "not print"
        result = '{"error_code":%s, "error_extra_info":"%s", "url":"%s"}' % (error_code, content, self.clip_url)
        return result


if __name__ == '__main__':

    params = sys.stdin.readline()
    param_dic = {}
    if params.startswith("http"):
        input = {}
        input["clip_url"] = params.strip()
        param_dic = input
    else:
        param_dic = json.loads(params)

    robot = InspectionRobot(param_dic)
    result = robot.get_status()
    print(result)
