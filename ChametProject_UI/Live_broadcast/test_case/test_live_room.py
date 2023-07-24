# coding=gb2312
import time
from ChametProject_UI.Live_broadcast.common.myunittest import StartEnd
import allure
import unittest
import pytest

@allure.epic("��Ŀ���ƣ�ֱ�����Զ�������")
@allure.issue("BUG���ӣ�http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("�����������ӣ�http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('ֱ����_˫�˽���')


class test_Live_room_interaction(StartEnd):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    csv_file = '../data/account.csv'
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����1����������ֱ����ҳ��')
    def Live_broadcast_room_001(self):
        A = self.multanchor
        A.Tab_live_list()
        A.Setup_live()
        self.assertIs(A.Test_X001(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����2���������չ���У��')
    def Live_broadcast_room_002(self):
        A = self.multanchor
        A.Setup_beauty()
        A.More_setting_beauty_reset()
        A.More_setting_beauty_confirmreset()
        self.assertIs(A.Test_X003(), True)
        A.driver.tap([(528, 528), (529, 529)], 200)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����3������ʹ����ֽ����')
    def Live_broadcast_room_003(self):
        A = self.multanchor
        A.Setup_sticker()
        A.Sticker_download()
        time.sleep(5)
        self.assertIs(A.Sticker_downloading(), True)
        A.driver.tap([(528, 528), (529, 529)], 200)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����4�������ɹ�����ֱ����')
    def Live_broadcast_room_004(self):
        A = self.multanchor
        A.Two_Setup()
        self.assertIs(A.Test_X005(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����5������ֱ���侯����Ϣ���')
    def Live_broadcast_room_005(self):
        A = self.multanchor
        A.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(A.Test_X059(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����6������ֱ�����������������Ϣ���')
    def Live_broadcast_room_006(self):
        A = self.multanchor
        A.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(A.Test_006(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����7�����ڴ���Ⱥ�ĳ���,����Ⱥ�Ľ�������ֱ����')
    def Live_broadcast_room_007(self):
        S = self.multspectator
        S.Tab_group()
        S.Tab_group_group()
        S.My_group()
        S.My_group_one()
        S.Supernatant_message_face_gif()
        S.Supernatant_message_face_gif_one()
        S.Group_more()
        S.Group_more_two_people()
        S.Six_party_supernatant_anchor_head()
        S.Homepage_video()
        self.assertIs(S.Test_7(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����8�����ڽ���ֱ������Чչʾ')
    def Live_broadcast_room_008(self):
        S = self.multspectator
        self.assertIs(S.Test_X066(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����9�����ڽ���ֱ������Ϣ')
    def Live_broadcast_room_009(self):
        S = self.multspectator
        self.assertIs(S.Test_8(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����10������ͷ��-��ת������ҳ')
    def Live_broadcast_room_010(self):
        S = self.multspectator
        S.Live_anchor_avatar()
        S.Six_party_supernatant_anchor_head()
        self.assertIs(S.Test_10(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����11��������ҳ-��תֱ����')
    def Live_broadcast_room_011(self):
        S = self.multspectator
        S.Homepage_video()
        self.assertIs(S.Test_129(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����12�������鿴���ڽ���ֱ�������Чչʾ')
    def Live_broadcast_room_012(self):
        A = self.multanchor
        self.assertIs(A.Test_X066(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����13�������鿴���ڽ���ֱ������Ϣ����ʾ')
    def Live_broadcast_room_013(self):
        A = self.multanchor
        time.sleep(3)
        self.assertIs(A.Test_X067(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����14��������Ϣ����-��������ťУ��')
    def Live_broadcast_room_014(self):
        S = self.multspectator
        S.Live_anchor_avatar()
        self.assertIs(S.Test_14_1(), True)
        self.assertIs(S.Test_14_2(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����15��������ֱ�����й�ע����')
    def Live_broadcast_room_015(self):
        S = self.multspectator
        S.Six_party_follow_anchor()
        self.assertIs(S.Test_X092(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����16����Ϣ�����оٱ�����У��')
    def Live_broadcast_room_016(self):
        S = self.multspectator
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X093(), True)
        S.driver.tap([(213, 213), (214, 214)], 200)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����17�������������������ﰴť')
    def Live_broadcast_room_017(self):
        S = self.multspectator
        A = self.multanchor
        S.Live_anchor_avatar()
        S.Six_party_supernatant_gift()
        self.assertIs(A.Test_X17(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����18��������������������')
    def Live_broadcast_room_018(self):
        S = self.multspectator
        A = self.multanchor
        S.Six_party_one_gift()
        S.Six_party_gift_single()
        S.Six_party_send_gift()
        S.Confirmation_winning()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(A.Test_18(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����19������������������붯̬��ͼģʽ')
    def Live_broadcast_room_019(self):
        S = self.multspectator
        A = self.multanchor
        S.Live_anchor_avatar()
        S.Live_superposed_trends_two()
        self.assertIs(A.Test_19(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����20����̬��Ŀ-��ͼģʽ����')
    def Live_broadcast_room_019(self):
        S = self.multspectator
        A = self.multanchor
        S.Trends_gift()
        S.Confirmation_winning()
        self.assertIs(S.Test_20(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����21����̬��Ŀ-��ͼģʽ����')
    def Live_broadcast_room_021(self):
        S = self.multspectator
        S.Trends_likes()
        self.assertIs(S.Test_21(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����22����̬��Ŀ-��ͼģʽ����')
    def Live_broadcast_room_022(self):
        S = self.multspectator
        S.Trends_review()
        S.Trends_review_commend()
        S.Trends_review_commend_edit()
        S.Trends_review_commend_send()
        self.assertIs(S.Test_22(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����23����̬��Ŀ-��ͼģʽ����ť')
    def Live_broadcast_room_023(self):
        A = self.multanchor
        S = self.multspectator
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Trends_call()
        S.check_perBtn()
        S.check_perBtn()
        S.check_perBtn()
        self.assertIs(S.Test_23(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����24����̬��Ŀ-��̬����ҳ-���ؼ�')
    def Live_broadcast_room_024(self):
        A = self.multanchor
        S = self.multspectator
        S.Trends_back()
        self.assertIs(S.Test_24(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����25��������ֱ����@����')
    def Live_broadcast_room_025(self):
        A = self.multanchor
        S = self.multspectator
        S.Six_party_at_anchor()
        S.Six_party_room_message_send()
        S.driver.tap([(552, 189), (553, 190)], 200)
        self.assertIs(A.Test_X096(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����26����Ƶͨ����ť')
    def Live_broadcast_room_026(self):
        A = self.multanchor
        S = self.multspectator
        S.Live_call()
        self.assertIs(S.Test_26(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����28��ֱ������ڶ˶˷���')
    def Live_broadcast_room_028(self):
        S = self.multspectator
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X117(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����29��ֱ������Ϣ����Ϣ����')
    def Live_broadcast_room_029(self):
        S = self.multspectator
        S.Six_party_gift()
        S.Six_party_one_gift()
        S.Six_party_gift_single()
        S.More_message_people_sendgift()
        S.Confirmation_winning()
        S.More_message_people_sendgift()
        S.Confirmation_winning()
        S.driver.swipe(357, 1519, 357, 2030)
        self.assertIs(S.Test_X119(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����30����������ť')
    def Live_broadcast_room_030(self):
        S = self.multspectator
        S.Live_guide_call()
        self.assertIs(S.Test_26(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����31���򿪷�˿��')
    def Live_broadcast_room_031(self):
        S = self.multspectator
        S.Live_vermicelli_top()
        self.assertIs(S.Test_31(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����32�������˿�����û�ͷ��')
    def Live_broadcast_room_032(self):
        S = self.multspectator
        S.Live_vermicelli_top_one_people()
        self.assertIs(S.Test_24(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����33��ֱ�����й��ڴ򿪹����б�')
    def Live_broadcast_room_033(self):
        S = self.multspectator
        S.Six_party_more_people()
        self.assertIs(S.Test_X098(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����34��ֱ�����й������»��������б�')
    def Live_broadcast_room_034(self):
        S = self.multspectator
        S.driver.swipe(837, 410, 837, 1800)
        S.driver.swipe(837, 1800, 837, 410)
        self.assertIs(S.Test_X098(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����35��ֱ�����й��ڵ���鿴����ͷ��')
    def Live_broadcast_room_035(self):
        S = self.multspectator
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X101(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����35�����˰���������ͷ����ת������ҳ')
    def Live_broadcast_room_035(self):
        S = self.multspectator
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X101(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����26��ֱ���侯����Ϣ���')
    def Live_broadcast_room_026(self):
        S = self.multspectator
        S.driver.tap([(200, 189), (201, 190)], 200)
        time.sleep(1)
        S.driver.tap([(200, 189), (201, 190)], 200)
        self.assertIs(S.Test_X116(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����30��������ֱ�����д����񸡴�')
    def Live_broadcast_room_030(self):
        S = self.multspectator
        S.Six_party_gift()
        time.sleep(1)
        self.assertIs(S.Test_X128(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����31��������ֱ�����и�����������')
    def Live_broadcast_room_031(self):
        S = self.multspectator
        A = self.multanchor
        S.Six_party_send_all_gift()
        S.Six_party_one_gift()
        S.Six_party_gift_single()
        S.Six_party_send_gift()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(A.Test_X13(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����32��������ֱ����������ʱ����')
    def Live_broadcast_room_032(self):
        S = self.multspectator
        S.Six_party_gift()
        S.Six_party_send_all_gift()
        S.Six_party_four_gift()
        S.More_message_people_sendgift()
        self.assertIs(S.Test_32(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����33��ֱ�����е������bannerҳ')
    def Live_broadcast_room_033(self):
        S = self.multspectator
        S.driver.tap([(200, 201), (201, 202)], 200)
        time.sleep(1)
        S.driver.tap([(200, 201), (201, 202)], 200)
        time.sleep(1)
        S.driver.tap([(936, 2013), (937, 2014)], 200)
        time.sleep(5)
        self.assertIs(S.Test_X072(), True)
        S.driver.tap([(200, 201), (201, 202)], 200)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����34��ֱ�����й��ڵ�����밴ť')
    def Live_broadcast_room_034(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        self.assertIs(S.Test_X138(), True)
        S.Six_party_twice_apply()
        S.check_perBtn()
        S.check_perBtn()
        S.check_perBtn()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����35��ֱ�����й��ڴ���Ϣ�б�')
    def Live_broadcast_room_035(self):
        S = self.multspectator
        S.More_Setting()
        S.More_Message()
        self.assertIs(S.Test_X137(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����36��Ⱥ�Ľ��淢����ͼƬ')
    def Live_broadcast_room_036(self):
        S = self.multspectator
        S.Supernatant_message_group()
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_photo()
        S.Supernatant_message_setiing_photo_confirm()
        S.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(S.Test_X032(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����37��Ⱥ�Ľ��淢���ͼƬ')
    def Live_broadcast_room_037(self):
        S = self.multspectator
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_camera()
        time.sleep(2)
        S.Myphoto_one()
        self.assertIs(S.Test_X140(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����38��Ⱥ�Ľ��淢��Ϣ')
    def Live_broadcast_room_038(self):
        S = self.multspectator
        S.Supernatant_message_group_chat()
        S.Supernatant_message_group_chat_send()
        self.assertIs(S.Test_X034(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����39��Ⱥ�Ľ��淢����')
    def Live_broadcast_room_039(self):
        S = self.multspectator
        S.Supernatant_message_face_gif()
        S.Supernatant_message_group_gif_one()
        self.assertIs(S.Test_X035(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����40��Ⱥ�Ľ��淢����')
    def Live_broadcast_room_040(self):
        S = self.multspectator
        S.Supernatant_message_group_voice()
        S.driver.tap([(500, 2010), (510, 2020)], 3000)
        self.assertIs(S.Test_X036(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����41��Ⱥ�Ľ�������')
    def Live_broadcast_room_041(self):
        S = self.multspectator
        S.Supernatant_message_group_upmic()
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����42��Ⱥ�Ľ��淢���')
    def Live_broadcast_room_042(self):
        S = self.multspectator
        S.Supernatant_message_group_packet()
        S.Supernatant_message_group_packet_number()
        S.Supernatant_message_group_packet_diamond()
        S.Supernatant_message_group_packet_send()
        self.assertIs(S.Test_X038(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����43��Ⱥ�Ľ�������')
    def Live_broadcast_room_043(self):
        S = self.multspectator
        S.Supernatant_message_group_gift()
        S.Six_party_one_gift()
        S.Six_party_gift_single()
        S.More_message_people_sendgift()
        S.driver.tap([(500, 500), (501, 501)], 200)
        self.assertIs(S.Test_X040(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����44��Ⱥ�Ľ������')
    def Live_broadcast_room_044(self):
        S = self.multspectator
        S.Supernatant_message_group_more()
        S.driver.tap([(864, 974), (865, 975)], 200)
        time.sleep(10)
        self.assertIs(S.Test_X041(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����45��ֱ�����н��г�ֵ')
    def Live_broadcast_room_045(self):
        S = self.multspectator
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
    @allure.title('����46���������α�λ')
    def Live_broadcast_room_046(self):
        S = self.multspectator
        S.More_top_up_confirm()
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        time.sleep(5)
        self.assertIs(S.Test_X139(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����47������ͬ����������')
    def Live_broadcast_room_047(self):
        S = self.multspectator
        A = self.multanchor
        A.Six_party_invite()
        A.Six_party_agree_list_one()
        A.driver.tap([(200, 420), (201, 421)], 200)
        time.sleep(1)
        self.assertIs(A.Test_45(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����48��ֱ�����йر���˷�')
    def Live_broadcast_room_048(self):
        S = self.multspectator
        time.sleep(5)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_switch_microphone()
        S.More_setting_switch_microphone()
        self.assertIs(S.Test_X079(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����49��ֱ������������ֽ')
    def Live_broadcast_room_049(self):
        S = self.multspectator
        S.More_setting_sticker()
        S.More_setting_sticker_1()
        time.sleep(6)
        S.More_setting_sticker_1()
        self.assertIs(S.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����50��ֱ�����п�������')
    def Live_broadcast_room_050(self):
        S = self.multspectator
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_beauty()
        S.More_setting_beauty_reset()
        S.More_setting_beauty_confirmreset()
        self.assertIs(S.Test_X081(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����51��ֱ�����п�������ģʽ')
    def Live_broadcast_room_051(self):
        S = self.multspectator
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_mirror_mode()
        self.assertIs(S.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����52��ֱ�����йر�����ͷ')
    def Live_broadcast_room_052(self):
        S = self.multspectator
        S.More_setting_turn_off_camera()
        S.More_setting_turn_off_camera()
        S.More_setting_turn_off_camera()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X155(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����53��ֱ�������л�����ͷ')
    def Live_broadcast_room_053(self):
        S = self.multspectator
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_switch_camera()
        S.More_setting_switch_camera()
        self.assertIs(S.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����54��ֱ�����й��ڵ���뿪�α�λ')
    def Live_broadcast_room_054(self):
        S = self.multspectator
        S.Six_party_off_mic()
        self.assertIs(S.Test_X157(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����55��ֱ�����й���ȡ���뿪�α�λ')
    def Live_broadcast_room_055(self):
        S = self.multspectator
        S.Close_six_party_two_cancle()
        self.assertIs(S.Test_X158(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����56��ֱ�����й���ȷ���뿪�α�λ')
    def Live_broadcast_room_056(self):
        S = self.multspectator
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X159(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����57��ֱ�����й��ڸ���������Լ��')
    def Live_broadcast_room_057(self):
        S = self.multspectator
        S.Six_party_anchor()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_56(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����58�������뿪ֱ����')
    def Live_broadcast_room_058(self):
        S = self.multspectator
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Close_six_party()
        self.assertIs(S.Test_X162(), True)
        S.Group_more_two_people()
        S.Six_party_supernatant_anchor_head()
        S.Homepage_video()


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����59����������Ϣ����������û���')
    def Live_broadcast_room_059(self):
        A = self.multanchor
        A.Six_message_inuser()
        self.assertIs(A.Test_X068(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����60�������򿪹����б�')
    def Live_broadcast_room_060(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Six_party_more_people()
        self.assertIs(A.Test_X006(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����61�������ڹ����б����»���')
    def Live_broadcast_room_061(self):
        A = self.multanchor
        A.driver.swipe(700, 700, 700, 1800)
        time.sleep(1)
        A.driver.swipe(700, 1800, 700, 700)
        self.assertIs(A.Test_X007(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����62�������ڹ����б�ͷ�����鿴')
    def Live_broadcast_room_062(self):
        A = self.multanchor
        A.Six_party_more_people_list_one()
        self.assertIs(A.Test_X017(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����63�������ڹ��ڸ�����Ϣ�����ٱ����')
    def Live_broadcast_room_063(self):
        A = self.multanchor
        A.Six_party_report_anchor()
        self.assertIs(A.Test_X010(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����64�������ڹ��ڸ�����Ϣ���������������ҳ')
    def Live_broadcast_room_064(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Six_party_more_people_list_one()
        A.Six_party_supernatant_anchor_head()
        self.assertIs(A.Test_X011(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����65������İ���˸�����Ϣ������ע��ť���')
    def Live_broadcast_room_065(self):
        A = self.multanchor
        A.Homepage_back()
        A.Six_party_more_people_list_one()
        A.Six_party_supernatant_follow()
        self.assertIs(A.Test_X012(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����66�������ڹ��ڸ�����Ϣ���������﹦����֤')
    def Live_broadcast_room_066(self):
        A = self.multanchor
        A.Six_party_supernatant_gift()
        self.assertIs(A.Test_X105(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����67�������ڹ��ڸ�����Ϣ������������')
    def Live_broadcast_room_067(self):
        A = self.multanchor
        A.Six_party_one_gift()
        A.Six_party_gift_single()
        A.More_message_people_sendgift()
        A.Confirmation_winning()
        time.sleep(1)
        A.driver.tap([(200, 400), (201, 401)], 200)
        A.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(A.Test_31(), True)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����68�����������ڸ�����Ϣ������Ϣ��ť')
    def Live_broadcast_room_068(self):
        A = self.multanchor
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_message()
        self.assertIs(A.Test_X015(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����69��˽�Ľ�����ఴť�ļ��')
    def Live_broadcast_room_069(self):
        A = self.multanchor
        A.Supernatant_message_more()
        self.assertIs(A.Test_X017(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����70��˽�Ľ����˳���ť���')
    def Live_broadcast_room_070(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Supernatant_message_back()
        self.assertIs(A.Test_X016(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����71�������ڸ�����Ϣ����--��Ƶͨ��')
    def Live_broadcast_room_071(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Six_party_more_people_list_one()
        A.Supernatant_message()
        A.Supernatant_message_more()
        A.Six_party_call_anchor()
        self.assertIs(A.Test_X015(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����72��˽�Ľ����۵���ť������')
    def Live_broadcast_room_072(self):
        A = self.multanchor
        A.Supernatant_message_setiing()
        self.assertIs(A.Test_X021(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����73��˽�Ľ����۵������밴ť������')
    def Live_broadcast_room_073(self):
        A = self.multanchor
        A.Supernatant_message_setiing_translate()
        self.assertIs(A.Test_X022(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����74��˽�Ľ����۵�������Ṧ�ܼ��')
    def Live_broadcast_room_074(self):
        A = self.multanchor
        A.Supernatant_message_setiing_photo()
        self.assertIs(A.Test_X024(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����75��˽�Ľ��淢�����')
    def Live_broadcast_room_075(self):
        A = self.multanchor
        A.Myphoto_message_one()
        A.Myphoto_comfirm()
        self.assertIs(A.Test_X025(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����76��˽�Ľ����۵�����������ܼ��')
    def Live_broadcast_room_076(self):
        A = self.multanchor
        A.Supernatant_message_setiing_camera()
        self.assertIs(A.Test_X026(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����77��˽�Ľ��淢��������Ƭ')
    def Live_broadcast_room_077(self):
        A = self.multanchor
        A.Supernatant_message_setiing_photo_confirm()
        A.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(A.Test_X027(), True)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����78��˽�Ľ��淢�ͱ���')
    def Live_broadcast_room_078(self):
        A = self.multanchor
        A.Supernatant_message_face_gif()
        A.Supernatant_message_face_gif_one()
        self.assertIs(A.Test_X030(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����79��˽�Ľ���������')
    def Live_broadcast_room_079(self):
        A = self.multanchor
        A.More_message_people_gift()
        A.Six_party_one_gift()
        A.More_message_people_sendgift()
        time.sleep(1)
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.driver.tap([(528, 528), (529, 529)], 200)
        self.assertIs(A.Test_X031(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����80��Ⱥ�Ľ��淢����ͼƬ')
    def Live_broadcast_room_080(self):
        A = self.multanchor
        A.Supernatant_message_back()
        A.Supernatant_message_group()
        A.Supernatant_message_group_pic()
        A.Supernatant_message_group_pic_photo()
        A.Supernatant_message_setiing_photo_confirm()
        A.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(A.Test_X032(), True)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����81��Ⱥ�Ľ��淢���ͼƬ')
    def Live_broadcast_room_081(self):
        A = self.multanchor
        A.Supernatant_message_group_pic()
        A.Supernatant_message_group_pic_camera()
        time.sleep(2)
        A.Myphoto_one()
        self.assertIs(A.Test_X033(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����82��Ⱥ�Ľ��淢��Ϣ')
    def Live_broadcast_room_082(self):
        A = self.multanchor
        A.Supernatant_message_group_chat()
        A.Supernatant_message_group_chat_send()
        self.assertIs(A.Test_X034(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����83��Ⱥ�Ľ��淢����')
    def Live_broadcast_room_083(self):
        A = self.multanchor
        A.Supernatant_message_face_gif()
        A.Supernatant_message_group_gif_one()
        self.assertIs(A.Test_X035(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����84��Ⱥ�Ľ��淢����')
    def Live_broadcast_room_084(self):
        A = self.multanchor
        A.Supernatant_message_group_voice()
        A.driver.tap([(500, 2010), (510, 2020)], 3000)
        self.assertIs(A.Test_X036(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����85��Ⱥ�Ľ�������')
    def Live_broadcast_room_085(self):
        A = self.multanchor
        A.Supernatant_message_group_upmic()
        self.assertIs(A.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����86��Ⱥ�Ľ��淢���')
    def Live_broadcast_room_086(self):
        A = self.multanchor
        A.Supernatant_message_group_packet()
        A.Supernatant_message_group_packet_number()
        A.Supernatant_message_group_packet_diamond()
        A.Supernatant_message_group_packet_send()
        self.assertIs(A.Test_X038(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����87��Ⱥ�Ľ�������')
    def Live_broadcast_room_087(self):
        A = self.multanchor
        A.Supernatant_message_group_packet_get()
        A.Supernatant_message_group_packet_open()
        self.assertIs(A.Test_X039(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����88��Ⱥ�Ľ�������')
    def Live_broadcast_room_088(self):
        A = self.multanchor
        A.driver.tap([(500, 1950), (501, 1951)], 200)
        A.Supernatant_message_group_gift()
        A.Six_party_one_gift()
        A.Six_party_gift_single()
        A.More_message_people_sendgift()
        A.Confirmation_winning()
        A.driver.tap([(500, 500), (501, 501)], 200)
        self.assertIs(A.Test_X040(), True)

    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('����89��Ⱥ�Ľ������')
    # def Live_broadcast_room_089(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_more()
    #     A.Supernatant_message_group_more_banner()
    #     time.sleep(10)
    #     self.assertIs(A.Test_X041(), True)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����90�����ڸ�����Ϣ�������Թ���')
    def Live_broadcast_room_090(self):
        A = self.multanchor
        A.driver.tap([(500, 500), (501, 501)], 200)
        # A.driver.tap([(500, 500), (501, 501)], 200)
        # A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(A.Test_106(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����91�����ڱ����Ժ�������У��')
    def Live_broadcast_room_091(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_90(), True)
        S.driver.tap([(500, 500), (501, 501)], 200)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����92�����ڸ�����Ϣ����ȡ�����Թ���')
    def Live_broadcast_room_092(self):
        A = self.multanchor
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.Six_party_more_people_list_one()
        self.assertIs(A.Test_X043(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����93�����ڸ�����Ϣ����@���ڹ���')
    def Live_broadcast_room_093(self):
        A = self.multanchor
        A.Six_party_at_anchor()
        A.Room_message_button_send()
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(A.Test_X044(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����94�������������α�λ')
    def Live_broadcast_room_094(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_X139(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����95�������鿴�����б�����������Ϣ')
    def Live_broadcast_room_095(self):
        A = self.multanchor
        A.Six_party_invite()
        self.assertIs(A.Test_X95(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����96������ɾ��������Ϣ')
    def Live_broadcast_room_096(self):
        A = self.multanchor
        A.Six_party_invite_list_one_refuse()
        self.assertIs(A.Test_X96(), True)
        time.sleep(1)
        A.driver.tap([(200, 420), (201, 421)], 200)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����97�������������α�λ')
    def Live_broadcast_room_097(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_X139(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����98������ͬ�������������')
    def Live_broadcast_room_098(self):
        A = self.multanchor
        A.Six_party_invite()
        A.Six_party_agree_list_one()
        A.driver.tap([(200, 420), (201, 421)], 200)
        time.sleep(1)
        self.assertIs(A.Test_45(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����99��ֱ�����й����뿪�α�λ')
    def Live_broadcast_room_099(self):
        S = self.multspectator
        A = self.multanchor
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()
        self.assertIs(A.Test_99(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����100�����������������')
    def Live_broadcast_room_100(self):
        A = self.multanchor
        S = self.multspectator
        A.Six_party_invite()
        A.Six_party_invite_list_one()
        time.sleep(1)
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(S.Test_X100(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����101������ͬ������')
    def Live_broadcast_room_101(self):
        S = self.multspectator
        S.Six_party_agree_invite()
        self.assertIs(S.Test_101(), True)
        #��������
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����102�����ھܾ�����')
    def Live_broadcast_room_102(self):
        A = self.multanchor
        S = self.multspectator
        A.Six_party_invite()
        A.Six_party_invite_list_one()
        A.driver.tap([(200, 420), (201, 421)], 200)
        S.Six_party_down_invite()
        S.More_Setting()
        self.assertIs(S.Test_102(), True)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����103������������Ϣ�������ѡ��')
    def Live_broadcast_room_103(self):
        A = self.multanchor
        S = self.multspectator
        S.More_join()
        S.Six_party_twice_apply()
        A.Six_party_invite()
        A.Six_party_agree_list_one()
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.Six_party_one_position()
        A.Six_party_anchor_floating_emo()
        self.assertIs(A.Test_103(), True)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����104�������鿴�α���Ϣ����')
    def Live_broadcast_room_104(self):
        A = self.multanchor
        A.Six_party_two_position()
        self.assertIs(A.Test_X017(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����105�������Ƴ��α�')
    def Live_broadcast_room_105(self):
        A = self.multanchor
        A.Supernatant_remove()
        self.assertIs(A.Test_105(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����106���������Լα�')
    def Live_broadcast_room_106(self):
        A = self.multanchor
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(A.Test_106(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����107��У��α��Ƿ��Ƴ���λ')
    def Live_broadcast_room_107(self):
        A = self.multanchor
        A.Six_party_two_position()
        self.assertIs(A.Test_99(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����108��ֱ���侯����Ϣ���')
    def Live_broadcast_room_108(self):
        A = self.multanchor
        A.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(A.Test_X059(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����109��ֱ���������˷���')
    def Live_broadcast_room_109(self):
        A = self.multanchor
        A.Six_party_room_message_button()
        A.Six_party_room_message()
        A.Six_party_room_message_send()
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(A.Test_109(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����110��ֱ������Ϣ���ϻ���Ϣ')
    def Live_broadcast_room_110(self):
        A = self.multanchor
        A.driver.swipe(363, 1478,  363, 2040)
        self.assertIs(A.Test_X062(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����111��ֱ������Ϣ���»���Ϣ')
    def Live_broadcast_room_111(self):
        A = self.multanchor
        A.driver.swipe(363, 2040, 363, 1478)
        self.assertIs(A.Test_X063(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����112��������ֱ�����и��Լ�����')
    def Live_broadcast_room_112(self):
        A = self.multanchor
        A.Six_party_gift()
        self.assertIs(A.Test_X070(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����113��ֱ�����е������bannerҳ')
    def Live_broadcast_room_113(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.Room_banner()
        time.sleep(5)
        self.assertIs(A.Test_X072(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����114��ֱ�����б���ѡ��')
    def Live_broadcast_room_114(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_background()
        time.sleep(1)
        A.driver.swipe(900, 2000, 100, 2000)
        time.sleep(2)
        self.assertIs(A.Test_X073(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����115������ֱ���䱳��')
    def Live_broadcast_room_115(self):
        A = self.multanchor
        A.driver.swipe(100, 2000, 900, 2000)
        A.More_Setting_background_Lv20()
        time.sleep(2)
        self.assertIs(A.Test_X074(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����116��ֱ�����д���Ϣ�б�')
    def Live_broadcast_room_116(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Message()
        self.assertIs(A.Test_X075(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����117��ֱ�����н��г�ֵ')
    def Live_broadcast_room_117(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_top_up()
        time.sleep(2)
        A.More_top_up_4500()
        time.sleep(5)
        A.More_top_up_pay()
        time.sleep(5)
        self.assertIs(A.Test_X078(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����118��ֱ�����йر���˷�')
    def Live_broadcast_room_118(self):
        A = self.multanchor
        A.More_top_up_confirm()
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_switch_microphone()
        A.More_setting_switch_microphone()
        self.assertIs(A.Test_X079(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����119��ֱ������������ֽ')
    def Live_broadcast_room_119(self):
        A = self.multanchor
        A.More_setting_sticker()
        A.More_setting_sticker_1()
        time.sleep(5)
        self.assertIs(A.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����120��ֱ�����п�������')
    def Live_broadcast_room_120(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_beauty()
        A.More_setting_beauty_reset()
        A.More_setting_beauty_confirmreset()
        self.assertIs(A.Test_X081(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����121��ֱ�����п�������ģʽ')
    def Live_broadcast_room_121(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_turn_off_camera()
        A.More_setting_mirror_mode()
        self.assertIs(A.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����122��ֱ�����йر�����ͷ')
    def Live_broadcast_room_122(self):
        A = self.multanchor
        A.More_setting_turn_off_camera()
        A.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(A.Test_X083(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����123��ֱ�������л�����ͷ')
    def Live_broadcast_room_123(self):
        A = self.multanchor
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_turn_off_camera()
        A.More_setting_switch_camera()
        A.More_setting_switch_camera()
        self.assertIs(A.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����124���ر�ֱ����������ҳ')
    def Live_broadcast_room_124(self):
        A = self.multanchor
        A.driver.tap([(213, 213), (214, 214)], 200)
        A.Close_six_party()
        A.Close_six_party_two_confirm()
        self.assertIs(A.Test_X085(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����125�������������ҳУ��')
    def Live_broadcast_room_125(self):
        A = self.multanchor
        self.assertIs(A.Test_X163(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����126�����ڽ������ҳУ��')
    def Live_broadcast_room_126(self):
        S = self.multspectator
        self.assertIs(S.Test_X163(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����127����������ҳ��ʾ����')
    def Live_broadcast_room_127(self):
        A = self.multanchor
        self.assertIs(A.Test_X087(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����128�������ڽ���ҳ���������ҳ')
    def Live_broadcast_room_128(self):
        A = self.multanchor
        A.Six_party_endpage_profile()
        self.assertIs(A.Test_X086(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����129�������ڽ���ҳ��������ֱ����')
    def Live_broadcast_room_129(self):
        A = self.multanchor
        A.Homepage_back()
        A.End_party_two()
        self.assertIs(A.Test_129(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����130�������Զ���ת����ֱ����У��')
    def Live_broadcast_room_130(self):
        S = self.multspectator
        self.assertIs(S.Test_129(), True)




    if __name__ == '__main__':
        pytest.main()
