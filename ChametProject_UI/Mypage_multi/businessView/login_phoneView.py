# coding=utf-8

import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import time,os

'''该类用于【登录】模块的操作页面涉及到的元素和逻辑'''
class LoginView(Common):
    more_btn = (By.ID, 'com.hkfuliao.chamet:id/tv_more')
    phonenumber_btn = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView')
    input_phonenumber = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText')
    next_btn =(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[4]')
    input_password=(By.ID,'com.hkfuliao.chamet:id/edit_password')
    login_verification_code=[(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[1]'),(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[2]'),(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[3]'),(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[4]')]
    code_next_btn=(By.ID,'com.hkfuliao.chamet:id/tv_next')
    password_login_btn=(By.ID,'com.hkfuliao.chamet:id/tv_login')
    regist_gender_man=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView')
    out_country=(By.ID,'com.hkfuliao.chamet:id/tv_area_code')
    inner_country_name =(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[1]')
    inner_country_area_number =(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[2]')
    inner_A_Z_bar=(By.ID,'com.hkfuliao.chamet:id/index_bar')
    start_btn=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView')
    google_btn=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView')
    google_popover=(By.ID,'com.google.android.gms:id/account_picker_container')
    google_account=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout')

    '''获取更多按钮并点击，前提是先同意check_perBtn权限允许弹窗'''
    def more_Btn(self):
        self.check_perBtn()
        logging.info('================点击更多=====================')
        try:
            more_btn=self.driver.find_element(*self.more_btn)
        except NoSuchElementException:
            logging.info('no more_btn')
        else:
            more_btn.click()
            logging.info('click 更多 already')

    '''查找：一键登录按钮'''
    def find_start_btn_ele(self):
        try:
            fs=self.driver.find_element(*self.start_btn)
        except NoSuchElementException:
            return False
        else:
            return True

    '''点击一键登录并判断登录逻辑'''
    def start_Btn_login(self):
        logging.info('================一键登录=====================')
        if self.find_start_btn_ele:
            self.driver.find_element(*self.start_btn).click()
            if not self.find_start_btn_ele:
                logging.info('click 一键登录 already')
                return  True
            else:
                logging.info('已点击，未一键登录成功')
                return False

        else:
            logging.info('no start_btn')
            return False

    '''查找：一键登录调起的谷歌浮层'''
    def find_google_popover_ele(self):
        try:
            fg=self.driver.find_element(*self.google_popover)
        except NoSuchElementException:
            return False
        else:
            return True

    '''点击谷歌登录并判断登录逻辑'''
    def google_Btn_login(self):
        logging.info('================谷歌登录=====================')
        self.driver.find_element(self.google_btn).click()
        if self.find_google_popover_ele:
            self.driver.find_element(*self.google_account).click()
            try:
                 self.driver.find_element(*self.google_btn)
            except NoSuchElementException:
                logging.info('click 谷歌登录 already')
                return True
            else:
                logging.info('已点击，未谷歌登录成功')
                return False

        else:
            logging.info('no google_popover')
            return False

    '''查找：手机号按钮并点击'''
    def phonenumber_Btn(self):
        logging.info('================点击手机号登录=====================')
        try:
            phonenumber_btn=self.driver.find_element(*self.phonenumber_btn)

        except NoSuchElementException:
            logging.info('no phonenumber_btn')
        else:
            phonenumber_btn.click()
            logging.info('click  手机号按钮 already')

    # 未完成的逻辑，需要滑动并选择到+86
    # def choose_country_area(self):
    #     time.sleep(5)
    #     country_area =self.driver.find_elements(*self.out_country)
    #     if country_area[0].get_attribute('text') == '+86':
    #         logging.info('已默认选择中国+86')
    #         pass
    #     else:
    #         country_area[0].click()
    #         inner_A_Z_bar = self.driver.find_elements(*self.inner_A_Z_bar)
    #         inner_A_Z_bar[0].click()
    #         self.swip_get_country_area_number()


    '''输入手机号的函数:例如4086222，不用输入国家号'''
    def login_input_phonenumber(self,phonenumber):
        logging.info('================输入手机号码=====================')
        self.phonenumber = phonenumber
        logging.info('手机号码是：%s' %phonenumber)
        self.driver.find_element(*self.input_phonenumber).clear()
        self.driver.find_element(*self.input_phonenumber).set_value(phonenumber)
        # self.getScreenShot(f'{phonenumber}')

    '''查找：输入手机号页面的下一步按钮'''
    def find_next_btn_ele(self):
        try:
            fn=self.driver.find_element(*self.next_btn)
        except NoSuchElementException:
            return False
        else:
            return True

    '''查找：验证码页面的下一步按钮'''
    def find_code_next_btn_ele(self):
        try:
            self.driver.find_element(*self.code_next_btn)
        except NoSuchElementException:
            return False
        else:
            return True

    '''输入手机账号后的判断，true即走进了下一页'''
    def next_Btn(self):
        logging.info('已输入账号，开始点击下一步')
        n=self.driver.find_elements(*self.next_btn)
        n[0].click()

        if self.find_next_btn_ele():
            if self.driver.find_elements(*self.next_btn)[0].get_attribute('enabled')=='false':
                logging.error('next_btn置灰不可点击!!')
                #     # self.getScreenShot('login fail!')
                return False
            else:
                logging.info('账号不正确或未选择国家')
                #     # self.getScreenShot('login fail!')
                return False
        else:
            logging.info('click next_btn already')
            return True

    '''查找:验证码四位输入元素'''
    def find_code_ele(self):
        try:
            self.driver.find_element(*self.login_verification_code[3])
        except NoSuchElementException:
            return False
        else:
            return True

    '''查找:密码输入元素'''
    def find_pass_ele(self):
        try:
            self.driver.find_element(*self.input_password)
        except NoSuchElementException:
            return False
        else:
            logging.info('---输入的账号没有同设备，走输入密码方式')
            return True

    '''查找:注册页面性别选择元素'''
    def find_rig_gender(self):
        try:
            self.driver.find_element(*self.regist_gender_man)
        except NoSuchElementException:
            return False
        else:
            return True

    '''验证码正确输入'''
    def code_input_correct(self):
        if self.find_code_ele():
            code_item = self.driver.find_element(*self.login_verification_code[3])
            ver_code = Common.request_get_correct_code(self, 86, self.phonenumber)
            code_item.send_keys(ver_code)
            logging.info('输入的账号，走验证码方式')
            return True
        else:
            return False

    ''' 验证码错误输入'''
    def code_input_wrong(self):
        if self.find_code_ele():
            code_item = self.driver.find_element(*self.login_verification_code[3])
            code_item.send_keys('2222')
            logging.info('输入的账号，走验证码方式')
            return True
        else:
            return False

    # 查找密码输入元素
    # def password_input(self):
    #     if self.find_pass_ele():
    #         # code_item = self.driver.find_element(*self.input_password)
    #         # code_item.send_keys(self.password)
    #         logging.info('---输入的账号没有同设备，走输入密码方式')
    #         return True
    #     else:
    #         return False

    '''输入手机号后进入验证码或者密码的判断和登入'''
    def login_input_password_or_code(self, password):
        if self.next_Btn():  # 已经点击下一步之后
            if self.code_input_correct():  #识别验证码元素
                if self.find_code_ele():
                    return False
                elif self.find_rig_gender():
                    logging.info('账号未注册！')
                    return False
                else:
                    return True
            else:
                if self.find_pass_ele():
                    password_item = self.driver.find_element(*self.input_password)
                    password_item.send_keys(password)
                    password_login_btn = self.driver.find_element(*self.password_login_btn)
                    if password_login_btn.get_attribute('enabled') != 'false':
                        password_login_btn.click()
                        # y=Common.get_toast_data(self, message="密码错误" or "密码错误,你可以通过验证码登录")
                        # time.sleep(3)
                        # if y=="密码错误" and "密码错误,你可以使用验证码登录":
                        #     logging.info("未登录成功，密码错误，请重试")
                        #     return False
                        if not self.find_pass_ele():
                            logging.info('click password_login_btn already')
                            return True
                        elif password_login_btn.get_attribute('enabled') == 'true':
                            logging.info("未登录成功，密码错误，请重试")
                            return False
                        else:
                            return False


                    else:
                        logging.error('password_login_btn置灰不可点击!!')
                        return False

                else:
                    logging.info('无需密码，登陆成功')
                    return True
        else:
            logging.error('账号问题，未走进下一步')
            return False

    '''用于手机号、密码直接登陆账号——给我的页面模块测试专用'''
    def login_input_phone_password(self, password):
        password_item = self.driver.find_element(*self.input_password)
        password_item.send_keys(password)
        password_login_btn = self.driver.find_element(*self.password_login_btn)
        password_login_btn.click()

    # 输入手机号后点击下一步，判断走验证码方式还是密码方式
    # def login_input_password_or_code(self, password):
    #     if self.next_Btn():  # 已经点击下一步之后
    #         if self.code_input_correct():  #识别验证码元素
    #             if self.find_code_ele():
    #                 return False
    #             elif self.find_rig_gender():
    #                 logging.info('账号未注册！')
    #                 return False
    #             else:
    #                 return True
    #         else:
    #             if self.find_pass_ele():
    #                 password_item = self.driver.find_element(*self.input_password)
    #                 password_item.send_keys(password)
    #                 password_login_btn = self.driver.find_element(*self.password_login_btn)
    #                 if password_login_btn.get_attribute('enabled') != 'false':
    #                     password_login_btn.click()
    #                     # y=Common.get_toast_data(self, message="密码错误" or "密码错误,你可以通过验证码登录")
    #                     # time.sleep(3)
    #                     # if y=="密码错误" and "密码错误,你可以使用验证码登录":
    #                     #     logging.info("未登录成功，密码错误，请重试")
    #                     #     return False
    #                     if not self.find_pass_ele():
    #                         logging.info('click password_login_btn already')
    #                         return True
    #                     elif password_login_btn.get_attribute('enabled') == 'true':
    #                         logging.info("未登录成功，密码错误，请重试")
    #                         return False
    #                     else:
    #                         return False
    #
    #
    #                 else:
    #                     logging.error('password_login_btn置灰不可点击!!')
    #                     return False
    #
    #             else:
    #                 logging.info('无需密码，登陆成功')
    #                 return True
    #     else:
    #         logging.error('账号问题，未走进下一步')
    #         return False


    # def login_input_password_or_code(self, password):
    #     code_item = self.driver.find_element(*self.login_verification_code[3])
    #     ver_code = Common.request_get_correct_code(self, 86, self.phonenumber)
    #     print(ver_code,type(ver_code))
    #     code_item.send_keys(ver_code)

'''内部测试执行；手机号-密码登录'''
if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.more_Btn()
    l.phonenumber_Btn()
    time.sleep(2)
    l.login_input_phonenumber('4086555')
    l.login_input_password_or_code('111111')
    driver.quit()
