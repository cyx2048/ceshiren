# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 10:48
# @Author  : cyx
# @function: app企业添加联系人，知识点：断言时看页面上的toast提示是否正确1

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["automationName"]='uiautomator2'      # toast提示识别
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1   # 控制 动态页面的等待时长
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addpeople(self):
        '''
        前提条件: 已登录状态（ noReset=True）
        打卡用例：
        1、打开【企业微信】应用
        2、进入【通讯录】
        3、点击【添加成员】
        4、点击【手动输入添加】
        5、输入【姓名手机号】
        6、点击【保存】
        7、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/cth").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b7m").send_keys("阿1")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fwi").send_keys("18600000007")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/aj_").click()
        # 断言：添加联系人成功，断言：识别页面上的toast提示，caps["automationName"]='uiautomator2'
        msg_xpath = "//*[@text='添加成功']"
        toast_element = self.driver.find_element(MobileBy.XPATH,msg_xpath)
        print(toast_element.text)
        assert toast_element.text=='添加成功'




