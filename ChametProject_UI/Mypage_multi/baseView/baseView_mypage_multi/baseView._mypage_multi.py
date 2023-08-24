# coding=utf-8

"""该类中放置着基础操作如找元素，将driver的使用拓展并简写函数"""
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy

class BaseView(object):

    def __init__(self,driver):
        self.driver = driver

    '''找到一个元素'''
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    '''找到一组元素'''
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    '''获取屏幕的长和宽'''
    def get_window_size(self):
        return self.driver.get_window_size()

    '''从初始x,y位置滑动到终止x,y位置，可控制时长'''
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def tap(self, x, y):
        return TouchAction(self.driver).tap(x=x, y=y, count=1).perform()

    def system_goback_key(self):
        """
        系统返回键点击一次
        """
        self.driver.keyevent('4')
        # driver.press_keycode('4')