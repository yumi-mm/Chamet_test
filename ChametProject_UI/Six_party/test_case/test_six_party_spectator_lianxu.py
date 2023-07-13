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

@allure.epic("��Ŀ���ƣ�6�˽��ѷ�")
@allure.issue("BUG���ӣ�http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("�����������ӣ�http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('���ѷ�6�˷�_���ڶ˹���')


class Test_six_party(StartEnd):
    csv_file = '../data/account.csv'
    @unittest.skip('skip test_changjingmoni')
    def test_changjingmoni(self):
        logging.info("===��ʼ����ģ��===")
        l = LoginView(self.driver)
        S = Six_partyView_anchor(self.driver)
        # ���    S.driver.tap([(528, 2191), (529, 5292)], 200)
        # ����    S.driver.swipe(800, 800, 200, 800)
        self.assertIs(S.Test_XX(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����89�����ѷ�ҳǩ������ʾ')
    def test_Six_Party_089(self):
        S = Six_partyView_anchor(self.driver)
        S.Tab_party()
        S.driver.swipe(600, 1800, 600, 800)
        S.driver.swipe(600, 800, 600, 1800)
        self.assertIs(S.Test_X089(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����90���ӽ��ѷ�ҳǩ���뽻�ѷ�')
    def test_Six_Party_090(self):
        S = Six_partyView_anchor(self.driver)
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X090(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����91�����ѷ��ó�����Ϊ0�����ڲ鿴��������')
    def test_Six_Party_091(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X133(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����92�������ڽ��ѷ�������ʱ����')
    def test_Six_Party_092(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_gift()
        time.sleep(1)
        S.Six_party_two_gift()
        S.More_message_people_sendgift()
        time.sleep(5)
        self.assertIs(S.Test_X127(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����94�������ڽ��ѷ��е������ͷ��')
    def test_Six_Party_094(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(2)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Six_party_anchor_head()
        self.assertIs(S.Test_X091(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����95�������ڽ��ѷ��й�ע����')
    def test_Six_Party_095(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_follow_anchor()
        self.assertIs(S.Test_X092(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����96�������ڽ��ѷ��оٱ�����')
    def test_Six_Party_096(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X093(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����97�������ڽ��ѷ���ͨ������������ҳ����������������')
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
    @allure.title('����98�������ڽ��ѷ��и�����������Ƶͨ��')
    def test_Six_Party_098(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_anchor_head()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_X095(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����99�������ڽ��ѷ�@����')
    def test_Six_Party_099(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(5)
        S.Six_party_at_anchor()
        S.Six_party_room_message_send()
        S.driver.tap([(552, 189), (553, 190)], 200)
        S.driver.tap([(552, 189), (553, 190)], 200)
        self.assertIs(S.Test_X096(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����100�����ڴ�����������ҳ���뽻�ѷ�')
    def test_Six_Party_100(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_anchor_head()
        S.Six_party_supernatant_anchor_head()
        time.sleep(2)
        S.Homepage_video()
        self.assertIs(S.Test_X097(), True)

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('����101��LV7�����Ϲ��ڽ��뽻�ѷ���Чչʾ')
    # def test_Six_Party_101(self):
    #     S = Six_partyView_anchor(self.driver)
    #     time.sleep(5)
    #     self.assertIs(S.Test_X066(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����102�����ڽ��뽻�ѷ���Ϣ����ʾ')
    def test_Six_Party_102(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(3)
        self.assertIs(S.Test_X102(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����104�����ѷ��й��ڴ򿪹����б�')
    def test_Six_Party_104(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people()
        self.assertIs(S.Test_X098(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����105�����ѷ��й������»��������б�')
    def test_Six_Party_105(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(837, 410, 837, 1800)
        S.driver.swipe(837, 1800, 837, 410)
        self.assertIs(S.Test_X098(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����107�����ѷ��й��ڵ���鿴����ͷ��')
    def test_Six_Party_107(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_more_people_list_two()
        self.assertIs(S.Test_X101(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����108�����ڸ�����Ϣ�����ٱ����')
    def test_Six_Party_108(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X093(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����109�����ڸ�����Ϣ�������������ҳ')
    def test_Six_Party_109(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(915, 439), (916, 440)], 200)
        S.Six_party_more_people_list_two()
        S.Six_party_supernatant_anchor_head()
        self.assertIs(S.Test_X103(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����110��İ���˸�����Ϣ������ע��ť���')
    def test_Six_Party_110(self):
        S = Six_partyView_anchor(self.driver)
        S.Homepage_back()
        S.Six_party_more_people_list_two()
        S.Six_party_supernatant_follow()
        self.assertIs(S.Test_X104(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����111�����ڸ�����Ϣ���������﹦��')
    def test_Six_Party_111(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_supernatant_gift()
        self.assertIs(S.Test_X105(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����112�����ڸ�����Ϣ���������﹦��')
    def test_Six_Party_112(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_one_gift()
        S.More_message_people_sendgift()
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X106(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����113�����ѷ��ó�����Ϊ0�����ڲ鿴��������')
    def test_Six_Party_113(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X134(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����114�����ڸ�����Ϣ����@��')
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
    @allure.title('����123�����ѷ�������Ϣ���')
    def test_Six_Party_123(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X116(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����124�����ѷ����ڶ˶˷���')
    def test_Six_Party_124(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X117(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����125�����ѷ���Ϣ����Ϣ����')
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
    @allure.title('����126�����ѷ���Ϣ���ϻ���Ϣ')
    def test_Six_Party_126(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.swipe(357, 1519, 357, 2030)
        self.assertIs(S.Test_X119(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����128�������ڽ��ѷ��д����񸡴�')
    def test_Six_Party_128(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_gift()
        self.assertIs(S.Test_X128(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����130�������ڽ��ѷ��и����мα�����')
    def test_Six_Party_130(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_send_all_gift()
        S.Six_party_one_gift()
        S.Six_party_send_gift()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X094(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����131�������ڽ��ѷ�������ʱ����')
    def test_Six_Party_131(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_gift()
        S.Six_party_send_all_gift()
        S.Six_party_two_gift()
        S.More_message_people_sendgift()
        self.assertIs(S.Test_X127(), True)

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('����134�����ѷ������һ���banner')
    # def test_Six_Party_134(self):
    #     S = Six_partyView_anchor(self.driver)
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     S.driver.swipe(1000, 2000, 860, 2000)
    #     self.assertIs(S.Test_X071(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����135�����ѷ��е������bannerҳ')
    def test_Six_Party_135(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.driver.tap([(936, 2013), (937, 2014)], 200)
        time.sleep(5)
        self.assertIs(S.Test_X072(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����136�����ѷ��й��ڵ�����밴ť')
    def test_Six_Party_136(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 201), (201, 202)], 200)
        S.More_Setting()
        S.More_join()
        self.assertIs(S.Test_X138(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����137�����ѷ��й��ڴ���Ϣ�б�')
    def test_Six_Party_137(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_twice_apply()
        S.More_Setting()
        S.More_Message()
        self.assertIs(S.Test_X137(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����138��Ⱥ�Ľ��淢����ͼƬ')
    def test_Six_Party_138(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group()
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_photo()
        S.Supernatant_message_setiing_photo_confirm()
        S.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(S.Test_X032(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����139��Ⱥ�Ľ��淢���ͼƬ')
    def test_Six_Party_139(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_camera()
        time.sleep(2)
        S.Myphoto_one()
        self.assertIs(S.Test_X140(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����140��Ⱥ�Ľ��淢��Ϣ')
    def test_Six_Party_140(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_chat()
        S.Supernatant_message_group_chat_send()
        self.assertIs(S.Test_X034(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����141��Ⱥ�Ľ��淢����')
    def test_Six_Party_141(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_face_gif()
        S.Supernatant_message_group_gif_one()
        self.assertIs(S.Test_X035(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����142��Ⱥ�Ľ��淢����')
    def test_Six_Party_142(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_voice()
        S.driver.tap([(500, 2010), (510, 2020)], 3000)
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����143��Ⱥ�Ľ�������')
    def test_Six_Party_143(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_upmic()
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����144��Ⱥ�Ľ��淢���')
    def test_Six_Party_144(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_packet()
        S.Supernatant_message_group_packet_number()
        S.Supernatant_message_group_packet_diamond()
        S.Supernatant_message_group_packet_send()
        self.assertIs(S.Test_X038(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����145��Ⱥ�Ľ�������')
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
    @allure.title('����146��Ⱥ�Ľ������')
    def test_Six_Party_146(self):
        S = Six_partyView_anchor(self.driver)
        S.Supernatant_message_group_more()
        S.driver.tap([(864, 974), (865, 975)], 200)
        time.sleep(10)
        self.assertIs(S.Test_X041(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����147�����ѷ��н��г�ֵ')
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
    @allure.title('����148������α�λ')
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
    @allure.title('����149�����ѷ��йر���˷�')
    def test_Six_Party_149(self):
        S = Six_partyView_anchor(self.driver)
        time.sleep(5)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_switch_microphone()
        S.More_setting_switch_microphone()
        self.assertIs(S.Test_X079(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����150�����ѷ���������ֽ')
    def test_Six_Party_150(self):
        S = Six_partyView_anchor(self.driver)
        S.More_setting_sticker()
        S.More_setting_sticker_1()
        time.sleep(5)
        self.assertIs(S.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����151�����ѷ��п�������')
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
    @allure.title('����152�����ѷ��п�������ģʽ')
    def test_Six_Party_152(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_mirror_mode()
        self.assertIs(S.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����153�����ѷ��йر�����ͷ')
    def test_Six_Party_153(self):
        S = Six_partyView_anchor(self.driver)
        S.More_setting_turn_off_camera()
        S.More_setting_turn_off_camera()
        S.More_setting_turn_off_camera()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X155(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����154�����ѷ����л�����ͷ')
    def test_Six_Party_154(self):
        S = Six_partyView_anchor(self.driver)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_switch_camera()
        S.More_setting_switch_camera()
        self.assertIs(S.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����155�����ѷ��й��ڵ���뿪�α�λ')
    def test_Six_Party_155(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_off_mic()
        self.assertIs(S.Test_X157(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����156�����ѷ��й���ȡ���뿪�α�λ')
    def test_Six_Party_156(self):
        S = Six_partyView_anchor(self.driver)
        S.Close_six_party_two_cancle()
        self.assertIs(S.Test_X158(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����157�����ѷ��й���ȷ���뿪�α�λ')
    def test_Six_Party_157(self):
        S = Six_partyView_anchor(self.driver)
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X159(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����159�����ѷ��й��ڸ���������Լ��')
    def test_Six_Party_159(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_anchor()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_X095(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����160���뿪���ѷ�')
    def test_Six_Party_160(self):
        S = Six_partyView_anchor(self.driver)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Close_six_party()
        self.assertIs(S.Test_X162(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����161�������رս��ѷ��Ľ���ҳУ��')
    def test_Six_Party_161(self):
        S = Six_partyView_anchor(self.driver)
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X163(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����162������ҳУ��-���������ҳ')
    def test_Six_Party_162(self):
        S = Six_partyView_anchor(self.driver)
        S.Six_party_endpage_profile()
        self.assertIs(S.Test_X011(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����163������ҳУ��-����ҳ����')
    def test_Six_Party_163(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X165(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����164������ҳУ��-����ҳ�ɶ�ʱ��/����')
    def test_Six_Party_164(self):
        S = Six_partyView_anchor(self.driver)
        self.assertIs(S.Test_X166(), True)

    if __name__ == '__main__':
        pytest.main()
