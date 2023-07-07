from appium.webdriver.common.mobileby import MobileBy
from businessView.login_phoneView import LoginView
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
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

    # 点击系统返回键
    def back(self,num):
        for i in range(num):
            self.driver.back()

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
    def anchor_sign_in(self):
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
        permission_allow_foreground_only_button = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
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
    def party_textmessage(self,num):
        logging.info('===获取消息区最后一条文本消息===')
        party_textmessage = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        return party_textmessage[num].text

    # 获取消息区@消息
    def party_textmessage_aite(self,num):
        logging.info('===获取消息区最后一条文本消息===')
        party_textmessage = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
        return party_textmessage[num].text

    # 打开送礼弹窗
    def open_gift_window(self):
        logging.info('===打开送礼弹窗===')
        room_gift_but = (MobileBy.ID, "com.hkfuliao.chamet:id/vc_gift")
        send_gift_but = self.driver.find_element(*room_gift_but)
        send_gift_but.click()
        logging.info('#####################')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("简体中文chinese simplified")').click()

    # 获取礼物弹窗中礼物列表
    def gift_lst(self):
        logging.info('===获取礼物列表===')
        gift_list_text = (MobileBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        giftlst_text = self.driver.find_elements(*gift_list_text)
        return giftlst_text

    # 获取某个元素的属性
    def get_attr(self, attr, *ele):
        return self.driver.find_element(*ele).get_attribute(attr)

    # 主播端获取礼物弹窗中列表
    def audience_giftwin_textlist(self):
        logging.info('===获取礼物列表===')
        giftwin_text_ele = (MobileBy.XPATH,"//android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        audience_giftwin_textlist = self.driver.find_elements(*giftwin_text_ele)
        return audience_giftwin_textlist

    # 主播左右滑动礼物弹窗
    def left_right_swipegiftwin(self):
        audience_giftwin_list = self.audience_giftwin_textlist()
        audience_giftwin_list[1].click()
        logging.info('===左滑===')
        self.swipe_xy(930, 1600, 130, 1600)
        logging.info('===获取该页面第一个礼物名称===')
        next_first_gifttext = self.audience_giftwin_textlist()[0].text
        print(next_first_gifttext)
        logging.info('===右滑===')
        self.swipe_xy(130, 1600, 930, 1600)
        logging.info('===获取该页面第一个礼物名称===')
        last_first_gifttext = self.audience_giftwin_textlist()[0].text
        print(last_first_gifttext)
        return next_first_gifttext,last_first_gifttext

    # 主播端申请上麦未读消息
    def applicants(self):
        applicants = (MobileBy.ID,"com.hkfuliao.chamet:id/applicantsCount")
        try:
            applicants_ele = self.driver.find_element(*applicants)
            return True
        except:
            return False

    # 主播端打开申请列表
    def open_applylist(self):
        applybut = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_invite")
        try:
            applybut_ele = self.driver.find_element(*applybut)
        except:
            logging.info('===下方无申请列表按钮===')
        else:
            applybut_ele.click()

    # 主播同意观众上麦(下方)
    def agree_apply(self):
        self.open_applylist()
        logging.info('===同意观众上麦===')
        self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/live_queue_invite").click()
        self.driver.back()

    # 主播同意观众上麦(右上角)
    def agree_applyright(self):
        self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_more_people").click()
        self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/rl_applicants").click()
        logging.info('===同意观众上麦===')
        self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/live_queue_invite").click()
        self.driver.back()

    # 第二个交友位是否存在嘉宾
    def second_guest(self):
        try:
            second_guest = self.driver.find_element(MobileBy.XPATH,
                                       "//android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout[1]")
            return True
        except:
            logging.info('===未成功上麦===')
            return False

    # 第二个交友位嘉宾检查
    def guest_watch(self):
        two_site = (MobileBy.XPATH,"//android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout[1]")
        return self.driver.find_element(*two_site)

    # 点击展开嘉宾个人主页半屏弹窗
    def open_guesthalfwin(self):
        try:
            audience_site = (MobileBy.XPATH,
                         "//android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout[1]")
            two_site = self.driver.find_element(*audience_site)
        except:
            logging.info('===交友位不存在嘉宾===')
        else:
            logging.info('===展开嘉宾个人主页半屏浮窗===')
            two_site.click()

    # 主播移除嘉宾
    def remove_guest(self):
        try:
            remove_guestbut = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_remove")
        except:
            logging.info('===不存在移除按钮===')
        else:
            logging.info('===主播移除嘉宾===')
            remove_guestbut.click()

    # 获取嘉宾用户名
    def get_guestname(self):
        try:
            guest_name = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/profile_name").text
        except:
            logging.info('===获取嘉宾用户名失败===')
        else:
            logging.info('===获取嘉宾用户名===')
            logging.info('===嘉宾用户名为：%s===' %guest_name)
            return guest_name

    # 主播禁言嘉宾
    def mute_guest(self):
        try:
            mute_guestbut = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_mute")
        except:
            logging.info('===不存在禁言按钮===')
        else:
            logging.info('===主播禁言嘉宾===')
            mute_guestbut.click()

    # 通过id过去元素xpath
    def get_elexpath_byid(self,ele_id):
        # 获取元素的 ID
        element_id = ele_id
        # 使用 Android UI Automator 获取元素的 XPath
        xpath = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiSelector().resourceId("{element_id}").toString()')
        return xpath

    # 获取name对应的邀请按钮
    def invite_guest(self, ele_text):
        # 嘉宾name
        element_text = ele_text
        self.open_audiencelist()
        audience_list = self.get_audience_list()
        if len(audience_list) == 0:
            logging.info('===交友房无观众===')
            raise
        elif len(audience_list) == 1:
            logging.info('===交友房有一个观众===')
            self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/live_queue_invite").click()
        else:
            num = 1
            for i in audience_list:
                if i.text == element_text:
                    break
                num += 1
            logging.info('===指定观众在%d位===' %num)
            logging.info('===点击观众后的邀请按钮===')
            a = (MobileBy.XPATH,"//android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.ImageView" %num)
            print(a)
            self.driver.find_element(*a).click()
            return a


    # 获取观众列表name
    def get_audience_list(self):
        logging.info('===获取所有观众name===')
        audience_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
        return audience_list

    # 主播禁言嘉宾
    def cancelmute_guest(self):
        try:
            cancelmute_guestbut = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("取消禁言")')
        except:
            logging.info('===不存在取消禁言按钮===')
        else:
            logging.info('===主播取消禁言===')
            cancelmute_guestbut.click()

    # 主播打开右上角观众列表
    def open_audiencelist(self):
        try:
            audiencelist_but = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_more_people")
        except:
            logging.info('===右上角不存在观众列表按钮===')
        else:
            logging.info('===打开观众列表===')
            audiencelist_but.click()

    # 获取某个元素的属性
    def audience_get_attr(self, attr, *ele):
        return self.driver.find_element(*ele).get_attribute(attr)

    # 主播接听约聊电话
    def accept_phone(self):
        try:
            accpet_phonebut = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/vc_iv_accept")
            accpet_phonebut.click()
            logging.info('===主播成功接听电话===')
            return True
        except:
            logging.info('===主播接听电话失败===')
            return False

    # 主播拒绝约聊电话
    def reject_phone(self):
        try:
            reject_phonebut = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/vc_iv_reject")
            reject_phonebut.click()
            logging.info('===主播拒绝接听电话===')
            return True
        except:
            logging.info('===主播拒绝电话失败===')
            return False

    # 主播进入私聊界面
    def enter_privatechatpage(self):
        logging.info('===主播点击私信弹窗消息进入私聊页面===')
        privatechat_win = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/rl_live_chat")
        privatechat_win.click()

    # 获取聊天区最后一条文本消息
    def get_messagetext(self,num):
        logging.info('===获取主播聊天区文本消息===')
        message_list = self.driver.find_elements(MobileBy.ID,"com.hkfuliao.chamet:id/tv_content")
        return message_list[num].text

    # 私聊界面发送文字
    def usermessage_send_text(self,message_text):
        logging.info('===准备发送文字消息===')
        usermessage_edit_frame = (MobileBy.ID, "com.hkfuliao.chamet:id/editEt")
        usermessage_edit_sendbut = (MobileBy.ID, "com.hkfuliao.chamet:id/btn_send")
        self.driver.find_element(*usermessage_edit_frame).click()
        self.driver.find_element(*usermessage_edit_frame).send_keys(message_text)
        self.driver.find_element(*usermessage_edit_sendbut).click()
        logging.info('===发送成功===')

    # 查看私聊界面对方发送表情(Chamet表情)
    def watch_othersendexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" %message_num)
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.view.ViewGroup/android.widget.ImageView" %message_num)
        return head_frame,expression

    # 查看私聊界面自己发送表情(Chamet表情)
    def watch_selfsendexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        try:
            head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" %message_num)
        except NoSuchElementException as e:
            logging.info('===断言成功，为自己发的消息===')
            assert True
        else:
            logging.info('===断言失败，自己未发消息===')
            assert False
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.view.ViewGroup/android.widget.ImageView" %message_num)
        return expression

    # 查看私聊界面对方发送表情(谷歌表情)
    def watch_othersendgoogleexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" %message_num)
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.view.ViewGroup/android.widget.ImageView[2]" %message_num)
        return head_frame,expression

    # 查看私聊界面自己发送表情(谷歌表情)
    def watch_selfsendgooglexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        try:
            head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" %message_num)
        except NoSuchElementException as e:
            logging.info('===断言成功，为自己发的消息===')
            assert True
        else:
            logging.info('===断言失败，自己未发消息===')
            assert False
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.view.ViewGroup/android.widget.ImageView[2]" %message_num)
        return expression

    def usermessage_send_expression(self,index):
        logging.info('===准备发送表情===')
        usermessage_expression_but = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_face_gif")
        usermessage_expression = (MobileBy.XPATH,
                                  "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
        self.driver.find_element(*usermessage_expression_but).click()
        time.sleep(2)
        if index == 0:
            self.driver.find_elements(*usermessage_expression)[index].click()
            google_expression_searchframe = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/et_search_id")
            google_expression_searchframe.send_keys("wow")
            google_expression_searchbut = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_search")
            google_expression_searchbut.click()
            time.sleep(0.5)
            google_expression_list = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")
            time.sleep(0.5)
            google_expression_list[0].click()
        else:
            self.driver.find_elements(*usermessage_expression)[index].click()
            self.touch_tap(350, 800)

    # 点击空白处
    def touch_tap(self, x, y, duration=2000):  # 点击坐标  ,x1,x2,y1,y2,duration
        logging.info('===点击空白处===')
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)



