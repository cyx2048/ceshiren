# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 19:51
# @Author  : cyx
# @function: 该功能描述
# @gitbub  : This page is the wechat work homepage after login in, chrome browser reuse function is needed, please make sure

from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.contact_page.contact_page import ContactPage


class MainPage:
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(6)

    def goto_contact(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()  # click on contacts tab
        return ContactPage(self.driver)