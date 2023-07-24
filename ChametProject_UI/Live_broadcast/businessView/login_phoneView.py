import logging
from ChametProject_UI.Live_broadcast.common.common_fun import Common, NoSuchElementException
from selenium.webdriver.common.by import By
import time,os

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
    One_click=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView')
    pkPag = (By.ID,'com.hkfuliao.chamet:id/pkPag')
    Goolgle_button = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView')
    Goolgle_id = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout')


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

    def phonenumber_Btn(self):
        logging.info('================点击手机号登录=====================')
        try:
            phonenumber_btn=self.driver.find_element(*self.phonenumber_btn)

        except NoSuchElementException:
            logging.info('no phonenumber_btn')
        else:
            phonenumber_btn.click()
            logging.info('click 手机号按钮 already')

    def login_input_phonenumber(self,phonenumber):
        logging.info('================输入手机号码=====================')
        self.phonenumber = phonenumber
        logging.info('手机号码是：%s' %phonenumber)
        self.driver.find_element(*self.input_phonenumber).clear()
        self.driver.find_element(*self.input_phonenumber).set_value(phonenumber)
        # self.getScreenShot(f'{phonenumber}')

    def find_next_btn_ele(self):
        try:
            nt=self.driver.find_element(*self.next_btn)
        except NoSuchElementException:
            return False
        else:
            return True

    def find_code_next_btn_ele(self):
        try:
            self.driver.find_element(*self.code_next_btn)
        except NoSuchElementException:
            return False
        else:
            return True

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

    def find_code_ele(self):
        try:
            self.driver.find_element(*self.login_verification_code[3])
        except NoSuchElementException:
            return False
        else:
            return True

    def find_pass_ele(self):
        try:
            self.driver.find_element(*self.input_password)
        except NoSuchElementException:
            return False
        else:
            return True

    def find_rig_gender(self):
        try:
            self.driver.find_element(*self.regist_gender_man)
        except NoSuchElementException:
            return False
        else:
            return True

    def code_input(self):
        if self.find_code_ele():
            code_item = self.driver.find_element(*self.login_verification_code[1])
            ver_code = Common.request_get_correct_code(self, 86, self.phonenumber)
            code_item.send_keys(ver_code)
            logging.info('输入的账号，走验证码方式')
            return True
        else:
            return False

    def wrong_code_input(self):
        if self.find_code_ele():
            code_item = self.driver.find_element(*self.login_verification_code[3])
