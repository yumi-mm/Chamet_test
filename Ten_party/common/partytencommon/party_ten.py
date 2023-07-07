from appium.webdriver.common.mobileby import MobileBy
from businessView.login_phoneView import LoginView
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
import logging
import time,os
import allure

class PartyTen(object):

    logon_button = (MobileBy.ID,"com.hkfuliao.chamet:id/tv_login")
    password_frame = (MobileBy.ID,"com.hkfuliao.chamet:id/edit_password")
    party_tab = (MobileBy.ID, "com.hkfuliao.chamet:id/rl_tab_party")
    my_tab = (MobileBy.ID ,"com.hkfuliao.chamet:id/image_mine")
    message = (MobileBy.ANDROID_UIAUTOMATOR ,'text("留言")')
    my_level = (MobileBy.ANDROID_UIAUTOMATOR ,'text("我的等级")')
    settings = (MobileBy.ANDROID_UIAUTOMATOR,'text("设置")')
    log_out = (MobileBy.ANDROID_UIAUTOMATOR,'text("登出")')
    recharge = (MobileBy.ANDROID_UIAUTOMATOR,'text("充值")')
    task_but = (MobileBy.ANDROID_UIAUTOMATOR,'text("任务")')
    task_page = (MobileBy.ID,"com.hkfuliao.chamet:id/tv_tab_tasks")
    partyPreviewPage_quit = (MobileBy.ID, "com.hkfuliao.chamet:id/closeTv")
    partyPreviewPage_enter = (MobileBy.ID,"com.hkfuliao.chamet:id/btn")
    party_enterbut = (MobileBy.ID,"com.hkfuliao.chamet:id/btn_live")
    ten_people = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_live_room_ten")
    party_quitbut = (MobileBy.ID, "com.hkfuliao.chamet:id/vc_close")
    warning_message = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
    room_gift_but = (MobileBy.ID,"com.hkfuliao.chamet:id/vc_gift")
    gift_list_text = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
    send_gift_but = (MobileBy.ID,"com.hkfuliao.chamet:id/sendTv")
    more_but = (MobileBy.ID,"com.hkfuliao.chamet:id/vc_setting")
    background = (MobileBy.ANDROID_UIAUTOMATOR,'text("背景")')
    sign_in_windows = (MobileBy.ANDROID_UIAUTOMATOR,'text("连续签到")')
    sign_in_but = (MobileBy.ID,"com.hkfuliao.chamet:id/tvSubmit")
    permission_windows = (MobileBy.ID, "com.android.permissioncontroller:id/permission_message")
    permission_allow_foreground_only_button = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    permission_allow_one_time_button = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button")
    permission_deny_button = (MobileBy.ID, "com.android.permissioncontroller:id/permission_deny_button")
    permission_allow_button = (MobileBy.ID,"com.android.permissioncontroller:id/permission_allow_button")
    background_list = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
    partyroom_leve = (MobileBy.ID,"com.hkfuliao.chamet:id/tv_user_level")
    background_title = (MobileBy.ID,'com.hkfuliao.chamet:id/tv_title')
    partymessage = (MobileBy.ANDROID_UIAUTOMATOR,'text("留言")')
    chamet_customer_service = (MobileBy.ID,"com.hkfuliao.chamet:id/rl_customer_service_content")
    party_message_lists = (MobileBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout")
    party_message_user_lists = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout")
    party_message_group_lists = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout")
    message_page_name = (MobileBy.ID,"com.hkfuliao.chamet:id/tv_name")
    usermessage_edit_frame = (MobileBy.ID, "com.hkfuliao.chamet:id/editEt")
    usermessage_region_text = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView")
    usermessage_region_expression = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView")
    groupmessage_region_expression = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView")
    usermessage_edit_sendbut = (MobileBy.ID,"com.hkfuliao.chamet:id/btn_send")
    usermessage_expression_but = (MobileBy.ID,"com.hkfuliao.chamet:id/iv_face_gif")
    usermessage_expression = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
    google_expression_list = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[2]")
    groupgoogle_expression_list = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView")
    usermessage_translate = (MobileBy.ANDROID_UIAUTOMATOR,'text("翻译")')
    usermessage_drop_down_list = (MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout")
    usermessage_gift_but = (MobileBy.XPATH,"//android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ImageView")
    groupmessage_number = (MobileBy.ID,"com.hkfuliao.chamet:id/tv_group_number")
    gift_listimage = (MobileBy.XPATH,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView")
    group_giftmessageimage = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageView")
    invite_but = (MobileBy.ID,"com.hkfuliao.chamet:id/iv_invite")
    audience_ele = (MobileBy.ID,"com.hkfuliao.chamet:id/rl_audiences")
    game_but = (MobileBy.ID,"com.hkfuliao.chamet:id/vc_box")
    game_race = (MobileBy.ID,"com.hkfuliao.chamet:id/iv_race_game")
    game_LuckyNumber = (MobileBy.ID,"com.hkfuliao.chamet:id/ivLuckyNumber")
    race_rank = (MobileBy.ID,"com.hkfuliao.chamet:id/iv_race_rank")
    LuckyNumber_rank = (MobileBy.ID,"com.hkfuliao.chamet:id/rank")
    giftnaming_wall = (MobileBy.ID,"com.hkfuliao.chamet:id/gift_honor_wall_drag_view")
    giftwall_title = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_title")



    def __init__(self,driver):
        self.driver = driver

    def login_account(self):
        logging.info('===登录===')
        logon = LoginView(self.driver)
        logon.more_Btn()
        logon.phonenumber_Btn()
        logon.login_input_phonenumber('1839172')
        logon.next_Btn()
        # l.login_input_password_or_code('1839174')
        self.driver.find_element(*self.password_frame).send_keys("1839172")
        self.driver.find_element(*self.logon_button).click()

    def quit_account(self):
        logging.info('===退出===')
        self.driver.find_element(*self.my_tab).click()
        message_key = self.driver.find_element(*self.message)
        level_key = self.driver.find_element(*self.my_level)
        self.driver.drag_and_drop(level_key,message_key)
        self.driver.find_element(*self.settings).click()
        self.driver.find_element(*self.log_out).click()
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_confirm").click()

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

    # 长按
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

    # 进入交友房页签
    def party_tab_Btn(self):
        logging.info('===进入交友房页签===')
        time.sleep(3)
        self.driver.find_element(*self.party_tab).click()

    # 进入交友房预览页
    def enter_party_PreviewPage(self):
        logging.info('===进入交友房预览页===')
        time.sleep(3)
        self.driver.find_element(*self.partyPreviewPage_enter).click()
        pw = self.permission_window()
        if pw:
            self.choic_permission_window()
            self.choic_permission_window()
            self.choic_permission_window()
        else:
            logging.info('===无权限弹窗===')

    # 退出交友房预览页
    def quit_party_PreviewPage(self):
        logging.info('===退出交友房预览页===')
        self.driver.find_element(*self.partyPreviewPage_quit).click()

    # 进入10人交友房
    def enter_tenparty(self):
        logging.info('===进入10人交友房===')
        self.driver.find_element(*self.ten_people).click()
        self.driver.find_element(*self.party_enterbut).click()

    # 退出交友房
    def quit_party(self):
        logging.info('===退出交友房===')
        time.sleep(0.5)
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/vc_close").click()
        time.sleep(0.5)
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/positive_btn").click()
        time.sleep(0.5)
        self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/closeTv").click()
        time.sleep(0.5)

    # 获取toast消息
    def toast_message(self,message):
        return WebDriverWait(self.driver, 10, 0.05).until(EC.presence_of_element_located((MobileBy.XPATH, '//*[contains(@text, "%s")]' % message)))

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

    # 坐标之间的滑动
    def swipe_xy(self, start_x, start_y, end_x, end_y,time=2000):
        logging.info('===滑动===')
        self.driver.swipe(start_x, start_y, end_x, end_y,time)

    # 元素之间的滑动
    def swipe_el(self,origin_el,destination_el):
        logging.info('===滑动===')
        self.driver.drag_and_drop(origin_el,destination_el)

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


    # 打开送礼弹窗
    def open_gift_window(self):
        logging.info('===打开送礼弹窗===')
        send_gift_but = self.driver.find_element(*self.room_gift_but)
        send_gift_but.click()
        logging.info('#####################')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("简体中文chinese simplified")').click()

    # 获取礼物弹窗中礼物列表
    def gift_lst(self):
        logging.info('===获取礼物列表===')
        giftlst_text = self.driver.find_elements(*self.gift_list_text)
        return giftlst_text

    # 获取某个元素的属性
    def get_attr(self, attr, *ele):
        return self.driver.find_element(*ele).get_attribute(attr)

    # 判断有无签到弹窗
    def sign_in_window(self):
        try:
            signin_window= self.driver.find_element(*self.sign_in_windows)
        except:
            return False
        else:
            logging.info('===有签到弹窗===')
            return True

    # 签到
    def sign_in(self):
        try:
            signin_window = self.sign_in_window()
            if signin_window:
                self.driver.find_element(*self.sign_in_but).click()
                self.driver.back()
            else:
                self.party_tab_Btn()
        except:
            logging.info('===签到执行失败===')

    # 判断有无权限弹窗
    def permission_window(self):
        try:
            window = self.driver.find_element(*self.permission_windows)
        except:
            return False
        else:
            logging.info('===有权限弹窗===')
            return True

    # 同意权限弹窗
    def choic_permission_window(self):
        try:
            if self.driver.find_element(*self.permission_allow_foreground_only_button):
                self.driver.find_element(*self.permission_allow_foreground_only_button).click()
            else:
                self.driver.find_element(*self.permission_allow_button).click()
        except:
            logging.info('===权限执行失败===')

    # 判断有无私聊消息
    def message_user_list(self):
        try:
            logging.info('===查看私聊列表===')
            message_user_lists = self.driver.find_elements(*self.party_message_user_lists)
            return message_user_lists
        except:
            logging.info('===寻找私聊列表时出错===')

    # 有用户消息，进入用户消息
    def message_user_enter(self):
        message_userlist = self.message_user_list()
        logging.info('===进入私聊页面===')
        message_userlist[0].click()

    # 私聊界面发送文字
    def usermessage_send_text(self,message_text):
        logging.info('===准备发送文字消息===')
        self.driver.find_element(*self.usermessage_edit_frame).click()
        self.driver.find_element(*self.usermessage_edit_frame).send_keys(message_text)
        self.driver.find_element(*self.usermessage_edit_sendbut).click()
        logging.info('===发送成功===')

    # 私聊界面发送表情
    def usermessage_send_expression(self,index):
        logging.info('===准备发送表情===')
        self.driver.find_element(*self.usermessage_expression_but).click()
        time.sleep(3)
        if index == 0:
            self.driver.find_elements(*self.usermessage_expression)[index].click()
            google_expression_searchframe = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/et_search_id")
            google_expression_searchframe.send_keys("wow")
            google_expression_searchbut = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_search")
            google_expression_searchbut.click()
            time.sleep(0.5)
            google_expression_list = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")
            time.sleep(0.5)
            google_expression_list[0].click()
        else:
            self.driver.find_elements(*self.usermessage_expression)[index].click()

    # 点击展开交友房私聊页面下拉列
    def usermessage_drop_down(self):
        logging.info('===展开下拉列表===')
        iv_more_bottom = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_more_bottom")
        iv_more_bottom.click()

    # 开启私聊页面翻译功能
    def usermessage_open_translate(self):
        logging.info('===开启翻译功能===')
        self.driver.find_elements(*self.usermessage_drop_down_list)[0].click()

    # 私聊页面发送相册照片
    def usermessage_send_photo(self,num):
        logging.info('===打开相册===')
        self.driver.find_elements(*self.usermessage_drop_down_list)[1].click()
        logging.info('===发送相册照片===')
        try:
            for i in range(num):
                self.driver.find_elements(MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView[2]")[i].click()
            self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/menu_id_confirm").click()
            return True
        except:
            return False

    # 发送相机照片
    def usermessage_send_cameraphoto(self):
        logging.info('===打开相机===')
        self.driver.find_elements(*self.usermessage_drop_down_list)[2].click()
        try:
            logging.info('===拍照发送===')
            self.driver.find_element(MobileBy.ID,"com.oppo.camera:id/shutter_button").click()
            self.driver.find_element(MobileBy.ID,"com.oppo.camera:id/done_button").click()
            time.sleep(2)
            return True
        except:
            return False

    # 私聊页面拨打语音聊天
    def usermessage_Voice_chat(self):
        logging.info('===拨打语音聊天===')
        self.driver.find_elements(*self.usermessage_drop_down_list)[3].click()

    # 打开私聊送礼页面
    def usermessage_open_giftpage(self):
        try:
            logging.info('===打开私聊送礼页面===')
            open_giftbut = self.driver.find_element(MobileBy.ID,'com.hkfuliao.chamet:id/iv_chat_gift')
            open_giftbut.click()
        except:
            logging.info('===无礼物按钮===')

    # 私聊礼物页面左滑右滑
    def usermessage_scroll_gift(self):
        gift_list_text = self.driver.find_elements(MobileBy.XPATH,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        gift_list_text[1].click()
        self.swipe_xy(600, 1200, 100, 1200)
        nowgift_list_text = self.driver.find_elements(MobileBy.XPATH,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        self.swipe_xy(100, 1200, 600, 1200)
        newgift_list_text = self.driver.find_elements(MobileBy.XPATH,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        return nowgift_list_text,newgift_list_text

    # 充值优惠卷
    def enrich_window(self):
        logging.info("===判断有无充值优惠券===")
        try:
            enrich_window = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("去使用")')
            return True
        except:
            return False

    # 取消充值优惠券
    def cancel_enrich_window(self):
        enrich_window = self.enrich_window()
        if enrich_window:
            logging.info("===有优惠券===")
            self.driver.back()
            self.driver.back()
        else:
            logging.info("===无优惠券===")
            self.driver.back()

    # 私聊礼物按钮中送礼
    def usermessage_sendgift(self):
        logging.info("===送礼物===")
        self.driver.find_element(*self.usermessage_gift_but).click()
        lucky_window = self.lucky_window()
        if lucky_window:
            finish = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("真棒！")')
            finish.click()
            self.cancel_enrich_window()
        else:
            self.cancel_enrich_window()


    # 私聊中打开个人主页浮层
    def open_Profile_float(self):
        logging.info("===打开个人主页浮层===")
        more_but=self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_more")
        more_but.click()
        time.sleep(1)

    # 判断有无群聊消息
    def message_group_list(self):
        try:
            logging.info('===查看群聊列表===')
            message_group_list = self.driver.find_elements(*self.party_message_group_lists)
            return message_group_list
        except:
            logging.info('===寻找群聊列表时出错===')

    # 有用户消息，进入用户消息
    def message_group_enter(self):
        message_grouplist = self.message_group_list()
        logging.info('===进入群聊页面===')
        message_grouplist[0].click()

    # 群聊界面发送文字
    def groupmessage_send_text(self,message_text):
        logging.info('===准备发送文字消息===')
        groupmessage_edit_frame = (MobileBy.ID,"com.hkfuliao.chamet:id/et_edit_chat_info")
        groupmessage_edit_sendbut = (MobileBy.ID,"com.hkfuliao.chamet:id/iv_send_message")
        self.driver.find_element(*groupmessage_edit_frame).click()
        self.driver.find_element(*groupmessage_edit_frame).send_keys(message_text)
        self.driver.find_element(*groupmessage_edit_sendbut).click()
        logging.info('===发送成功===')

    # 群聊页面发送语音
    def groupmessage_send_voice(self):
        logging.info('===准备发送语音===')
        groupmessage_voicebut = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_voice")
        groupmessage_voicebut.click()
        groupmessage_voice_frame = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_add_voice")
        # 长按录入语音
        self.click_hold(groupmessage_voice_frame)

    # 获取群聊中语音文本
    def voice_text(self):
        voice_ele = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView")
        voice_time = voice_ele.text
        return voice_time

    # 群聊中发送相册图片
    def groupmessage_send_photo(self,num):
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

    # 群聊中发送拍摄图片
    def groupmessage_send_cameraphoto(self):
        logging.info('===发送照片===')
        photo_camera_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_more_pic")
        photo_camera_but.click()
        cameraphoto_choicebut = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("拍照")')
        cameraphoto_choicebut.click()
        logging.info('===发送拍摄照片===')
        try:
            self.driver.find_element(MobileBy.ID,"com.oppo.camera:id/shutter_button").click()
            self.driver.find_element(MobileBy.ID,"com.oppo.camera:id/done_button").click()
            time.sleep(2)
            return True
        except:
            return False

    # 群聊页面上麦
    def up_microphone(self):
        logging.info('===主播端上麦===')
        microphone = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_bottom_up_mic")
        microphone.click()

    # 群聊页面发送钻石包
    def send_diamond_envelope(self,envelope_num,diamond_num):
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

    # 群聊页面领取钻石包
    def get_diamond_envelope(self):
        logging.info('===领取钻石包===')
        envelope = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, 'text("幸运红包")')
        envelope[-1].click()
        open_envelope = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_open_diamond_packet")
        open_envelope.click()

    # 夺宝礼物弹窗
    def lucky_window(self):
        logging.info('===判断有无夺宝弹窗===')
        try:
            lucky_window = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/ll_lucky_content")
            logging.info('===获得夺宝弹窗===')
            return True
        except:
            logging.info('===无夺宝弹窗===')
            return False

    # 群聊页面送礼
    def groupmessage_send_gift(self,num):
        logging.info('===打开礼物页面===')
        gift_but = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[4]")
        gift_but.click()
        gift_list = self.driver.find_elements(*self.gift_listimage)
        gift_list[num].click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("77")').click()
        send_gift = self.driver.find_element(*self.usermessage_gift_but)
        send_gift.click()
        lucky_window = self.lucky_window()
        if lucky_window:
            finish = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("真棒！")')
            finish.click()
            self.driver.back()
        else:
            self.driver.back()

    # 进入10人交友房充值页面
    def enter_recharge_page(self):
        logging.info('===进入充值页面===')
        recharge = self.driver.find_element(*self.recharge)
        recharge.click()

    # 进入10人交友房充值页面
    def recharge_diamond(self):
        logging.info('===进行充值===')
        recharge_level = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup")
        recharge_level[0].click()
        time.sleep(2)
        buy_but = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("一键购买")')
        buy_but.click()
        time.sleep(2)

    # 进入10人交友房设置页面
    def enter_setting_page(self):
        logging.info('===进入设置页面===')
        setting_page = self.driver.find_element(*self.settings)
        setting_page.click()

    # 10人交友房主播端关闭麦克风
    def close_voice(self):
        logging.info('===打开/关闭麦克风===')
        try:
            logging.info('===主播端关闭麦克风===')
            voice_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/switch_microphone")
            voice_but.click()
            time.sleep(1)
            return True
        except:
            return False

    # 查看有无任务按钮
    def haveno_task_but(self):
        logging.info('===查看有无任务按钮===')
        try:
            task_but = self.driver.find_element(*self.task_but)
            logging.info('===有任务按钮===')
            return True
        except:
            logging.info('===无任务按钮===')
            return False

    # 进入任务页面
    def enter_task_page(self):
        logging.info('===进入任务页面===')
        task_but = self.driver.find_element(*self.task_but)
        task_but.click()

    #进入邀请页面
    def enter_invit_window(self):
        logging.info('===进入邀请页面===')
        invit_but = self.driver.find_element(*self.invite_but)
        invit_but.click()

    # 进入游戏页面
    def enter_game_window(self,game_type):
        logging.info('===进入游戏页面===')
        game_but = self.driver.find_element(*self.game_but)
        game_but.click()
        game_race = self.driver.find_element(*self.game_race)
        game_LuckyNumber = self.driver.find_element(*self.game_LuckyNumber)
        if game_type == "Chamet赛车":
            logging.info('===进入赛车游戏===')
            game_race.click()
            time.sleep(5)
        elif game_type == "幸运数字":
            logging.info('===进入幸运数字===')
            game_LuckyNumber.click()
            time.sleep(3)
        else:
            logging.info('===游戏类型输入错误===')
            raise

    # 进入礼物荣誉墙
    def enter_giftnamingwall(self):
        logging.info('===进入礼物荣誉墙===')
        giftnamingwall_but = self.driver.find_element(*self.giftnaming_wall)
        giftnamingwall_but.click()
        time.sleep(1)

    #进入活动banner
    def enter_banner(self):
        try:
            banner_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/image")
            banner_but.click()
            logging.info('===进入活动页===')
            time.sleep(2)
            return True
        except:
            logging.info('===未成功进入活动页===')
            return False













        # if (member_num >= 2) and (envelope_num >= 2) and (diamond_num >= 1000):
        #     packet_count.send_keys(envelope_num)
        #     packet_total_energy.send_keys(diamond_num)
        #     send_but.click()
        # elif (member_num >= 2) and (envelope_num < 2) and (diamond_num >= 1000):
        #     packet_count.send_keys(envelope_num)
        #     packet_total_energy.send_keys(diamond_num)
        # elif (member_num >= 2) and (envelope_num >= 2) and (diamond_num < 1000):
        #     packet_count.send_keys(envelope_num)
        #     packet_total_energy.send_keys(diamond_num)
        # elif (member_num < 2) and (envelope_num >= 2) and (diamond_num >= 1000):
        #     packet_count.send_keys(envelope_num)
        #     packet_total_energy.send_keys(diamond_num)
        # elif (member_num > 1) and (envelope_num >= 2) and (diamond_num >= 1000):
        #     packet_count.send_keys(envelope_num)
        #     packet_total_energy.send_keys(diamond_num)
        # else:
        #     raise










