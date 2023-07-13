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
from ChametProject_UI.Six_party.common.desired_caps import anchor_appium_desired

@allure.epic("项目名称：6人交友房")
@allure.issue("BUG链接：http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("测试用例链接：http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('交友房6人房_主播端功能')

class Test_six_party(StartEnd):
    csv_file = '../data/account.csv'
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例1：进入创建交友房页面')
    @unittest.skip('skip test_changjingmoni')
    def test_changjingmoni(self):
        logging.info("===开始场景模拟===")
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        time.sleep(2)
        # 点击    S.driver.tap([(528, 2191), (529, 5292)], 200)
        # 滑动    S.driver.swipe(800, 800, 200, 800)
        self.assertIs(l.check_loginStatus(), True)

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

    def test_Six_Party_002(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        self.assertIs(S.Test_X002(), True)

    def test_Six_Party_003(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Setup_beauty()
        self.assertIs(S.Test_X003(), True)

    def test_Six_Party_004(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Setup_sticker()
        S.Sticker_download()
        self.assertIs(S.Sticker_downloading(), True)

    def test_Six_Party_005(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        self.assertIs(S.Test_X005(), True)

    def test_Six_Party_006(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        self.assertIs(S.Test_X006(), True)

    def test_Six_Party_007(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.Six_party_more_people()
        S.driver.swipe(700, 700, 700, 1800)
        S.driver.swipe(700, 1800, 700, 700)
        self.assertIs(S.Test_X007(), True)

    def test_Six_Party_009(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X009(), True)

    def test_Six_Party_010(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X010(), True)

    def test_Six_Party_011(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_anchor_head()
        self.assertIs(S.Test_X011(), True)

    def test_Six_Party_012(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X012(), True)

    def test_Six_Party_013(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_gift()
        self.assertIs(S.Test_X013(), True)

    def test_Six_Party_014(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_gift()
        S.More_message_people_sendgift()
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.Six_party_one_gift()
        self.assertIs(S.Test_X014(), True)

    def test_Six_Party_017(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.More_Setting()
        S.More_Message()
        S.Stranger_message()
        S.Stranger_message_people()
        S.Private_letter_more()
        self.assertIs(S.Test_X017(), True)

    def test_Six_Party_018(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.More_Setting()
        S.More_Message()
        S.Stranger_message()
        S.Stranger_message_people()
        S.Private_letter_more()
        S.Private_letter_more_follow()
        self.assertIs(S.Test_X018(), True)

    def test_Six_Party_019(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.More_Setting()
        S.More_Message()
        time.sleep(1)
        S.More_message_people()
        S.More_message_people_gift()
        S.More_message_people_sendgift()
        self.assertIs(S.Test_X019(), True)

    def test_Six_Party_058(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        S.Room_Homeowner_place()
        S.Room_Homeowner_place_emo()
        self.assertIs(S.Test_X058(), True)

    def test_Six_Party_059(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        self.assertIs(S.Test_X059(), True)

    def test_Six_Party_060(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.Room_message_button()
        S.Room_message_button_input()
        S.Room_message_button_send()
        self.assertIs(S.Test_X060(), True)

    def test_Six_Party_071(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.driver.swipe(1000, 2000, 860, 2000)
        self.assertIs(S.Test_X071(), True)

    def test_Six_Party_072(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.Room_banner()
        time.sleep(5)
        self.assertIs(S.Test_X072(), True)

    def test_Six_Party_073(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_background()
        S.driver.swipe(900, 2000, 100, 2000)
        time.sleep(2)
        self.assertIs(S.Test_X073(), True)

    def test_Six_Party_074(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_background()
        S.driver.swipe(900, 2000, 100, 2000)
        time.sleep(2)
        S.More_Setting_background_Lv20()
        self.assertIs(S.Test_X073(), True)

    def test_Six_Party_075(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_background()
        S.driver.swipe(900, 2000, 100, 2000)
        time.sleep(2)
        S.More_Setting_background_Lv20()
        self.assertIs(S.Test_X073(), True)

    def test_Six_Party_078(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_top_up()
        time.sleep(2)
        S.More_top_up_4500()
        time.sleep(5)
        S.More_top_up_pay()
        time.sleep(5)
        self.assertIs(S.Test_X078(), True)

    def test_Six_Party_079(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_switch_microphone()
        S.More_setting_switch_microphone()
        self.assertIs(S.Test_X079(), True)

    def test_Six_Party_080(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_sticker()
        S.More_setting_sticker_1()
        self.assertIs(S.Test_X080(), True)

    def test_Six_Party_081(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_beauty()
        S.More_setting_beauty_reset()
        time.sleep(1)
        S.More_setting_beauty_confirmreset()
        self.assertIs(S.Test_X081(), True)

    def test_Six_Party_082(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_mirror_mode()
        self.assertIs(S.Test_X082(), True)

    def test_Six_Party_083(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X083(), True)

    def test_Six_Party_084(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_switch_camera()
        S.More_setting_switch_camera()
        self.assertIs(S.Test_X084(), True)

    def test_Six_Party_085(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.Close_six_party()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X085(), True)

    def test_Six_Party_086(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.Close_six_party()
        S.Close_six_party_two_confirm()
        S.Six_party_endpage_profile()
        self.assertIs(S.Test_X086(), True)

    def test_Six_Party_087(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Setup_party()
        S.Setup_six_party()
        S.Two_Setup()
        time.sleep(2)
        S.Close_six_party()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X087(), True)

    def test_Six_Party_088(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.driver.swipe(600, 1800, 600, 800)
        S.driver.swipe(600, 800, 600, 1800)
        self.assertIs(S.Test_X088(), True)

    def test_Six_Party_089(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.driver.swipe(600, 1800, 600, 800)
        S.driver.swipe(600, 800, 600, 1800)
        self.assertIs(S.Test_X089(), True)

    def test_Six_Party_090(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X090(), True)

    def test_Six_Party_091(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_anchor_head()
        self.assertIs(S.Test_X091(), True)

    def test_Six_Party_092(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_follow_anchor()
        self.assertIs(S.Test_X092(), True)

    def test_Six_Party_093(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_anchor_head()
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X093(), True)

    def test_Six_Party_094(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_gift()
        S.Six_party_one_gift()
        S.Six_party_send_gift()
        self.assertIs(S.Test_X094(), True)

    def test_Six_Party_095(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_anchor_head()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_X095(), True)

    def test_Six_Party_096(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_anchor_head()
        S.Six_party_at_anchor()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(552, 189), (553, 190)], 200)
        self.assertIs(S.Test_X096(), True)

    def test_Six_Party_097(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_anchor_head()
        S.Six_party_supernatant_anchor_head()
        S.driver.tap([(915, 439), (916, 440)], 200)
        self.assertIs(S.Test_X097(), True)

    def test_Six_Party_098(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        self.assertIs(S.Test_X098(), True)

    def test_Six_Party_099(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        S.driver.swipe(837, 410, 837, 1800)
        S.driver.swipe(837, 1800, 837, 410)
        self.assertIs(S.Test_X098(), True)

    def test_Six_Party_101(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X101(), True)

    def test_Six_Party_102(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X093(), True)

    def test_Six_Party_103(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_anchor_head()
        self.assertIs(S.Test_X103(), True)

    def test_Six_Party_104(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_follow()
        self.assertIs(S.Test_X104(), True)

    def test_Six_Party_105(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_gift()
        self.assertIs(S.Test_X105(), True)

    def test_Six_Party_106(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_gift()
        S.Six_party_send_gift()
        self.assertIs(S.Test_X019(), True)

    def test_Six_Party_107(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Six_party_at_anchor()
        self.assertIs(S.Test_X107(), True)

    def test_Six_Party_114(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        time.sleep(5)
        S.Six_party_tow_location()
        l.check_perBtn()
        l.check_perBtn()
        l.check_perBtn()
        self.assertIs(S.Test_X114(), True)

    def test_Six_Party_116(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        time.sleep(5)
        self.assertIs(S.Test_X116(), True)

    def test_Six_Party_117(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        time.sleep(5)
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X096(), True)

    def test_Six_Party_118(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        time.sleep(5)
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X118(), True)

    def test_Six_Party_119(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        time.sleep(5)
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.driver.swipe(360, 1443, 340, 2100)
        self.assertIs(S.Test_X119(), True)

    def test_Six_Party_121(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X121(), True)

    def test_Six_Party_122(self):
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X122(), True)


    if __name__ == '__main__':
        pytest.main()
