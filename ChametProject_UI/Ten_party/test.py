# 主播
def anchor_appium_desired():
    desired_caps = {}
    desired_caps['platformName'] = Android   #设备的操作系统平台
    desired_caps['deviceName'] = DKTUT20512001326  #设备名称
    desired_caps['udid'] = DKTUT20512001326   #设备唯一标识符
    desired_caps['appPackage'] = com.hkfuliao.chamet   #应用程序的包名
    desired_caps['appActivity'] = com.oversea.chat.splash.SplashActivity   #启动应用程序的主活动
    desired_caps['automationName'] = Uiautomator2  #自动化引擎
    desired_caps['noReset'] = True   #会话之间重置应用程序状态
    desired_caps['unicodeKeyboard'] = False   #控制是否启用或禁用 Unicode 键盘
    desired_caps['resetKeyboard'] = False   #控制是否启用或禁用 Unicode 键盘
    desired_caps['newCommandTimeout'] = 3000   #命令超时时间
    driver = webdriver.Remote('http://localhost' + ":" + "4726" + '/wd/hub', desired_caps)
    return driver

# 观众
def audience_appium_desired():
    desired_caps = {}
    desired_caps['platformName'] = Android
    desired_caps['deviceName'] = 832c16a4
    desired_caps['udid'] = 832c16a4
    desired_caps['appPackage'] = com.hkfuliao.chamet
    desired_caps['appActivity'] = com.oversea.chat.splash.SplashActivity
    desired_caps['automationName'] = Uiautomator2
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = False
    desired_caps['resetKeyboard'] = False
    desired_caps['newCommandTimeout'] = 3000
    driver = webdriver.Remote('http://localhost' + ":" + "4723" + '/wd/hub', desired_caps)
    return driver


# 调用：
anchor_driver = anchor_appium_desired()
audience_driver = audience_appium_desired()