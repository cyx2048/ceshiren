# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 19:54
# @Author  : cyx
# @function: This is register page for new users
# @gitbub  :

from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("LMJPHOTO_TEST")  # Company Name
        self.driver.find_element(By.XPATH, "//*[@id='manager_name']").send_keys("LMJ_TEST")  # Admin Name