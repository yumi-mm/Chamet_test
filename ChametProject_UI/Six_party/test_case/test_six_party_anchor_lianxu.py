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

@allure.epic("��Ŀ���ƣ�6�˽��ѷ�")
@allure.issue("BUG���ӣ�http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("�����������ӣ�http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('���ѷ�6�˷�_�����˹���')


class Test_six_party(StartEnd):
    csv_file = '../data/account.csv'
    @allure.severity(allure.severity_level.BLOCKER)
    @unittest.skip('skip test_changjingmoni')
    def test_changjingmoni(self):
        logging.info("===��ʼ����ģ��===")
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        # ���    S.driver.tap([(528, 2191), (529, 5292)], 200)
        # ����    S.driver.swipe(800, 800, 200, 800)
        self.assertIs(S.Test_XX(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����1���������ѷ�ҳ��')
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
    @allure.title('����2���л���6�˽��ѷ�ģʽ')
    def test_Six_Party_002(self):
        S = Six_partyView_anchor(self.driver)
        S.Setup_six_party()
        self.assertIs(S.Test_X002(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����3��ʹ�����չ���')
    def test_Six_Party_003(self):
        S = Six_partyView_anchor(self.driver)
        S.Setup_beauty()
        self.assertIs(S.Test_X003(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����4��ʹ����ֽ����')
    def test_Six_Party_004(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Setup_sticker()
        S.Sticker_download()
        self.assertIs(S.Sticker_downloading(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����5���ɹ�����6�˽��ѷ�')
    def test_Six_Party_005(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Two_Setup()
        self.assertIs(S.Test_X005(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����6�����ڽ��뽻�ѷ���Чչʾ')
    def test_Six_Party_006(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(5)
        self.assertIs(S.Test_X066(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����7�����ڽ��뽻�ѷ���Ϣ����ʾ')
    def test_Six_Party_007(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(3)
        self.assertIs(S.Test_X067(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����8�����ѷ���Ϣ����������û���')
    def test_Six_Party_008(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_message_user()
        self.assertIs(S.Test_X068(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����9���򿪹����б�')
    def test_Six_Party_009(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Six_party_more_people()
        self.assertIs(S.Test_X006(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����10�������б����»���')
    def test_Six_Party_010(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(700, 700, 700, 1800)
        S.driver.swipe(700, 1800, 700, 700)
        self.assertIs(S.Test_X007(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����12�������б�ͷ�����鿴')
    def test_Six_Party_012(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X009(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����13�����ڸ�����Ϣ�����ٱ����')
    def test_Six_Party_013(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X010(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����14�����ڸ�����Ϣ�������������ҳ')
    def test_Six_Party_014(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Six_party_more_people_list_one()
        S.Six_party_supernatant_anchor_head()
        self.assertIs(S.Test_X011(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����15��İ���˸�����Ϣ������ע��ť���')
    def test_Six_Party_015(self):
        S = Six_partyView_anchor(self.driver)
        S.Homepage_back()
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X012(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����16�����ڸ�����Ϣ���������﹦����֤')
    def test_Six_Party_016(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_supernatant_gift()
        self.assertIs(S.Test_X013(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����17�����ڸ�����Ϣ������������')
    def test_Six_Party_017(self):
        S = Six_partyView_anchor(self.driver)
        S.Gift_window_Activity()
        S.Six_party_one_gift()
        S.More_message_people_sendgift()
        S.driver.tap([(200, 400), (201, 401)], 200)
        S.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(S.Test_X014(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����18�����ڸ�����Ϣ������Ϣ��ť')
    def test_Six_Party_018(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Supernatant_message()
        self.assertIs(S.Test_X015(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����19��˽�Ľ�����ఴť���')
    def test_Six_Party_019(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_more()
        self.assertIs(S.Test_X017(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����20��˽�Ľ����˳���ť���')
    def test_Six_Party_020(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Supernatant_message_back()
        self.assertIs(S.Test_X016(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����23�������ڸ�����Ϣ����--��Ƶͨ��')
    def test_Six_Party_023(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(528, 528), (529, 529)], 200)
        S.Six_party_more_people_list_one()
        S.Supernatant_message()
        S.Supernatant_message_more()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_X015(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����24��˽�Ľ����۵���ť������')
    def test_Six_Party_024(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing()
        self.assertIs(S.Test_X021(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����25��˽�Ľ����۵������밴ť������')
    def test_Six_Party_025(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing_translate()
        self.assertIs(S.Test_X022(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����27��˽�Ľ����۵�������Ṧ�ܼ��')
    def test_Six_Party_027(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing_photo()
        self.assertIs(S.Test_X024(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����28��˽�Ľ��淢�����')
    def test_Six_Party_028(self):
        S = Six_partyView_anchor(self.driver)
        S.Myphoto_one()
        S.Myphoto_comfirm()
        self.assertIs(S.Test_X025(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����29��˽�Ľ����۵�����������ܼ��')
    def test_Six_Party_029(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing_camera()
        self.assertIs(S.Test_X026(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����30��˽�Ľ��淢��������Ƭ')
    def test_Six_Party_030(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_setiing_photo_confirm()
        S.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(S.Test_X027(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����32��˽�Ľ��淢������')
    def test_Six_Party_032(self):
        S = Six_partyView_anchor(self.driver)
        S.Room_message_button_click()
        S.Room_message_button_input()
        S.Room_message_button_send()
        self.assertIs(S.Test_X029(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����33��˽�Ľ��淢�ͱ���')
    def test_Six_Party_033(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_face_gif()
        S.Supernatant_message_face_gif_one()
        self.assertIs(S.Test_X030(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����34��˽�Ľ���������')
    def test_Six_Party_034(self):
        S = Six_partyView_anchor(self.driver)
        S.More_message_people_gift()
        S.Gift_window_Activity()
        S.More_message_people_sendgift()
        S.driver.tap([(528, 528), (529, 529)], 200)
        self.assertIs(S.Test_X031(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����35��Ⱥ�Ľ��淢����ͼƬ')
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
    @allure.title('����36��Ⱥ�Ľ��淢���ͼƬ')
    def test_Six_Party_036(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_camera()
        time.sleep(2)
        S.Myphoto_one()
        self.assertIs(S.Test_X033(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����37��Ⱥ�Ľ��淢��Ϣ')
    def test_Six_Party_037(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_chat()
        S.Supernatant_message_group_chat_send()
        self.assertIs(S.Test_X034(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����38��Ⱥ�Ľ��淢����')
    def test_Six_Party_038(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_face_gif()
        S.Supernatant_message_group_gif_one()
        self.assertIs(S.Test_X035(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����39��Ⱥ�Ľ��淢����')
    def test_Six_Party_039(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_voice()
        S.driver.tap([(500, 2010), (510, 2020)], 3000)
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����40��Ⱥ�Ľ�������')
    def test_Six_Party_040(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_upmic()
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����41��Ⱥ�Ľ��淢���')
    def test_Six_Party_041(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_packet()
        S.Supernatant_message_group_packet_number()
        S.Supernatant_message_group_packet_diamond()
        S.Supernatant_message_group_packet_send()
        self.assertIs(S.Test_X038(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����42��Ⱥ�Ľ�������')
    def test_Six_Party_042(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_packet_get()
        S.Supernatant_message_group_packet_open()
        self.assertIs(S.Test_X039(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����43��Ⱥ�Ľ�������')
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
    @allure.title('����44��Ⱥ�Ľ������')
    def test_Six_Party_044(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_more()
        S.driver.tap([(864, 974), (865, 975)], 200)
        time.sleep(10)
        self.assertIs(S.Test_X041(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����45�����ڸ�����Ϣ�������Թ���')
    def test_Six_Party_045(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(500, 500), (501, 501)], 200)
        S.driver.tap([(500, 500), (501, 501)], 200)
        S.Six_party_more_people_list_one()
        S.Supernatant_mute()
        S.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(S.Test_X042(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����46�����ڸ�����Ϣ����ȡ�����Թ���')
    def test_Six_Party_046(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people()
        S.Six_party_more_people_list_one()
        S.Supernatant_mute()
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X043(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����47�����ڸ�����Ϣ����@���ڹ���')
    def test_Six_Party_047(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_at_anchor()
        S.Room_message_button_send()
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(S.Test_X044(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����61�������ڽ���λ��չʾ����')
    def test_Six_Party_061(self):
        S = Six_partyView_anchor(self.driver)
        S.Room_Homeowner_place()
        S.Room_Homeowner_place_emo()
        self.assertIs(S.Test_X058(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����62�����ѷ�������Ϣ���')
    def test_Six_Party_062(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(S.Test_X059(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����63�����ѷ������˷���')
    def test_Six_Party_063(self):
        S = Six_partyView_anchor(self.driver)
        S.Room_message_button()
        S.Room_message_button_input()
        S.Room_message_button_send()
        S.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(S.Test_X060(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����65�����ѷ���Ϣ���ϻ���Ϣ')
    def test_Six_Party_065(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(S.Test_X062(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����66�����ѷ���Ϣ���»���Ϣ')
    def test_Six_Party_066(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(363, 2040, 363, 1478)
        self.assertIs(S.Test_X063(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����70�������ڽ��ѷ��и��Լ�����')
    def test_Six_Party_070(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_gift()
        self.assertIs(S.Test_X070(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����71�����ѷ������һ���banner')
    def test_Six_Party_071(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.driver.swipe(1000, 2000, 860, 2000)
        self.assertIs(S.Test_X071(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����72�����ѷ��е������bannerҳ')
    def test_Six_Party_072(self):
        S = Six_partyView_anchor(self.driver)
        S.Room_banner()
        time.sleep(5)
        self.assertIs(S.Test_X072(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����73�����ѷ��б���ѡ��')
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
    @allure.title('����74���������ѷ�����')
    def test_Six_Party_074(self):
        S = Six_partyView_anchor(self.driver)
        S.More_Setting_background_Lv20()
        time.sleep(2)
        self.assertIs(S.Test_X074(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����75�����ѷ��д���Ϣ�б�')
    def test_Six_Party_075(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Message()
        self.assertIs(S.Test_X075(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����78�����ѷ��н��г�ֵ')
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
    @allure.title('����79�����ѷ��йر���˷�')
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
    @allure.title('����80�����ѷ���������ֽ')
    def test_Six_Party_080(self):
        S = Six_partyView_anchor(self.driver)
        S.More_setting_sticker()
        S.More_setting_sticker_1()
        time.sleep(5)
        self.assertIs(S.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����81�����ѷ��п�������')
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
    @allure.title('����82�����ѷ��п�������ģʽ')
    def test_Six_Party_082(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_mirror_mode()
        self.assertIs(S.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����83�����ѷ��йر�����ͷ')
    def test_Six_Party_083(self):
        S = Six_partyView_anchor(self.driver)
        S.More_setting_turn_off_camera()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X083(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����84�����ѷ����л�����ͷ')
    def test_Six_Party_084(self):
        S = Six_partyView_anchor(self.driver)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_switch_camera()
        S.More_setting_switch_camera()
        self.assertIs(S.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����85���رս��ѷ��������ҳ')
    def test_Six_Party_085(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Close_six_party()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X085(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����86������ҳ��ʾ����')
    def test_Six_Party_086(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X087(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����87������ҳ��������������ҳ')
    def test_Six_Party_087(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_endpage_profile()
        self.assertIs(S.Test_X086(), True)



    if __name__ == '__main__':
        pytest.main()
