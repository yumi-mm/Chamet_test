# coding=gb2312
import time
from Six_party.common.myunittest import StartEnd
import allure
import unittest
import pytest

@allure.epic("��Ŀ���ƣ�6�˽��ѷ�")
@allure.issue("BUG���ӣ�http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("�����������ӣ�http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('���ѷ�6�˷�_˫�˽���')


class Test_six_party_interaction(StartEnd):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    csv_file = '../data/account.csv'
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����1�������������ѷ�ҳ��')
    def test_Six_Party_001(self):
        A = self.multanchor
        A.Tab_party()
        A.Setup_party()
        self.assertIs(A.Test_X001(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����2�������л���6�˽��ѷ�ģʽ')
    def test_Six_Party_002(self):
        A = self.multanchor
        A.Setup_six_party()
        self.assertIs(A.Test_X002(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����3���������չ���У��')
    def test_Six_Party_003(self):
        A = self.multanchor
        A.Setup_beauty()
        A.More_setting_beauty_reset()
        A.More_setting_beauty_confirmreset()
        self.assertIs(A.Test_X003(), True)
        A.driver.tap([(528, 528), (529, 529)], 200)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����4������ʹ����ֽ����')
    def test_Six_Party_004(self):
        A = self.multanchor
        A.Setup_sticker()
        A.Sticker_download()
        time.sleep(5)
        self.assertIs(A.Sticker_downloading(), True)
        A.driver.tap([(528, 528), (529, 529)], 200)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����5�������ɹ�����6�˽��ѷ�')
    def test_Six_Party_005(self):
        A = self.multanchor
        A.Two_Setup()
        self.assertIs(A.Test_X005(), True)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����6�����ڽ��ѷ�ҳǩ������ʾ')
    def test_Six_Party_006(self):
        S = self.multspectator
        S.driver.tap([(734, 2211), (735, 2212)], 200)
        S.Tab_party()
        S.driver.swipe(600, 1800, 600, 800)
        S.driver.swipe(600, 800, 600, 1800)
        S.driver.swipe(600, 800, 600, 1800)
        self.assertIs(S.Test_X089(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����7�����ڴӽ��ѷ�ҳǩ���뽻�ѷ�')
    def test_Six_Party_007(self):
        S = self.multspectator
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X090(), True)
        S.Close_six_party()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����8�����ڴ���Ⱥ�ĳ���,����Ⱥ�Ľ����������ѷ�')
    def test_Six_Party_008(self):
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
        self.assertIs(S.Test_8(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����9�������鿴���ڽ��뽻�ѷ�����Чչʾ')
    def test_Six_Party_009(self):
        A = self.multanchor
        self.assertIs(A.Test_X066(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����10�������鿴���ڽ��뽻�ѷ���Ϣ����ʾ')
    def test_Six_Party_010(self):
        A = self.multanchor
        time.sleep(3)
        self.assertIs(A.Test_X067(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����11���������ѷ�������Ϣ���')
    def test_Six_Party_011(self):
        A = self.multanchor
        A.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(A.Test_X059(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����12�����ѷ��ó�����Ϊ0�����ڲ鿴��������')
    def test_Six_Party_012(self):
        S = self.multspectator
        self.assertIs(S.Test_X133(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����13�������ڽ��ѷ�������ʱ����')
    def test_Six_Party_013(self):
        S = self.multspectator
        A = self.multanchor
        S.Six_party_gift()
        time.sleep(1)
        S.Six_party_four_gift()
        S.More_message_people_sendgift()
        self.assertIs(A.Test_X13(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����14�������ڽ��ѷ��е������ͷ��')
    def test_Six_Party_014(self):
        S = self.multspectator
        S.driver.tap([(213, 213), (214, 214)], 200)
        time.sleep(2)
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Six_party_anchor_head()
        self.assertIs(S.Test_X091(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����15�������ڽ��ѷ��й�ע����')
    def test_Six_Party_015(self):
        S = self.multspectator
        S.Six_party_follow_anchor()
        self.assertIs(S.Test_X092(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����16����Ϣ�����оٱ�����У��')
    def test_Six_Party_016(self):
        S = self.multspectator
        S.Six_party_report_anchor()
        self.assertIs(S.Test_X093(), True)
        S.driver.tap([(213, 213), (214, 214)], 200)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����17�������ڽ��ѷ���ͨ������������ҳ����������������')
    def test_Six_Party_017(self):
        S = self.multspectator
        A = self.multanchor
        S.Six_party_anchor_head()
        S.Six_party_supernatant_gift()
        S.Six_party_one_gift()
        S.Six_party_gift_single()
        S.More_message_people_sendgift()
        self.assertIs(A.Test_X16(), True)
        S.driver.tap([(213, 213), (214, 214)], 200)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����18�����ѷ��ó�����Ϊ0�����ڲ鿴��������')
    def test_Six_Party_018(self):
        S = self.multspectator
        self.assertIs(S.Test_X135(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����19�������ڽ��ѷ��и�����������Ƶͨ��')
    def test_Six_Party_019(self):
        A = self.multanchor
        S = self.multspectator
        S.Six_party_anchor_head()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_56(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����20�������ڽ��ѷ�@����')
    def test_Six_Party_020(self):
        A = self.multanchor
        S = self.multspectator
        time.sleep(5)
        S.Six_party_at_anchor()
        S.Six_party_room_message_send()
        S.driver.tap([(552, 189), (553, 190)], 200)
        self.assertIs(A.Test_X096(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����21�����ڴ�����������ҳ���뽻�ѷ�')
    def test_Six_Party_021(self):
        S = self.multspectator
        S.Six_party_anchor_head()
        S.Six_party_supernatant_anchor_head()
        time.sleep(2)
        S.Homepage_video()
        self.assertIs(S.Test_X097(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����22�����ڽ��뽻�ѷ���Ϣ����ʾ')
    def test_Six_Party_022(self):
        S = self.multspectator
        time.sleep(3)
        self.assertIs(S.Test_X102(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����23�����ѷ��й��ڴ򿪹����б�')
    def test_Six_Party_023(self):
        S = self.multspectator
        S.Six_party_more_people()
        self.assertIs(S.Test_X098(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����24�����ѷ��й������»��������б�')
    def test_Six_Party_024(self):
        S = self.multspectator
        S.driver.swipe(837, 410, 837, 1800)
        S.driver.swipe(837, 1800, 837, 410)
        self.assertIs(S.Test_X098(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����25�����ѷ��й��ڵ���鿴����ͷ��')
    def test_Six_Party_025(self):
        S = self.multspectator
        S.Six_party_more_people_list_one()
        self.assertIs(S.Test_X101(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����26�����ѷ�������Ϣ���')
    def test_Six_Party_026(self):
        S = self.multspectator
        S.driver.tap([(200, 189), (201, 190)], 200)
        time.sleep(1)
        S.driver.tap([(200, 189), (201, 190)], 200)
        self.assertIs(S.Test_X116(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����27�����ѷ����ڶ˶˷���')
    def test_Six_Party_027(self):
        S = self.multspectator
        S.Six_party_room_message_button()
        S.Six_party_room_message()
        S.Six_party_room_message_send()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X117(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����28�����ѷ���Ϣ����Ϣ����')
    def test_Six_Party_028(self):
        S = self.multspectator
        S.Six_party_gift()
        S.Six_party_one_gift()
        S.Six_party_gift_single()
        S.More_message_people_sendgift()
        S.Confirmation_winning()
        S.More_message_people_sendgift()
        S.Confirmation_winning()
        S.More_message_people_sendgift()
        S.Confirmation_winning()
        S.More_message_people_sendgift()
        S.Confirmation_winning()
        S.More_message_people_sendgift()
        S.Confirmation_winning()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(S.Test_X118(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����29�����ѷ���Ϣ���ϻ���Ϣ')
    def test_Six_Party_029(self):
        S = self.multspectator
        S.driver.swipe(357, 1519, 357, 2030)
        self.assertIs(S.Test_X119(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����30�������ڽ��ѷ��д����񸡴�')
    def test_Six_Party_030(self):
        S = self.multspectator
        S.Six_party_gift()
        time.sleep(1)
        self.assertIs(S.Test_X128(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����31�������ڽ��ѷ��и�����������')
    def test_Six_Party_031(self):
        S = self.multspectator
        A = self.multanchor
        S.Six_party_send_all_gift()
        S.Six_party_one_gift()
        S.Six_party_gift_single()
        S.Six_party_send_gift()
        S.driver.tap([(200, 201), (201, 202)], 200)
        self.assertIs(A.Test_X13(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����32�������ڽ��ѷ�������ʱ����')
    def test_Six_Party_032(self):
        S = self.multspectator
        S.Six_party_gift()
        S.Six_party_send_all_gift()
        S.Six_party_four_gift()
        S.More_message_people_sendgift()
        self.assertIs(S.Test_32(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����33�����ѷ��е������bannerҳ')
    def test_Six_Party_033(self):
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
    @allure.title('����34�����ѷ��й��ڵ�����밴ť')
    def test_Six_Party_034(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        self.assertIs(S.Test_X138(), True)
        S.Six_party_twice_apply()
        S.check_perBtn()
        S.check_perBtn()
        S.check_perBtn()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����35�����ѷ��й��ڴ���Ϣ�б�')
    def test_Six_Party_035(self):
        S = self.multspectator
        S.More_Setting()
        S.More_Message()
        self.assertIs(S.Test_X137(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����36��Ⱥ�Ľ��淢����ͼƬ')
    def test_Six_Party_036(self):
        S = self.multspectator
        S.Supernatant_message_group()
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_photo()
        S.Supernatant_message_setiing_photo_confirm()
        S.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(S.Test_X032(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����37��Ⱥ�Ľ��淢���ͼƬ')
    def test_Six_Party_037(self):
        S = self.multspectator
        S.Supernatant_message_group_pic()
        S.Supernatant_message_group_pic_camera()
        time.sleep(2)
        S.Myphoto_one()
        self.assertIs(S.Test_X140(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����38��Ⱥ�Ľ��淢��Ϣ')
    def test_Six_Party_038(self):
        S = self.multspectator
        S.Supernatant_message_group_chat()
        S.Supernatant_message_group_chat_send()
        self.assertIs(S.Test_X034(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����39��Ⱥ�Ľ��淢����')
    def test_Six_Party_039(self):
        S = self.multspectator
        S.Supernatant_message_face_gif()
        S.Supernatant_message_group_gif_one()
        self.assertIs(S.Test_X035(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����40��Ⱥ�Ľ��淢����')
    def test_Six_Party_040(self):
        S = self.multspectator
        S.Supernatant_message_group_voice()
        S.driver.tap([(500, 2010), (510, 2020)], 3000)
        self.assertIs(S.Test_X036(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����41��Ⱥ�Ľ�������')
    def test_Six_Party_041(self):
        S = self.multspectator
        S.Supernatant_message_group_upmic()
        self.assertIs(S.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����42��Ⱥ�Ľ��淢���')
    def test_Six_Party_042(self):
        S = self.multspectator
        S.Supernatant_message_group_packet()
        S.Supernatant_message_group_packet_number()
        S.Supernatant_message_group_packet_diamond()
        S.Supernatant_message_group_packet_send()
        self.assertIs(S.Test_X038(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����43��Ⱥ�Ľ�������')
    def test_Six_Party_043(self):
        S = self.multspectator
        S.Supernatant_message_group_gift()
        S.Six_party_one_gift()
        S.Six_party_gift_single()
        S.More_message_people_sendgift()
        S.driver.tap([(500, 500), (501, 501)], 200)
        self.assertIs(S.Test_X040(), True)

    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('����44��Ⱥ�Ľ������')
    # def test_Six_Party_044(self):
    #     S = self.multspectator
    #     S.Supernatant_message_group_more()
    #     S.driver.tap([(864, 974), (865, 975)], 200)
    #     time.sleep(10)
    #     self.assertIs(S.Test_X041(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����45�����ѷ��н��г�ֵ')
    def test_Six_Party_045(self):
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
    def test_Six_Party_046(self):
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
    def test_Six_Party_047(self):
        S = self.multspectator
        A = self.multanchor
        A.Six_party_invite()
        A.Six_party_agree_list_one()
        A.driver.tap([(200, 420), (201, 421)], 200)
        time.sleep(1)
        self.assertIs(A.Test_45(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����48�����ѷ��йر���˷�')
    def test_Six_Party_048(self):
        S = self.multspectator
        time.sleep(5)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_switch_microphone()
        S.More_setting_switch_microphone()
        self.assertIs(S.Test_X079(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����49�����ѷ���������ֽ')
    def test_Six_Party_049(self):
        S = self.multspectator
        S.More_setting_sticker()
        S.More_setting_sticker_1()
        time.sleep(6)
        S.More_setting_sticker_1()
        self.assertIs(S.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����50�����ѷ��п�������')
    def test_Six_Party_050(self):
        S = self.multspectator
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_beauty()
        S.More_setting_beauty_reset()
        S.More_setting_beauty_confirmreset()
        self.assertIs(S.Test_X081(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����51�����ѷ��п�������ģʽ')
    def test_Six_Party_051(self):
        S = self.multspectator
        S.driver.tap([(200, 420), (201, 421)], 200)
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_mirror_mode()
        self.assertIs(S.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����52�����ѷ��йر�����ͷ')
    def test_Six_Party_052(self):
        S = self.multspectator
        S.More_setting_turn_off_camera()
        S.More_setting_turn_off_camera()
        S.More_setting_turn_off_camera()
        S.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(S.Test_X155(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����53�����ѷ����л�����ͷ')
    def test_Six_Party_053(self):
        S = self.multspectator
        S.More_Setting()
        S.More_Setting_setting()
        S.More_setting_turn_off_camera()
        S.More_setting_switch_camera()
        S.More_setting_switch_camera()
        self.assertIs(S.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����54�����ѷ��й��ڵ���뿪�α�λ')
    def test_Six_Party_054(self):
        S = self.multspectator
        S.Six_party_off_mic()
        self.assertIs(S.Test_X157(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����55�����ѷ��й���ȡ���뿪�α�λ')
    def test_Six_Party_055(self):
        S = self.multspectator
        S.Close_six_party_two_cancle()
        self.assertIs(S.Test_X158(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����56�����ѷ��й���ȷ���뿪�α�λ')
    def test_Six_Party_056(self):
        S = self.multspectator
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X159(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����57�����ѷ��й��ڸ���������Լ��')
    def test_Six_Party_057(self):
        S = self.multspectator
        S.Six_party_anchor()
        S.Six_party_call_anchor()
        self.assertIs(S.Test_56(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����58�������뿪���ѷ�')
    def test_Six_Party_058(self):
        S = self.multspectator
        S.driver.tap([(213, 213), (214, 214)], 200)
        S.Close_six_party()
        self.assertIs(S.Test_X162(), True)
        S.Tab_group()
        S.Tab_group_group()
        S.My_group()
        S.My_group_one()
        S.Group_more()
        S.Group_more_two_people()
        S.Six_party_supernatant_anchor_head()
        S.Homepage_video()


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����59����������Ϣ����������û���')
    def test_Six_Party_059(self):
        A = self.multanchor
        A.Six_message_inuser()
        self.assertIs(A.Test_X068(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����60�������򿪹����б�')
    def test_Six_Party_060(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Six_party_more_people()
        self.assertIs(A.Test_X006(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����61�������ڹ����б����»���')
    def test_Six_Party_061(self):
        A = self.multanchor
        A.driver.swipe(700, 700, 700, 1800)
        time.sleep(1)
        A.driver.swipe(700, 1800, 700, 700)
        self.assertIs(A.Test_X007(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����62�������ڹ����б�ͷ�����鿴')
    def test_Six_Party_062(self):
        A = self.multanchor
        A.Six_party_more_people_list_one()
        self.assertIs(A.Test_X017(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����63�������ڹ��ڸ�����Ϣ�����ٱ����')
    def test_Six_Party_063(self):
        A = self.multanchor
        A.Six_party_report_anchor()
        self.assertIs(A.Test_X010(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����64�������ڹ��ڸ�����Ϣ���������������ҳ')
    def test_Six_Party_064(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Six_party_more_people_list_one()
        A.Six_party_supernatant_anchor_head()
        self.assertIs(A.Test_X011(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����65������İ���˸�����Ϣ������ע��ť���')
    def test_Six_Party_065(self):
        A = self.multanchor
        A.Homepage_back()
        A.Six_party_more_people_list_one()
        self.assertIs(A.Test_X012(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����66�������ڹ��ڸ�����Ϣ���������﹦����֤')
    def test_Six_Party_066(self):
        A = self.multanchor
        A.Six_party_supernatant_gift()
        self.assertIs(A.Test_X105(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����67�������ڹ��ڸ�����Ϣ������������')
    def test_Six_Party_067(self):
        A = self.multanchor
        A.Six_party_one_gift()
        A.Six_party_gift_single()
        A.More_message_people_sendgift()
        A.Confirmation_winning()
        A.driver.tap([(200, 400), (201, 401)], 200)
        A.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(A.Test_31(), True)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����68�����������ڸ�����Ϣ������Ϣ��ť')
    def test_Six_Party_068(self):
        A = self.multanchor
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_message()
        self.assertIs(A.Test_X015(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����69��˽�Ľ�����ఴť�ļ��')
    def test_Six_Party_069(self):
        A = self.multanchor
        A.Supernatant_message_more()
        self.assertIs(A.Test_X017(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����70��˽�Ľ����˳���ť���')
    def test_Six_Party_070(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Supernatant_message_back()
        self.assertIs(A.Test_X016(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����71�������ڸ�����Ϣ����--��Ƶͨ��')
    def test_Six_Party_071(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Six_party_more_people_list_one()
        A.Supernatant_message()
        A.Supernatant_message_more()
        A.Six_party_call_anchor()
        self.assertIs(A.Test_X015(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����72��˽�Ľ����۵���ť������')
    def test_Six_Party_072(self):
        A = self.multanchor
        A.Supernatant_message_setiing()
        self.assertIs(A.Test_X021(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����73��˽�Ľ����۵������밴ť������')
    def test_Six_Party_073(self):
        A = self.multanchor
        A.Supernatant_message_setiing_translate()
        self.assertIs(A.Test_X022(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����74��˽�Ľ����۵�������Ṧ�ܼ��')
    def test_Six_Party_074(self):
        A = self.multanchor
        A.Supernatant_message_setiing_photo()
        self.assertIs(A.Test_X024(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����75��˽�Ľ��淢�����')
    def test_Six_Party_075(self):
        A = self.multanchor
        A.Myphoto_message_one()
        A.Myphoto_comfirm()
        self.assertIs(A.Test_X025(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����76��˽�Ľ����۵�����������ܼ��')
    def test_Six_Party_076(self):
        A = self.multanchor
        A.Supernatant_message_setiing_camera()
        self.assertIs(A.Test_X026(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����77��˽�Ľ��淢��������Ƭ')
    def test_Six_Party_077(self):
        A = self.multanchor
        A.Supernatant_message_setiing_photo_confirm()
        A.Supernatant_message_setiing_photo_twoconfirm()
        self.assertIs(A.Test_X027(), True)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����78��˽�Ľ��淢�ͱ���')
    def test_Six_Party_078(self):
        A = self.multanchor
        A.Supernatant_message_face_gif()
        A.Supernatant_message_face_gif_one()
        self.assertIs(A.Test_X030(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����79��˽�Ľ���������')
    def test_Six_Party_079(self):
        A = self.multanchor
        A.More_message_people_gift()
        A.six_party_one_gift()
        A.More_message_people_sendgift()
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.driver.tap([(528, 528), (529, 529)], 200)
        self.assertIs(A.Test_X031(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����80��Ⱥ�Ľ��淢����ͼƬ')
    def test_Six_Party_080(self):
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
    def test_Six_Party_081(self):
        A = self.multanchor
        A.Supernatant_message_group_pic()
        A.Supernatant_message_group_pic_camera()
        time.sleep(2)
        A.Myphoto_one()
        self.assertIs(A.Test_X033(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����82��Ⱥ�Ľ��淢��Ϣ')
    def test_Six_Party_082(self):
        A = self.multanchor
        A.Supernatant_message_group_chat()
        A.Supernatant_message_group_chat_send()
        self.assertIs(A.Test_X034(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����83��Ⱥ�Ľ��淢����')
    def test_Six_Party_083(self):
        A = self.multanchor
        A.Supernatant_message_face_gif()
        A.Supernatant_message_group_gif_one()
        self.assertIs(A.Test_X035(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����84��Ⱥ�Ľ��淢����')
    def test_Six_Party_084(self):
        A = self.multanchor
        A.Supernatant_message_group_voice()
        A.driver.tap([(500, 2010), (510, 2020)], 3000)
        self.assertIs(A.Test_X036(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����85��Ⱥ�Ľ�������')
    def test_Six_Party_085(self):
        A = self.multanchor
        A.Supernatant_message_group_upmic()
        self.assertIs(A.Test_X037(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����86��Ⱥ�Ľ��淢���')
    def test_Six_Party_086(self):
        A = self.multanchor
        A.Supernatant_message_group_packet()
        A.Supernatant_message_group_packet_number()
        A.Supernatant_message_group_packet_diamond()
        A.Supernatant_message_group_packet_send()
        self.assertIs(A.Test_X038(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����87��Ⱥ�Ľ�������')
    def test_Six_Party_087(self):
        A = self.multanchor
        A.Supernatant_message_group_packet_get()
        A.Supernatant_message_group_packet_open()
        self.assertIs(A.Test_X039(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����88��Ⱥ�Ľ�������')
    def test_Six_Party_088(self):
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
    # def test_Six_Party_089(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_more()
    #     A.Supernatant_message_group_more_banner()
    #     time.sleep(10)
    #     self.assertIs(A.Test_X041(), True)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����90�����ڸ�����Ϣ�������Թ���')
    def test_Six_Party_090(self):
        A = self.multanchor
        A.driver.tap([(500, 500), (501, 501)], 200)
        # A.driver.tap([(500, 500), (501, 501)], 200)
        # A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(A.Test_X042(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����91�����ڱ����Ժ�������У��')
    def test_Six_Party_091(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_90(), True)
        S.driver.tap([(500, 500), (501, 501)], 200)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����92�����ڸ�����Ϣ����ȡ�����Թ���')
    def test_Six_Party_092(self):
        A = self.multanchor
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.Six_party_more_people_list_one()
        self.assertIs(A.Test_X043(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����93�����ڸ�����Ϣ����@���ڹ���')
    def test_Six_Party_093(self):
        A = self.multanchor
        A.Six_party_at_anchor()
        A.Room_message_button_send()
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(A.Test_X044(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����94�������������α�λ')
    def test_Six_Party_094(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_X139(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����95�������鿴�����б�����������Ϣ')
    def test_Six_Party_095(self):
        A = self.multanchor
        A.Six_party_invite()
        self.assertIs(A.Test_X95(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����96������ɾ��������Ϣ')
    def test_Six_Party_096(self):
        A = self.multanchor
        A.Six_party_invite_list_one_refuse()
        self.assertIs(A.Test_X96(), True)
        time.sleep(1)
        A.driver.tap([(200, 420), (201, 421)], 200)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����97�������������α�λ')
    def test_Six_Party_097(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_X139(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����98������ͬ�������������')
    def test_Six_Party_098(self):
        A = self.multanchor
        A.Six_party_invite()
        A.Six_party_agree_list_one()
        A.driver.tap([(200, 420), (201, 421)], 200)
        time.sleep(1)
        self.assertIs(A.Test_45(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����99�����ѷ��й����뿪�α�λ')
    def test_Six_Party_099(self):
        S = self.multspectator
        A = self.multanchor
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()
        self.assertIs(A.Test_99(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����100�����������������')
    def test_Six_Party_100(self):
        A = self.multanchor
        S = self.multspectator
        A.Six_party_invite()
        A.Six_party_invite_list_one()
        time.sleep(1)
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(S.Test_X100(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����101������ͬ������')
    def test_Six_Party_101(self):
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
    def test_Six_Party_102(self):
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
    def test_Six_Party_103(self):
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
    def test_Six_Party_104(self):
        A = self.multanchor
        A.Six_party_two_position()
        self.assertIs(A.Test_X017(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����105�������Ƴ��α�')
    def test_Six_Party_105(self):
        A = self.multanchor
        A.Supernatant_remove()
        self.assertIs(A.Test_105(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����106���������Լα�')
    def test_Six_Party_106(self):
        A = self.multanchor
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(A.Test_106(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����107��У��α��Ƿ��Ƴ���λ')
    def test_Six_Party_107(self):
        A = self.multanchor
        A.Six_party_two_position()
        self.assertIs(A.Test_99(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����108�����ѷ�������Ϣ���')
    def test_Six_Party_108(self):
        A = self.multanchor
        A.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(A.Test_X059(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����109�����ѷ������˷���')
    def test_Six_Party_109(self):
        A = self.multanchor
        A.Room_message_button()
        A.Room_message_button_input()
        A.Room_message_button_send()
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(A.Test_109(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����110�����ѷ���Ϣ���ϻ���Ϣ')
    def test_Six_Party_110(self):
        A = self.multanchor
        A.driver.swipe(363, 1478,  363, 2040)
        self.assertIs(A.Test_X062(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����111�����ѷ���Ϣ���»���Ϣ')
    def test_Six_Party_111(self):
        A = self.multanchor
        A.driver.swipe(363, 2040, 363, 1478)
        self.assertIs(A.Test_X063(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('����112�������ڽ��ѷ��и��Լ�����')
    def test_Six_Party_112(self):
        A = self.multanchor
        A.Six_party_gift()
        self.assertIs(A.Test_X070(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����113�����ѷ��е������bannerҳ')
    def test_Six_Party_113(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.Room_banner()
        time.sleep(5)
        self.assertIs(A.Test_X072(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����114�����ѷ��б���ѡ��')
    def test_Six_Party_114(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_background()
        time.sleep(1)
        A.driver.swipe(900, 2000, 100, 2000)
        time.sleep(2)
        self.assertIs(A.Test_X073(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����115���������ѷ�����')
    def test_Six_Party_115(self):
        A = self.multanchor
        A.driver.swipe(100, 2000, 900, 2000)
        A.More_Setting_background_Lv20()
        time.sleep(2)
        self.assertIs(A.Test_X074(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����116�����ѷ��д���Ϣ�б�')
    def test_Six_Party_116(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Message()
        self.assertIs(A.Test_X075(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����117�����ѷ��н��г�ֵ')
    def test_Six_Party_117(self):
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
    @allure.title('����118�����ѷ��йر���˷�')
    def test_Six_Party_118(self):
        A = self.multanchor
        A.More_top_up_confirm()
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_switch_microphone()
        A.More_setting_switch_microphone()
        self.assertIs(A.Test_X079(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����119�����ѷ���������ֽ')
    def test_Six_Party_119(self):
        A = self.multanchor
        A.More_setting_sticker()
        A.More_setting_sticker_1()
        time.sleep(5)
        self.assertIs(A.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����120�����ѷ��п�������')
    def test_Six_Party_120(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_beauty()
        A.More_setting_beauty_reset()
        A.More_setting_beauty_confirmreset()
        self.assertIs(A.Test_X081(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����121�����ѷ��п�������ģʽ')
    def test_Six_Party_121(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_turn_off_camera()
        A.More_setting_mirror_mode()
        self.assertIs(A.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����122�����ѷ��йر�����ͷ')
    def test_Six_Party_122(self):
        A = self.multanchor
        A.More_setting_turn_off_camera()
        A.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(A.Test_X083(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����123�����ѷ����л�����ͷ')
    def test_Six_Party_123(self):
        A = self.multanchor
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_turn_off_camera()
        A.More_setting_switch_camera()
        A.More_setting_switch_camera()
        self.assertIs(A.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����124���رս��ѷ��������ҳ')
    def test_Six_Party_124(self):
        A = self.multanchor
        A.driver.tap([(213, 213), (214, 214)], 200)
        A.Close_six_party()
        A.Close_six_party_two_confirm()
        self.assertIs(A.Test_X085(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����125�����ڽ������ҳУ��')
    def test_Six_Party_125(self):
        S = self.multspectator
        self.assertIs(S.Test_X163(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����126�����ڽ���ҳУ��-���������ҳ')
    def test_Six_Party_126(self):
        S = self.multspectator
        S.Six_party_endpage_profile()
        self.assertIs(S.Test_X011(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����127������ҳУ��-����ҳ����')
    def test_Six_Party_127(self):
        S = self.multspectator
        self.assertIs(S.Test_X165(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����128������ҳУ��-����ҳ�ɶ�ʱ��/����')
    def test_Six_Party_128(self):
        S = self.multspectator
        self.assertIs(S.Test_X166(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����129����������ҳ��ʾ����')
    def test_Six_Party_129(self):
        A = self.multanchor
        self.assertIs(A.Test_X087(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����130������ҳ��������������ҳ')
    def test_Six_Party_130(self):
        A = self.multanchor
        A.Six_party_endpage_profile()
        self.assertIs(A.Test_X086(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('����130������ҳ��������������ҳ')
    def test_Six_Party_130(self):
        A = self.multanchor
        A.Six_party_endpage_profile()
        self.assertIs(A.Test_X086(), True)

    if __name__ == '__main__':
        pytest.main()
