import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import time,os

class LoginView(Common):
    more_btn = (By.ID, 'com.hkfuliao.chamet:id/tv_more')
    phonenumber_btn = (By.XPATH,
                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView')
    input_phonenumber = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText')
    next_btn =(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[4]')
    input_password=(By.ID,'com.hkfuliao.chamet:id/edit_password')
    login_verification_code=[(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[1]'),(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[2]'),(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[3]'),(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[4]')]
    code_next_btn=(By.ID,'com.hkfuliao.chamet:id/tv_next')
    password_login_btn=(By.ID,'com.hkfuliao.chamet:id/tv_login')
    regist_gender_man=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView')

    def more_Btn(self):
        self.check_perBtn()
        logging.info('================�������=====================')
        try:
            more_btn=self.driver.find_element(*self.more_btn)

        except NoSuchElementException:
            logging.info('no more_btn')
        else:
            more_btn.click()
            logging.info('click already')

    def phonenumber_Btn(self):
        logging.info('================����ֻ��ŵ�¼=====================')
        try:
            phonenumber_btn=self.driver.find_element(*self.phonenumber_btn)

        except NoSuchElementException:
            logging.info('no phonenumber_btn')
        else:
            phonenumber_btn.click()
            logging.info('click already')

    def login_input_phonenumber(self,phonenumber):
        logging.info('================�����ֻ�����=====================')
        self.phonenumber = phonenumber
        logging.info('�ֻ������ǣ�%s' %phonenumber)
        self.driver.find_element(*self.input_phonenumber).clear()
        self.driver.find_element(*self.input_phonenumber).set_value(phonenumber)
        # self.getScreenShot(f'{phonenumber}')

    def next_Btn(self):
        logging.info('��ʼ�����һ��')
        n= self.driver.find_elements(*self.next_btn)
        if n[0].get_attribute('enabled')=='false':
            logging.error('next_btn�ûҲ��ɵ��!!')
            self.getScreenShot('login fail!')
            return False

        else:
            n[0].click()
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

    def code_input(self):
        if self.find_code_ele():
            # code_item = self.driver.find_element(*self.login_verification_code[3])
            # ver_code = Common.request_get_correct_code(self, 86, self.phonenumber)
            # # code_item.send_keys(ver_code)
            logging.info('������˺�ͬ�豸����δע�ᣬ����֤�뷽ʽ')
            return True
        else:
            return False

    def password_input(self):
        if self.find_pass_ele():
            # code_item = self.driver.find_element(*self.input_password)
            # # code_item.send_keys(self.password)
            logging.info('---������˺�û��ͬ�豸�����������뷽ʽ')
            return True
        else:
            return False

    def login_input_password_or_code(self, password):
        if self.code_input():
            code_item = self.driver.find_element(*self.login_verification_code[3])
            ver_code = Common.request_get_correct_code(self, 86, self.phonenumber)
            print(ver_code)
            code_item.send_keys(ver_code)
            if self.find_code_ele():
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
                    y=Common.get_toast_data(self, message="�������" or "�������,�����ͨ����֤���¼")
                    time.sleep(3)
                    if y=="�������" and "�������,�����ʹ����֤���¼":
                        logging.info("δ��¼�ɹ����������������")
                        return False
                    else:
                        return True
                    # else:
                    #     if self.find_pass_ele():
                    #         return False
                    #     else:
                    #         logging.info('click password_login_btn already')
                    #         return True

                else:
                    logging.error('password_login_btn�ûҲ��ɵ��!!')
                    return False








    #     logging.info('�ж���֤���¼���������¼')
    #     try:
    #         input_password_y = self.driver.find_element(*self.input_password)
    #     # ����֤�뷽ʽ
    #     except NoSuchElementException:
    #         code_correct_or_wrong()
    #
    #     # �����뷽ʽ
    #     else:
    #         logging.info('---������˺�û��ͬ�豸�����������뷽ʽ')
    #         input_password_y.set_value(password)
    #         password_login_btn = self.driver.find_element(*self.password_login_btn)
    #
    # def login_input_password_or_code(self, password):
    #     logging.info('����¼��ʽ')
    #     try:
    #         input_password_y=self.driver.find_element(*self.input_password)
    #
    #     except NoSuchElementException :
    #         logging.info('������˺�ͬ�豸����δע�ᣬ����֤�뷽ʽ')
    #         try:
    #             code_item=self.driver.find_element(*self.login_verification_code[3])
    #             print(code_item,type(code_item))
    #         except NoSuchElementException:
    #             logging.info('�Ҳ�����֤�������')
    #             return False
    #         else:
    #         # code=Common.request_get_correct_code(86, self.phonenumber)
    #         # time.sleep(3)
    #             code_item.send_keys("5555")
    #             try:
    #                 code_next_btn=self.driver.find_element(*self.code_next_btn)
    #             except NoSuchElementException :
    #                 logging.info('û����һ���İ�ť!!')
    #                 return True
    #             else:
    #                 code_next_btn.click()
    #                 x = Common.get_toast_data(self, message="��֤�����")
    #                 return False
    #
    #     else:
    #         logging.info('---������˺�û��ͬ�豸�����������뷽ʽ')
    #         input_password_y.set_value(password)
    #         password_login_btn=self.driver.find_element(*self.password_login_btn)
    #         if password_login_btn.get_attribute('enabled') == 'false':
    #             logging.error('password_login_btn�ûҲ��ɵ��!!')
    #             self.getScreenShot('���벻��6λ��login fail!')
    #             return False
    #
    #         else:
    #             y=Common.get_toast_data(self,message="�������"or "�������,�����ͨ����֤���¼")
    #             password_login_btn.click()
    #             if y=="�������" and "�������,�����ʹ����֤���¼":
    #                 logging.info("δ��¼�ɹ����������������")
    #                 return False
    #             else:
    #                 logging.info('click password_login_btn already')
    #                 return True
    #


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.more_Btn()
    l.phonenumber_Btn()
    time.sleep(3)
    l.login_input_phonenumber('7087014')
    l.next_Btn()
    l.login_input_password_or_code('1111')
    driver.quit()