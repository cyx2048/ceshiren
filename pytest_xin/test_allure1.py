# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 21:15
# @Author  : cyx
# @function: 该功能描述

import pytest
import allure

@allure.feature("搜索模块")
class TestSearch():
    def test_case1(self):
        print("case1")

    def test_case2(self):
        print("case2")

@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤一，打开应用"):
            print("打开应用")
        with allure.step("步骤二，打开登录页面"):
            print("登录成功")

    @allure.story("登录失败")
    def test_fail(self):
        print("这是登录失败用例")