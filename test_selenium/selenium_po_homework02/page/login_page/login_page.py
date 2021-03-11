
# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 19:53
# @Author  : cyx
# @function: This is the login page, including scan QR code and Company registration
# @gitbub  :

from selenium.webdriver.common.by import By
from Web.login_page.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()  # Company registration
        return RegisterPage(self.driver)