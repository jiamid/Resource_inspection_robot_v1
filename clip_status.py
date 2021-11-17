# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/17 10:55
@File     ：clip_status.py
@Software ：PyCharm
"""
import sys
import json
from status_inspection_robot import InspectionRobot

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