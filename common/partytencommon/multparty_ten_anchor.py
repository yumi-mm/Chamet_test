from appium.webdriver.common.mobileby import MobileBy
from businessView.login_phoneView import LoginView
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
import logging
import time, os
import allure


class Multanchor(object):
    warning_message = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")


    def __init__(self, driver):
        self.driver = driver

    # 登录
    def login_account(self, phone, password):
        password_frame = (MobileBy.ID, "com.hkfuliao.chamet:id/edit_password")
        logon_button = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_login")
        logging.info('===登录===')
        logon = LoginView(self.driver)
        logon.more_Btn()
        logon.phonenumber_Btn()
        logon.login_input_phonenumber(phone)
        logon.next_Btn()
        self.driver.find_element(*password_frame).send_keys(password)
        self.driver.find_element(*logon_button).click()

    # 坐标之间的滑动
    def swipe_xy(self, start_x, start_y, end_x, end_y,time=2000):
        self.driver.swipe(start_x, start_y, end_x, end_y,time)

    # 判断有无签到弹窗
    def sign_in_window(self):
        try:
            sign_in_windows = (MobileBy.ANDROID_UIAUTOMATOR, 'text("连续签到")')
            signin_window = self.driver.find_element(*sign_in_windows)
        except:
            return False
        else:
            logging.info('===有签到弹窗===')
            return True


    # 进入交友房页签
    def party_tab_Btn(self):
        logging.info('===进入交友房页签===')
        time.sleep(3)
        party_tab = (MobileBy.ID, "com.hkfuliao.chamet:id/rl_tab_party")
        self.driver.find_element(*party_tab).click()


    # 签到
    def sign_in(self):
        try:
            signin_window = self.sign_in_window()
            if signin_window:
                sign_in_but = (MobileBy.ID, "com.hkfuliao.chamet:id/tvSubmit")
                self.driver.find_element(*sign_in_but).click()
                self.driver.back()
                self.party_tab_Btn()
            else:
                self.party_tab_Btn()
        except:
            logging.info('===签到执行失败===')


    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now


    # 失败截图
    def screenshot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '../../screenshots/party_ten/%s_%s.png' % (module, time)
        self.driver.get_screenshot_as_file(image_file)
        with open(image_file, mode='rb') as f:
            file = f.read()
        allure.attach(file, module, allure.attachment_type.PNG)
        return image_file


    # 进入交友房预览页
    def enter_party_PreviewPage(self):
        logging.info('===进入交友房预览页===')
        time.sleep(1)
        partyPreviewPage_enter = (MobileBy.ID, "com.hkfuliao.chamet:id/btn")
        self.driver.find_element(*partyPreviewPage_enter).click()
        pw = self.permission_window()
        if pw:
            self.choic_permission_window()
            self.choic_permission_window()
            self.choic_permission_window()
        else:
            logging.info('===无权限弹窗===')


    # 判断有无权限弹窗
    def permission_window(self):
        permission_windows = (MobileBy.ID, "com.android.permissioncontroller:id/permission_message")
        try:
            window = self.driver.find_element(*permission_windows)
        except:
            return False
        else:
            logging.info('===有权限弹窗===')
            return True


    # 同意权限弹窗
    def choic_permission_window(self):
        permission_allow_foreground_only_button = (
        MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        permission_allow_button = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        try:
            if self.driver.find_element(*permission_allow_foreground_only_button):
                self.driver.find_element(*permission_allow_foreground_only_button).click()
            else:
                self.driver.find_element(*permission_allow_button).click()
        except:
            logging.info('===权限执行失败===')


    # 进入10人交友房
    def enter_tenparty(self):
        logging.info('===进入10人交友房===')
        ten_people = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_live_room_ten")
        party_enterbut = (MobileBy.ID, "com.hkfuliao.chamet:id/btn_live")
        self.driver.find_element(*ten_people).click()
        self.driver.find_element(*party_enterbut).click()

    # 主播端发言
    def anchor_speak_list(self,speak_content):
        logging.info('===主播端发言===')
        self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/vc_edt").click()
        if type(speak_content) == list:
            for i in speak_content:
                self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/editEt").send_keys(i)
                self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/btn_send").click()
        else:
            self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/editEt").send_keys(speak_content)
            self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/btn_send").click()
        self.driver.back()
        self.driver.back()

    # 消息区内容
    def chat_area(self,num1):
        logging.info('===消息内容===')
        chat = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/contentTv")
        chat_content = chat[num1].text
        chat_text_1 = chat_content.split(":")[-1]
        chat_text_2 = chat_text_1.strip()
        return chat_text_2


    # 观众进入交友房页签
    def anchor_party_tab_Btn(self):
        logging.info('===进入交友房页签===')
        party_tab = (MobileBy.ID, "com.hkfuliao.chamet:id/rl_tab_party")
        time.sleep(3)
        self.driver.find_element(*party_tab).click()

    # 跳转至关注页面
    def go_carepage(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("关注")').click()

    # 获取交友房卡片页列表
    def party_list(self):
        try:
            self.go_carepage()
            party_list = self.driver.find_elements(MobileBy.XPATH,
                                                   "//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.FrameLayout")
            party_list_num = len(party_list)
            return party_list_num
        except:
            logging.info('===查找交由房列表出错===')


    # 观众进入10人交友房并获得页面用户名
    def anchor_enter_tenparty(self, num):
        party_list = self.driver.find_elements(MobileBy.XPATH,
                                               "//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.FrameLayout")
        partycard_username = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/tv_title")[num].text
        logging.info('===进入交友房===')
        party_list[num].click()
        return partycard_username


    # 获取交友房页面用户名
    def party_title(self):
        logging.info('===查看交友房房主用户名===')
        return self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/live_titletv").text

    # 获取消息区最后一条文本消息
    def party_textmessage(self):
        logging.info('===获取消息区最后一条文本消息===')
        party_textmessage = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        return party_textmessage[-1].text