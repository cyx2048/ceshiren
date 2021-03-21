# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 21:42
# @Author  : cyx
# @function: 使用mitmproxy 实现map local功能, 修改的是请求

import json
from mitmproxy import ctx, http

class AD:
    def request(self, flow: http.HTTPFlow):
        """
        使用request事件实现map local
        :param flow:
        :return:
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open("D:\\ceshiren\\test_mock\\xueqiu_batch_quote.json", encoding="utf-8") as f:
                # 给flow.response属性进行赋值，
                # 赋值调用mitmproxy 响应对象的 make方法
                # 响应体在make函数里面所需要的数据为str
                flow.response = http.HTTPResponse.make(200,  # (optional) status code
                                                       f.read(),  # (optional) content
                                                       {"Content-Type": "text/html"}  # (optional) headers
                                                       )

    def response(self, flow: http.HTTPFlow):
        pass
# addons 是mitmproxy 的强制要求的规范
# 一定要使用此变量名存放类的实例
addons = [
    AD()
]