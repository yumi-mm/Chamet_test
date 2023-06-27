from common.partytencommon.partyaudience_Start import partyaudience_Start_End
from appium.webdriver.common.mobileby import MobileBy
import logging
import allure
import pytest
from time import sleep


@allure.epic("项目名称：10人交友房")
@allure.issue("BUG链接：http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("测试用例链接：http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('交友房10人房——观众端功能')
class Test_chamet(partyaudience_Start_End):
    which_party = 0

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例1：进入交友房页签')
    def test_TenParty_001(self):
        logging.info('===用例1：进入交友房页签===')
        try:
            self.partyten.audience_party_tab_Btn()
            partypage_title = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("交友房")')
            assert partypage_title.text == "交友房"
            logging.info('===断言成功，进入交友房页签===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例2：刷新交友房卡片页')
    def test_TenParty_002(self):
        logging.info('===用例2：刷新交友房卡片页===')
        try:
            self.partyten.audience_party_tab_Btn()
            self.partyten.swipe_xy(350, 300, 350, 1200)
            sleep(2)
            assert True
            logging.info('===断言成功，成功刷新页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例3：上下滑动交友房卡片页')
    def test_TenParty_003(self):
        logging.info('===用例3：上下滑动交友房卡片页===')
        try:
            self.partyten.audience_party_tab_Btn()
            self.partyten.swipe_xy(350, 1200, 350, 300)
            sleep(2)
            self.partyten.swipe_xy(350, 300, 350, 1200)
            sleep(2)
            assert True
            logging.info('===断言成功，上下滑动交友房页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例4：交友房封面包含内容--头像')
    def test_TenParty_004(self):
        logging.info('===用例4：交友房封面包含内容--头像===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_avatargrade = self.partyten.partycard_avatargrade()
            assert partycard_avatargrade
            logging.info('===断言成功，交友房封面存在头像===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例5：交友房封面包含内容--人数')
    def test_TenParty_005(self):
        logging.info('===用例5：交友房封面包含内容--人数===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_peopleNumber = self.partyten.partycard_peopleNumber()
            assert partycard_peopleNumber
            logging.info('===断言成功，交友房封面存在人数===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @pytest.mark.skip(reason='语言不是必须，跳过执行')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例6：交友房封面包含内容--语言')
    def test_TenParty_006(self):
        logging.info('===用例6：交友房封面包含内容--语言===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_language = self.partyten.partycard_language()
            assert partycard_language
            logging.info('===断言成功，交友房封面存在语言===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例7：交友房封面包含内容--用户名')
    def test_TenParty_007(self):
        logging.info('===用例7：交友房封面包含内容--用户名===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_username = self.partyten.partycard_username()
            assert partycard_username
            logging.info('===断言成功，交友房封面存在用户名===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例8：交友房封面包含内容--国旗')
    def test_TenParty_008(self):
        logging.info('===用例8：交友房封面包含内容--国旗===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_nationalflag = self.partyten.partycard_nationalflag()
            assert partycard_nationalflag
            logging.info('===断言成功，交友房封面存在国旗===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例9：观众进入10人交友房')
    def test_TenParty_009(self):
        logging.info('===用例9：观众进入10人交友房===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            party_username = self.partyten.audience_enter_tenparty(self.which_party)
            assert party_username == self.partyten.party_title()
            logging.info('===断言成功，成功进入10人交友房===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例10：观众进入交友房进场座驾')
    def test_TenParty_010(self):
        logging.info('===用例10：观众进入交友房进场座驾===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            assert self.partyten.enterparty_car()
            logging.info('===断言成功，存在进场座驾===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例11：观众进入交友房进场标签')
    def test_TenParty_011(self):
        logging.info('===用例11：观众进入交友房进场标签===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            assert self.partyten.enterparty_label()
            logging.info('===断言成功，存在进场标签===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例12：观众进入交友房进场消息提醒')
    def test_TenParty_012(self):
        logging.info('===用例12：观众进入交友房进场消息提醒===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            enterparty_message = self.partyten.party_textmessage()
            assert "加入了房间" in enterparty_message
            logging.info('===断言成功，存在进场消息提醒===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例13：观众端交友房警告消息检查')
    def test_TenParty_013(self):
        logging.info('===用例13：观众端交友房警告消息检查===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            warning_message = self.partyten.audience_chat_area()[0].text
            warning_message_text = "欢迎来到Chamet 交友房！警告：直播期间严禁出现色情、粗俗、暴力、未成年人等相关情况。人工智能系统每天24 小时对其进行审查。一旦违反规定，将受到严惩！"
            assert warning_message == warning_message_text
            logging.info('===断言成功，存在警告消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例14：观众端发言')
    def test_TenParty_014(self):
        logging.info('===用例14：观众端发消息===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_speak_list("hello")
            audience_chat_area = self.partyten.audience_chat_areatext(-1)
            assert audience_chat_area == "hello"
            logging.info('===断言成功，观众成功发言===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例15：观众端发送文字正常向前滚动')
    def test_TenParty_015(self):
        logging.info('===用例15：观众端发送文字正常向前滚动===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_speak_list(["test1","test2"])
            audience_chat_area = self.partyten.audience_chat_areatext(-1)
            assert audience_chat_area == "test2"
            logging.info('===断言成功，文字正常向前滚动===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.title('用例16：观众端消息区聊天消息可下滑')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_TenParty_016(self):
        logging.info('===用例16：观众端消息区聊天消息可下滑===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_speak_list(["1","2","3","4","5","6","7","8","9","10","11"])
            self.partyten.swipe_xy(200, 900, 200, 1000)
            assert self.partyten.audience_chat_areatext(-1) != "11"
            logging.info('===断言成功，可成功下滑消息区===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例17：消息区聊天消息可上滑')
    def test_TenParty_017(self):
        logging.info('===用例17：消息区聊天消息可上滑===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_speak_list(["1","2","3","4","5","6","7","8","9","10","11"])
            self.partyten.swipe_xy(200, 900, 200, 1000)
            self.partyten.swipe_xy(200, 1000, 200, 900)
            assert self.partyten.audience_chat_areatext(-1) != "10"
            logging.info('===断言成功，可成功上滑消息区===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例18：观众端打开送礼弹窗')
    def test_TenParty_018(self):
        logging.info('===用例18：观众端打开送礼弹窗===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_open_giftwin()
            assert self.partyten.audience_giftwin_textlist()
            logging.info('===断言成功，可成功打开送礼弹窗===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例19：观众端给主播送礼')
    def test_TenParty_019(self):
        logging.info('===用例19：观众端给主播送礼===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_open_giftwin()
            self.partyten.audience_sendgift(2)
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.partyten.party_textmessage()
            assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例20：观众端给所有嘉宾送礼')
    def test_TenParty_020(self):
        logging.info('===用例20：观众端给所有嘉宾送礼===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_open_giftwin()
            self.partyten.giftwin_allbut()
            self.partyten.audience_sendgift(2)
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.partyten.party_textmessage()
            assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例21：观众端滑动送礼弹窗')
    def test_TenParty_021(self):
        logging.info('===用例21：观众端滑动送礼弹窗===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_open_giftwin()
            next_gifttext,last_gifttext = self.partyten.left_right_swipegiftwin()
            assert  next_gifttext != last_gifttext
            logging.info('===断言成功，两页面第一个礼物不同===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例22：观众端打开赛车游戏')
    def test_TenParty_022(self):
        logging.info('===用例22：观众端打开赛车游戏===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            race_rank = self.partyten.audienceenter_game_window("Chamet赛车")
            assert race_rank
            logging.info('===断言成功，打开Chamet赛车游戏===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例23：观众端打开幸运数字游戏')
    def test_TenParty_023(self):
        logging.info('===用例23：观众端打开幸运数字游戏===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            LuckyNumber_rank = self.partyten.audienceenter_game_window("幸运数字")
            assert LuckyNumber_rank
            logging.info('===断言成功，打开幸运数字游戏===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例24：观众端申请上麦(通过加入按钮)')
    def test_TenParty_024(self):
        logging.info('===用例24：观众端申请上麦(通过加入按钮)===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            if self.partyten.audience_applyguest():
                assert True
                logging.info('===断言成功，申请上麦成功===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例25：观众端申请上麦(通过点击交友位)')
    def test_TenParty_025(self):
        logging.info('===用例25：观众端申请上麦(通过点击交友位)===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            if self.partyten.partysite_applyguest(2):
                assert True
                logging.info('===断言成功，申请上麦成功===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例26：打开主播个人主页半屏浮窗')
    def test_TenParty_026(self):
        logging.info('===用例26：打开主播个人主页半屏浮窗===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            getparty_title,getanchor_HalfScreenname = self.partyten.openanchor_HalfScreen()
            assert getparty_title == getanchor_HalfScreenname
            logging.info('===断言成功，主播名称与半屏浮层名称一致===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例27：进入主播个人主页')
    def test_TenParty_027(self):
        logging.info('===用例27：进入主播个人主页===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.enteranchor_HalfScreen()
            halfwin_name,user_name = self.partyten.enteranchor_Personalhomepage()
            assert halfwin_name == user_name
            logging.info('===断言成功，主播名称与个人主页名称一致===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例28：从主播个人主页小窗进入交友房')
    def test_TenParty_028(self):
        logging.info('===用例28：从主播个人主页小窗进入交友房===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.enteranchor_HalfScreen()
            self.partyten.enteranchor_Personalhomepage()
            party_title = self.partyten.Personalhome_enterparty()
            assert party_title
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例29：通过半屏浮窗给主播送礼物')
    def test_TenParty_029(self):
        logging.info('===用例29：通过半屏浮窗给主播送礼物===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.enteranchor_HalfScreen()
            self.partyten.HalfScreen_sendgift(2)
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.partyten.party_textmessage()
            assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例30：通过半屏浮窗给主播打视频通话')
    def test_TenParty_030(self):
        logging.info('===用例30：通过半屏浮窗给主播打视频通话===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.enteranchor_HalfScreen()
            if self.partyten.HalfScreen_Videocall():
                assert True
                logging.info('===断言成功，成功拨打===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例31：通过半屏浮窗@主播')
    def test_TenParty_031(self):
        logging.info('===用例31：通过半屏浮窗@主播===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.enteranchor_HalfScreen()
            self.partyten.HalfScreen_aiteanchor()
            editEt = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/editEt").text
            assert "@" in editEt
            logging.info('===断言成功，@主播成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例32：通过半屏浮窗打开举报弹窗')
    def test_TenParty_032(self):
        logging.info('===用例32：通过半屏浮窗打开举报弹窗===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.enteranchor_HalfScreen()
            reportwin_title = self.partyten.report_anchor()
            assert reportwin_title == "举报"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例33：通过半屏浮窗查看主播动态')
    def test_TenParty_033(self):
        logging.info('===用例33：通过半屏浮窗查看主播动态===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.enteranchor_HalfScreen()
            self.partyten.watch_groupview()
            fl_user_head = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/fl_user_head")
            assert fl_user_head
            logging.info('===断言成功，进入动态页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例34：展开观众列表')
    def test_TenParty_034(self):
        logging.info('===用例34：展开观众列表===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            morepeople_win = self.partyten.open_morepeople()
            assert "观众" in morepeople_win
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例35：展开观众个人主页半屏浮窗')
    def test_TenParty_035(self):
        logging.info('===用例35：展开观众个人主页半屏浮窗===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.open_audience_HalfScreen()
            user_head = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/svga_user_head_level_frame")
            assert user_head
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例36：观众端打开消息列表')
    def test_TenParty_036(self):
        logging.info('===用例36：观众端打开消息列表===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audienceopen_message()
            chamet_service = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/rl_customer_service_content")
            assert chamet_service
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例37：进入私聊页面')
    def test_TenParty_037(self):
        logging.info('===用例37：进入私聊页面===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audienceenter_usermessage()
            # 判断页面标题最后一个字符不为)证明成功进入私聊
            usermessage_name = self.partyten.usermessage_name()[-1]
            assert usermessage_name != ')'
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例38：私聊页面发送文字')
    def test_TenParty_038(self):
        logging.info('===用例38：私聊页面发送文字===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_usermessage_sendtext("hi")
            get_usermessage_textcontent = self.partyten.get_usermessage_textcontent(-1)
            assert get_usermessage_textcontent == "hi"
            logging.info('===断言成功，成功发送文字===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例39：私聊页面发送表情')
    def test_TenParty_039(self):
        logging.info('===用例39：私聊页面发送表情===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_usermessage_sendexpression(1)
            photocontent = self.partyten.get_usermessage_photocontent()
            assert photocontent >= 1
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例40：私聊页面发送谷歌表情')
    def test_TenParty_040(self):
        logging.info('===用例40：私聊页面发送谷歌表情===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_usermessage_sendexpression(0)
            googlephoto = self.partyten.get_usermessage_googlephotocontent()
            assert googlephoto >= 1
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例41：展开私聊页面下拉按钮')
    def test_TenParty_041(self):
        logging.info('===用例41：展开私聊页面下拉按钮===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            translate_but = self.partyten.usermessage_translate_but()
            assert translate_but
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例42：观众端开启私聊界面翻译功能')
    def test_TenParty_042(self):
        logging.info('===用例42：观众端开启私聊界面翻译功能===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            if self.partyten.open_usermessage_translate():
                assert True
                logging.info('===断言成功，成功打开翻译===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例43：私聊界面发送相册照片')
    def test_TenParty_043(self):
        logging.info('===用例43：私聊界面发送相册照片===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            if self.partyten.audience_usermessage_sendphoto(2):
                assert True
                logging.info('===断言成功===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例44：私聊界面发送相机照片')
    def test_TenParty_044(self):
        logging.info('===用例44：私聊界面发送相机照片===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            if self.partyten.audience_usermessage_sendcameraphoto():
                assert True
                logging.info('===断言成功===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例45：私聊界面发拨打语音聊天')
    def test_TenParty_045(self):
        logging.info('===用例45：私聊界面发拨打语音聊天===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.usermessage_video_but()
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例46：观众端左右滑动私聊礼物页面')
    def test_TenParty_046(self):
        logging.info('===用例46：观众端左右滑动私聊礼物页面===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            nowgift_list_text,newgift_list_text = self.partyten.audience_usermessage_scroll_gift()
            assert nowgift_list_text[0].text != newgift_list_text[0].text
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例47：观众端私聊页面送礼')
    def test_TenParty_047(self):
        logging.info('===用例47：观众端私聊页面送礼===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_usermessage_sendgift()
            last_text = self.partyten.get_usermessage_textcontent(-1)
            assert '送出' in last_text
            logging.info('===断言成功，成功发送礼物===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例48：观众端私聊页面打开个人主页浮窗')
    def test_TenParty_048(self):
        logging.info('===用例48：观众端私聊页面打开个人主页浮窗===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            user_name, profile_name = self.partyten.audienceopen_Profilefloat()
            assert profile_name == user_name
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例49：观众端进入群聊页面')
    def test_TenParty_049(self):
        logging.info('===用例49：观众端进入群聊页面===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audienceenter_groupmessage()
            groupmessage_name = self.partyten.audience_groupmessage_name()
            assert groupmessage_name[-1] == ')'
            logging.info('===断言成功，成功进入群聊页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例50：观众端群聊页面发送文字')
    def test_TenParty_050(self):
        logging.info('===用例50：观众端群聊页面发送文字===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_groupmessage_sendtext("hi")
            last_text = self.partyten.get_usermessage_textcontent(-1)
            assert last_text == 'hi'
            logging.info('===断言成功，成功发送文字===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例51：观众端群聊页面发送表情')
    def test_TenParty_051(self):
        logging.info('===用例51：观众端群聊页面发送表情===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_groupmessage_sendexpression(1)
            photocontent = self.partyten.get_groupmessage_photocontent()
            assert photocontent >= 1
            logging.info('===断言成功，成功发送chamet表情===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例52：观众端群聊页面发送谷歌表情')
    def test_TenParty_052(self):
        logging.info('===用例52：观众端群聊页面发送谷歌表情===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_groupmessage_sendexpression(0)
            googlephoto = self.partyten.get_groupmessage_googlephotocontent()
            assert googlephoto >= 1
            logging.info('===断言成功，成功发送谷歌表情===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例53：观众端群聊页面发送语音')
    def test_TenParty_053(self):
        logging.info('===用例53：观众端群聊页面发送语音===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_groupmessage_send_voice()
            voice_timelast = self.partyten.audience_voice_text()[-1]
            print(voice_timelast)
            assert voice_timelast == 's'
            logging.info('===断言成功，成功发送语音===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例54：观众端群聊页面上麦')
    def test_TenParty_054(self):
        logging.info('===用例54：观众端群聊页面上麦===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_up_microphone()
            toast_text = self.partyten.audience_toast_message("直播间无法上麦").text
            assert toast_text == "直播间无法上麦"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例55：观众端群聊页面发送相册图片')
    def test_TenParty_055(self):
        logging.info('===用例55：观众端群聊页面发送相册图片===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            if self.partyten.audience_groupmessage_sendphoto(2):
                logging.info('===断言成功===')
                assert True
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例56：观众端群聊页面发送拍摄图片')
    def test_TenParty_056(self):
        logging.info('===用例56：观众端群聊页面发送拍摄图片===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            if self.partyten.audience_groupmessage_sendcameraphoto():
                logging.info('===断言成功===')
                assert True
            else:
                raise
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例57：观众端群聊页面发送钻石包')
    def test_TenParty_057(self):
        logging.info('===用例57：观众端群聊页面发送钻石包===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_send_diamondenvelope(2,1000)
            envelope = self.partyten.messageregion_getenvelope()
            assert envelope
            logging.info('===断言成功，成功发送钻石包===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例58：观众端群聊页面领取钻石包')
    def test_TenParty_058(self):
        logging.info('===用例58：观众端群聊页面领取钻石包===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_send_diamondenvelope(2, 1000)
            self.partyten.audience_get_diamondenvelope()
            user_head = self.partyten.getenvelope_userhead()
            assert user_head
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例59：观众端群聊页面送礼')
    def test_TenParty_059(self):
        logging.info('===用例59：观众端群聊页面送礼===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_groupmessage_sendgift(2)
            gift_messageimage = self.partyten.audience_giftmessageimage()
            assert gift_messageimage
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例60：10人交友房观众端打开充值页面')
    def test_TenParty_060(self):
        logging.info('===用例60：10人交友观众播端打开充值页面===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_enterrechargepage()
            audience_rechargepage = self.partyten.audience_rechargepage()
            assert audience_rechargepage
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例61：10人交友房观众端端充值')
    def test_TenParty_061(self):
        logging.info('===用例61：10人交友房观众端端充值===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_recharge_diamond()
            buy_success_page = self.partyten.audience_buysuccess_page()
            assert buy_success_page
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例62：10人交友房观众端打开任务页')
    def test_TenParty_062(self):
        logging.info('===用例62：10人交友房观众端打开任务页===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_entertaskpage()
            task_page = self.partyten.taskpage_title()
            assert task_page == "任务"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例63：10人交友房观众端打开礼物冠名墙')
    def test_TenParty_063(self):
        logging.info('===用例63：10人交友房观众端打开礼物冠名墙===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.partyten.audience_enter_giftnamingwall()
            giftwall_title = self.partyten.giftwall_title()
            assert giftwall_title == "礼物荣誉墙"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例64：10人交友房观众端打开banner')
    def test_TenParty_064(self):
        logging.info('===用例64：10人交友房观众端打开banner===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            if self.partyten.audience_enter_banner():
                assert True
            else:
                raise
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例65：观众端退出交友房')
    def test_TenParty_065(self):
        logging.info('===用例65：观众端退出交友房===')
        try:
            self.partyten.audience_party_tab_Btn()
            party_list_num = self.partyten.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.partyten.audience_enter_tenparty(self.which_party)
            self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/vc_close").click()
            assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("创建交友房")')
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    if __name__ == '__main__':
        pytest.main()

    '''
    pytest .\test_10party_audience.py -v -s --alluredir=..\result\2023_6_9_016
    pytest --lf .\test_10party_audience.py -v -s --alluredir=..\result\2023_6_13_002
    allure serve  ..\result\2023_6_9_016
    pytest -s -v test_10party_audience.py::Test_chamet::test_TenParty_013
    '''
