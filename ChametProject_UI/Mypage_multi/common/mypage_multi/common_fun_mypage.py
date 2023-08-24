# -*- coding: utf-8 -*-

import allure
import requests
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import time,os
import csv

class Common(BaseView):
    per_btn = (MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    country_number_start=(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[13]/android.widget.TextView[1]')
    country_number_end = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView[1]')
    out_country = (MobileBy.ID, 'com.hkfuliao.chamet:id/tv_area_code')
    inner_country_name = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[1]')
    # inner_country_area_number = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView[2]')
    inner_country_area_number = (MobileBy.XPATH,"//*[@text='+86']")


    def check_perBtn(self):
        '''
        即点击获取定位权限弹窗的确定按钮
        '''

        logging.info('================check_perB=====================')
        try:
            per_btn=self.driver.find_element(*self.per_btn)

        except NoSuchElementException:
            logging.info('no perbtn')
        else:
            per_btn.click()
            logging.info('click check_perBtn already')


    def get_size(self):
        '''获取该手机屏幕的长和宽'''
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y

    '''向左滑动一下的函数'''
    def swipeLeft(self):
        logging.info('================swipeLeft================')
        l=self.get_size()
        x1=int(l[0]*0.9)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.1)
        self.swipe(x1,y1,x2,y1,1000)

    '''向右滑动一下的函数'''
    def swipeRight(self):
        logging.info('================swipeLeft================')
        s = self.get_size()
        sx = s[0] * 0.43
        sy = s[1] * 0.75
        ex = s[0] * 0.54
        ey = 0
        self.driver.swipe(sx, sy, ex, ey,1000)

    '''向上滑动一下的函数'''
    def swipeUp(self):
        logging.info('================swipeLeft================')
        s = self.get_size()
        sx = s[0] * 0.43
        sy = s[1] * 0.45
        ex = 0
        ey = s[1] * 0.55
        self.driver.swipe(sx, sy, ex, -ey,1000)

    '''向下滑动一下的函数'''
    def swipeDown(self):
        logging.info('================swipeLeft================')
        s = self.get_size()
        sx = s[0] * 0.35
        sy = s[1] * 0.45
        ex = 0
        ey = s[1] * 0.55
        self.driver.swipe(sx, sy, ex, ey,1000)


    # '''点击页面某位置，可设置点击时长'''
    # def tap(self, x, y):
    #     return TouchAction(self.driver).tap(x=x, y=y, count=1).perform()

    '''获取当前时间：年-月-日 时-分-秒'''
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    '''对当前时间的页面进行截图并保存在image_file处'''
    def getScreenShot(self, module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    '''allure关联截图工具'''
    def screenshot(self, module):
        time = self.getTime()
        # image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/my_page/%s_%s.png' % (module, time)
        image_file = os.path.dirname(os.path.dirname(__file__)) + '../../screenshots/my_page/%s_%s.png' % (module, time)
        self.driver.get_screenshot_as_file(image_file)
        with open(image_file, mode='rb') as f:
            file = f.read()
        allure.attach(file, module, allure.attachment_type.PNG)
        return image_file

        # testcase中的写入方式
        # except:
        #     logging.info("===no===")
        #     screen_name = self.partyten.screenshot('party_open')
        #     logging.info(f'截图成功，图片为{screen_name}')
        #     raise Exception


    '''打开csv文件并获取行的line，并返回该行的值'''
    def get_csv_data(self,csv_file,line):
        logging.info('===get_csv_data===')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

    '''ui2功能：可以获取当前页面toast值并与输入值作比较'''
    def get_toast_data(self,message):  # 查找toast值
        '''
        method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
        parameter explain：【text】查找的toast值
        Usage:
            device.get_Toast('再按一次退出iBer')
        '''
        self.message=message
        # logging.info("开始查找toast值---'%s'" % (message))
        try:
            message = '//*[@text=\'{}\']'.format(message)
            ele = WebDriverWait(self.driver, 2, 0.5).until(expected_conditions.presence_of_element_located((MobileBy.XPATH, message)))
            logging.info("成功查找到toast----%s" % message)
            return ele.get_attribute("text")

        except:
            logging.error("未查找到toast----%s" % message)
            return False

    '''页面toast获取'''
    def toast_message(self, message):
        return WebDriverWait(self.driver, 10, 0.05).until(expected_conditions.presence_of_element_located((MobileBy.XPATH, '//*[contains(@text, "%s")]' % message)))



    '''请求接口并获得正确验证码，返回4位验证码'''
    def request_get_correct_code(self, area, message):
        url='https://api.ichamet.net/test/getSmsCode'
        para={"mobile": str(area)+str(message)}
        # print(para)
        resp=requests.post(url, json=para)
        js=resp.json()
        return js["info"]

    '''进入h5界面后，获取上下文，并切换至h5'''
    def native_to_h5(self):
        '''Common.native_to_h5(self) 可以直接调用'''
        context = self.driver.contexts
        self.driver.switch_to.context(context[-1])

    '''返回至原生界面后，切换至原生界面'''
    def h5_to_native(self):
       '''Common.h5_to_native(self) '''
       self.driver.switch_to.context('NATIVE_APP')


    def system_goback_key(self):
        '''系统返回键点击一次'''
        self.driver.keyevent('4')
        # driver.press_keycode('4')

    '''长按'''
    def click_hold(self,ele):
        # 使用Ww3c长按该元素
        actions = ActionChains(self.driver)
        # 使用click_and_hold方法按住元素并保持
        actions.w3c_actions.pointer_action.click_and_hold(ele)
        # 使用pause方法指定按住的停顿时间2s
        actions.w3c_actions.pointer_action.pause(2)
        # 使用release方法松开鼠标
        actions.w3c_actions.pointer_action.release()
        # 最后使用perform方法执行以上操作。
        actions.perform()


    def longPress_action(self,ele):
        # 根据元素进行长按(能用元素最好用元素，用坐标可能存在兼容问题)
        action = TouchAction(self.driver)
        # 5000是设置的长按时间（单位/毫秒）
        action.long_press(ele).wait(2000).release().perform()



if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_perBtn()
    th=TouchAction(driver)


