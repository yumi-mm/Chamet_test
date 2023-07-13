# coding=gb2312
import time
from appium.webdriver.common.touch_action import TouchAction
from uiautomator2.webview import driver
from appium import webdriver
from Six_party.common.myunittest import StartEnd
from Six_party.businessView.six_party_anchor import Six_partyView_anchor
from Six_party.businessView.login_phoneView import LoginView
import unittest
import logging
import allure
import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Six_party.common.desired_caps_anchor import anchor_appium_desired

@allure.epic("项目名称：6人交友房")
@allure.issue("BUG链接：http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("测试用例链接：http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('交友房6人房_主播端功能')


class Test_six_party(StartEnd):
    csv_file = '../data/account.csv'
    @allure.severity(allure.severity_level.BLOCKER)
    @unittest.skip('skip test_changjingmoni')
    def test_changjingmoni(self):
        logging.info("===开始场景模拟===")
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        # 点击    S.driver.tap([(528, 2191), (529, 5292)], 200)
        # 滑动    S.driver.swipe(800, 800, 200, 800)
        self.assertIs(S.Test_XX(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例1：创建交友房页面')
    def test_Six_Party_001(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        l.check_perBtn()
        l.One_click_login()
        S.Tab_party()
        S.Setup_party()
        l.check_perBtn()
        l.check_perBtn()
        l.check_perBtn()
        self.assertIs(S.Test_X001(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例2：切换到6人交友房模式')
    def test_Six_Party_002(self):
        S = Six_partyView_anchor(self.driver)
        S.Setup_six_party()
        self.assertIs(S.Test_X002(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例3：使用美颜功能')
    def test_Six_Party_003(self):
        S = Six_partyView_anchor(self.driver)
        S.Setup_beauty()
        self.assertIs(S.Test_X003(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例4：使用贴纸功能')
    def test_Six_Party_004(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Setup_sticker()
        S.Sticker_download()
        self.assertIs(S.Sticker_downloading(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例5：成功创建6人交友房')
    def test_Six_Party_005(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Two_Setup()
        self.assertIs(S.Test_X005(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例6：观众进入交友房特效展示')
    def test_Six_Party_006(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(5)
        self.assertIs(S.Test_X066(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例7：观众进入交友房消息区提示')
    def test_Six_Party_007(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(3)
        self.assertIs(S.Test_X067(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例8：交友房消息区点击观众用户名')
    def test_Six_Party_008(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_message_user()
        self.assertIs(S.Test_X068(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例9：打开观众列表')
    def test_Six_Party_009(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Six_party_more_people()
        self.assertIs(S.Test_X006(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例10：观众列表上下滑动')
    def test_Six_Party_010(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(700, 700, 700, 1800)
        S.driver.swipe(700, 1800, 700, 700)
        self.assertIs(S.Test_X007(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例12：观众列表头像点击查看')
    def test_Six_Party_012(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X009(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例13：观众个人信息浮窗举报检查')
    def test_Six_Party_013(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X010(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例14：观众个人信息浮窗进入个人主页')
    def test_Six_Party_014(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_anchor_head()
        self.assertIs(S.Test_X011(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例15：陌生人个人信息浮窗关注按钮检查')
    def test_Six_Party_015(self):
        S = Six_partyView_anchor(self.driver)
        S.Homepage_back()
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X012(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例16：观众个人信息浮窗送礼物功能验证')
    def test_Six_Party_016(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_supernatant_gift()
        self.assertIs(S.Test_X013(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例17：观众个人信息浮窗赠送礼物')
    def test_Six_Party_017(self):
        S = Six_partyView_anchor(self.driver)
        S.Gift_window_Activity()
        S.Six_party_one_gift()
        S.More_message_people_sendgift()
        S.driver.tap([(200, 400), (201, 401)], 200)
        S.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(S.Test_X014(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例18：观众个人信息浮窗信息按钮')
    def test_Six_Party_018(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Supernatant_message()
        self.assertIs(S.Test_X015(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例19：私聊界面更多按钮检查')
    def test_Six_Party_019(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_more()
        self.assertIs(S.Test_X017(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例20：私聊界面退出按钮检查')
    def test_Six_Party_020(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Supernatant_message_back()
        self.assertIs(S.Test_X016(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例23：房主在个人信息浮窗--视频通话')
    def test_Six_Party_023(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Six_party_more_people_list_one()
        S.Supernatant_message()
        S.Supernatant_message_more()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_X015(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例24：私聊界面折叠按钮点击检查')
    def test_Six_Party_024(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing()
        self.assertIs(S.Test_X021(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例25：私聊界面折叠区域翻译按钮点击检查')
    def test_Six_Party_025(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing_translate()
        self.assertIs(S.Test_X022(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例27：私聊界面折叠区域相册功能检查')
    def test_Six_Party_027(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing_photo()
        self.assertIs(S.Test_X024(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例28：私聊界面发送相册')
    def test_Six_Party_028(self):
        S = Six_partyView_anchor(self.driver)
        S.Myphoto_one()
        S.Myphoto_comfirm()
        self.assertIs(S.Test_X025(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例29：私聊界面折叠区域相机功能检查')
    def test_Six_Party_029(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing_camera()
        self.assertIs(S.Test_X026(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例30：私聊界面发送拍摄照片')
    def test_Six_Party_030(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing_photo_confirm()
        S.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(S.Test_X027(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例32：私聊界面发送文字')
    def test_Six_Party_032(self):
        S = Six_partyView_anchor(self.driver)
        S.Room_message_button_click()
        S.Room_message_button_input()
        S.Room_message_button_send()
        self.assertIs(S.Test_X029(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例33：私聊界面发送表情')
    def test_Six_Party_033(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_face_gif()
        S.Supernatant_message_face_gif_one()
        self.assertIs(S.Test_X030(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例34：私聊界面送礼物')
    def test_Six_Party_034(self):
        S = Six_partyView_anchor(self.driver)
        S.More_message_people_gift()
        S.Gift_window_Activity()
        S.More_message_people_sendgift()
        S.driver.tap([(528, 528), (529, 529)], 200)
        self.assertIs(S.Test_X031(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例35：群聊界面发拍照图片')
    def test_Six_Party_035(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_back()
        S.Supernatant_message_group()
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_photo()
        S.Supernatant_message_setiing_photo_confirm()
        S.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(S.Test_X032(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例36：群聊界面发相册图片')
    def test_Six_Party_036(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_camera()
        time.sleep(2)
        S.Myphoto_one()
        self.assertIs(S.Test_X033(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例37：群聊界面发消息')
    def test_Six_Party_037(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_chat()
        S.Supernatant_message_group_chat_send()
        self.assertIs(S.Test_X034(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例38：群聊界面发表情')
    def test_Six_Party_038(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_face_gif()
        S.Supernatant_message_group_gif_one()
        self.assertIs(S.Test_X035(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例39：群聊界面发语音')
    def test_Six_Party_039(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_voice()
        S.driver.tap([(500, 2010), (510, 2020)], 3000)
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例40：群聊界面上麦')
    def test_Six_Party_040(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_upmic()
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例41：群聊界面发红包')
    def test_Six_Party_041(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_packet()
        S.Supernatant_message_group_packet_number()
        S.Supernatant_message_group_packet_diamond()
        S.Supernatant_message_group_packet_send()
        self.assertIs(S.Test_X038(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例42：群聊界面领红包')
    def test_Six_Party_042(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_packet_get()
        S.Supernatant_message_group_packet_open()
        self.assertIs(S.Test_X039(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例43：群聊界面送礼')
    def test_Six_Party_043(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(500, 1950), (501, 1951)], 200)
        S.Supernatant_message_group_gift()
        S.Gift_window_Activity()
        S.Six_party_one_gift()
        S.More_message_people_sendgift()
        S.driver.tap([(500, 500), (501, 501)], 200)
        self.assertIs(S.Test_X040(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例44：群聊界面进入活动')
    def test_Six_Party_044(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_more()
        S.driver.tap([(864, 974), (865, 975)], 200)
        time.sleep(10)
        self.assertIs(S.Test_X041(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例45：观众个人信息浮窗禁言功能')
    def test_Six_Party_045(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(500, 500), (501, 501)], 200)
        S.driver.tap([(500, 500), (501, 501)], 200)
        S.Six_party_more_people_list_one()
        S.Supernatant_mute()
        S.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(S.Test_X042(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例46：观众个人信息浮窗取消禁言功能')
    def test_Six_Party_046(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Supernatant_mute()
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X043(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例47：观众个人信息浮窗@观众功能')
    def test_Six_Party_047(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_at_anchor()
        S.Room_message_button_send()
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(S.Test_X044(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例61：主播在交友位上展示表情')
    def test_Six_Party_061(self):
        S = Six_partyView_anchor(self.driver)
        S.Room_Homeowner_place()
        S.Room_Homeowner_place_emo()
        self.assertIs(S.Test_X058(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例62：交友房警告消息检查')
    def test_Six_Party_062(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(S.Test_X059(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例63：交友房主播端发言')
    def test_Six_Party_063(self):
        S = Six_partyView_anchor(self.driver)
        S.Room_message_button()
        S.Room_message_button_input()
        S.Room_message_button_send()
        S.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(S.Test_X060(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例65：交友房消息区上滑消息')
    def test_Six_Party_065(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(S.Test_X062(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例66：交友房消息区下滑消息')
    def test_Six_Party_066(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(363, 2040, 363, 1478)
        self.assertIs(S.Test_X063(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例70：主播在交友房中给自己送礼')
    def test_Six_Party_070(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_gift()
        self.assertIs(S.Test_X070(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例71：交友房中左右滑动banner')
    def test_Six_Party_071(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.driver.swipe(1000, 2000, 860, 2000)
        self.assertIs(S.Test_X071(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例72：交友房中点击进入banner页')
    def test_Six_Party_072(self):
        S = Six_partyView_anchor(self.driver)
        S.Room_banner()
        time.sleep(5)
        self.assertIs(S.Test_X072(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例73：交友房中背景选择')
    def test_Six_Party_073(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_background()
        time.sleep(1)
        S.driver.swipe(900, 2000, 100, 2000)
        time.sleep(2)
        self.assertIs(S.Test_X073(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例74：更换交友房背景')
    def test_Six_Party_074(self):
        S = Six_partyView_anchor(self.driver)
        S.More_Setting_background_Lv20()
        time.sleep(2)
        self.assertIs(S.Test_X074(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例75：交友房中打开消息列表')
    def test_Six_Party_075(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Message()
        self.assertIs(S.Test_X075(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例78：交友房中进行充值')
    def test_Six_Party_078(self):
        S = Six_partyView_anchor(self.driver)
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
    @allure.title('用例79：交友房中关闭麦克风')
    def test_Six_Party_079(self):
        S = Six_partyView_anchor(self.driver)
        S.More_top_up_confirm()
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_switch_microphone()
        S.More_setting_switch_microphone()
        self.assertIs(S.Test_X079(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例80：交友房中设置贴纸')
    def test_Six_Party_080(self):
        S = Six_partyView_anchor(self.driver)
        S.More_setting_sticker()
        S.More_setting_sticker_1()
        time.sleep(5)
        self.assertIs(S.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例81：交友房中开启美颜')
    def test_Six_Party_081(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_beauty()
        S.More_setting_beauty_reset()
        S.More_setting_beauty_confirmreset()
        self.assertIs(S.Test_X081(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例82：交友房中开启镜像模式')
    def test_Six_Party_082(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_mirror_mode()
        self.assertIs(S.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例83：交友房中关闭摄像头')
    def test_Six_Party_083(self):
        S = Six_partyView_anchor(self.driver)
        S.More_setting_turn_off_camera()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X083(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例84：交友房中切换摄像头')
    def test_Six_Party_084(self):
        S = Six_partyView_anchor(self.driver)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_switch_camera()
        S.More_setting_switch_camera()
        self.assertIs(S.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例85：关闭交友房进入结束页')
    def test_Six_Party_085(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Close_six_party()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X085(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例86：结束页显示内容')
    def test_Six_Party_086(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X087(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例87：结束页进入主播个人主页')
    def test_Six_Party_087(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_endpage_profile()
        self.assertIs(S.Test_X086(), True)



    if __name__ == '__main__':
        pytest.main()
