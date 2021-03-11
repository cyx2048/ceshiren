# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 22:47
# @Author  : cyx
# @function: This cases are to test the contact function
# @gitbub  :

from Web.contact_page.main_page import MainPage

class TestContact:
    def test_add_member(self):
        main = MainPage()
        main.goto_contact().add_member()
