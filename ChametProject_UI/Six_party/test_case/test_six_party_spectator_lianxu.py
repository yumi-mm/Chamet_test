# coding=gb2312
import time
from appium.webdriver.common.touch_action import TouchAction
from uiautomator2.webview import driver
from appium import webdriver
from ChametProject_UI.Six_party.common.myunittest import StartEnd
from ChametProject_UI.Six_party.businessView.six_party_anchor import Six_partyView_anchor
from ChametProject_UI.Six_party.businessView.login_phoneView import LoginView
import unittest
import logging
import allure
import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from common.desired_caps import appium_desired

@allure.epic("项目名称：6人交友房")
@allure.issue("BUG链接：http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("测试用例链接：http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('交友房6人房_观众端功能')


class Test_six_party(StartEnd):
    csv_file = '../data/account.csv'
    @unittest.skip('skip test_changjingmoni')
    def test_changjingmoni(self):
        logging.info("===开始场景模拟===")
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        # 点击    S.driver.tap([(528, 2191), (529, 5292)], 200)
        # 滑动    S.driver.swipe(800, 800, 200, 800)
        self.assertIs(S.Test_XX(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例89：交友房页签房间显示')
    def test_Six_Party_089(self):
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.driver.swipe(600, 1800, 600, 800)
        S.driver.swipe(600, 800, 600, 1800)
        self.assertIs(S.Test_X089(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例90：从交友房页签进入交友房')
    def test_Six_Party_090(self):
        S = Six_partyView_anchor(self.driver)
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X090(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例91：交友房该场送礼为0，观众查看送礼榜入口')
    def test_Six_Party_091(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X133(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例92：观众在交友房中送礼时余额不足')
    def test_Six_Party_092(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_gift()
        time.sleep(1)
        S.Six_party_two_gift()
        S.More_message_people_sendgift()
        time.sleep(5)
        self.assertIs(S.Test_X127(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例94：观众在交友房中点击主播头像')
    def test_Six_Party_094(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(2)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Six_party_anchor_head()
        self.assertIs(S.Test_X091(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例95：观众在交友房中关注主播')
    def test_Six_Party_095(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_follow_anchor()
        self.assertIs(S.Test_X092(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例96：观众在交友房中举报主播')
    def test_Six_Party_096(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X093(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例97：观众在交友房中通过主播个人主页浮窗给主播送礼物')
    def test_Six_Party_097(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Six_party_anchor_head()
        S.Six_party_supernatant_gift()
        S.Six_party_one_gift()
        S.More_message_people_sendgift()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X094(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例98：观众在交友房中给主播发起视频通话')
    def test_Six_Party_098(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_anchor_head()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_X095(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例99：观众在交友房@主播')
    def test_Six_Party_099(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(5)
        S.Six_party_at_anchor()
        S.Six_party_room_message_send()
        S.driver.tap([(552, 189), (553, 190)], 200)
        S.driver.tap([(552, 189), (553, 190)], 200)
        self.assertIs(S.Test_X096(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例100：观众从主播个人主页进入交友房')
    def test_Six_Party_100(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_anchor_head()
        S.Six_party_supernatant_anchor_head()
        time.sleep(2)
        S.Homepage_video()
        self.assertIs(S.Test_X097(), True)

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例101：LV7及以上观众进入交友房特效展示')
    # def test_Six_Party_101(self):
    #     S = Six_partyView_anchor(self.driver)
    #     time.sleep(5)
    #     self.assertIs(S.Test_X066(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例102：观众进入交友房消息区提示')
    def test_Six_Party_102(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(3)
        self.assertIs(S.Test_X102(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例104：交友房中观众打开观众列表')
    def test_Six_Party_104(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people()
        self.assertIs(S.Test_X098(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例105：交友房中观众上下滑动观众列表')
    def test_Six_Party_105(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(837, 410, 837, 1800)
        S.driver.swipe(837, 1800, 837, 410)
        self.assertIs(S.Test_X098(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例107：交友房中观众点击查看观众头像')
    def test_Six_Party_107(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people_list_two()
        self.assertIs(S.Test_X101(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例108：观众个人信息浮窗举报检查')
    def test_Six_Party_108(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X093(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例109：观众个人信息浮窗进入个人主页')
    def test_Six_Party_109(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(915, 439), (916, 440)], 200)
        S.Six_party_more_people_list_two()
        S.Six_party_supernatant_anchor_head()
        self.assertIs(S.Test_X103(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例110：陌生人个人信息浮窗关注按钮检查')
    def test_Six_Party_110(self):
        S = Six_partyView_anchor(self.driver)
        S.Homepage_back()
        S.Six_party_more_people_list_two()
        S.Six_party_supernatant_follow()
        self.assertIs(S.Test_X104(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例111：观众个人信息浮窗送礼物功能')
    def test_Six_Party_111(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_supernatant_gift()
        self.assertIs(S.Test_X105(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例112：观众个人信息浮窗送礼物功能')
    def test_Six_Party_112(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_one_gift()
        S.More_message_people_sendgift()
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X106(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例113：交友房该场送礼不为0，观众查看送礼榜入口')
    def test_Six_Party_113(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X134(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例114：观众个人信息浮窗@她')
    def test_Six_Party_114(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people()
        S.Six_party_more_people_list_two()
        S.Six_party_at_anchor()
        S.Room_message_button_send()
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X107(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例123：交友房警告消息检查')
    def test_Six_Party_123(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X116(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例124：交友房观众端端发言')
    def test_Six_Party_124(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X117(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例125：交友房消息区消息滚动')
    def test_Six_Party_125(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people()
        S.Six_party_more_people_list_two()
        S.Six_party_supernatant_gift()
        S.More_message_people_sendgift()
        S.More_message_people_sendgift()
        S.More_message_people_sendgift()
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X118(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例126：交友房消息区上滑消息')
    def test_Six_Party_126(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(357, 1519, 357, 2030)
        self.assertIs(S.Test_X119(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例128：观众在交友房中打开送礼浮窗')
    def test_Six_Party_128(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_gift()
        self.assertIs(S.Test_X128(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例130：观众在交友房中给所有嘉宾送礼')
    def test_Six_Party_130(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_send_all_gift()
        S.Six_party_one_gift()
        S.Six_party_send_gift()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X094(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例131：观众在交友房中送礼时余额不足')
    def test_Six_Party_131(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_gift()
        S.Six_party_send_all_gift()
        S.Six_party_two_gift()
        S.More_message_people_sendgift()
        self.assertIs(S.Test_X127(), True)

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例134：交友房中左右滑动banner')
    # def test_Six_Party_134(self):
    #     S = Six_partyView_anchor(self.driver)
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     S.driver.swipe(1000, 2000, 860, 2000)
    #     self.assertIs(S.Test_X071(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例135：交友房中点击进入banner页')
    def test_Six_Party_135(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.driver.tap([(936, 2013), (937, 2014)], 200)
        time.sleep(5)
        self.assertIs(S.Test_X072(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例136：交友房中观众点击加入按钮')
    def test_Six_Party_136(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.More_Setting()
        S.More_join()
        self.assertIs(S.Test_X138(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例137：交友房中观众打开消息列表')
    def test_Six_Party_137(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_twice_apply()
        S.More_Setting()
        S.More_Message()
        self.assertIs(S.Test_X137(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例138：群聊界面发拍照图片')
    def test_Six_Party_138(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group()
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_photo()
        S.Supernatant_message_setiing_photo_confirm()
        S.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(S.Test_X032(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例139：群聊界面发相册图片')
    def test_Six_Party_139(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_camera()
        time.sleep(2)
        S.Myphoto_one()
        self.assertIs(S.Test_X140(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例140：群聊界面发消息')
    def test_Six_Party_140(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_chat()
        S.Supernatant_message_group_chat_send()
        self.assertIs(S.Test_X034(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例141：群聊界面发表情')
    def test_Six_Party_141(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_face_gif()
        S.Supernatant_message_group_gif_one()
        self.assertIs(S.Test_X035(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例142：群聊界面发语音')
    def test_Six_Party_142(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_voice()
        S.driver.tap([(500, 2010), (510, 2020)], 3000)
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例143：群聊界面上麦')
    def test_Six_Party_143(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_upmic()
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例144：群聊界面发红包')
    def test_Six_Party_144(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_packet()
        S.Supernatant_message_group_packet_number()
        S.Supernatant_message_group_packet_diamond()
        S.Supernatant_message_group_packet_send()
        self.assertIs(S.Test_X038(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例145：群聊界面送礼')
    def test_Six_Party_145(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(500, 1950), (501, 1951)], 200)
        S.Supernatant_message_group_gift()
        S.Gift_window_Activity()
        S.Six_party_one_gift()
        S.More_message_people_sendgift()
        S.driver.tap([(500, 500), (501, 501)], 200)
        self.assertIs(S.Test_X040(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例146：群聊界面进入活动')
    def test_Six_Party_146(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_more()
        S.driver.tap([(864, 974), (865, 975)], 200)
        time.sleep(10)
        self.assertIs(S.Test_X041(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例147：交友房中进行充值')
    def test_Six_Party_147(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(2)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_top_up()
        time.sleep(2)
        S.More_top_up_4500()
        time.sleep(5)
        S.More_top_up_pay()
        time.sleep(5)
        self.assertIs(S.Test_X078(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例148：进入嘉宾位')
    def test_Six_Party_148(self):
        S = Six_partyView_anchor(self.driver)
        S.More_top_up_confirm()
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        time.sleep(5)
        self.assertIs(S.Test_X139(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例149：交友房中关闭麦克风')
    def test_Six_Party_149(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(5)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_switch_microphone()
        S.More_setting_switch_microphone()
        self.assertIs(S.Test_X079(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例150：交友房中设置贴纸')
    def test_Six_Party_150(self):
        S = Six_partyView_anchor(self.driver)
        S.More_setting_sticker()
        S.More_setting_sticker_1()
        time.sleep(5)
        self.assertIs(S.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例151：交友房中开启美颜')
    def test_Six_Party_151(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_beauty()
        S.More_setting_beauty_reset()
        S.More_setting_beauty_confirmreset()
        self.assertIs(S.Test_X081(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例152：交友房中开启镜像模式')
    def test_Six_Party_152(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_mirror_mode()
        self.assertIs(S.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例153：交友房中关闭摄像头')
    def test_Six_Party_153(self):
        S = Six_partyView_anchor(self.driver)
        S.More_setting_turn_off_camera()
        S.More_setting_turn_off_camera()
        S.More_setting_turn_off_camera()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X155(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例154：交友房中切换摄像头')
    def test_Six_Party_154(self):
        S = Six_partyView_anchor(self.driver)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_switch_camera()
        S.More_setting_switch_camera()
        self.assertIs(S.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例155：交友房中观众点击离开嘉宾位')
    def test_Six_Party_155(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_off_mic()
        self.assertIs(S.Test_X157(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例156：交友房中观众取消离开嘉宾位')
    def test_Six_Party_156(self):
        S = Six_partyView_anchor(self.driver)
        S.Close_six_party_two_cancle()
        self.assertIs(S.Test_X158(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例157：交友房中观众确认离开嘉宾位')
    def test_Six_Party_157(self):
        S = Six_partyView_anchor(self.driver)
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X159(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例159：交友房中观众给房主拨打约聊')
    def test_Six_Party_159(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_anchor()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_X095(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例160：离开交友房')
    def test_Six_Party_160(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Close_six_party()
        self.assertIs(S.Test_X162(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例161：主播关闭交友房的结束页校验')
    def test_Six_Party_161(self):
        S = Six_partyView_anchor(self.driver)
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X163(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例162：结束页校验-进入个人主页')
    def test_Six_Party_162(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_endpage_profile()
        self.assertIs(S.Test_X011(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例163：结束页校验-结束页标题')
    def test_Six_Party_163(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X165(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例164：结束页校验-结束页派对时长/观众')
    def test_Six_Party_164(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X166(), True)

    if __name__ == '__main__':
        pytest.main()
