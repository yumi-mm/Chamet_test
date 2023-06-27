from appium.webdriver.common.mobileby import MobileBy
from businessView.login_phoneView import LoginView
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
import logging
import time,os
import allure
import pytest

class PartyTenaudience(object):
    logon_button = (MobileBy.ID,"com.hkfuliao.chamet:id/tv_login")
    password_frame = (MobileBy.ID,"com.hkfuliao.chamet:id/edit_password")
    party_tab = (MobileBy.ID, "com.hkfuliao.chamet:id/rl_tab_party")


    def __init__(self,driver):
        self.driver = driver

    # 坐标之间的滑动
    def swipe_xy(self, start_x, start_y, end_x, end_y,time=2000):
        self.driver.swipe(start_x, start_y, end_x, end_y,time)

    # 获取当前系统时间
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 失败截图
    def screenshot(self, module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/party_ten/%s_%s.png' %(module,time)
        self.driver.get_screenshot_as_file(image_file)
        with open(image_file, mode='rb') as f:
            file = f.read()
        allure.attach(file, module, allure.attachment_type.PNG)
        return image_file

    # 进入h5界面后，获取上下文，并切换至h5
    def native_to_h5(self):
        '''Common.native_to_h5(self) 可以直接调用'''
        context = self.driver.contexts
        self.driver.switch_to.context(context[-1])

    # 返回至原生界面后，切换至原生界面
    def h5_to_native(self):
        '''Common.h5_to_native(self)  可以直接调用'''
        self.driver.switch_to.context('NATIVE_APP')

    # 点击系统返回键
    def back(self,num):
        for i in range(num):
            self.driver.back()

    # 判断有无签到弹窗
    def sign_in_window(self):
        try:
            sign_in_windows = (MobileBy.ANDROID_UIAUTOMATOR, 'text("连续签到")')
            signin_window= self.driver.find_element(*sign_in_windows)
        except:
            return False
        else:
            logging.info('===有签到弹窗===')
            return True

    # 签到
    def audience_sign_in(self):
        try:
            signin_window = self.sign_in_window()
            if signin_window:
                sign_in_but = (MobileBy.ID, "com.hkfuliao.chamet:id/tvSubmit")
                self.driver.find_element(*sign_in_but).click()
                self.driver.back()
            else:
                self.audience_party_tab_Btn()
        except:
            logging.info('===签到执行失败===')

    # 获取某个元素的属性
    def audience_get_attr(self, attr, *ele):
        return self.driver.find_element(*ele).get_attribute(attr)

    # 获取toast消息
    def audience_toast_message(self,message):
        return WebDriverWait(self.driver, 10, 0.05).until(EC.presence_of_element_located((MobileBy.XPATH, '//*[contains(@text, "%s")]' % message)))

    # 长按
    def audience_click_hold(self,ele):
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

    # 登陆账号(账号密码)
    def audience_login_account(self):
        logging.info('===登录===')
        logon = LoginView(self.driver)
        logon.more_Btn()
        logon.phonenumber_Btn()
        logon.login_input_phonenumber('1839172')
        logon.next_Btn()
        # l.login_input_password_or_code('1839174')
        self.driver.find_element(*self.password_frame).send_keys("1839172")
        self.driver.find_element(*self.logon_button).click()

    # 进入交友房页签
    def audience_party_tab_Btn(self):
        logging.info('===进入交友房页签===')
        time.sleep(3)
        self.driver.find_element(*self.party_tab).click()

    # 获取交友房卡片页列表
    def party_list(self):
        try:
            self.go_carepage()
            party_list = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.FrameLayout")
            party_list_num = len(party_list)
            return party_list_num
        except:
            logging.info('===查找交由房列表出错===')

    # 获取交友房卡片内容--头像
    def partycard_avatargrade(self):
        party_list_num = self.party_list()
        try:
            if party_list_num != 0:
                logging.info('===有交友房===')
                partycard_avatargrade = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/fl_party_max_level_user")
                return partycard_avatargrade
            else:
                raise
        except:
            logging.info('===没有交友房===')

    # 获取交友房卡片内容--人数
    def partycard_peopleNumber(self):
        party_list_num = self.party_list()
        try:
            if party_list_num != 0:
                logging.info('===有交友房===')
                partycard_peopleNumber = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/ll_live_num")
                return partycard_peopleNumber
            else:
                raise
        except:
            logging.info('===没有交友房===')

    # 获取交友房卡片内容--语言
    def partycard_language(self):
        party_list_num = self.party_list()
        try:
            if party_list_num != 0:
                logging.info('===有交友房===')
                partycard_language = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/city_and_language_animation")
                return partycard_language
            else:
                raise
        except:
            logging.info('===没有交友房===')

    # 获取交友房卡片内容--用户名
    def partycard_username(self):
        party_list_num = self.party_list()
        try:
            if party_list_num != 0:
                logging.info('===有交友房===')
                partycard_username = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/tv_title")
                return partycard_username
            else:
                raise
        except:
            logging.info('===没有交友房===')

    # 获取交友房卡片内容--国旗
    def partycard_nationalflag(self):
        party_list_num = self.party_list()
        try:
            if party_list_num != 0:
                logging.info('===有交友房===')
                partycard_nationalflag = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/nationalFlagIv")
                return partycard_nationalflag
            else:
                raise
        except:
            logging.info('===没有交友房===')

    # 跳转至关注页面
    def go_carepage(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("关注")').click()

    # 观众进入10人交友房并获得页面用户名
    def audience_enter_tenparty(self,num):
        party_list = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.FrameLayout")
        partycard_username = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/tv_title")[num].text
        logging.info('===进入交友房===')
        party_list[num].click()
        return partycard_username

    # 获取交友房页面用户名
    def party_title(self):
        logging.info('===查看交友房房主用户名===')
        return self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/live_titletv").text

    # 获取观众进场座驾
    def enterparty_car(self):
        try:
            enterparty_car = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/special_effects_pic_bg")
            logging.info('===有进场座驾===')
            return True
        except:
            logging.info('===无进场座驾===')
            return False

    # 获取观众进场标签
    def enterparty_label(self):
        try:
            enterparty_label = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/special_effects_pic_bg")
            logging.info('===有进场标签===')
            return True
        except:
            logging.info('===无进场标签===')
            return False

    # 获取消息区最后一条文本消息
    def party_textmessage(self):
        logging.info('===获取消息区最后一条文本消息===')
        party_textmessage = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        return party_textmessage[-1].text

    # 观众端发言
    def audience_speak_list(self,speak_content):
        logging.info('===观众端发言===')
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

    # 观众端消息区文字内容
    def audience_chat_areatext(self,num1):
        logging.info('===消息区文字内容===')
        chat = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/contentTv")
        chat_content = chat[num1].text
        chat_text_1 = chat_content.split(":")[-1]
        chat_text_2 = chat_text_1.strip()
        return chat_text_2

    # 观众端消息区内容
    def audience_chat_area(self):
        logging.info('===消息区内容===')
        chat = self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/contentTv")
        return chat

    # 观众端礼物按钮
    def audience_gift_but(self):
        logging.info('===获取礼物按钮===')
        audience_gift_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/vc_gift")
        return audience_gift_but

    # 打开观众端送礼物弹窗
    def audience_open_giftwin(self):
        audience_gift_but = self.audience_gift_but()
        logging.info('===打开礼物弹窗===')
        audience_gift_but.click()
        logging.info('#####################')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("简体中文chinese simplified")').click()

    # 观众端获取礼物弹窗中列表
    def audience_giftwin_textlist(self):
        logging.info('===获取礼物列表===')
        giftwin_text_ele = (MobileBy.XPATH,"//android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        audience_giftwin_textlist = self.driver.find_elements(*giftwin_text_ele)
        return audience_giftwin_textlist

    # 观众端送礼
    def audience_sendgift(self,num):
        logging.info('===送礼===')
        audience_giftwin_list = self.audience_giftwin_textlist()
        audience_giftwin_list[num].click()
        audience_sendgift_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/sendTv")
        audience_sendgift_but.click()
        lucky_window = self.audience_lucky_window()
        if lucky_window:
            finish = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("真棒！")')
            finish.click()
            self.driver.back()
        else:
            self.driver.back()

    # 礼物窗送礼all按钮
    def giftwin_allbut(self):
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/switchBtn").click()


    # 观众端夺宝礼物弹窗
    def audience_lucky_window(self):
        logging.info('===判断有无夺宝弹窗===')
        try:
            lucky_window = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/ll_lucky_content")
            logging.info('===获得夺宝弹窗===')
            return True
        except:
            logging.info('===无夺宝弹窗===')
            return False

    # 观众左右滑动礼物弹窗
    def left_right_swipegiftwin(self):
        audience_giftwin_list = self.audience_giftwin_textlist()
        audience_giftwin_list[1].click()
        logging.info('===左滑===')
        self.swipe_xy(600, 1200, 100, 1200)
        logging.info('===获取该页面第一个礼物名称===')
        next_first_gifttext = self.audience_giftwin_textlist()[0].text
        print(next_first_gifttext)
        logging.info('===右滑===')
        self.swipe_xy(100, 1200, 600, 1200)
        logging.info('===获取该页面第一个礼物名称===')
        last_first_gifttext = self.audience_giftwin_textlist()[0].text
        print(last_first_gifttext)
        return next_first_gifttext,last_first_gifttext

    # 观众进入游戏页面
    def audienceenter_game_window(self, game_type):
        logging.info('===进入游戏页面===')
        game_but = (MobileBy.ID, "com.hkfuliao.chamet:id/vc_box")
        game_race = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_race_game")
        game_LuckyNumber = (MobileBy.ID, "com.hkfuliao.chamet:id/ivLuckyNumber")
        race_rank = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_race_rank")
        LuckyNumber_rank = (MobileBy.ID, "com.hkfuliao.chamet:id/rank")
        game_but = self.driver.find_element(*game_but)
        game_but.click()
        game_race = self.driver.find_element(*game_race)
        game_LuckyNumber = self.driver.find_element(*game_LuckyNumber)
        if game_type == "Chamet赛车":
            logging.info('===进入赛车游戏===')
            game_race.click()
            time.sleep(5)
            return self.driver.find_element(*race_rank)
        elif game_type == "幸运数字":
            logging.info('===进入幸运数字===')
            game_LuckyNumber.click()
            time.sleep(3)
            return self.driver.find_element(*LuckyNumber_rank)
        else:
            logging.info('===游戏类型输入错误===')
            raise

    # 观众点击更多按钮
    def audience_morebut(self):
        morebut = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/vc_setting")
        logging.info('===点击展开更多===')
        morebut.click()

    # 观众申请成为嘉宾（通过加入按钮）
    def audience_applyguest(self):
        try:
            self.audience_morebut()
            enjoin = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("加入")')
            logging.info('===点击加入按钮===')
            enjoin.click()
            apply_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/apply")
            apply_but.click()
            time.sleep(1)
            return True
        except:
            return False

    # 观众端10人交友房交友位
    def tenparty_site(self):
        tenparty_site = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        return tenparty_site

    # 观众端申请上麦
    def partysite_applyguest(self,num):
        tenparty_site = self.tenparty_site()
        try:
            logging.info('===点击交友位===')
            tenparty_site[num].click()
            apply_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/apply")
            apply_but.click()
            time.sleep(1)
            return True
        except:
            return False

    # 观众进入主播个人主页半屏浮窗
    def enteranchor_HalfScreen(self):
        tenparty_site = self.tenparty_site()
        logging.info('===点击展开主播个人主页半屏浮窗===')
        tenparty_site[0].click()

    # 获取半屏浮层主播名字
    def getanchor_HalfScreenname(self):
        logging.info('===获取半屏浮层主播名字===')
        anchor_name = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/profile_name")
        return anchor_name.text

    # 获取交友房标题
    def getparty_title(self):
        logging.info('===获取交友房主播名称===')
        getparty_title = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/live_titletv")
        return getparty_title.text

    # 获取半层浮屏主播名称
    def gethalfwin_name(self):
        logging.info('===获取半屏交友房主播名称===')
        halfwin_name = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/profile_name")
        return halfwin_name.text

    # 观众打开主播个人主页半屏浮窗
    def openanchor_HalfScreen(self):
        getparty_title = self.getparty_title()
        logging.info(getparty_title)
        self.enteranchor_HalfScreen()
        getanchor_HalfScreenname = self.getanchor_HalfScreenname()
        logging.info(getanchor_HalfScreenname)
        return getparty_title,getanchor_HalfScreenname

    # 进入主播个人主页
    def enteranchor_Personalhomepage(self):
        halfwin_name = self.gethalfwin_name()
        time.sleep(1)
        logging.info('===点击进入主播个人主页===')
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_user_head").click()
        user_name = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_user_name").text
        return halfwin_name,user_name

    # 进入主播个人主页(无返回值)
    def enteranchor_Personalhome(self):
        self.enteranchor_HalfScreen()
        time.sleep(1)
        logging.info('===点击进入主播个人主页===')
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_user_head").click()

    # 从主播个人主页交友房小窗进入直播间
    def Personalhome_enterparty(self):
        party_littlewindow = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/live_icon")
        logging.info('===点击个人主页交友房小窗===')
        party_littlewindow.click()
        getparty_title = self.getparty_title()
        return getparty_title

    # 个人主页浮层送礼
    def HalfScreen_sendgift(self,num):
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/profile_gift").click()
        logging.info('#####################')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("简体中文chinese simplified")').click()
        self.audience_sendgift(num)

    # 个人主页浮层拨打通话
    def HalfScreen_Videocall(self):
        try:
            call_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/ll_enable")
            logging.info('===给主播拨打视频通话===')
            call_but.click()
            time.sleep(3)
            return True
        except:
            return False

    # 个人主页浮层@主播
    def HalfScreen_aiteanchor(self):
        logging.info('===观众@主播===')
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_atHer").click()
        time.sleep(1)

    # 查看主播有无动态
    def abchor_groupview(self):
        try:
            group_view = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/rl_group_view")
            logging.info('===有动态===')
            return True
        except:
            logging.info('===无动态===')
            return False

    # 有动态时返回动态列表
    def watch_groupview(self):
        if self.abchor_groupview():
            groupviewlist = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")
            logging.info('===点击查看动态===')
            groupviewlist[0].click()
        else:
            pytest.skip("没有动态，跳过该测试用例")

    # 展开观众列表
    def open_morepeople(self):
        time.sleep(3)
        morepeople_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_more_people")
        logging.info('===展开观众列表浮窗===')
        morepeople_but.click()
        audiencesCount = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/audiencesCount").text
        return audiencesCount

    # 打开观众个人主页半屏浮窗
    def open_audience_HalfScreen(self):
        self.open_morepeople()
        audiencelist = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]")
        logging.info('===点击展开观众个人主页半屏浮窗===')
        audiencelist[0].click()
        time.sleep(2)

    # 通过半屏浮层举报主播
    def report_anchor(self):
        report_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_report")
        logging.info('===点击举报按钮===')
        report_but.click()
        reportwin_title = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_report_title")
        return reportwin_title.text

    # 观众端点击更多按钮
    def audienceopen_more(self):
        try:
            more_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/vc_setting")
            logging.info('===点击更多按钮===')
            more_but.click()
        except:
            logging.info('===不存在更多按钮===')

    # 观众端打开消息列表
    def audienceopen_message(self):
        self.audienceopen_more()
        message_but = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("留言")')
        logging.info('===打开留言浮窗===')
        message_but.click()

    # 观众端获取私聊列表
    def audience_usermessagelist(self):
        try:
            logging.info('===查看私聊列表===')
            usermessage_ele = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout")
            usermessage_lists = self.driver.find_elements(*usermessage_ele)
            return usermessage_lists
        except:
            logging.info('===寻找私聊列表时出错===')

    # 观众端进入私聊页面
    def audienceenter_usermessage(self):
        self.audienceopen_message()
        audience_usermessagelists = self.audience_usermessagelist()
        if len(audience_usermessagelists) == 0:
            pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
        logging.info('===进入私聊页面===')
        audience_usermessagelists[0].click()

    # 观众端私聊页面查看用户名标题
    def usermessage_name(self):
        usermessage_nameele = (MobileBy.ID,"com.hkfuliao.chamet:id/tv_name")
        usermessage_name = self.driver.find_element(*usermessage_nameele)
        return usermessage_name.text

    # 观众端私聊页面发送文字
    def audience_usermessage_sendtext(self,message_text):
        self.audienceenter_usermessage()
        logging.info('===准备发送文字消息===')
        usermessage_edit_frame = (MobileBy.ID, "com.hkfuliao.chamet:id/editEt")
        self.driver.find_element(*usermessage_edit_frame).click()
        self.driver.find_element(*usermessage_edit_frame).send_keys(message_text)
        usermessage_edit_sendbut = (MobileBy.ID, "com.hkfuliao.chamet:id/btn_send")
        self.driver.find_element(*usermessage_edit_sendbut).click()
        logging.info('===发送成功===')
        time.sleep(1)

    # 获取聊天区文本消息
    def get_usermessage_textcontent(self,num):
        # usermessage_region_textele = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView")
        usermessage_region_textele = (MobileBy.XPATH,
                                   "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView")
        usermessage_region_text = self.driver.find_elements(*usermessage_region_textele)
        logging.info(len(usermessage_region_text))
        return usermessage_region_text[num].text

    # 观众端私聊页面发送表情
    def audience_usermessage_sendexpression(self,index):
        self.audienceenter_usermessage()
        logging.info('===准备发送表情===')
        usermessage_expression_but = (MobileBy.ID,"com.hkfuliao.chamet:id/iv_face_gif")
        self.driver.find_element(*usermessage_expression_but).click()
        time.sleep(3)
        usermessage_expression = (MobileBy.XPATH,
                                  "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
        if index == 0:
            logging.info('===发送google表情===')
            self.driver.find_elements(*usermessage_expression)[index].click()
            google_expression_searchframe = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/et_search_id")
            google_expression_searchframe.send_keys("hah")
            google_expression_searchbut = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_search")
            google_expression_searchbut.click()
            time.sleep(0.5)
            google_expression_list = self.driver.find_elements(MobileBy.XPATH,
                                                               "//android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
            time.sleep(1)
            google_expression_list[0].click()
        else:
            logging.info('===发送Chamet表情===')
            self.driver.find_elements(*usermessage_expression)[index].click()
        logging.info('===发送成功===')

    # 获取私聊页面聊天区图片消息
    def get_usermessage_photocontent(self):
        usermessage_region_expression = (MobileBy.XPATH,
                                         "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView")
        expression_list = self.driver.find_elements(*usermessage_region_expression)
        return len(expression_list)

    # 获取聊天区google图片消息
    def get_usermessage_googlephotocontent(self):
        google_expression_list = (MobileBy.XPATH,
                                  "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[2]")
        google_expression_list = self.driver.find_elements(*google_expression_list)
        return len(google_expression_list)

    # 观众端展开私聊页面下拉按钮
    def open_usermessage_dropdown(self):
        self.audienceenter_usermessage()
        logging.info('===展开下拉列表===')
        iv_more_bottom = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_more_bottom")
        iv_more_bottom.click()

    # 获取翻译元素
    def usermessage_translate_but(self):
        self.open_usermessage_dropdown()
        translate_butele = (MobileBy.ANDROID_UIAUTOMATOR,'text("翻译")')
        translate_but = self.driver.find_element(*translate_butele)
        return translate_but

    # 开启翻译功能
    def open_usermessage_translate(self):
        try:
            self.open_usermessage_dropdown()
            translate_butele = (MobileBy.ID, "com.hkfuliao.chamet:id/translateView")
            translate_but = self.driver.find_element(*translate_butele)
            logging.info('===点击翻译按钮===')
            translate_but.click()
            time.sleep(2)
            return True
        except:
            return False

    # 判断有无权限弹窗
    def permission_window(self):
        try:
            permission_windows = (MobileBy.ID, "com.android.permissioncontroller:id/permission_message")
            window = self.driver.find_element(*permission_windows)
        except:
            return False
        else:
            logging.info('===有权限弹窗===')
            return True

    # 同意权限弹窗
    def choic_permission_window(self):
        try:
            permission_allow_foreground_only_button = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            permission_allow_button = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
            if self.driver.find_element(*permission_allow_foreground_only_button):
                self.driver.find_element(*permission_allow_foreground_only_button).click()
            else:
                self.driver.find_element(*permission_allow_button).click()
        except:
            logging.info('===权限执行失败===')

    # 观众端私聊界面打开相册
    def usermessage_photo_but(self):
        self.open_usermessage_dropdown()
        photo_butele = (MobileBy.ANDROID_UIAUTOMATOR,'text("相册")')
        photo_but = self.driver.find_element(*photo_butele)
        logging.info('===打开相册===')
        photo_but.click()
        pw = self.permission_window()
        # if pw:
        #     self.choic_permission_window()
        #     self.choic_permission_window()
        #     self.choic_permission_window()
        # else:
        #     logging.info('===无权限弹窗===')

    # 观众端私聊页面发送相册照片
    def audience_usermessage_sendphoto(self,num):
        self.usermessage_photo_but()
        logging.info('===发送相册照片===')
        try:
            for i in range(num):
                self.driver.find_elements(MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView[2]")[i].click()
            self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/menu_id_confirm").click()
            time.sleep(2)
            return True
        except:
            return False

    # 观众端私聊界面打开相机
    def usermessage_camera_but(self):
        self.open_usermessage_dropdown()
        camera_butele = (MobileBy.ANDROID_UIAUTOMATOR, 'text("相机")')
        camera_but = self.driver.find_element(*camera_butele)
        logging.info('===打开相机===')
        camera_but.click()

    # 观众端私聊页面发送相机照片
    def audience_usermessage_sendcameraphoto(self):
        self.usermessage_camera_but()
        logging.info('===拍照发送===')
        try:
            self.driver.find_element(MobileBy.ID,"com.oppo.camera:id/shutter_button").click()
            self.driver.find_element(MobileBy.ID,"com.oppo.camera:id/done_button").click()
            time.sleep(2)
            return True
        except:
            return False

    # 获取聊天区未接电话文本消息
    def get_usermessage_voicecontent(self,num):
        usermessage_region_voiceele = (MobileBy.XPATH,
                                   "//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]")
        usermessage_region_voice = self.driver.find_elements(*usermessage_region_voiceele)
        return usermessage_region_voice[num].text

    # 用户无法接通
    def not_available_ele(self):
        try:
            not_availableele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("用户此时无法连接。请稍后拨打。")')
            logging.info('===用户不在线===')
            return True
        except:
            logging.info('===用户在线===')
            return False

    def not_available_win(self):
        not_available_ele = self.not_available_ele()
        if not_available_ele:
            single_btn = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/single_btn")
            single_btntext = single_btn.text
            assert single_btntext == "确认"
            logging.info('===断言成功，用户无法接通===')
            single_btn.click()
            time.sleep(1)
        else:
            time.sleep(6)
            get_usermessage_voicecontent = self.get_usermessage_voicecontent(-1)
            assert "用户没有回答" in get_usermessage_voicecontent
            logging.info('===断言成功，成功拨打电话===')


    # 观众端私聊页面拨打语音聊天
    def usermessage_video_but(self):
        # try:
        self.open_usermessage_dropdown()
        video_butele = (MobileBy.ANDROID_UIAUTOMATOR, 'text("语音聊天")')
        video_but = self.driver.find_element(*video_butele)
        logging.info('===拨打语言聊天===')
        video_but.click()
        self.not_available_win()
            # time.sleep(7)
            # return True
        # except:
        #     return False

    # 观众端打开私聊送礼页面
    def audience_usermessage_open_giftpage(self):
        self.audienceenter_usermessage()
        try:
            logging.info('===打开私聊送礼页面===')
            open_giftbut = self.driver.find_element(MobileBy.ID,'com.hkfuliao.chamet:id/iv_chat_gift')
            open_giftbut.click()
        except:
            logging.info('===无礼物按钮===')

    # 观众端私聊礼物页面左滑右滑
    def audience_usermessage_scroll_gift(self):
        self.audience_usermessage_open_giftpage()
        logging.info('#####################')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("简体中文chinese simplified")').click()
        gift_list_text = self.driver.find_elements(MobileBy.XPATH,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        gift_list_text[0].click()
        self.swipe_xy(600, 1200, 100, 1200)
        nowgift_list_text = self.driver.find_elements(MobileBy.XPATH,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        self.swipe_xy(100, 1200, 600, 1200)
        newgift_list_text = self.driver.find_elements(MobileBy.XPATH,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        return nowgift_list_text,newgift_list_text


    # 观众端充值优惠卷
    def audience_enrich_window(self):
        logging.info("===判断有无充值优惠券===")
        try:
            enrich_window = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("去使用")')
            return True
        except:
            return False

    # 观众端取消充值优惠券
    def audience_cancel_enrich_window(self):
        enrich_window = self.audience_enrich_window()
        if enrich_window:
            logging.info("===有优惠券===")
            self.driver.back()
            self.driver.back()
        else:
            logging.info("===无优惠券===")
            self.driver.back()

    # 观众端私聊礼物按钮中送礼
    def audience_usermessage_sendgift(self):
        self.audience_usermessage_open_giftpage()
        logging.info('#####################')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("简体中文chinese simplified")')
        logging.info("===送礼物===")
        usermessage_gift_but = (MobileBy.XPATH,
                                "//android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ImageView")
        self.driver.find_element(*usermessage_gift_but).click()
        self.audience_cancel_enrich_window()

    # 观众端私聊中打开个人主页浮层
    def audienceopen_Profilefloat(self):
        self.audienceenter_usermessage()
        user_name = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_name").text
        logging.info("===打开个人主页浮层===")
        more_but = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_more")
        more_but.click()
        time.sleep(1)
        profile_name = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/profile_name").text
        return user_name,profile_name

    # 观众端获取群聊列表
    def audience_groupmessagelist(self):
        try:
            logging.info('===查看群聊列表===')
            groupmessage_ele = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout")
            groupmessage_lists = self.driver.find_elements(*groupmessage_ele)
            return groupmessage_lists
        except:
            logging.info('===寻找私聊列表时出错===')

    # 观众端进入群聊页面
    def audienceenter_groupmessage(self):
        self.audienceopen_message()
        audience_groupmessagelists = self.audience_groupmessagelist()
        if len(audience_groupmessagelists) == 0:
            pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
        logging.info('===进入群聊页面===')
        audience_groupmessagelists[0].click()

    # 观众端群聊页面查看标题
    def audience_groupmessage_name(self):
        groupmessage_nameele = (MobileBy.ID,"com.hkfuliao.chamet:id/tv_group_number")
        groupmessage_name = self.driver.find_element(*groupmessage_nameele)
        return groupmessage_name.text

    # 观众端群聊页面发送文字
    def audience_groupmessage_sendtext(self,message_text):
        self.audienceenter_groupmessage()
        logging.info('===准备发送文字消息===')
        groupmessage_edit_frame = (MobileBy.ID, "com.hkfuliao.chamet:id/et_edit_chat_info")
        groupmessage_edit_sendbut = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_send_message")
        self.driver.find_element(*groupmessage_edit_frame).click()
        self.driver.find_element(*groupmessage_edit_frame).send_keys(message_text)
        self.driver.find_element(*groupmessage_edit_sendbut).click()
        logging.info('===发送成功===')
        time.sleep(1)

    # 获取群聊页面聊天区图片消息
    def get_groupmessage_photocontent(self):
        groupmessage_region_expression = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView")
        expression_list = self.driver.find_elements(*groupmessage_region_expression)
        return len(expression_list)

    # 观众端群聊页面发送表情
    def audience_groupmessage_sendexpression(self,index):
        self.audienceenter_groupmessage()
        logging.info('===准备发送表情===')
        usermessage_expression_but = (MobileBy.ID,"com.hkfuliao.chamet:id/iv_face_gif")
        self.driver.find_element(*usermessage_expression_but).click()
        time.sleep(3)
        usermessage_expression = (MobileBy.XPATH,
                                  "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
        if index == 0:
            logging.info('===发送google表情===')
            self.driver.find_elements(*usermessage_expression)[index].click()
            google_expression_searchframe = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/et_search_id")
            google_expression_searchframe.send_keys("hah")
            google_expression_searchbut = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_search")
            google_expression_searchbut.click()
            time.sleep(0.5)
            google_expression_list = self.driver.find_elements(MobileBy.XPATH,
                                                               "//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")
            time.sleep(0.5)
            google_expression_list[0].click()
        else:
            logging.info('===发送Chamet表情===')
            self.driver.find_elements(*usermessage_expression)[index].click()
            time.sleep(1)
        logging.info('===发送成功===')

    # 获取群聊页聊天区google图片消息
    def get_groupmessage_googlephotocontent(self):
        groupgoogle_expression_list = (MobileBy.XPATH,
                                       "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView")
        google_expression_list = self.driver.find_elements(*groupgoogle_expression_list)
        return len(google_expression_list)

    # 观众端群聊页面发送语音
    def audience_groupmessage_send_voice(self):
        self.audienceenter_groupmessage()
        logging.info('===准备发送语音===')
        groupmessage_voicebut = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_voice")
        groupmessage_voicebut.click()
        groupmessage_voice_frame = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_add_voice")
        # 长按录入语音
        self.audience_click_hold(groupmessage_voice_frame)

    # 观众端获取群聊中语音文本
    def audience_voice_text(self):
        voice_ele = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView")
        voice_time = voice_ele.text
        return voice_time

    # 观众端群聊页面上麦
    def audience_up_microphone(self):
        self.audienceenter_groupmessage()
        logging.info('===观众端上麦===')
        microphone = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_bottom_up_mic")
        microphone.click()

    # 观众端群聊中发送相册图片
    def audience_groupmessage_sendphoto(self,num):
        self.audienceenter_groupmessage()
        logging.info('===发送照片===')
        photo_camera_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_more_pic")
        photo_camera_but.click()
        photo_choicebut = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("从相册挑选")')
        photo_choicebut.click()
        logging.info('===发送相册照片===')
        try:
            self.driver.find_elements(MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView")[num].click()
            time.sleep(1)
            return True
        except:
            return False

    # 观众端群聊中发送拍摄图片
    def audience_groupmessage_sendcameraphoto(self):
        self.audienceenter_groupmessage()
        logging.info('===发送照片===')
        photo_camera_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_more_pic")
        photo_camera_but.click()
        cameraphoto_choicebut = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("拍照")')
        cameraphoto_choicebut.click()
        logging.info('===发送拍摄照片===')
        try:
            self.driver.find_element(MobileBy.ID,"com.oppo.camera:id/shutter_button").click()
            time.sleep(2)
            self.driver.find_element(MobileBy.ID,"com.oppo.camera:id/done_button").click()
            time.sleep(2)
            return True
        except:
            return False

    # 观众端群聊页面发送钻石包
    def audience_send_diamondenvelope(self,envelope_num,diamond_num):
        self.audienceenter_groupmessage()
        logging.info('===发送钻石包===')
        diamond_envelope_but =  self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_packet")
        diamond_envelope_but.click()
        member = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_label_members").text
        packet_count = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/ed_packet_count")
        packet_total_energy = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/ed_packet_total_energy")
        send_but = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/btn_send_packet")
        packet_count.send_keys(envelope_num)
        packet_total_energy.send_keys(diamond_num)
        send_but.click()
        time.sleep(1)

    # 观众端群聊页面领取钻石包
    def audience_get_diamondenvelope(self):
        logging.info('===领取钻石包===')
        messageregion_getenvelope = self.messageregion_getenvelope()
        messageregion_getenvelope[-1].click()
        open_envelope = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_open_diamond_packet")
        open_envelope.click()

    # 钻石红包获取
    def messageregion_getenvelope(self):
        time.sleep(1)
        envelope = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, 'text("幸运红包")')
        return envelope

    # 领红包标识（用户头像）
    def getenvelope_userhead(self):
        user_head = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/civ_user_head")
        return user_head

    # 观众端群聊页面送礼
    def audience_groupmessage_sendgift(self,num):
        self.audienceenter_groupmessage()
        logging.info('===打开礼物页面===')
        gift_but = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[4]")
        gift_but.click()
        logging.info('##############')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("简体中文chinese simplified")').click()
        gift_listimage = (MobileBy.XPATH,
                          "//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView")
        gift_list = self.driver.find_elements(*gift_listimage)
        gift_list[num].click()
        groupmessage_gift_but = (MobileBy.XPATH,
                                "//android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ImageView")
        send_gift = self.driver.find_element(*groupmessage_gift_but)
        send_gift.click()
        lucky_window = self.audience_lucky_window()
        if lucky_window:
            finish = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("真棒！")')
            finish.click()
            self.driver.back()
        else:
            self.driver.back()

    #
    def audience_giftmessageimage(self):
        group_giftmessageimage = (MobileBy.XPATH,
                                  "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageView")
        return self.driver.find_elements(*group_giftmessageimage)

    # 进入10人交友房充值页面
    def audience_enterrechargepage(self):
        self.audienceopen_more()
        logging.info('===进入充值页面===')
        recharge = (MobileBy.ANDROID_UIAUTOMATOR, 'text("充值")')
        recharge = self.driver.find_element(*recharge)
        recharge.click()

    # 充值页面标识
    def audience_rechargepage(self):
        audience_rechargepage = (MobileBy.ANDROID_UIAUTOMATOR, 'text("我的钻石")')
        return self.driver.find_element(*audience_rechargepage)

    # 进入10人交友房充值页面
    def audience_recharge_diamond(self):
        self.audience_enterrechargepage()
        logging.info('===进行充值===')
        recharge_level = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup")
        recharge_level[0].click()
        time.sleep(2)
        buy_but = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("一键购买")')
        buy_but.click()
        time.sleep(2)

    # 获取钻石弹窗
    def audience_buysuccess_page(self):
        buy_success_page = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_card_icon")
        return self.driver.find_element(*buy_success_page)

    # 观众端进入任务页面
    def audience_entertaskpage(self):
        self.audienceopen_more()
        logging.info('===进入任务页面===')
        task_but = (MobileBy.ANDROID_UIAUTOMATOR, 'text("任务")')
        task_but = self.driver.find_element(*task_but)
        task_but.click()

    # 任务页标题
    def taskpage_title(self):
        task_page = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_tab_tasks")
        return self.driver.find_element(*task_page).text

    # 观众进入礼物荣誉墙
    def audience_enter_giftnamingwall(self):
        logging.info('===进入礼物荣誉墙===')
        giftnaming_wall = (MobileBy.ID, "com.hkfuliao.chamet:id/gift_honor_wall_drag_view")
        giftnamingwall_but = self.driver.find_element(*giftnaming_wall)
        giftnamingwall_but.click()

    # 礼物荣誉墙标题
    def giftwall_title(self):
        giftwall_title = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_title")
        return self.driver.find_element(*giftwall_title).text

    # 观众进入活动banner
    def audience_enter_banner(self):
        try:
            banner_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/image")
            banner_but.click()
            logging.info('===进入活动页===')
            return True
        except:
            logging.info('===未成功进入活动页===')
            return False






