

from common.desired_caps import appium_desired
import logging
from time import sleep
from businessView.my_page import MyPage
from common.common_fun import Common


'''该类用于【我的页面】启动和结束的步骤'''
class StartEnd():

    # '''我的页面-打开页面点进入登陆流程进入首页'''
    # def login_step(self,phone,password):
    #     self.phone = phone
    #     self.password=password
    #
    #     LoginView.more_Btn()
    #     LoginView.phonenumber_Btn()
    #     sleep(2)
    #     LoginView.login_input_phonenumber(phone)
    #     LoginView.login_input_phone_password(password)

    # '''开始前先登录'''
    def setup_class(self):
        logging.info('===setUp===')
        self.driver=appium_desired()
        self.l = MyPage(self.driver)
        self.c=Common(self.driver)
        self.l.login_direct_phone(4086222, 111111)
        # self.l.login_step(4086222, 111111)
        # l.login_step(6088011, 111111)
        # self.l.login_step(4087032, 111111)陌生人用户


    def teardown_class(self):
        logging.info('===tearDown===')
        sleep(5)
        self.driver.quit()
