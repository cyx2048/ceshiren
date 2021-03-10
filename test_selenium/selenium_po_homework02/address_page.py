# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 22:13
# @Author  : cyx
# @function: 该功能描述
# @gitbub  :
from selenium.webdriver.common.by import By


class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_addcontacts(self):
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']").click()

