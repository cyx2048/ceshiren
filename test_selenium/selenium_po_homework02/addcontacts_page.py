# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 22:25
# @Author  : cyx
# @function: 该功能描述
# @gitbub  :

class Addcontacts_Page:

    def __init__(self, driver):
        self.driver = driver

    def addcontacts(self):
        self.driver.find_element(By.XPATH, "//*[@name='username']").

