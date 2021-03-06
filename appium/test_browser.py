# -*-coding:utf-8-*-
# appium连接模拟器 安装重启qq
from appium import webdriver
from time import sleep

class TestBrowser():
    def setup(self):
        des_caps = {
            "platformName":"Android",
            "platformVersion":"7.1.2",
            "browserName":"Chrome",
            "noReset":True,
            "deviceName":"127.0.0.1:21503"
          #  "chromedriverExcutable" = f"D:\driver"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub" , des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
         self.driver.get("https://www.baidu.com/")
         sleep(5)

