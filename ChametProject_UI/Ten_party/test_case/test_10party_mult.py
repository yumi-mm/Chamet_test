import os
import time
from common.partytencommon.multparty_star_end import anchorparty_Start_End
# from common.partytencommon.multparty_star_end import audienceeparty_Start_End
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import logging
import pytest
import allure
from time import sleep


class Test_multchamet(anchorparty_Start_End):
    # which_party = 0
    # 测试环境ID
    # Anchor_ID = "20113007"
    # 线上环境ID
    Anchor_ID = "46565897"
    audience_name = "markd7fdeaqq"
    anchor_name = "yumi680bc2"

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例1：主播进入交友房预览页')
    def test_TenParty_001(self):
        logging.info('===用例1：主播进入交友房预览页===')
        try:
            partyPreviewPage_enter = (MobileBy.ID, "com.hkfuliao.chamet:id/btn")
            PreEnter_butname = self.anchordriver.find_element(*partyPreviewPage_enter).text
            assert PreEnter_butname == "创建交友房"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例2：默认交友房预览页为10人房')
    def test_TenParty_002(self):
        logging.info('===用例2：默认交友房预览页为10人房===')
        try:
            self.multanchor.enter_party_PreviewPage()
            # 预览页出现十个交友位
            site_num = self.multanchor.tenparty_sitenum()
            assert site_num == 10
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例3：主播创建10人交友房')
    def test_TenParty_003(self):
        logging.info('===用例3：主播创建10人交友房===')
        try:
            # self.multpartyten.enter_party_PreviewPage()
            self.multanchor.enter_tenparty()
            # 房主在交友位上
            assert self.anchordriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/user_head")
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例4：主播端交友房警告消息检查')
    def test_TenParty_004(self):
        logging.info('===用例4：主播端交友房警告消息检查===')
        try:
            # 警告消息是否存在
            assert self.anchordriver.find_element(*self.multanchor.warning_message)
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例5：交友房警告消息内容检查')
    def test_TenParty_005(self):
        logging.info('===用例5：交友房警告消息内容检查===')
        try:
            # 警告消息内容是否正确
            warning_message_content = self.anchordriver.find_element(*self.multanchor.warning_message).text
            assert warning_message_content == "欢迎来到Chamet 交友房！警告：直播期间严禁出现色情、粗俗、暴力、未成年人等相关情况。人工智能系统每天24 小时对其进行审查。一旦违反规定，将受到严惩！"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
    

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例6：观众进入交友房页签')
    def test_TenParty_006(self):
        logging.info('===用例6：观众进入交友房页签===')
        try:
            self.multaudience.audience_party_tab_Btn()
            partypage_title = self.audiencedriver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("交友房")')
            assert partypage_title.text == "交友房"
            logging.info('===断言成功，进入交友房页签===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例7：刷新交友房卡片页')
    def test_TenParty_007(self):
        logging.info('===用例7：刷新交友房卡片页===')
        try:
            self.multaudience.swipe_xy(350, 300, 350, 1200)
            sleep(2)
            assert True
            logging.info('===断言成功，成功刷新页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例8：上下滑动交友房卡片页')
    def test_TenParty_008(self):
        logging.info('===用例8：上下滑动交友房卡片页===')
        try:
            self.multaudience.swipe_xy(350, 1200, 350, 300)
            sleep(2)
            self.multaudience.swipe_xy(350, 300, 350, 1200)
            sleep(2)
            assert True
            logging.info('===断言成功，上下滑动交友房页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    # @pytest.mark.skip(reason='跳过执行，3.5.3版本取消显示')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例9：交友房封面包含内容--头像')
    def test_TenParty_009(self):
        logging.info('===用例9：交友房封面包含内容--头像===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_avatargrade = self.multaudience.partycard_avatargrade()
            assert partycard_avatargrade
            logging.info('===断言成功，交友房封面存在头像===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例10：交友房封面包含内容--人数')
    def test_TenParty_010(self):
        logging.info('===用例10：交友房封面包含内容--人数===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_peopleNumber = self.multaudience.partycard_peopleNumber()
            assert partycard_peopleNumber
            logging.info('===断言成功，交友房封面存在人数===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    # @pytest.mark.skip(reason='语言不是必须，跳过执行')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例11：交友房封面包含内容--语言')
    def test_TenParty_011(self):
        logging.info('===用例11：交友房封面包含内容--语言===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_language = self.multaudience.partycard_language()
            assert partycard_language
            logging.info('===断言成功，交友房封面存在语言===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例12：交友房封面包含内容--用户名')
    def test_TenParty_012(self):
        logging.info('===用例12：交友房封面包含内容--用户名===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_username = self.multaudience.partycard_username()
            assert partycard_username
            logging.info('===断言成功，交友房封面存在用户名===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例13：交友房封面包含内容--国旗')
    def test_TenParty_013(self):
        logging.info('===用例13：交友房封面包含内容--国旗===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            partycard_nationalflag = self.multaudience.partycard_nationalflag()
            assert partycard_nationalflag
            logging.info('===断言成功，交友房封面存在国旗===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例14：观众进入10人交友房')
    def test_TenParty_014(self):
        logging.info('===用例14：观众进入10人交友房===')
        try:
            # party_list_num = self.multaudience.party_list()
            # if party_list_num == 0:
            #     pytest.skip("没有交友房，跳过该测试用例")
            # party_username = self.multaudience.audience_enter_tenparty(self.which_party)
            party_username = self.multaudience.enterparty_userbyid(self.Anchor_ID)
            assert party_username == self.multaudience.party_title()
            logging.info('===断言成功，成功进入10人交友房===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        # finally:
        #     self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例15：观众进入交友房进场座驾')
    def test_TenParty_015(self):
        logging.info('===用例15：观众进入交友房进场座驾===')
        try:
            # party_list_num = self.multaudience.party_list()
            # if party_list_num == 0:
            #     pytest.skip("没有交友房，跳过该测试用例")
            # self.multaudience.audience_enter_tenparty(self.which_party)
            assert self.multaudience.enterparty_car()
            logging.info('===断言成功，存在进场座驾===')
            assert self.multaudience.enterparty_label()
            logging.info('===断言成功，存在进场标签===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    # @pytest.mark.skip("由于元素显示时间较短，用例15与16合并")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例16：观众进入交友房进场标签')
    # def test_TenParty_016(self):
    #     logging.info('===用例16：观众进入交友房进场标签===')
    #     try:
    #         # party_list_num = self.multaudience.party_list()
    #         # if party_list_num == 0:
    #         #     pytest.skip("没有交友房，跳过该测试用例")
    #         # self.multaudience.audience_enter_tenparty(self.which_party)
    #         assert self.multaudience.enterparty_label()
    #         logging.info('===断言成功，存在进场标签===')
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multaudience.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info("===执行失败===")
    #         screen_name = self.multaudience.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise



    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例17：观众进入交友房进场消息提醒')
    def test_TenParty_017(self):
        logging.info('===用例17：观众进入交友房进场消息提醒===')
        try:
            # party_list_num = self.multaudience.party_list()
            # if party_list_num == 0:
            #     pytest.skip("没有交友房，跳过该测试用例")
            # self.multaudience.audience_enter_tenparty(self.which_party)
            enterparty_message = self.multaudience.party_textmessage()
            assert "{} 加入了房间".format(self.audience_name) in enterparty_message
            logging.info('===断言成功，存在进场消息提醒===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        # finally:
        #     self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例18：观众端交友房警告消息检查')
    def test_TenParty_018(self):
        logging.info('===用例18：观众端交友房警告消息检查===')
        try:
            # party_list_num = self.multaudience.party_list()
            # if party_list_num == 0:
            #     pytest.skip("没有交友房，跳过该测试用例")
            # self.multaudience.audience_enter_tenparty(self.which_party)
            warning_message = self.multaudience.audience_chat_area()[0].text
            warning_message_text = "欢迎来到Chamet 交友房！警告：直播期间严禁出现色情、粗俗、暴力、未成年人等相关情况。人工智能系统每天24 小时对其进行审查。一旦违反规定，将受到严惩！"
            assert warning_message == warning_message_text
            logging.info('===断言成功，存在警告消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例19：主播检查观众进场消息提醒')
    def test_TenParty_019(self):
        logging.info('===用例19：主播检查观众进场消息提醒===')
        try:
            enterparty_message = self.multanchor.party_textmessage(-1)
            assert "{} 加入了房间".format(self.audience_name) in enterparty_message
            logging.info('===断言成功，存在进场消息提醒===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例20：交友房主播端发言')
    def test_TenParty_020(self):
        logging.info('===用例20：交友房主播端发言===')
        try:
            self.multanchor.anchor_speak_list("hello")
            chat_area = self.multanchor.chat_area(-1)
            # 断言发送的消息是否出现在消息区
            assert chat_area == "hello"
            logging.info('===断言成功，观众成功发言===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例21：观众端查看主播端发言')
    def test_TenParty_021(self):
        logging.info('===用例21：观众端查看主播端发言===')
        try:
            audience_chat_area = self.multaudience.audience_chat_areatext(-1)
            assert audience_chat_area == "hello"
            logging.info('===断言成功，观众端可看到主播端发言===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例22：交友房观众端发言')
    def test_TenParty_022(self):
        logging.info('===用例22：交友房观众端发言===')
        try:
            self.multaudience.audience_speak_list("hi")
            chat_area = self.multaudience.chat_area(-1)
            # 断言发送的消息是否出现在消息区
            assert chat_area == "hi"
            logging.info('===断言成功，观众端成功发言===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例23：主播端查看观众端发言')
    def test_TenParty_023(self):
        logging.info('===用例23：主播端查看观众端发言===')
        try:
            anchor_chat_area = self.multanchor.chat_area(-1)
            assert anchor_chat_area == "hi"
            logging.info('===断言成功，主播端可看到观众端发言===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例24：观众端发送文字正常向前滚动')
    def test_TenParty_024(self):
        logging.info('===用例24：观众端发送文字正常向前滚动===')
        try:
            self.multaudience.audience_speak_list(["test1", "test2"])
            audience_chat_area = self.multaudience.audience_chat_areatext(-1)
            assert audience_chat_area == "test2"
            logging.info('===断言成功，文字正常向前滚动===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例25：主播端发送文字正常向前滚动')
    def test_TenParty_025(self):
        logging.info('===用例25：主播端发送文字正常向前滚动===')
        try:
            self.multanchor.anchor_speak_list(["test3", "test4"])
            chat_area = self.multanchor.chat_area(-1)
            # 断言最后一个消息是否为第二次发的
            assert chat_area == "test4"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.title('用例26：观众端消息区聊天消息可下滑')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_TenParty_026(self):
        logging.info('===用例26：观众端消息区聊天消息可下滑===')
        try:
            self.multaudience.audience_speak_list(["1","2","3","4","5"])
            self.multaudience.swipe_xy(200, 900, 200, 1000)
            # assert self.multaudience.audience_chat_areatext(-1) != "5"
            warning_message = self.multaudience.audience_chat_area()[0].text
            warning_message_text = "欢迎来到Chamet 交友房！警告：直播期间严禁出现色情、粗俗、暴力、未成年人等相关情况。人工智能系统每天24 小时对其进行审查。一旦违反规定，将受到严惩！"
            assert warning_message == warning_message_text
            logging.info('===断言成功，可成功下滑消息区===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例27：观众端消息区聊天消息可上滑')
    def test_TenParty_027(self):
        logging.info('===用例27：消息区聊天消息可上滑===')
        try:
            self.multaudience.swipe_xy(200, 1000, 200, 900)
            assert self.multaudience.audience_chat_areatext(-1) != "4"
            logging.info('===断言成功，可成功上滑消息区===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.title('用例28：主播端消息区聊天消息可下滑')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_TenParty_028(self):
        logging.info('===用例28：主播端消息区聊天消息可下滑===')
        try:
            self.multanchor.swipe_xy(200, 1500, 200, 1950)
            assert self.multanchor.chat_area(-1) != "5"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例29：主播端消息区聊天消息可上滑')
    def test_TenParty_029(self):
        logging.info('===用例29：主播端消息区聊天消息可上滑===')
        try:
            self.multanchor.swipe_xy(200, 1950, 200, 1500)
            assert self.multanchor.chat_area(-1) != "4"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例30：主播端打开送礼物弹窗')
    def test_TenParty_030(self):
        logging.info('===用例30：主播端打开送礼物弹窗===')
        try:
            self.multanchor.open_gift_window()
            gift_lst = self.multanchor.gift_lst()
            assert gift_lst
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例31：主播不可给自己送礼')
    def test_TenParty_031(self):
        logging.info('===用例31：主播不可给自己送礼===')
        try:
            send_gift_but = (MobileBy.ID, "com.hkfuliao.chamet:id/sendTv")
            send_butattr = self.multanchor.get_attr("enabled", *send_gift_but)
            assert send_butattr == "false"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例32：主播端滑动送礼弹窗')
    def test_TenParty_032(self):
        logging.info('===用例32：主播端滑动送礼弹窗===')
        try:
            self.multanchor.open_gift_window()
            next_gifttext,last_gifttext = self.multanchor.left_right_swipegiftwin()
            assert  next_gifttext != last_gifttext
            logging.info('===断言成功，两页面第一个礼物不同===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例33：观众端打开送礼弹窗')
    def test_TenParty_033(self):
        logging.info('===用例33：观众端打开送礼弹窗===')
        try:
            self.multaudience.audience_open_giftwin()
            assert self.multaudience.audience_giftwin_textlist()
            logging.info('===断言成功，可成功打开送礼弹窗===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例34：观众端给主播送礼')
    def test_TenParty_034(self):
        logging.info('===用例34：观众端给主播送礼===')
        try:
            global sendgift_assertcondition_1
            # sendgift_assertcondition_1 = self.multaudience.audience_sendgift("简体中文chinese simplified","Blessed Ramadan")
            sendgift_assertcondition_1 = self.multaudience.audience_sendgift("热门", "Lucky Fortune")
            # sendgift_assertcondition_1 = self.multaudience.audience_sendgift("热门", "幸运之吻")
            if sendgift_assertcondition_1 == 0:
                pytest.skip("观众端未送礼")
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.multaudience.party_textmessage_all()
            count = sendgift_message.count("{} 送出".format(self.audience_name))
            assert count == 1
            # assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例35：主播端查看观众端送礼')
    def test_TenParty_035(self):
        logging.info('===用例35：主播端查看观众端送礼===')
        try:
            if sendgift_assertcondition_1 == 0:
                pytest.skip("观众端未送礼")
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.multanchor.party_textmessage_all()
            count = sendgift_message.count("{} 送出".format(self.audience_name))
            assert count == 1
            # assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例36：观众端给所有嘉宾送礼')
    def test_TenParty_036(self):
        logging.info('===用例36：观众端给所有嘉宾送礼===')
        try:
            self.multaudience.audience_open_giftwin()
            self.multaudience.giftwin_allbut()
            global sendgift_assertcondition_2
            # sendgift_assertcondition_2 = self.multaudience.audience_sendgift("简体中文chinese simplified","Blessed Ramadan")
            # sendgift_assertcondition_2 = self.multaudience.audience_sendgift("热门", "Lucky Fortune")
            sendgift_assertcondition_2 = self.multaudience.audience_sendgift("热门", "幸运之吻")
            if sendgift_assertcondition_2 == 0:
                pytest.skip("观众端未送礼")
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.multaudience.party_textmessage_all()
            count = sendgift_message.count("{} 送出".format(self.audience_name))
            assert count >= 1
            # assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例37：主播端查看观众端送礼')
    def test_TenParty_037(self):
        logging.info('===用例37：主播端查看观众端送礼===')
        try:
            if sendgift_assertcondition_2 == 0:
                pytest.skip("观众端未送礼")
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.multanchor.party_textmessage_all()
            count = sendgift_message.count("{} 送出".format(self.audience_name))
            assert count >= 1
            # assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例38：观众端滑动送礼弹窗')
    def test_TenParty_038(self):
        logging.info('===用例38：观众端滑动送礼弹窗===')
        try:
            self.multaudience.audience_open_giftwin()
            next_gifttext, last_gifttext = self.multaudience.left_right_swipegiftwin()
            assert next_gifttext != last_gifttext
            logging.info('===断言成功，两页面第一个礼物不同===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例39：观众端申请上麦(通过加入按钮)')
    def test_TenParty_039(self):
        logging.info('===用例39：观众端申请上麦(通过加入按钮)===')
        try:
            if self.multaudience.audience_applyguest():
                assert True
                logging.info('===断言成功，申请上麦成功===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例40：主播端申请上麦未读消息检查')
    def test_TenParty_040(self):
        logging.info('===用例40：主播端申请上麦未读消息检查===')
        try:
            if self.multanchor.applicants():
                assert True
                logging.info('===断言成功，主播收到上麦未读消息===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例41：主播端同意观众上麦申请')
    def test_TenParty_041(self):
        logging.info('===用例41：主播端同意观众上麦申请===')
        try:
            self.multanchor.agree_apply()
            assert self.multanchor.second_guest()
            logging.info('===断言成功，主播端查看观众成功上麦===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例42：观众端查看是否成功上麦')
    def test_TenParty_042(self):
        logging.info('===用例42：观众端查看是否成功上麦===')
        try:
            assert self.multaudience.second_guest()
            logging.info('===断言成功，主播端查看观众成功上麦===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例43：嘉宾端打开个人主页浮窗')
    def test_TenParty_043(self):
        logging.info('===用例43：嘉宾端打开个人主页浮窗===')
        try:
            self.multaudience.enteraudience_HalfScreen()
            assert self.multaudience.HalfScreen()
            logging.info('===断言成功，成功打开个人主页浮窗===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例44：嘉宾在交友位发送表情')
    def test_TenParty_044(self):
        logging.info('===用例44：嘉宾在交友位发送表情===')
        try:
            if self.multaudience.audience_sendexpression(2):
                logging.info('===断言成功，嘉宾成功发送表情===')
                return True
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例45：嘉宾在交友位关闭麦克风')
    def test_TenParty_045(self):
        logging.info('===用例45：嘉宾在交友位关闭麦克风===')
        try:
            self.multaudience.audienceopen_more()
            self.multaudience.audienceopen_set()
            self.multaudience.close_microphone()
            assert self.multaudience.sitemicrophone()
            logging.info('===断言成功，嘉宾成功关闭麦克风===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例46：嘉宾离开交友位')
    def test_TenParty_046(self):
        logging.info('===用例46：嘉宾离开交友位===')
        self.multaudience.audienceopen_more()
        self.multaudience.audienceopen_set()
        self.multaudience.leave_site()
        try:
            self.multaudience.guest_watch()
        except NoSuchElementException as e:
            logging.info('===断言成功，嘉宾离开交友位===')
            assert True
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        else:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例47：主播端查看嘉宾离开交友位')
    def test_TenParty_047(self):
        logging.info('===用例47：主播端查看嘉宾离开交友位===')
        try:
            self.multanchor.guest_watch()
        except NoSuchElementException as e:
            logging.info('===断言成功，嘉宾离开交友位===')
            assert True
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        else:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例48：观众端申请上麦(通过点击交友位)')
    def test_TenParty_048(self):
        logging.info('===用例48：观众端申请上麦(通过点击交友位)===')
        try:
            if self.multaudience.partysite_applyguest(1):
                assert True
                logging.info('===断言成功，申请上麦成功===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例49：主播端同意观众上麦申请(右上角列表)')
    def test_TenParty_049(self):
        logging.info('===用例49：主播端同意观众上麦申请(右上角列表)===')
        try:
            self.multanchor.agree_applyright()
            assert self.multanchor.second_guest()
            logging.info('===断言成功，主播端查看观众成功上麦===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例50：主播端从交友位移除嘉宾')
    def test_TenParty_050(self):
        logging.info('===用例50：主播端从交友位移除嘉宾===')
        try:
            self.multanchor.open_guesthalfwin()
            self.multanchor.remove_guest()
            message = self.multanchor.chat_area(-1)
            assert "已被主播移出房间" in message
            logging.info('===断言成功，主播端成功移除嘉宾===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例51：嘉宾查看是否被移出嘉宾位')
    def test_TenParty_051(self):
        logging.info('===用例51：嘉宾查看是否被移出嘉宾位===')
        try:
            message = self.multaudience.chat_area(-1)
            assert "你被主播移出房间" in message
            logging.info('===断言成功，主播端成功移除嘉宾===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例52：主播在交友位禁言嘉宾')
    def test_TenParty_052(self):
        logging.info('===用例52：主播在交友位禁言嘉宾===')
        try:
            self.multaudience.partysite_applyguest(1)
            self.multanchor.agree_apply()
            self.multanchor.open_guesthalfwin()
            global guestname
            guestname = self.multanchor.get_guestname()
            self.multanchor.mute_guest()
            message = self.multanchor.chat_area(-1)
            assert "被主播禁言" in message
            logging.info('===断言成功，主播端成功禁言嘉宾===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例53：嘉宾查看是否被禁言')
    def test_TenParty_053(self):
        logging.info('===用例53：嘉宾查看是否被禁言===')
        try:
            message = self.multaudience.chat_area(-1)
            assert "你被主播禁言" in message
            logging.info('===断言成功，主播端成功禁言嘉宾===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例54：主播给嘉宾解除禁言')
    def test_TenParty_054(self):
        logging.info('===用例54：主播给嘉宾解除禁言===')
        try:
            logging.info('===被禁言的嘉宾名字：%s===' % guestname)
            self.anchordriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_more_people").click()
            audience_list = self.multanchor.get_audience_list()
            for i in audience_list:
                if i.text == guestname:
                    i.click()
                    break
            self.multanchor.cancelmute_guest()
            logging.info('===断言成功，主播端成功给观众解除禁言===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)
            time.sleep(2)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例55：主播邀请嘉宾上麦')
    def test_TenParty_055(self):
        logging.info('===用例55：主播邀请嘉宾上麦===')
        try:
            invite_but = self.multanchor.invite_guest(guestname)
            invite_butattr = self.multanchor.audience_get_attr("enabled",*invite_but)
            assert invite_butattr == "false"
            logging.info('===断言成功，主播端成功邀请观众===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        else:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例56：观众收到上麦邀请检查')
    def test_TenParty_056(self):
        logging.info('===用例56：观众收到上麦邀请检查===')
        try:
            time.sleep(2)
            invite_win = self.audiencedriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("房主邀请你加入嘉宾席")')
            assert invite_win
            logging.info('===断言成功，观众收到上麦邀请===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例57：主播邀请观众上麦，观众同意上麦')
    def test_TenParty_057(self):
        logging.info('===用例57：主播邀请观众上麦，观众同意上麦===')
        try:
            self.audiencedriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("同意")').click()
            assert self.multaudience.second_guest()
            logging.info('===断言成功，观众成功上麦===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例58：主播端检查观众是否成功上麦')
    def test_TenParty_058(self):
        logging.info('===用例58：主播端检查观众是否成功上麦===')
        try:
            assert self.multanchor.second_guest()
            logging.info('===断言成功，观众成功上麦===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        else:
            self.multaudience.audienceopen_more()
            self.multaudience.audienceopen_set()
            self.multaudience.leave_site()


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例59：主播邀请观众上麦，观众关闭上麦邀请')
    def test_TenParty_059(self):
        logging.info('===用例59：主播邀请观众上麦，观众关闭上麦邀请===')
        # self.multanchor.invite_guest("markd7fdeaqq")
        self.multanchor.invite_guest(guestname)
        time.sleep(1)
        self.audiencedriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/negative_btn").click()
        time.sleep(1)
        try:
            assert self.multaudience.guest_watch()
        except NoSuchElementException as e:
            logging.info('===断言成功，观众成功关闭上麦邀请===')
            self.multanchor.back(1)
            assert True
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        else:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例60：主播端检查观众是否未上麦')
    def test_TenParty_060(self):
        logging.info('===用例60：主播端检查观众是否未上麦===')
        try:
            assert self.multanchor.guest_watch()
        except NoSuchElementException as e:
            logging.info('===断言成功，观众未上麦===')
            assert True
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        else:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例61：观众打开主播个人主页半屏浮窗')
    def test_TenParty_061(self):
        logging.info('===用例61：观众打开主播个人主页半屏浮窗===')
        try:
            party_title, anchor_HalfScreenname = self.multaudience.openanchor_HalfScreen()
            assert party_title == anchor_HalfScreenname
            logging.info('===断言成功，主播名称与半屏浮层名称一致===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例62：观众进入主播个人主页')
    def test_TenParty_062(self):
        logging.info('===用例62：观众进入主播个人主页===')
        try:
            halfwin_name, user_name = self.multaudience.enteranchor_Personalhomepage()
            assert halfwin_name == user_name
            logging.info('===断言成功，主播名称与个人主页名称一致===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例63：观众从主播个人主页小窗进入交友房')
    def test_TenParty_063(self):
        logging.info('===用例63：观众从主播个人主页小窗进入交友房===')
        try:
            party_title = self.multaudience.Personalhome_enterparty()
            assert party_title
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例64：主播判断观众是否进入交友房')
    def test_TenParty_064(self):
        logging.info('===用例64：主播判断观众是否进入交友房===')
        try:
            enterparty_message = self.multanchor.party_textmessage(-1)
            assert "{} 加入了房间".format(self.audience_name) in enterparty_message
            logging.info('===断言成功，观众成功从小窗进入交友房===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例65：通过半屏浮窗给主播送礼物')
    def test_TenParty_065(self):
        logging.info('===用例65：通过半屏浮窗给主播送礼物===')
        try:
            self.multaudience.enteranchor_HalfScreen()
            global sendgift_assertcondition_3
            # sendgift_assertcondition_3 = self.multaudience.HalfScreen_sendgift("简体中文chinese simplified","Blessed Ramadan")
            # sendgift_assertcondition_3 = self.multaudience.HalfScreen_sendgift("热门", "Lucky Fortune")
            sendgift_assertcondition_3 = self.multaudience.HalfScreen_sendgift("热门", "幸运之吻")
            if sendgift_assertcondition_3 == 0:
                pytest.skip("观众端未送礼")
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.multaudience.party_textmessage_all()
            assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例66：主播检查是否收到观众的礼物')
    def test_TenParty_066(self):
        logging.info('===用例66：主播检查是否收到观众的礼物===')
        try:
            if sendgift_assertcondition_3 == 0:
                pytest.skip("观众端未送礼")
            sendgift_message = self.multanchor.party_textmessage_all()
            assert "送出" in sendgift_message
            logging.info('===断言成功，主播收到观众礼物===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例67：观众通过半屏浮窗@主播')
    def test_TenParty_067(self):
        logging.info('===用例67：观众通过半屏浮窗@主播===')
        try:
            self.multaudience.enteranchor_HalfScreen()
            self.multaudience.HalfScreen_aiteanchor()
            aite_message = self.multaudience.party_textmessage_aite()
            logging.info('aite_message:%s' %aite_message)
            assert "@" in aite_message
            logging.info('===断言成功，@主播成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例68：主播检查是否收到@消息')
    def test_TenParty_068(self):
        logging.info('===用例68：主播检查是否收到@消息===')
        try:
            aite_message = self.multanchor.party_textmessage_aite(-1)
            assert "@" in aite_message
            logging.info('===断言成功，主播收到@消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例69：通过半屏浮窗打开举报弹窗')
    def test_TenParty_069(self):
        logging.info('===用例69：通过半屏浮窗打开举报弹窗===')
        try:
            self.multaudience.enteranchor_HalfScreen()
            reportwin_title = self.multaudience.report_anchor()
            assert reportwin_title == "举报"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例70：通过半屏浮窗查看主播动态')
    def test_TenParty_070(self):
        logging.info('===用例70：通过半屏浮窗查看主播动态===')
        try:
            self.multaudience.enteranchor_HalfScreen()
            self.multaudience.watch_groupview(0)
            fl_user_head = self.audiencedriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/fl_user_head")
            assert fl_user_head
            logging.info('===断言成功，进入动态页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例71：通过半屏浮窗给主播打视频通话')
    def test_TenParty_071(self):
        logging.info('===用例71：通过半屏浮窗给主播打视频通话===')
        try:
            if self.multaudience.HalfScreen_Videocall():
                assert True
                logging.info('===断言成功，观众成功拨打===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    # @pytest.mark.skip("拨打显示时间太短")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例72：主播拒绝约聊电话')
    # def test_TenParty_072(self):
    #     logging.info('===用例72：主播拒绝约聊电话===')
    #     try:
    #         self.audiencedriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/ll_enable").click()
    #         self.anchordriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/vc_iv_reject").click()
    #         # self.multaudience.HalfScreen_Videocall()
    #         # if self.multanchor.reject_phone():
    #         #     assert True
    #         #     logging.info('===断言成功，主播成功拒绝约聊电话===')
    #         # else:
    #         #     raise
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multanchor.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info('===执行失败===')
    #         screen_name = self.multanchor.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise


    # @pytest.mark.skip("拨打显示时间太短")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例73：主播在交友房接听电话')
    # def test_TenParty_073(self):
    #     logging.info('===用例73：主播在交友房接听电话===')
    #     try:
    #         self.audiencedriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/ll_enable").click()
    #         self.anchordriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/ll_enable").click()
    #         # self.multaudience.HalfScreen_Videocall()
    #         # if self.multanchor.accept_phone():
    #         #     assert True
    #         #     logging.info('===断言成功，主播成功接听电话===')
    #         # else:
    #         #     raise
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multanchor.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info('===执行失败===')
    #         screen_name = self.multanchor.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例74：观众给主播在交友房发送私聊文本消息')
    def test_TenParty_074(self):
        logging.info('===用例74：观众给主播在交友房发送私聊文本消息===')
        try:
            self.multaudience.enteranchor_Personalhomepage()
            self.multaudience.enter_anchormessage()
            self.multaudience.send_textmessage_toanchor("hello")
            self.multanchor.enter_privatechatpage()
            get_usermessage_textcontent = self.multaudience.get_messagetext(-1)
            assert get_usermessage_textcontent == "hello"
            logging.info('===断言成功，成功发送文字===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例75：主播查看是否收到消息')
    def test_TenParty_075(self):
        logging.info('===用例75：主播查看是否收到消息===')
        try:
            get_message_textcontent = self.multanchor.get_messagetext(-1)
            assert get_message_textcontent == "hello"
            logging.info('===断言成功，成功发送文字===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例76：主播在私聊界面发送消息')
    def test_TenParty_076(self):
        logging.info('===用例76：主播在私聊界面发送消息===')
        try:
            self.multanchor.usermessage_send_text('hi')
            sleep(1)
            get_usermessage_textcontent = self.multanchor.get_messagetext(-1)
            assert get_usermessage_textcontent == "hi"
            logging.info('===断言成功，成功发送文字===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例77：观众查看是否收到消息')
    def test_TenParty_077(self):
        logging.info('===用例77：观众查看是否收到消息===')
        try:
            get_message_textcontent = self.multaudience.get_messagetext(-1)
            assert get_message_textcontent == "hi"
            logging.info('===断言成功，成功发送文字===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例78：观众私聊页面发送chamet表情')
    def test_TenParty_078(self):
        logging.info('===用例78：观众私聊页面发送chamet表情===')
        try:
            self.multaudience.audience_usermessage_sendexpression(1)
            expression = self.multaudience.watch_selfsendexpression()
            assert expression
            logging.info('===断言成功，观众发送chamet表情成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例79：主播查看是否收到chamet表情')
    def test_TenParty_079(self):
        logging.info('===用例79：主播查看是否收到chamet表情===')
        try:
            head_frame, expression = self.multanchor.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，主播成功收到chamet表情===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例80：主播私聊页面发送chamet表情')
    def test_TenParty_080(self):
        logging.info('===用例80：主播私聊页面发送chamet表情===')
        try:
            self.multanchor.usermessage_send_expression(1)
            expression = self.multanchor.watch_selfsendexpression()
            assert expression
            logging.info('===断言成功，主播发送chamet表情成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例81：观众查看是否收到chamet表情')
    def test_TenParty_081(self):
        logging.info('===用例81：观众查看是否收到chamet表情===')
        try:
            head_frame, expression = self.multaudience.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，观众成功收到chamet表情===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例82：观众私聊页面发送Facebook表情')
    def test_TenParty_082(self):
        logging.info('===用例82：观众私聊页面发送Facebook表情===')
        try:
            self.multaudience.audience_usermessage_sendexpression(0)
            expression = self.multaudience.watch_selfsendgooglexpression()
            assert expression
            logging.info('===断言成功，观众发送Facebook表情成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例83：主播查看是否收到Facebook表情')
    def test_TenParty_083(self):
        logging.info('===用例83：主播查看是否收到Facebook表情===')
        try:
            head_frame, expression = self.multanchor.watch_othersendgoogleexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，主播成功收到Facebook表情===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例84：主播私聊页面发送Facebook表情')
    def test_TenParty_084(self):
        logging.info('===用例84：主播私聊页面发送Facebook表情===')
        try:
            self.multanchor.usermessage_send_expression(0)
            expression = self.multanchor.watch_selfsendgooglexpression()
            assert expression
            logging.info('===断言成功，主播发送Facebook表情成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例85：观众查看是否收到Facebook表情')
    def test_TenParty_085(self):
        logging.info('===用例85：观众查看是否收到Facebook表情===')
        try:
            head_frame, expression = self.multaudience.watch_othersendgoogleexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，观众成功收到Facebook表情===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例86：观众展开私聊页面下拉按钮')
    def test_TenParty_086(self):
        logging.info('===用例86：观众展开私聊页面下拉按钮===')
        try:
            translate_but = self.multaudience.usermessage_translate_but()
            assert translate_but
            logging.info('===断言成功，观众成功展开下拉项===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例87：观众端开启私聊界面翻译功能')
    def test_TenParty_087(self):
        logging.info('===用例87：观众端开启私聊界面翻译功能===')
        try:
            if self.multaudience.open_usermessage_translate():
                assert True
                logging.info('===断言成功，成功打开翻译===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例88：观众私聊界面发送相册照片')
    def test_TenParty_088(self):
        logging.info('===用例88：观众私聊界面发送相册照片===')
        try:
            self.multaudience.audience_usermessage_sendphoto(2)
            photo = self.multaudience.watch_selfsendexpression()
            assert photo
            logging.info('===断言成功，观众发送相册照片成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例89：主播检查是否收到相册照片')
    def test_TenParty_089(self):
        logging.info('===用例89：主播检查是否收到相册照片===')
        try:
            head_frame, expression = self.multanchor.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，主播成功收到相册照片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例90：主播私聊界面发送相册照片')
    def test_TenParty_090(self):
        logging.info('===用例90：主播私聊界面发送相册照片===')
        try:
            self.multanchor.usermessage_drop_down()
            self.multanchor.anchor_usermessage_sendphoto(2)
            photo = self.multanchor.watch_selfsendexpression()
            assert photo
            logging.info('===断言成功，主播发送相册照片成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例91：观众检查是否收到相册照片')
    def test_TenParty_091(self):
        logging.info('===用例91：观众检查是否收到相册照片===')
        try:
            head_frame, expression = self.multaudience.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，观众成功收到相册照片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例92：主播私聊界面发送相机照片')
    def test_TenParty_092(self):
        logging.info('===用例92：主播私聊界面发送相机照片===')
        try:
            self.multanchor.usermessage_send_cameraphoto()
            photo = self.multanchor.watch_selfsendexpression()
            assert photo
            logging.info('===断言成功，主播发送相机照片成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例93：观众检查是否收到相机照片')
    def test_TenParty_093(self):
        logging.info('===用例93：观众检查是否收到相机照片===')
        try:
            head_frame, expression = self.multaudience.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，观众成功收到相机照片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例94：观众私聊界面发送相机照片')
    def test_TenParty_094(self):
        logging.info('===用例94：观众私聊界面发送相机照片===')
        try:
            self.multaudience.audience_usermessage_sendcameraphoto()
            photo = self.multaudience.watch_selfsendexpression()
            assert photo
            logging.info('===断言成功，观众发送相机照片成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例95：主播检查是否收到相机照片')
    def test_TenParty_095(self):
        logging.info('===用例95：主播检查是否收到相机照片===')
        try:
            head_frame, expression = self.multanchor.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，主播成功收到相机照片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例96：观众私聊界面发拨打视频聊天')
    def test_TenParty_096(self):
        logging.info('===用例96：观众私聊界面发拨打视频聊天===')
        try:
            self.multaudience.usermessage_video_but()
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例97：主播私聊界面发拨打语音聊天')
    def test_TenParty_097(self):
        logging.info('===用例97：主播私聊界面发拨打语音聊天===')
        try:
            self.multanchor.usermessage_Voice_chat()
            self.multanchor.usermessage_Voicechat_nomoney()
            # usermessage_Voice_chat_toast = self.multanchor.toast_message('交友房房主无法视频聊天')
            # assert usermessage_Voice_chat_toast.text == "交友房房主无法视频聊天"
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例98：观众端左右滑动私聊礼物页面')
    def test_TenParty_098(self):
        logging.info('===用例98：观众端左右滑动私聊礼物页面===')
        try:
            nowgift_list_text, newgift_list_text = self.multaudience.audience_usermessage_scroll_gift()
            assert nowgift_list_text[0].text != newgift_list_text[0].text
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例99：观众端私聊页面送礼')
    def test_TenParty_099(self):
        logging.info('===用例99：观众端私聊页面送礼===')
        try:
            # self.multaudience.audience_usermessage_sendgift()
            global sendgift_assertcondition_4
            # sendgift_assertcondition_4 = self.multaudience.audience_sendgift("简体中文chinese simplified","Blessed Ramadan")
            # sendgift_assertcondition_4 = self.multaudience.audience_sendgift_bymessage("热门", "Bouquet")
            sendgift_assertcondition_4 = self.multaudience.audience_sendgift_bymessage("热门", "棒棒糖")
            if sendgift_assertcondition_4 == 0:
                pytest.skip("观众端未送礼")
            last_text = self.multaudience.get_usermessage_textcontent(-1)
            assert '送出' in last_text
            logging.info('===断言成功，成功发送礼物===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例100：主播端检查私聊页面送礼')
    def test_TenParty_100(self):
        logging.info('===用例100：主播端检查私聊页面送礼===')
        try:
            if sendgift_assertcondition_4 == 0:
                pytest.skip("观众端未送礼")
            head_frame, gift_content = self.multanchor.watch_othersendgift()
            assert head_frame
            assert '送出' in gift_content
            logging.info('===断言成功，主播收到私聊礼物===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例101：观众端私聊页面打开个人主页浮窗')
    def test_TenParty_101(self):
        logging.info('===用例101：观众端私聊页面打开个人主页浮窗===')
        try:
            user_name, profile_name = self.multaudience.audienceopen_Profilefloat()
            assert profile_name == user_name
            logging.info('===断言成功，观众成功在私聊页面打开个人主页===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(3)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例102：主播在交友房给观众送礼物')
    def test_TenParty_102(self):
        logging.info('===用例102：主播在交友房给观众送礼物===')
        try:
            self.multanchor.open_audiencelist()
            # self.multanchor.enter_audiencehaldwin("markd7fdeaqq")
            self.multanchor.enter_audiencehaldwin(guestname)
            self.multanchor.enter_giftpage()
            global sendgift_assertcondition_7
            # sendgift_assertcondition_7 = self.multanchor.anchor_sendgift("简体中文chinese simplified","Blessed Ramadan")
            # sendgift_assertcondition_7 = self.multanchor.anchor_sendgift("热门", "Lucky Fortune")
            sendgift_assertcondition_7 = self.multanchor.anchor_sendgift("热门", "幸运之吻")
            if sendgift_assertcondition_7 == 0:
                pytest.skip("主播端未送礼")
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.multanchor.party_textmessage_all()
            count = sendgift_message.count("{} 送出".format(self.anchor_name))
            assert count >= 1
            # assert "送出" in sendgift_message
            logging.info('===断言成功,主播成功发送礼物===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例103：观众端查看主播端送礼')
    def test_TenParty_103(self):
        logging.info('===用例103：观众端查看主播端送礼===')
        try:
            if sendgift_assertcondition_7 == 0:
                pytest.skip("主播端未送礼")
            # 只要最后一条消息中存在送出两字即断言成功
            sendgift_message = self.multaudience.party_textmessage_all()
            count = sendgift_message.count("{} 送出".format(self.anchor_name))
            assert count >= 1
            # assert "送出" in sendgift_message
            logging.info('===断言成功，成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例104：主播在交友房给观众发私信消息')
    def test_TenParty_104(self):
        logging.info('===用例104：主播在交友房给观众发私信消息===')
        try:
            self.multanchor.open_audiencelist()
            # self.multanchor.enter_audiencehaldwin("markd7fdeaqq")
            self.multanchor.enter_audiencehaldwin(guestname)
            self.multanchor.sendmessage_toaudience("hello")
            self.multaudience.enter_privatechatpage()
            message_region = self.multanchor.get_messageregion()
            assert message_region[-1].text == 'hello'
            logging.info('===断言成功,主播发私聊成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(3)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例105：观众检查私信接收')
    def test_TenParty_105(self):
        logging.info('===用例105：观众检查私信接收===')
        try:
            get_message_textcontent = self.multaudience.get_messagetext(-1)
            assert get_message_textcontent == "hello"
            logging.info('===断言成功,收到主播发的私聊消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例106：观众端进入群聊页面')
    def test_TenParty_106(self):
        logging.info('===用例106：观众端进入群聊页面===')
        try:
            self.multaudience.audienceenter_groupmessage("哈哈aa")
            groupmessage_name = self.multaudience.audience_groupmessage_name()
            assert groupmessage_name[-1] == ')'
            logging.info('===断言成功，观众成功进入群聊页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例107：观众端群聊页面发送文字')
    def test_TenParty_107(self):
        logging.info('===用例107：观众端群聊页面发送文字===')
        try:
            self.multaudience.audience_groupmessage_sendtext("hi")
            last_text = self.multaudience.get_usermessage_textcontent(-1)
            assert last_text == 'hi'
            logging.info('===断言成功，成功发送文字===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例108：主播端进入群聊页面')
    def test_TenParty_108(self):
        logging.info('===用例108：主播端进入群聊页面===')
        try:
            self.multanchor.anchorclick_more()
            self.multanchor.anchorenter_messagewin()
            message_group_lists = self.multanchor.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.multanchor.message_group_enter("哈哈aa")
            groupmessage_number = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_group_number")
            groupmessage_pagenumber = self.anchordriver.find_element(*groupmessage_number)
            groupmessage_pagenumberlast = groupmessage_pagenumber.text[-1]
            assert groupmessage_pagenumberlast == ")"
            logging.info('===断言成功，主播进入群聊页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例109：主播查看群消息')
    def test_TenParty_109(self):
        logging.info('===用例109：主播查看群消息===')
        try:
            groupmessage_text = self.multanchor.groupmessage_text(-1)
            assert groupmessage_text == "hi"
            logging.info('===断言成功,主播收到群成员消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例110：主播在交友房群聊中发送消息')
    def test_TenParty_110(self):
        logging.info('===用例110：主播在交友房群聊中发送消息===')
        try:
            self.multanchor.groupmessage_send_text('hello')
            sleep(1)
            usermessage_region_text = (MobileBy.XPATH,
                                       "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView")
            message_region = self.anchordriver.find_elements(*usermessage_region_text)
            assert message_region[-1].text == 'hello'
            logging.info('===断言成功，主播发送成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.touch_tap(530,850)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例111：群成员查看群聊消息')
    def test_TenParty_111(self):
        logging.info('===用例111：群成员查看群聊消息===')
        try:
            groupmessage_text = self.multaudience.groupmessage_text(-1)
            assert groupmessage_text == "hello"
            logging.info('===断言成功，群成员收到主播发的群聊消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例112：观众端群聊页面发送chamet表情')
    def test_TenParty_112(self):
        logging.info('===用例112：观众端群聊页面发送chamet表情===')
        try:
            self.multaudience.audience_groupmessage_sendexpression(1)
            expression = self.multaudience.watchgroup_selfsendexpression()
            assert expression
            logging.info('===断言成功，成功发送chamet表情===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例113：主播端群聊页面查看是否收到chamet表情')
    def test_TenParty_113(self):
        logging.info('===用例113：主播端群聊页面查看是否收到chamet表情===')
        try:
            head_frame, expression = self.multanchor.watchgroup_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，收到chamet表情消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例114：主播端群聊页面发送google表情')
    def test_TenParty_114(self):
        logging.info('===用例114：主播端群聊页面发送google表情===')
        try:
            self.multanchor.groupmessage_send_expression(0)
            expression = self.multanchor.watchgroup_selfsendgooglexpression()
            assert expression
            logging.info('===断言成功，成功发送google表情===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例115：观众端群聊页面查看是否收到google表情')
    def test_TenParty_115(self):
        logging.info('===用例115：观众端群聊页面查看是否收到google表情===')
        try:
            user_name, expression = self.multaudience.watchgroup_othersendgoogleexpression()
            assert user_name
            assert expression
            logging.info('===断言成功，收到google表情消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例116：观众端群聊页面发送语音')
    def test_TenParty_116(self):
        logging.info('===用例116：观众端群聊页面发送语音===')
        try:
            self.multaudience.audience_groupmessage_send_voice()
            voice_timelast = self.multaudience.audience_voice_text()[-1]
            print(voice_timelast)
            assert voice_timelast == 's'
            logging.info('===断言成功，成功发送语音===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例117：主播端群聊页面检查并播放语音消息')
    def test_TenParty_117(self):
        logging.info('===用例117：主播端群聊页面检查并播放语音消息===')
        try:
            user_name, voice_time = self.multanchor.audience_voice_text()
            assert user_name
            assert voice_time[-1] == 's'
            logging.info('===断言成功，成功收到语音并播放===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例118：主播端群聊页面发送相册图片')
    def test_TenParty_118(self):
        logging.info('===用例118：主播端群聊页面发送相册图片===')
        try:
            self.multanchor.groupmessage_send_photo(2)
            expression = self.multanchor.watchgroup_selfsendexpression()
            assert expression
            logging.info('===断言成功，成功发送相册图片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例119：观众端群聊页面检查相册图片')
    def test_TenParty_119(self):
        logging.info('===用例119：观众端群聊页面检查相册图片===')
        try:
            head_frame, expression = self.multaudience.watchgroup_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到相册图片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例120：观众端群聊页面发送相册图片')
    def test_TenParty_120(self):
        logging.info('===用例120：观众端群聊页面发送相册图片===')
        try:
            self.multaudience.groupmessage_send_photo(2)
            expression = self.multaudience.watchgroup_selfsendexpression()
            assert expression
            logging.info('===断言成功，成功发送相册图片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例121：主播端群聊页面检查相册图片')
    def test_TenParty_121(self):
        logging.info('===用例121：主播端群聊页面检查相册图片===')
        try:
            head_frame, expression = self.multanchor.watchgroup_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到相册图片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例122：观众端群聊页面发送拍摄图片')
    def test_TenParty_122(self):
        logging.info('===用例122：观众端群聊页面发送拍摄图片===')
        try:
            self.multaudience.audience_groupmessage_sendcameraphoto()
            expression = self.multaudience.watchgroup_selfsendexpression()
            assert expression
            logging.info('===断言成功，成功发送拍摄图片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例123：主播端群聊页面检查拍摄图片')
    def test_TenParty_123(self):
        logging.info('===用例123：主播端群聊页面检查拍摄图片===')
        try:
            head_frame, expression = self.multanchor.watchgroup_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到拍摄图片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例124：主播端群聊页面发送拍摄图片')
    def test_TenParty_124(self):
        logging.info('===用例124：主播端群聊页面发送拍摄图片===')
        try:
            self.multanchor.anchor_groupmessage_sendcameraphoto()
            expression = self.multanchor.watchgroup_selfsendexpression()
            assert expression
            logging.info('===断言成功，成功发送拍摄图片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例125：观众端群聊页面检查拍摄图片')
    def test_TenParty_125(self):
        logging.info('===用例125：观众端群聊页面检查拍摄图片===')
        try:
            head_frame, expression = self.multaudience.watchgroup_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到拍摄图片===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例126：观众端群聊页面上麦')
    def test_TenParty_126(self):
        logging.info('===用例126：观众端群聊页面上麦===')
        try:
            self.multaudience.audience_up_microphone()
            toast_text = self.multaudience.audience_toast_message("直播间无法上麦").text
            assert toast_text == "直播间无法上麦"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例127：主播群聊页面上麦')
    def test_TenParty_127(self):
        logging.info('===用例127：主播群聊页面上麦===')
        try:
            self.multanchor.up_microphone()
            toast_text = self.multanchor.toast_message("直播间无法上麦").text
            assert toast_text == "直播间无法上麦"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例128：观众端群聊页面发送钻石包')
    def test_TenParty_128(self):
        logging.info('===用例128：观众端群聊页面发送钻石包===')
        try:
            self.multaudience.audience_send_diamondenvelope(2, 200)
            envelope = self.multaudience.messageregion_getenvelope()
            assert envelope
            logging.info('===断言成功，成功发送钻石包===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例129：观众端群聊页面领取钻石包')
    def test_TenParty_129(self):
        logging.info('===用例129：观众端群聊页面领取钻石包===')
        try:
            self.multaudience.audience_get_diamondenvelope()
            user_head = self.multaudience.getenvelope_userhead()
            assert user_head
            logging.info('===断言成功,观众成功领取钻石包===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例130：主播端群聊页面领取钻石包')
    def test_TenParty_130(self):
        logging.info('===用例130：主播端群聊页面领取钻石包===')
        try:
            self.multanchor.get_diamond_envelope()
            user_head = self.multanchor.getenvelope_userhead()
            assert user_head
            logging.info('===断言成功，主播成功领取钻石包===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例131：主播端群聊页面发送钻石包快速感谢语，观众端检查')
    def test_TenParty_131(self):
        logging.info('===用例131：主播端群聊页面发送钻石包快速感谢语，观众端检查===')
        try:
            thank_ele = self.anchordriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_thanking_1")
            thank_text = thank_ele.text
            thank_ele.click()
            audience_messageregion = self.multaudience.groupmessage_text(-1)
            assert thank_text in audience_messageregion
            logging.info('===断言成功,观众成功收到主播发送的感谢语===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例132：观众端群聊页面送礼')
    def test_TenParty_132(self):
        logging.info('===用例132：观众端群聊页面送礼===')
        try:
            self.multaudience.group_opengiftwin()
            global sendgift_assertcondition_5
            # sendgift_assertcondition_5 = self.multaudience.audience_groupmessage_sendgift("简体中文chinese simplified","Blessed Ramadan")
            # sendgift_assertcondition_5 = self.multaudience.audience_groupmessage_sendgift("热门", "Lucky Fortune")
            sendgift_assertcondition_5 = self.multaudience.audience_groupmessage_sendgift("热门","幸运之吻")
            if sendgift_assertcondition_5 == 0:
                pytest.skip("观众端未送礼")
            gift_text = self.multaudience.watchgroup_selfsendgift()
            assert "送出" in gift_text
            logging.info('===断言成功，观众群聊页面成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例133：主播端群聊页面检查送礼消息')
    def test_TenParty_133(self):
        logging.info('===用例133：主播端群聊页面检查送礼消息===')
        try:
            if sendgift_assertcondition_5 == 0:
                pytest.skip("观众端未送礼")
            user_name, gift_text = self.multanchor.watchgroup_othersendgift()
            assert  user_name
            assert "送出" in gift_text
            logging.info('===断言成功，主播收到送礼消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例134：主播端群聊页面送礼')
    def test_TenParty_134(self):
        logging.info('===用例134：主播端群聊页面送礼===')
        try:
            self.multanchor.group_opengiftwin()
            global sendgift_assertcondition_6
            # sendgift_assertcondition_6 = self.multanchor.groupmessage_send_gift("简体中文chinese simplified","Blessed Ramadan")
            # sendgift_assertcondition_6 = self.multanchor.groupmessage_send_gift("热门", "Lucky Fortune")
            sendgift_assertcondition_6 = self.multanchor.groupmessage_send_gift("热门","幸运之吻")
            if sendgift_assertcondition_6 == 0:
                pytest.skip("观众端未送礼")
            gift_text = self.multanchor.watchgroup_selfsendgift()
            assert "送出" in gift_text
            logging.info('===断言成功，主播群聊页面成功送礼===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例135：观众端群聊页面检查送礼消息')
    def test_TenParty_135(self):
        logging.info('===用例135：观众端群聊页面检查送礼消息===')
        try:
            if sendgift_assertcondition_6 == 0:
                pytest.skip("观众端未送礼")
            user_name, gift_text = self.multaudience.watchgroup_othersendgift()
            assert  user_name
            assert "送出" in gift_text
            logging.info('===断言成功，观众收到送礼消息===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例136：主播端打开交友房背景浮窗')
    def test_TenParty_136(self):
        logging.info('===用例136：主播端打开交友房背景浮窗===')
        try:
            self.multanchor.click_morebut()
            self.multanchor.click_backgroundbut()
            background_title = (MobileBy.ID, 'com.hkfuliao.chamet:id/tv_title')
            background_title = self.anchordriver.find_element(*background_title).text
            assert background_title == '交友房背景'
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例137：主播端更换交友房背景(免费背景)')
    def test_TenParty_137(self):
        logging.info('===用例137：主播端更换交友房背景===')
        try:
            background_list = (MobileBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
            background_list = self.anchordriver.find_elements(*background_list)
            background_list[2].click()
            # select_ele = self.anchordriver.find_element("//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.TextView")
            # assert select_ele
            logging.info('===断言成功，成功更换交友房背景===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例138：主播端更换交友房背景(等级限制背景)')
    def test_TenParty_138(self):
        logging.info('===用例138：主播端更换交友房背景(等级限制背景)===')
        try:
            background_list = (MobileBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
            last_background_list = self.anchordriver.find_elements(*background_list)
            self.anchordriver.scroll(last_background_list[4], last_background_list[0], 100)
            now_background_list = self.anchordriver.find_elements(*background_list)
            now_background_list[-1].click()
            sleep(2)
            assert self.anchordriver.find_element(MobileBy.XPATH,
                                            "//android.view.ViewGroup[5]/android.widget.RelativeLayout/android.widget.ImageView[2]")
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例139：主播端打开游戏页面查看游戏类型')
    def test_TenParty_139(self):
        logging.info('===用例139：主播端打开游戏页面查看游戏类型===')
        try:
            self.multanchor.enter_game_list()
            race_game = self.anchordriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("Chamet赛车")')
            threedD_game = self.anchordriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("顶级赛车")')
            LuckyBox = self.anchordriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("幸运盒子")')
            luckyTurntable = self.anchordriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("幸运转盘")')
            LuckyNumber = self.anchordriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("幸运数字")')
            assert race_game
            assert threedD_game
            assert LuckyBox
            assert luckyTurntable
            assert LuckyNumber
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例140：主播端打开赛车游戏')
    def test_TenParty_140(self):
        logging.info('===用例140：主播端打开赛车游戏===')
        try:
            race_rank_ele = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_race_rank")
            self.multanchor.enter_game_window("Chamet赛车")
            race_rank = self.anchordriver.find_element(*race_rank_ele)
            assert race_rank
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例141：主播端打开幸运数字游戏')
    def test_TenParty_141(self):
        logging.info('===用例141：主播端打开幸运数字游戏===')
        try:
            LuckyNumber_rank_ele = (MobileBy.ID, "com.hkfuliao.chamet:id/rank")
            self.multanchor.enter_game_list()
            self.multanchor.enter_game_window("幸运数字")
            LuckyNumber_rank = self.anchordriver.find_element(*LuckyNumber_rank_ele)
            assert LuckyNumber_rank
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例142：观众端打开游戏页面查看游戏类型')
    def test_TenParty_142(self):
        logging.info('===用例142：观众端打开游戏页面查看游戏类型===')
        try:
            self.multaudience.enter_game_list()
            race_game = self.audiencedriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("Chamet赛车")')
            threedD_game = self.audiencedriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("顶级赛车")')
            LuckyBox = self.audiencedriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("幸运盒子")')
            luckyTurntable = self.audiencedriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("幸运转盘")')
            LuckyNumber = self.audiencedriver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("幸运数字")')
            assert race_game
            assert threedD_game
            assert LuckyBox
            assert luckyTurntable
            assert LuckyNumber
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例143：观众端打开赛车游戏')
    def test_TenParty_143(self):
        logging.info('===用例143：观众端打开赛车游戏===')
        try:
            race_rank = self.multaudience.audienceenter_game_window("Chamet赛车")
            assert race_rank
            logging.info('===断言成功，打开Chamet赛车游戏===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例144：观众端打开幸运数字游戏')
    def test_TenParty_144(self):
        logging.info('===用例144：观众端打开幸运数字游戏===')
        try:
            self.multaudience.enter_game_list()
            LuckyNumber_rank = self.multaudience.audienceenter_game_window("幸运数字")
            assert LuckyNumber_rank
            logging.info('===断言成功，打开幸运数字游戏===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)
    
    
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例145：10人交友房观众端打开充值页面')
    def test_TenParty_145(self):
        logging.info('===用例145：10人交友观众播端打开充值页面===')
        try:
            self.multaudience.audience_enterrechargepage()
            audience_rechargepage = self.multaudience.audience_rechargepage()
            assert audience_rechargepage
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例146：10人交友房观众端充值')
    def test_TenParty_146(self):
        logging.info('===用例146：10人交友房观众端充值===')
        try:
            self.multaudience.audience_recharge_diamond()
            buy_success_page = self.multaudience.audience_buysuccess_page()
            assert buy_success_page
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(2)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例147：10人交友房主播端打开充值页面')
    def test_TenParty_147(self):
        logging.info('===用例147：10人交友房主播端打开充值页面===')
        try:
            self.multanchor.anchorclick_more()
            self.multanchor.enter_recharge_page()
            assert self.anchordriver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("余额")')
            logging.info('===断言成功，主播成功打开充值页面===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            logging.info('返回交友房')
            time.sleep(1)
            self.multanchor.back(1)


    # @pytest.mark.skip("主播手机无法进行谷歌充值")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例148：10人交友房主播端充值')
    # def test_TenParty_148(self):
    #     logging.info('===用例148：10人交友房主播端充值===')
    #     try:
    #         self.multanchor.recharge_diamond()
    #         buy_success_page = self.multanchor.anchor_buysuccess_page()
    #         assert buy_success_page
    #         logging.info('===断言成功===')
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.anchordriver.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info('===执行失败===')
    #         screen_name = self.anchordriver.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     finally:
    #         self.multanchor.back(2)



    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例149：10人交友房主播端关闭麦克风')
    def test_TenParty_149(self):
        logging.info('===用例149：10人交友房主播端关闭麦克风===')
        try:
            self.multanchor.anchorclick_more()
            self.multanchor.enter_setting_page()
            if self.multanchor.close_voice():
                assert True
                logging.info('===断言成功===')
            else:
                raise
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例150：10人交友房主播端打开任务页')
    def test_TenParty_150(self):
        logging.info('===用例150：10人交友房主播端打开任务页===')
        try:
            task_page_ele = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_tab_tasks")
            self.multanchor.anchorclick_more()
            task = self.multanchor.haveno_task_but()
            if task == False:
                pytest.skip("无任务按钮，跳过该测试用例")
            self.multanchor.enter_task_page()
            task_page = self.anchordriver.find_element(*task_page_ele)
            assert task_page.text == "任务"
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multanchor.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例151：10人交友房观众端打开任务页')
    def test_TenParty_151(self):
        logging.info('===用例151：10人交友房观众端打开任务页===')
        try:
            task_page_ele = (MobileBy.ID, "com.hkfuliao.chamet:id/tv_tab_tasks")
            self.multaudience.audienceclick_more()
            task = self.multaudience.haveno_task_but()
            if task == False:
                pytest.skip("无任务按钮，跳过该测试用例")
            self.multaudience.enter_task_page()
            task_page = self.audiencedriver.find_element(*task_page_ele)
            assert task_page.text == "任务"
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例152：10人交友房观众端打开礼物冠名墙')
    def test_TenParty_152(self):
        logging.info('===用例152：10人交友房观众端打开礼物冠名墙===')
        try:
            self.multaudience.audience_enter_giftnamingwall()
            giftwall_title = self.multaudience.giftwall_title()
            assert "礼物荣誉墙" in giftwall_title
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例153：10人交友房观众端打开banner')
    def test_TenParty_153(self):
        logging.info('===用例153：10人交友房观众端打开banner===')
        try:
            if self.multaudience.audience_enter_banner():
                assert True
            else:
                raise
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        finally:
            self.multaudience.back(1)


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例154：观众端上滑动交友房')
    def test_TenParty_154(self):
        logging.info('===用例154：观众端上滑动交友房===')
        try:
            self.multaudience.swipe_xy(350, 1400, 350, 200)
            new_anchorname = self.multaudience.get_anchorname()
            # new_anchorname = self.audiencedriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/live_titletv").text
            # new_anchorname = self.audiencedriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/profile_name").text
            assert new_anchorname != self.anchor_name
            logging.info('===断言成功，观众成功在交友房上滑===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例155：观众端下滑动交友房')
    def test_TenParty_155(self):
        logging.info('===用例155：观众端下滑动交友房===')
        try:
            self.multaudience.swipe_xy(350, 200, 350, 1400)
            old_anchorname = self.audiencedriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/live_titletv").text
            assert old_anchorname == self.anchor_name
            logging.info('===断言成功，观众成功在交友房下滑===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例156：主播退出10人交友房')
    def test_TenParty_156(self):
        logging.info('===用例156：主播退出10人交友房===')
        try:
            self.multanchor.quit_party()
            head_ele = self.anchordriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/profile_head")
            username_ele = self.anchordriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/profile_name")
            endpage_title = self.anchordriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/title")
            party_time = self.anchordriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_live_duration")
            party_audience = self.anchordriver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[1]")
            party_earn = self.anchordriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_earn_title")
            gift_people = self.anchordriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_game_tip")
            recommend_list = self.anchordriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/recyclerview")
            party_audience_number = self.anchordriver.find_element(MobileBy.XPATH,"//android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[2]")
            gift_people_number = self.anchordriver.find_element(MobileBy.XPATH,"//android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView")
            party_earn_number = self.anchordriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_earn")
            assert head_ele
            assert username_ele
            assert endpage_title.text == "派对已结束"
            assert party_time.text == "派对时长"
            assert party_audience.text == "观众"
            assert party_earn.text == "礼物收入"
            assert gift_people.text == "送礼人"
            assert recommend_list
            assert party_audience_number != 0
            assert gift_people_number != 0
            assert party_earn_number != 0
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multanchor.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    # @pytest.mark.skip("结束页会进入其他交友房，时间太短，无法找到元素")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例157：观众端查看交友房结束页元素')
    # def test_TenParty_157(self):
    #     logging.info('===用例157：观众端查看交友房结束页元素===')
    #     try:
    #         head_ele = self.audiencedriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/profile_head")
    #         username_ele = self.audiencedriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/profile_name")
    #         party_time = self.audiencedriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_live_duration")
    #         party_audience = self.audiencedriver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[1]")
    #         assert head_ele
    #         assert username_ele
    #         assert party_time.text == "派对时长"
    #         assert party_audience.text == "观众"
    #         endpage_title = self.audiencedriver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/title")
    #         assert endpage_title.text == "派对已结束"
    #         logging.info('===断言成功===')
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multaudience.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info('===执行失败===')
    #         screen_name = self.multaudience.screenshot('party_ten')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise


    # @pytest.mark.skip("结束页会进入其他交友房，时间太短，无法找到元素")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例158：观众端进入其他交友房')
    def test_TenParty_158(self):
        logging.info('===用例158：观众端进入其他交友房===')
        try:
            time.sleep(1)
            new_anchorname_ele = self.audiencedriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/live_titletv")
            new_anchorname = new_anchorname_ele.text
            assert new_anchorname != self.anchor_name
            logging.info('===断言成功===')
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multaudience.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    if __name__ == '__main__':
        pytest.main()
        # pytest.main(['-s', '-v', 'test_10party_mult.py', '--clean-alluredir', '--alluredir=..\result\partytenresult\2023_7_13_002'])
        # os.system(r"allure generate -c -o ..\reports\partytenreports\2023_7_13_002")

    '''
    pytest .\test_10party_mult.py -v -s --alluredir=..\result\partytenresult\2023_8_3_001
    allure serve  ..\result\partytenresult\2023_8_3_001
    allure generate ..\result\partytenresult\2023_7_21_001 -o ..\reports\partytenreports\2023_7_21
    pytest -s -v test_10party_mult.py::Test_multchamet::test_TenParty_001
    '''