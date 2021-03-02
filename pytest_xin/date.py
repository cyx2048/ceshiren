# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 21:46
# @Author  : cyx
# @function: 该功能描述

import time,datetime

d1 = datetime.datetime.strptime('2019-07-22 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2021-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')

print(d1-d2)