from appium.webdriver.common.mobileby import MobileBy
from businessView.login_phoneView import LoginView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
import logging
import time, os
import allure
import pytest

# 余额不足提示
"送礼失败。余额不足。"
# 余额不足充值窗口
(MobileBy.ID,"com.hkfuliao.chamet:id/rootView")
# 有google充值的手机
(MobileBy.ID,"com.hkfuliao.chamet:id/recycler_top_up_list")

送礼
if 存在充值窗口&&存在goole充值的手机：
    充值
    送礼
elif 存在夺宝宝箱:
    pass
elif 存在充值窗口不存在goole充值:
    设置全局变量，跳过下方断言用例
    返回
    日志打印（”余额不足，设备无法充值，跳过下方断言用例。“）