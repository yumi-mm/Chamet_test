# coding=utf-8
import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep
from businessView.login_phoneView import LoginView

'''该类用于【我的页面】启动和结束的步骤'''
class StartEnd(unittest.TestCase):

    '''我的页面-打开页面点进入登陆流程进入首页'''
    def login_step(self,phone,password):
        self.phone = phone
        self.password=password

        LoginView.more_Btn()
        LoginView.phonenumber_Btn()
        sleep(2)
        LoginView.login_input_phonenumber(phone)
        LoginView.login_input_phone_password(password)

    '''开始前先登录'''
    def setUp(self):
        logging.info('===setUp===')
        self.driver=appium_desired()
        self.login_step(4086555,111111)

    # def tearDown(self):
    #     logging.info('===tearDown===')
    #     sleep(5)
    #     self.driver.close_app()
