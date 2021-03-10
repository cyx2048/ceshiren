# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 16:06
# @Author  : cyx
# @function: 该功能描述
# @gitbub  :
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

# 主页
class MainPage(object):

    def __init__(self,driver:webdriver):
        self.driver = driver
    def goto_addresslist(self):
        # 点击通讯录
        self.driver.