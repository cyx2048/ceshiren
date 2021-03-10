# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 20:47
# @Author  : cyx
# @function: 浏览器复用、cookie登录
# @gitbub  :
"""
作业：通过浏览器利用cookie实现企业微信登录
方法1：通过复用浏览器登录企业微信，获取用户cookie，具体实现思路
1)关闭所有的chrome浏览器进程
  然后cmd：chrome -remote-debugging-port=9222
  再然后 打开新的浏览器，并进行企业登录操作
2) 关键代码：chrome_arg = webdriver.ChromeOptions()
           chrome_arg.debugger_address = '127.0.0.1:9222'
           self.driver = webdriver.Chrome(options=chrome_arg)
3）run一下 打开已登录的企业微信，获取用户cookie，并记录到文本中【ps: 如果想cookie能够长期使用，可以修改cookie的有效时间】

方法2、通过复用浏览器登录企业微信，获取用户cookie，通过读取文件cookie进行企业登录
1）使用webdriver.Chrome()打开浏览器
2）从文件中读取cookie，并添加到请求中
3）去登录企业微信，登录成功，则实现了cookie登录；否则debug排查代码

另外获取cookie方法、手动登录企业微信、并把cookie存在文件中，下次通过读取cookie的形式进行企业登录

"""
import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    "方法1：复用已有浏览器登录,通过复用获取cookie方法"
    def test_get_cookie1(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_apps").click()
        sleep(8)
        cookie = self.driver.get_cookies()
        print(cookie, type(cookie))
        with open("cookie.txt", 'w', encoding="utf-8") as f:
            json.dump(cookie, f)

    "通过人工获取cookie方法：人工扫码登录，获取cookie"
    def test_get_cookie2(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(8)  # 手动扫码登录
        cookie = self.driver.get_cookies()
        print(cookie, type(cookie))
        with open("cookie.txt", 'w', encoding="utf-8") as f:
            json.dump(cookie, f)

    "方法2：读取cookie进行登录"
    def test_cookie_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        try:
            with open('cookie.txt', 'r', encoding='utf-8') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            "登录后的操作"
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "menu_customer")))
            self.driver.find_element_by_id("menu_customer").click()
        finally:
            sleep(3)
            self.driver.quit()
