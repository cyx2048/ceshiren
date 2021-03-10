# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 16:02
# @Author  : cyx
# @function: 该功能描述
# @gitbub  :

from appium import webdriver

# 启动app、停止app、重启app
class App:
    def start(self):
        #启动app
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["automationName"] = 'uiautomator2'  # toast提示识别
        caps["noReset"] = True  # 不清理缓存、进入app是登录状态
        caps["autoGrantPermissions"] = True  # 地理存储权限，默认忽略这些
        caps["dontStopAppOnReset"] = True  # 不需要重新启动app，（比如打开app，执行用例时会先关掉app，再打开app，耗时）
        caps["skipDeviceInitialization"] = True  # 跳过设备初始化,运行过一次用例后再设置True
        # caps["dontStopAppOnReset"] = True         # 执行完后不要杀死app，就停留到执行完的那个页面
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps['settings[waitForIdleTimeout]'] = 1  # 控制 动态页面的等待时长
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.refresh()

    def stop(self):
        #停止app
        self.driver.quit()

    def goto_main(self):
        return MainPage()