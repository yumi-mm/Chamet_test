import time
from Six_party.common.myunittest import StartEnd
from Six_party.businessView.six_party_spectator import Six_partyView_spectator
from Six_party.businessView.six_party_anchor import Six_partyView_anchor
from Six_party.businessView.login_phoneView import LoginView
import allure
import pytest

@allure.epic("项目名称：6人交友房")
@allure.issue("BUG链接：http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("测试用例链接：http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('交友房6人房_双端交互')


class Test_six_party_interaction(StartEnd):
    csv_file = '../data/account.csv'

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例1：主播创建交友房页面')
    def test_Six_Party_001(self):
        A = self.multanchor
        A.Tab_party()
        A.Setup_party()
        self.assertIs(A.Test_X001(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例2：主播切换到6人交友房模式')
    def test_Six_Party_002(self):
        A = self.multanchor
        A.Setup_six_party()
        self.assertIs(A.Test_X002(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例3：主播使用美颜功能')
    # def test_Six_Party_003(self):
    #     A = self.multanchor
    #     A.Setup_beauty()
    #     self.assertIs(A.Test_X003(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例4：主播使用贴纸功能')
    # def test_Six_Party_004(self):
    #     A = self.multanchor
    #     A.driver.tap([(528, 528), (529, 529)], 200)
    #     A.Setup_sticker()
    #     A.Sticker_download()
    #     self.assertIs(A.Sticker_downloading(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例5：主播成功创建6人交友房')
    def test_Six_Party_005(self):
        A = self.multanchor
        A.driver.tap([(528, 528), (529, 529)], 200)
        A.Two_Setup()
        self.assertIs(A.Test_X005(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例6：观众创建群聊场景')
    # def test_Six_Party_006(self):
    #     S = self.multspectator
    #     S.Tab_group()
    #     S.Tab_group_group()
    #     S.My_group()
    #     S.My_group_one()
    #     S.Supernatant_message_face_gif()
    #     S.Supernatant_message_face_gif_one()
    #     S.Supernatant_message_back()
    #     S.My_group_back()
    #     self.assertIs(S.Test_6(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例7：观众交友房页签房间显示')
    def test_Six_Party_007(self):
        S = self.multspectator
        S.Tab_party()
        S.driver.swipe(600, 1800, 600, 800)
        S.driver.swipe(600, 800, 600, 1800)
        S.driver.swipe(600, 800, 600, 1800)
        self.assertIs(S.Test_X089(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例8：观众从交友房页签进入交友房')
    def test_Six_Party_008(self):
        S = self.multspectator
        S.Partytab_one_partyroom()
        self.assertIs(S.Test_X090(), True)

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例9：主播查看观众进入交友房的特效展示')
    # def test_Six_Party_009(self):
    #     A = self.multanchor
    #     self.assertIs(A.Test_X066(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例10：主播查看观众进入交友房消息区提示')
    # def test_Six_Party_010(self):
    #     A = self.multanchor
    #     time.sleep(3)
    #     self.assertIs(A.Test_X067(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例11：主播交友房警告消息检查')
    # def test_Six_Party_011(self):
    #     A = self.multanchor
    #     A.driver.swipe(363, 1478, 363, 2040)
    #     self.assertIs(A.Test_X059(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例12：交友房该场送礼为0，观众查看送礼榜入口')
    # def test_Six_Party_012(self):
    #     S = self.multspectator
    #     self.assertIs(S.Test_X133(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例13：观众在交友房中送礼时余额不足')
    # def test_Six_Party_013(self):
    #     S = self.multspectator
    #     S.Six_party_gift()
    #     time.sleep(1)
    #     S.Six_party_two_gift()
    #     S.More_message_people_sendgift()
    #     time.sleep(5)
    #     self.assertIs(S.Test_X127(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例14：观众在交友房中点击主播头像')
    # def test_Six_Party_014(self):
    #     S = self.multspectator
    #     S.driver.tap([(213, 213), (214, 214)], 200)
    #     time.sleep(2)
    #     S.driver.tap([(213, 213), (214, 214)], 200)
    #     S.Six_party_anchor_head()
    #     self.assertIs(S.Test_X091(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例15：观众在交友房中关注主播')
    # def test_Six_Party_015(self):
    #     S = self.multspectator
    #     S.Six_party_follow_anchor()
    #     self.assertIs(S.Test_X092(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例16：观众在交友房中举报主播')
    # def test_Six_Party_016(self):
    #     S = self.multspectator
    #     S.Six_party_report_anchor()
    #     self.assertIs(S.Test_X093(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例17：观众在交友房中通过主播个人主页浮窗给主播送礼物')
    # def test_Six_Party_017(self):
    #     S = self.multspectator
    #     A = self.multanchor
    #     S.driver.tap([(213, 213), (214, 214)], 200)
    #     time.sleep(1)
    #     S.Six_party_anchor_head()
    #     S.Six_party_supernatant_gift()
    #     S.Six_party_one_gift()
    #     S.More_message_people_sendgift()
    #     time.sleep(1)
    #     S.driver.tap([(213, 213), (214, 214)], 200)
    #     self.assertIs(A.Test_X16(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例18：交友房该场送礼不为0，观众查看送礼榜入口')
    # def test_Six_Party_018(self):
    #     S = self.multspectator
    #     self.assertIs(S.Test_X135(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例19：观众在交友房中给主播发起视频通话')
    # def test_Six_Party_019(self):
    #     A = self.multanchor
    #     S = self.multspectator
    #     S.Six_party_anchor_head()
    #     S.Six_party_call_anchor()
    #     self.assertIs(S.Test_56(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例20：观众在交友房@主播')
    # def test_Six_Party_020(self):
    #     A = self.multanchor
    #     S = self.multspectator
    #     time.sleep(5)
    #     S.Six_party_at_anchor()
    #     S.Six_party_room_message_send()
    #     S.driver.tap([(552, 189), (553, 190)], 200)
    #     self.assertIs(A.Test_X096(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例21：观众从主播个人主页进入交友房')
    # def test_Six_Party_021(self):
    #     S = self.multspectator
    #     S.Six_party_anchor_head()
    #     S.Six_party_supernatant_anchor_head()
    #     time.sleep(2)
    #     S.Homepage_video()
    #     self.assertIs(S.Test_X097(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例22：观众进入交友房消息区提示')
    # def test_Six_Party_022(self):
    #     S = self.multspectator
    #     time.sleep(3)
    #     self.assertIs(S.Test_X102(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例23：交友房中观众打开观众列表')
    # def test_Six_Party_023(self):
    #     S = self.multspectator
    #     S.Six_party_more_people()
    #     self.assertIs(S.Test_X098(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例24：交友房中观众上下滑动观众列表')
    # def test_Six_Party_024(self):
    #     S = self.multspectator
    #     S.driver.swipe(837, 410, 837, 1800)
    #     S.driver.swipe(837, 1800, 837, 410)
    #     self.assertIs(S.Test_X098(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例25：交友房中观众点击查看观众头像')
    # def test_Six_Party_025(self):
    #     S = self.multspectator
    #     S.Six_party_more_people_list_one()
    #     self.assertIs(S.Test_X101(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例26：交友房警告消息检查')
    # def test_Six_Party_026(self):
    #     S = self.multspectator
    #     S.driver.tap([(200, 189), (201, 190)], 200)
    #     time.sleep(1)
    #     S.driver.tap([(200, 189), (201, 190)], 200)
    #     self.assertIs(S.Test_X116(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例27：交友房观众端端发言')
    # def test_Six_Party_027(self):
    #     S = self.multspectator
    #     S.Six_party_room_message_button()
    #     S.Six_party_room_message()
    #     S.Six_party_room_message_send()
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     self.assertIs(S.Test_X117(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例28：交友房消息区消息滚动')
    # def test_Six_Party_028(self):
    #     S = self.multspectator
    #     S.Six_party_gift()
    #     S.Six_party_one_gift()
    #     S.More_message_people_sendgift()
    #     S.More_message_people_sendgift()
    #     S.More_message_people_sendgift()
    #     S.More_message_people_sendgift()
    #     S.More_message_people_sendgift()
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     self.assertIs(S.Test_X118(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例29：交友房消息区上滑消息')
    # def test_Six_Party_029(self):
    #     S = self.multspectator
    #     S.driver.swipe(357, 1519, 357, 2030)
    #     self.assertIs(S.Test_X119(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例30：观众在交友房中打开送礼浮窗')
    # def test_Six_Party_030(self):
    #     S = self.multspectator
    #     S.Six_party_gift()
    #     time.sleep(1)
    #     self.assertIs(S.Test_X128(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例31：观众在交友房中给所有人送礼')
    # def test_Six_Party_031(self):
    #     S = self.multspectator
    #     A = self.multanchor
    #     S.Six_party_send_all_gift()
    #     S.Six_party_one_gift()
    #     S.Six_party_send_gift()
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     self.assertIs(A.Test_31(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例32：观众在交友房中送礼时余额不足')
    # def test_Six_Party_032(self):
    #     S = self.multspectator
    #     S.Six_party_gift()
    #     S.Six_party_send_all_gift()
    #     S.Six_party_two_gift()
    #     S.More_message_people_sendgift()
    #     self.assertIs(S.Test_X127(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例33：交友房中点击进入banner页')
    # def test_Six_Party_033(self):
    #     S = self.multspectator
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     time.sleep(1)
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     time.sleep(1)
    #     S.driver.tap([(936, 2013), (937, 2014)], 200)
    #     time.sleep(5)
    #     self.assertIs(S.Test_X072(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例34：交友房中观众点击加入按钮')
    # def test_Six_Party_034(self):
    #     S = self.multspectator
    #     S.driver.tap([(200, 201), (201, 202)], 200)
    #     S.More_Setting()
    #     S.More_join()
    #     self.assertIs(S.Test_X138(), True)
    #     S.Six_party_twice_apply()
    #     S.check_perBtn()
    #     S.check_perBtn()
    #     S.check_perBtn()
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例35：交友房中观众打开消息列表')
    # def test_Six_Party_035(self):
    #     S = self.multspectator
    #     S.More_Setting()
    #     S.More_Message()
    #     self.assertIs(S.Test_X137(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例36：群聊界面发拍照图片')
    # def test_Six_Party_036(self):
    #     S = self.multspectator
    #     S.Supernatant_message_group()
    #     S.Supernatant_message_group_pic()
    #     S.Supernatant_message_group_pic_photo()
    #     S.Supernatant_message_setiing_photo_confirm()
    #     S.Supernatant_message_setiing_photo_twoconfirm()
    #     self.assertIs(S.Test_X032(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例37：群聊界面发相册图片')
    # def test_Six_Party_037(self):
    #     S = self.multspectator
    #     S.Supernatant_message_group_pic()
    #     S.Supernatant_message_group_pic_camera()
    #     time.sleep(2)
    #     S.Myphoto_one()
    #     self.assertIs(S.Test_X140(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例38：群聊界面发消息')
    # def test_Six_Party_038(self):
    #     S = self.multspectator
    #     S.Supernatant_message_group_chat()
    #     S.Supernatant_message_group_chat_send()
    #     self.assertIs(S.Test_X034(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例39：群聊界面发表情')
    # def test_Six_Party_039(self):
    #     S = self.multspectator
    #     S.Supernatant_message_face_gif()
    #     S.Supernatant_message_group_gif_one()
    #     self.assertIs(S.Test_X035(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例40：群聊界面发语音')
    # def test_Six_Party_040(self):
    #     S = self.multspectator
    #     S.Supernatant_message_group_voice()
    #     S.driver.tap([(500, 2010), (510, 2020)], 3000)
    #     self.assertIs(S.Test_X037(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例41：群聊界面上麦')
    # def test_Six_Party_041(self):
    #     S = self.multspectator
    #     S.Supernatant_message_group_upmic()
    #     self.assertIs(S.Test_X037(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例42：群聊界面发红包')
    # def test_Six_Party_042(self):
    #     S = self.multspectator
    #     S.Supernatant_message_group_packet()
    #     S.Supernatant_message_group_packet_number()
    #     S.Supernatant_message_group_packet_diamond()
    #     S.Supernatant_message_group_packet_send()
    #     self.assertIs(S.Test_X038(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例43：群聊界面送礼')
    # def test_Six_Party_043(self):
    #     S = self.multspectator
    #     S.driver.tap([(500, 1950), (501, 1951)], 200)
    #     S.Supernatant_message_group_gift()
    #     S.Gift_window_Activity()
    #     S.Six_party_one_gift()
    #     S.More_message_people_sendgift()
    #     S.driver.tap([(500, 500), (501, 501)], 200)
    #     self.assertIs(S.Test_X040(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例44：群聊界面进入活动')
    # def test_Six_Party_044(self):
    #     S = self.multspectator
    #     S.Supernatant_message_group_more()
    #     S.driver.tap([(864, 974), (865, 975)], 200)
    #     time.sleep(10)
    #     self.assertIs(S.Test_X041(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例45：交友房中进行充值')
    # def test_Six_Party_045(self):
    #     S = self.multspectator
    #     S.driver.tap([(200, 420), (201, 421)], 200)
    #     S.driver.tap([(200, 420), (201, 421)], 200)
    #     S.More_Setting()
    #     S.More_top_up()
    #     time.sleep(2)
    #     S.More_top_up_4500()
    #     time.sleep(5)
    #     S.More_top_up_pay()
    #     time.sleep(5)
    #     self.assertIs(S.Test_X078(), True)

    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例46：申请进入嘉宾位')
    # def test_Six_Party_046(self):
    #     S = self.multspectator
    #     S.More_top_up_confirm()
    #     S.driver.tap([(200, 420), (201, 421)], 200)
    #     S.More_Setting()
    #     S.More_join()
    #     S.Six_party_twice_apply()
    #     time.sleep(5)
    #     self.assertIs(S.Test_X139(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例47：房主同意连麦申请')
    # def test_Six_Party_047(self):
    #     S = self.multspectator
    #     A = self.multanchor
    #     A.Six_party_invite()
    #     A.Six_party_invite_list_one()
    #     A.driver.tap([(200, 420), (201, 421)], 200)
    #     time.sleep(1)
    #     self.assertIs(A.Test_45(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例48：交友房中关闭麦克风')
    # def test_Six_Party_048(self):
    #     S = self.multspectator
    #     time.sleep(5)
    #     S.More_Setting()
    #     S.More_Setting_setting()
    #     S.More_setting_switch_microphone()
    #     S.More_setting_switch_microphone()
    #     self.assertIs(S.Test_X079(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例49：交友房中设置贴纸')
    # def test_Six_Party_049(self):
    #     S = self.multspectator
    #     S.More_setting_sticker()
    #     S.More_setting_sticker_1()
    #     time.sleep(5)
    #     self.assertIs(S.Test_X080(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例50：交友房中开启美颜')
    # def test_Six_Party_050(self):
    #     S = self.multspectator
    #     S.driver.tap([(200, 420), (201, 421)], 200)
    #     S.More_Setting()
    #     S.More_Setting_setting()
    #     S.More_setting_beauty()
    #     S.More_setting_beauty_reset()
    #     S.More_setting_beauty_confirmreset()
    #     self.assertIs(S.Test_X081(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例51：交友房中开启镜像模式')
    # def test_Six_Party_051(self):
    #     S = self.multspectator
    #     S.driver.tap([(200, 420), (201, 421)], 200)
    #     S.More_Setting()
    #     S.More_Setting_setting()
    #     S.More_setting_turn_off_camera()
    #     S.More_setting_mirror_mode()
    #     self.assertIs(S.Test_X082(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例52：交友房中关闭摄像头')
    # def test_Six_Party_052(self):
    #     S = self.multspectator
    #     S.More_setting_turn_off_camera()
    #     S.More_setting_turn_off_camera()
    #     S.More_setting_turn_off_camera()
    #     S.driver.tap([(213, 213), (214, 214)], 200)
    #     self.assertIs(S.Test_X155(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例53：交友房中切换摄像头')
    # def test_Six_Party_053(self):
    #     S = self.multspectator
    #     S.More_Setting()
    #     S.More_Setting_setting()
    #     S.More_setting_turn_off_camera()
    #     S.More_setting_switch_camera()
    #     S.More_setting_switch_camera()
    #     self.assertIs(S.Test_X084(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例54：交友房中观众点击离开嘉宾位')
    # def test_Six_Party_054(self):
    #     S = self.multspectator
    #     S.Six_party_off_mic()
    #     self.assertIs(S.Test_X157(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例55：交友房中观众取消离开嘉宾位')
    # def test_Six_Party_055(self):
    #     S = self.multspectator
    #     S.Close_six_party_two_cancle()
    #     self.assertIs(S.Test_X158(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例56：交友房中观众确认离开嘉宾位')
    # def test_Six_Party_056(self):
    #     S = self.multspectator
    #     S.More_Setting()
    #     S.More_Setting_setting()
    #     S.Six_party_off_mic()
    #     S.Close_six_party_two_confirm()
    #     self.assertIs(S.Test_X159(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例57：交友房中观众给房主拨打约聊')
    # def test_Six_Party_057(self):
    #     S = self.multspectator
    #     S.Six_party_anchor()
    #     S.Six_party_call_anchor()
    #     self.assertIs(S.Test_56(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例58：观众离开交友房')
    # def test_Six_Party_058(self):
    #     S = self.multspectator
    #     # S.driver.tap([(213, 213), (214, 214)], 200)
    #     S.Close_six_party()
    #     self.assertIs(S.Test_X162(), True)
    #     time.sleep(2)
    #     S.driver.swipe(600, 800, 600, 1800)
    #     S.Partytab_one_partyroom()

    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例59：主播在消息区点击观众用户名')
    # def test_Six_Party_059(self):
    #     A = self.multanchor
    #     A.Six_message_user()
    #     self.assertIs(A.Test_X068(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例60：主播打开观众列表')
    # def test_Six_Party_060(self):
    #     A = self.multanchor
    #     A.driver.tap([(528, 528), (529, 529)], 200)
    #     A.Six_party_more_people()
    #     self.assertIs(A.Test_X006(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例61：主播在观众列表上下滑动')
    # def test_Six_Party_061(self):
    #     A = self.multanchor
    #     A.driver.swipe(700, 700, 700, 1800)
    #     time.sleep(1)
    #     A.driver.swipe(700, 1800, 700, 700)
    #     self.assertIs(A.Test_X007(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例62：主播在观众列表头像点击查看')
    # def test_Six_Party_062(self):
    #     A = self.multanchor
    #     A.Six_party_more_people_list_one()
    #     self.assertIs(A.Test_X017(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例63：主播在观众个人信息浮窗举报检查')
    # def test_Six_Party_063(self):
    #     A = self.multanchor
    #     A.Six_party_report_anchor()
    #     self.assertIs(A.Test_X010(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例64：主播在观众个人信息浮窗进入其个人主页')
    # def test_Six_Party_064(self):
    #     A = self.multanchor
    #     A.driver.tap([(528, 528), (529, 529)], 200)
    #     A.Six_party_more_people_list_one()
    #     A.Six_party_supernatant_anchor_head()
    #     self.assertIs(A.Test_X011(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例65：主播陌生人个人信息浮窗关注按钮检查')
    # def test_Six_Party_065(self):
    #     A = self.multanchor
    #     A.Homepage_back()
    #     A.Six_party_more_people_list_one()
    #     self.assertIs(A.Test_X012(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例66：主播在观众个人信息浮窗送礼物功能验证')
    # def test_Six_Party_066(self):
    #     A = self.multanchor
    #     A.Six_party_supernatant_gift()
    #     self.assertIs(A.Test_X105(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例67：主播在观众个人信息浮窗赠送礼物')
    # def test_Six_Party_067(self):
    #     A = self.multanchor
    #     A.Gift_window_Activity()
    #     A.Six_party_one_gift()
    #     A.More_message_people_sendgift()
    #     A.driver.tap([(200, 400), (201, 401)], 200)
    #     A.driver.tap([(200, 400), (201, 401)], 200)
    #     self.assertIs(A.Test_31(), True)
    #
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例68：主播看观众个人信息浮窗信息按钮')
    # def test_Six_Party_068(self):
    #     A = self.multanchor
    #     A.Six_party_more_people()
    #     A.Six_party_more_people_list_one()
    #     A.Supernatant_message()
    #     self.assertIs(A.Test_X015(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例69：私聊界面更多按钮的检查')
    # def test_Six_Party_069(self):
    #     A = self.multanchor
    #     A.Supernatant_message_more()
    #     self.assertIs(A.Test_X017(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例70：私聊界面退出按钮检查')
    # def test_Six_Party_070(self):
    #     A = self.multanchor
    #     A.driver.tap([(528, 528), (529, 529)], 200)
    #     A.Supernatant_message_back()
    #     self.assertIs(A.Test_X016(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例71：房主在个人信息浮窗--视频通话')
    # def test_Six_Party_071(self):
    #     A = self.multanchor
    #     A.driver.tap([(528, 528), (529, 529)], 200)
    #     A.Six_party_more_people_list_one()
    #     A.Supernatant_message()
    #     A.Supernatant_message_more()
    #     A.Six_party_call_anchor()
    #     self.assertIs(A.Test_X015(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例72：私聊界面折叠按钮点击检查')
    # def test_Six_Party_072(self):
    #     A = self.multanchor
    #     A.Supernatant_message_setiing()
    #     self.assertIs(A.Test_X021(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例73：私聊界面折叠区域翻译按钮点击检查')
    # def test_Six_Party_073(self):
    #     A = self.multanchor
    #     A.Supernatant_message_setiing_translate()
    #     self.assertIs(A.Test_X022(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例74：私聊界面折叠区域相册功能检查')
    # def test_Six_Party_074(self):
    #     A = self.multanchor
    #     A.Supernatant_message_setiing_photo()
    #     self.assertIs(A.Test_X024(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例75：私聊界面发送相册')
    # def test_Six_Party_075(self):
    #     A = self.multanchor
    #     A.Myphoto_message_one()
    #     A.Myphoto_comfirm()
    #     self.assertIs(A.Test_X025(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例76：私聊界面折叠区域相机功能检查')
    # def test_Six_Party_076(self):
    #     A = self.multanchor
    #     A.Supernatant_message_setiing_camera()
    #     self.assertIs(A.Test_X026(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例77：私聊界面发送拍摄照片')
    # def test_Six_Party_077(self):
    #     A = self.multanchor
    #     A.Supernatant_message_setiing_photo_confirm()
    #     A.Supernatant_message_setiing_photo_twoconfirm()
    #     self.assertIs(A.Test_X027(), True)
    #
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例78：私聊界面发送表情')
    # def test_Six_Party_078(self):
    #     A = self.multanchor
    #     A.Supernatant_message_face_gif()
    #     A.Supernatant_message_face_gif_one()
    #     self.assertIs(A.Test_X030(), True)
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例79：私聊界面送礼物')
    # def test_Six_Party_079(self):
    #     A = self.multanchor
    #     A.More_message_people_gift()
    #     A.Gift_window_Activity()
    #     A.More_message_people_sendgift()
    #     A.driver.tap([(528, 528), (529, 529)], 200)
    #     self.assertIs(A.Test_X031(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例80：群聊界面发拍照图片')
    # def test_Six_Party_080(self):
    #     A = self.multanchor
    #     A.Supernatant_message_back()
    #     A.Supernatant_message_group()
    #     A.Supernatant_message_group_pic()
    #     A.Supernatant_message_group_pic_photo()
    #     A.Supernatant_message_setiing_photo_confirm()
    #     A.Supernatant_message_setiing_photo_twoconfirm()
    #     self.assertIs(A.Test_X032(), True)
    #
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例81：群聊界面发相册图片')
    # def test_Six_Party_081(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_pic()
    #     A.Supernatant_message_group_pic_camera()
    #     time.sleep(2)
    #     A.Myphoto_one()
    #     self.assertIs(A.Test_X033(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例82：群聊界面发消息')
    # def test_Six_Party_082(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_chat()
    #     A.Supernatant_message_group_chat_send()
    #     self.assertIs(A.Test_X034(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例83：群聊界面发表情')
    # def test_Six_Party_083(self):
    #     A = self.multanchor
    #     A.Supernatant_message_face_gif()
    #     A.Supernatant_message_group_gif_one()
    #     self.assertIs(A.Test_X035(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例84：群聊界面发语音')
    # def test_Six_Party_084(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_voice()
    #     A.driver.tap([(500, 2010), (510, 2020)], 3000)
    #     self.assertIs(A.Test_X037(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例85：群聊界面上麦')
    # def test_Six_Party_085(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_upmic()
    #     self.assertIs(A.Test_X037(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例86：群聊界面发红包')
    # def test_Six_Party_086(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_packet()
    #     A.Supernatant_message_group_packet_number()
    #     A.Supernatant_message_group_packet_diamond()
    #     A.Supernatant_message_group_packet_send()
    #     self.assertIs(A.Test_X038(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例87：群聊界面领红包')
    # def test_Six_Party_087(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_packet_get()
    #     A.Supernatant_message_group_packet_open()
    #     self.assertIs(A.Test_X039(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例88：群聊界面送礼')
    # def test_Six_Party_088(self):
    #     A = self.multanchor
    #     A.driver.tap([(500, 1950), (501, 1951)], 200)
    #     A.Supernatant_message_group_gift()
    #     A.Gift_window_Activity()
    #     A.Six_party_one_gift()
    #     A.More_message_people_sendgift()
    #     A.driver.tap([(500, 500), (501, 501)], 200)
    #     self.assertIs(A.Test_X040(), True)
    #
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('用例89：群聊界面进入活动')
    # def test_Six_Party_089(self):
    #     A = self.multanchor
    #     A.Supernatant_message_group_more()
    #     A.Supernatant_message_group_more_banner()
    #     time.sleep(10)
    #     self.assertIs(A.Test_X041(), True)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例90：观众个人信息浮窗禁言功能')
    def test_Six_Party_090(self):
        A = self.multanchor
        # A.driver.tap([(500, 500), (501, 501)], 200)
        # A.driver.tap([(500, 500), (501, 501)], 200)
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.driver.tap([(200, 400), (201, 401)], 200)
        self.assertIs(A.Test_X042(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例91：观众被禁言后上麦功能校验')
    def test_Six_Party_091(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_90(), True)
        S.driver.tap([(500, 500), (501, 501)], 200)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例92：观众个人信息浮窗取消禁言功能')
    def test_Six_Party_092(self):
        A = self.multanchor
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.Six_party_more_people_list_one()
        self.assertIs(A.Test_X043(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例93：观众个人信息浮窗@观众功能')
    def test_Six_Party_093(self):
        A = self.multanchor
        A.Six_party_at_anchor()
        A.Room_message_button_send()
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(A.Test_X044(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例94：观众申请进入嘉宾位')
    def test_Six_Party_094(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_X139(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例95：房主查看申请列表有无申请消息')
    def test_Six_Party_095(self):
        A = self.multanchor
        A.Six_party_invite()
        self.assertIs(A.Test_X95(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例96：房主删除申请消息')
    def test_Six_Party_096(self):
        A = self.multanchor
        A.Six_party_invite_list_one_refuse()
        self.assertIs(A.Test_X96(), True)
        time.sleep(1)
        A.driver.tap([(200, 420), (201, 421)], 200)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例97：观众申请进入嘉宾位')
    def test_Six_Party_097(self):
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        self.assertIs(S.Test_X139(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例98：房主同意观众上麦申请')
    def test_Six_Party_098(self):
        A = self.multanchor
        A.Six_party_invite()
        A.Six_party_agree_list_one()
        A.driver.tap([(200, 420), (201, 421)], 200)
        time.sleep(1)
        self.assertIs(A.Test_45(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例99：交友房中观众离开嘉宾位')
    def test_Six_Party_099(self):
        S = self.multspectator
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()
        self.assertIs(S.Test_X159(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例100：主播邀请观众上麦')
    def test_Six_Party_100(self):
        A = self.multanchor
        S = self.multspectator
        A.Six_party_invite()
        A.Six_party_invite_list_one()
        time.sleep(1)
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(S.Test_X159(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例101：观众同意邀请')
    def test_Six_Party_101(self):
        S = self.multspectator
        S.Six_party_agree_invite()
        self.assertIs(S.Test_101(), True)
        #观众下麦
        S.More_Setting()
        S.More_Setting_setting()
        S.Six_party_off_mic()
        S.Close_six_party_two_confirm()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例102：观众拒绝邀请')
    def test_Six_Party_102(self):
        A = self.multanchor
        S = self.multspectator
        A.Six_party_invite()
        A.Six_party_more_people_list_one()
        S.Six_party_down_invite()
        S.More_Setting()
        self.assertIs(S.Test_102(), True)
        S.driver.tap([(200, 420), (201, 421)], 200)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例103：房主个人信息浮层表情选择')
    def test_Six_Party_103(self):
        A = self.multanchor
        S = self.multspectator
        S.More_Setting()
        S.More_join()
        S.Six_party_twice_apply()
        A.Six_party_invite()
        A.Six_party_agree_list_one()
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.Six_party_one_position()
        A.Six_party_anchor_floating_emo()
        self.assertIs(A.Test_103(), True)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例104：房主查看嘉宾信息浮窗')
    def test_Six_Party_104(self):
        A = self.multanchor
        A.Six_party_two_position()
        self.assertIs(A.Test_X017(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例105：房主移除嘉宾')
    def test_Six_Party_105(self):
        A = self.multanchor
        A.Supernatant_remove()
        self.assertIs(A.Test_105(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例106：房主禁言嘉宾')
    def test_Six_Party_106(self):
        A = self.multanchor
        A.Six_party_more_people()
        A.Six_party_more_people_list_one()
        A.Supernatant_mute()
        A.driver.tap([(200, 420), (201, 421)], 200)
        self.assertIs(A.Test_106(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例107：校验嘉宾是否被移除麦位')
    def test_Six_Party_107(self):
        A = self.multanchor
        A.Six_party_two_position()
        self.assertIs(A.Test_107(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例108：交友房警告消息检查')
    def test_Six_Party_108(self):
        A = self.multanchor
        A.driver.swipe(363, 1478, 363, 2040)
        self.assertIs(A.Test_X059(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例109：交友房主播端发言')
    def test_Six_Party_109(self):
        A = self.multanchor
        A.Room_message_button()
        A.Room_message_button_input()
        A.Room_message_button_send()
        A.driver.tap([(200, 420), (201, 421)], 200)

        self.assertIs(A.Test_X060(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例110：交友房消息区上滑消息')
    def test_Six_Party_110(self):
        A = self.multanchor
        A.driver.swipe(363, 2040,  363, 1478)
        self.assertIs(A.Test_X062(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例111：交友房消息区下滑消息')
    def test_Six_Party_111(self):
        A = self.multanchor
        A.driver.swipe(363, 2040, 363, 1478)
        self.assertIs(A.Test_X063(), True)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例112：主播在交友房中给自己送礼')
    def test_Six_Party_112(self):
        A = self.multanchor
        A.Six_party_gift()
        self.assertIs(A.Test_X070(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例113：交友房中点击进入banner页')
    def test_Six_Party_113(self):
        A = self.multanchor
        A.Room_banner()
        time.sleep(5)
        self.assertIs(A.Test_X072(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例114：交友房中背景选择')
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
    @allure.title('用例115：更换交友房背景')
    def test_Six_Party_115(self):
        A = self.multanchor
        A.More_Setting_background_Lv20()
        time.sleep(2)
        self.assertIs(A.Test_X074(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例116：交友房中打开消息列表')
    def test_Six_Party_116(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Message()
        self.assertIs(A.Test_X075(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例117：交友房中进行充值')
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
    @allure.title('用例118：交友房中关闭麦克风')
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
    @allure.title('用例119：交友房中设置贴纸')
    def test_Six_Party_119(self):
        A = self.multanchor
        A.More_setting_sticker()
        A.More_setting_sticker_1()
        time.sleep(5)
        self.assertIs(A.Test_X080(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例120：交友房中开启美颜')
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
    @allure.title('用例121：交友房中开启镜像模式')
    def test_Six_Party_121(self):
        A = self.multanchor
        A.driver.tap([(200, 420), (201, 421)], 200)
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_turn_off_camera()
        A.More_setting_mirror_mode()
        self.assertIs(A.Test_X082(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例122：交友房中关闭摄像头')
    def test_Six_Party_122(self):
        A = self.multanchor
        A.More_setting_turn_off_camera()
        A.driver.tap([(213, 213), (214, 214)], 200)
        self.assertIs(A.Test_X083(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例123：交友房中切换摄像头')
    def test_Six_Party_123(self):
        A = self.multanchor
        A.More_Setting()
        A.More_Setting_setting()
        A.More_setting_turn_off_camera()
        A.More_setting_switch_camera()
        A.More_setting_switch_camera()
        self.assertIs(A.Test_X084(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例124：关闭交友房进入结束页')
    def test_Six_Party_124(self):
        A = self.multanchor
        A.driver.tap([(213, 213), (214, 214)], 200)
        A.Close_six_party()
        A.Close_six_party_two_confirm()
        self.assertIs(A.Test_X085(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例125：观众进入结束页校验')
    def test_Six_Party_125(self):
        S = self.multspectator
        self.assertIs(S.Test_X163(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例126：观众结束页校验-进入个人主页')
    def test_Six_Party_126(self):
        S = self.multspectator
        S.Six_party_endpage_profile()
        self.assertIs(S.Test_X011(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例127：结束页校验-结束页标题')
    def test_Six_Party_127(self):
        S = self.multspectator
        self.assertIs(S.Test_X165(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例128：结束页校验-结束页派对时长/观众')
    def test_Six_Party_128(self):
        S = self.multspectator
        self.assertIs(S.Test_X166(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例129：房主结束页显示内容')
    def test_Six_Party_129(self):
        A = self.multanchor
        self.assertIs(A.Test_X087(), True)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例130：结束页进入主播个人主页')
    def test_Six_Party_130(self):
        A = self.multanchor
        A.Six_party_endpage_profile()
        self.assertIs(A.Test_X086(), True)



    if __name__ == '__main__':
        pytest.main()
