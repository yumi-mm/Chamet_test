import logging
from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time,os

class LoginView(Common):
    more_btn = (By.ID, 'com.hkfuliao.chamet:id/tv_more')
    phonenumber_btn = (By.XPATH,
                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView')
    login_type = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText')
    next_btn =(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[4]')

    def more_Btn(self):
        self.check_perBtn()

        logging.info('================点击更多=====================')
        try:
            more_btn=self.driver.find_element(*self.more_btn)

        except NoSuchElementException:
            logging.info('no more_btn')
        else:
            more_btn.click()
            logging.info('click already')

    def phonenumber_Btn(self):
        logging.info('================点击手机号登录=====================')
        try:
            phonenumber_btn=self.driver.find_element(*self.phonenumber_btn)

        except NoSuchElementException:
            logging.info('no phonenumber_btn')
        else:
            phonenumber_btn.click()
            logging.info('click already')

    def login_action(self,phonenumber):
        logging.info('================输入手机号码=====================')
        logging.info('手机号码是：%s' %phonenumber)
        self.driver.find_element(*self.login_type).clear()
        self.driver.find_element(*self.login_type).set_value(phonenumber)
        self.getScreenShot('phonenumber')


    def next_Btn(self):
        logging.info('开始点击下一步')
        p=self.driver.find_elements(*self.next_btn)
        if p[0].get_attribute('enabled')=='false':
            return False
        else:
            return True


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.more_Btn()
    l.phonenumber_Btn()
    time.sleep(3)
    l.login_action('5678')
    print(l.next_Btn())