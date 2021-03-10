# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 10:48
# @Author  : cyx
# @function: 优化：app企业添加联系人  知识1：toast提示语定位  知识点2：滑动查找方法
# @github  : https://github.com/cyx2048/ceshiren/blob/master/appium/test_wework2.py

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
        caps["noReset"] = True                     # 不清理缓存、进入app是登录状态
        caps["autoGrantPermissions"] = True        # 地理存储权限，默认忽略这些
        caps["dontStopAppOnReset"] = True          # 不需要重新启动app，（比如打开app，执行用例时会先关掉app，再打开app，耗时）
        caps["skipDeviceInitialization"] = True    # 跳过设备初始化,运行过一次用例后再设置True
       # caps["dontStopAppOnReset"] = True         # 执行完后不要杀死app，就停留到执行完的那个页面
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps['settings[waitForIdleTimeout]'] = 1   # 控制 动态页面的等待时长
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 滑动查找的方法
    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次， 未找到。")

            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def test_addcontact(self):
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
        name = "hogwarts_2"
        phonenum = "13100000029"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        element = self.swipe_find("添加成员")
        element.click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 断言：添加成功后，识别页面上的toast提示做断言，caps["automationName"]='uiautomator2'
        msg_xpath = "//*[@text='添加成功']"
        toast_element = self.driver.find_element(MobileBy.XPATH,msg_xpath)
        print(toast_element.text)
        assert toast_element.text=='添加成功'