#            code_item.send_keys('1234')
            code_item.send_keys('1234')
            logging.info('输入的账号，走验证码方式')
            return True
        else:
            return False

    def password_input(self):
        if self.find_pass_ele():
            #code_item = self.driver.find_element(*self.input_password)
            # code_item.send_keys(self.password) #这里用来测试推送
            logging.info('---输入的账号没有同设备，走输入密码方式')
            return True
        else:
            return False

    def login_input_password_or_code(self, password):
        if self.next_Btn():
            if self.code_input():
                if self.find_code_ele():
                    return False
                elif self.find_rig_gender():
                    logging.info('账号未注册！')
                    return False
                else:
                    return True
            else:
                if self.password_input():
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
                        if not self.password_input():
                            logging.info('click password_login_btn already')
                            return True
                        elif password_login_btn.get_attribute('enabled') == 'true':
                            logging.info("未登录成功，密码错误，请重试")
                            return False
                        else:
                            return False

                        # if password_login_btn.get_attribute('enabled') == 'true':
                        #     logging.info("未登录成功，密码错误，请重试")
                        #     return False
                        # elif not self.password_input():
                        #     logging.info('click password_login_btn already')
                        #     return True
                        # else:
                        #     return False
                    else:
                        logging.error('password_login_btn置灰不可点击!!')
                        return False

                else:
                    logging.info('无需密码，登陆成功')
                    return True
        else:
            logging.error('账号问题，未走进下一步')
            return False

    def login_input_password_or_wrong_code(self, password):
        if self.next_Btn():
            if self.wrong_code_input():
                if self.find_code_ele():
                    return False
                elif self.find_rig_gender():
                    logging.info('账号未注册！')
                    return False
                else:
                    return True
            else:
                if self.password_input():
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
                        if not self.password_input():
                            logging.info('click password_login_btn already')
                            return True
                        elif password_login_btn.get_attribute('enabled') == 'true':
                            logging.info("未登录成功，密码错误，请重试")
                            return False
                        else:
                            return False

                        # if password_login_btn.get_attribute('enabled') == 'true':
                        #     logging.info("未登录成功，密码错误，请重试")
                        #     return False
                        # elif not self.password_input():
                        #     logging.info('click password_login_btn already')
                        #     return True
                        # else:
                        #     return False
                    else:
                        logging.error('password_login_btn置灰不可点击!!')
                        return False

                else:
                    logging.info('无需密码，登陆成功')
                    return True
        else:
            logging.error('账号问题，未走进下一步')
            return False

    def One_click_login(self):
        self.check_perBtn()
        logging.info('===开始寻找一键登录===')
        try:
            One_click=self.driver.find_element(*self.One_click)
        except NoSuchElementException:
            logging.info('===未找到一键登录===')
        else:
            One_click.click()
            logging.info('===点击一键登录===')

    def check_loginStatus(self):
        logging.info('--开始验证是否登录成功')
        try:
            self.driver.find_element(*self.pkPag)
        except NoSuchElementException:
            logging.error('--登陆失败--')
            self.getScreenShot('--登陆失败截图--')
            return False
        else:
            logging.info('--登录成功--')
            return True

    def Guge_Button(self):
        logging.info('--开始点击谷歌按钮--')
        try:
            Goolgle_button=self.driver.find_element(*self.Goolgle_button)
        except NoSuchElementException:
            logging.info('--未找到谷歌按钮--')
        else:
            Goolgle_button.click()
            logging.info('--找到谷歌按钮--')

    def Goolgle_ID(self):
        logging.info('--开始寻找谷歌账号--')
        try:
            Goolgle_id=self.driver.find_element(*self.Goolgle_id)
        except NoSuchElementException:
            logging.info('--没有找到谷歌账号--')
        else:
            Goolgle_id.cilck()
            logging.info('--找到了谷歌账号--')



    # def find_code_ele(self):
    #     try:
    #         self.driver.find_element(*self.login_verification_code[3])
    #     except NoSuchElementException:
    #         return False
    #     else:
    #         return True
    # def find_pass_ele(self):
    #     try:
    #         self.driver.find_element(*self.input_password)
    #     except NoSuchElementException:
    #         return False
    #     else:
    #         return True
    #
    # def code_input(self):
    #     if self.find_code_ele():
    #         # code_item = self.driver.find_element(*self.login_verification_code[3])
    #         # ver_code = Common.request_get_correct_code(self, 86, self.phonenumber)
    #         # # code_item.send_keys(ver_code)
    #         logging.info('输入的账号同设备或者未注册，走验证码方式')
    #         return True
    #     else:
    #         return False
    #
    # def password_input(self):
    #     if self.find_pass_ele():
    #         # code_item = self.driver.find_element(*self.input_password)
    #         # # code_item.send_keys(self.password)
    #         logging.info('---输入的账号没有同设备，走输入密码方式')
    #         return True
    #     else:
    #         return False
    #
    # def login_input_password_or_code(self, password):
    #     if self.code_input():
    #         code_item = self.driver.find_element(*self.login_verification_code[3])
    #         ver_code = Common.request_get_correct_code(self, 86, self.phonenumber)
    #         print(ver_code)
    #         code_item.send_keys(ver_code)
    #         if self.find_code_ele():
    #             return False
    #         else:
    #             return True
    #     else:
    #         if self.password_input():
    #             password_item = self.driver.find_element(*self.input_password)
    #             password_item.send_keys(password)
    #             password_login_btn = self.driver.find_element(*self.password_login_btn)
    #             if password_login_btn.get_attribute('enabled') != 'false':
    #                 password_login_btn.click()
    #                 y=Common.get_toast_data(self, message="密码错误" or "密码错误,你可以通过验证码登录")
    #                 time.sleep(3)
    #                 if y=="密码错误" and "密码错误,你可以使用验证码登录":
    #                     logging.info("未登录成功，密码错误，请重试")
    #                     return False
    #                 else:
    #                     return True
    #                 # else:
    #                 #     if self.find_pass_ele():
    #                 #         return False
    #                 #     else:
    #                 #         logging.info('click password_login_btn already')
    #                 #         return True
    #
    #             else:
    #                 logging.error('password_login_btn置灰不可点击!!')
    #                 return False

if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.more_Btn()
    l.phonenumber_Btn()
    time.sleep(2)
    l.login_input_phonenumber('123447474')
    l.login_input_password_or_code('123456')
    driver.quit()