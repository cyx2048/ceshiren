# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 22:14
# @Author  : cyx
# @function: 该功能描述
# @gitbub  :

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_adddresspage(self):
        self.driver.find_element(By.XPATH, "//*[@class='frame_nav_item_title']").click()

