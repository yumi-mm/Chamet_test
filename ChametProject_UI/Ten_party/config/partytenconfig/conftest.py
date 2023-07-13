class Android_Setting:
    def android_setting(self):
        self.desired_caps = {
            # 被手机的操作系统
            "platformName": "Android",
            # 被手机的操作系统的版本
            "platformVersion": "11",
            # 被测试APP的包名
            "appPackage": "com.hkfuliao.chamet",
            # 被测试的app的第一个界面的路径
            "appActivity": "com.oversea.chat.splash.SplashActivity",
            # 设备名称
            "deviceName": "832c16a4",
            # 元素定位方法
            "automationName": "UiAutomator2",
            # 输入法
            "uicodeKeyboard": True,
            # 重置输入法
            "resetKeyboard": True,
            # 界面缓存不重置
            "noReset": True,
            # 时间超时时间
            "newCommandTimeout": "3000"
        }

        return self.desired_caps