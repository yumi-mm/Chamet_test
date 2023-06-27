from common.partytencommon.multparty_star_end import anchorparty_Start_End
# from common.partytencommon.multparty_star_end import audienceeparty_Start_End
from appium.webdriver.common.mobileby import MobileBy
import logging
import pytest
import allure
from time import sleep


class Test_multchamet(anchorparty_Start_End):
    which_party = 0

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
            num1 = len(self.anchordriver.find_elements(MobileBy.XPATH,
                                                       "//android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout"))
            print(num1)
            assert num1 == 5
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


    @allure.severity(allure.severity_level.BLOCKER)
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

    @pytest.mark.skip(reason='头像不是必须，跳过执行')
    @allure.severity(allure.severity_level.BLOCKER)
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

    @pytest.mark.skip(reason='语言不是必须，跳过执行')
    @allure.severity(allure.severity_level.BLOCKER)
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
            # self.multaudience.audience_party_tab_Btn()
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            party_username = self.multaudience.audience_enter_tenparty(self.which_party)
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
        finally:
            self.multaudience.back(1)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例15：观众进入交友房进场座驾')
    def test_TenParty_015(self):
        logging.info('===用例15：观众进入交友房进场座驾===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.multaudience.audience_enter_tenparty(self.which_party)
            assert self.multaudience.enterparty_car()
            logging.info('===断言成功，存在进场座驾===')
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
        finally:
            self.multaudience.back(1)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例16：观众进入交友房进场标签')
    def test_TenParty_016(self):
        logging.info('===用例16：观众进入交友房进场标签===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.multaudience.audience_enter_tenparty(self.which_party)
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
        finally:
            self.multaudience.back(1)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例17：观众进入交友房进场消息提醒')
    def test_TenParty_017(self):
        logging.info('===用例17：观众进入交友房进场消息提醒===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.multaudience.audience_enter_tenparty(self.which_party)
            enterparty_message = self.multaudience.party_textmessage()
            assert "加入了房间" in enterparty_message
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
        finally:
            self.multaudience.back(1)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例18：观众端交友房警告消息检查')
    def test_TenParty_018(self):
        logging.info('===用例18：观众端交友房警告消息检查===')
        try:
            party_list_num = self.multaudience.party_list()
            if party_list_num == 0:
                pytest.skip("没有交友房，跳过该测试用例")
            self.multaudience.audience_enter_tenparty(self.which_party)
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
            enterparty_message = self.multanchor.party_textmessage()
            assert "加入了房间" in enterparty_message
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

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例23：观众端发送文字正常向前滚动')
    def test_TenParty_023(self):
        logging.info('===用例23：观众端发送文字正常向前滚动===')
        try:
            self.partyten.audience_speak_list(["test1", "test2"])
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

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例24：主播端发送文字正常向前滚动')
    def test_TenParty_024(self):
        logging.info('===用例24：主播端发送文字正常向前滚动===')
        try:
            self.partyten.anchor_speak_list("test_2")
            chat_area = self.partyten.chat_area(-1)
            # 断言最后一个消息是否为第二次发的
            assert chat_area == "test_2"
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


    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例9：观众端申请上麦(通过点击交友位)')
    # def test_TenParty_009(self):
    #     logging.info('===用例9：观众端申请上麦(通过点击交友位)===')
    #     try:
    #         if self.multaudience.partysite_applyguest(1):
    #             assert True
    #             logging.info('===断言成功，申请上麦成功===')
    #         else:
    #             raise
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
    #
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例10：主播端同意上麦')
    # def test_TenParty_010(self):
    #     logging.info('===用例10：主播端同意上麦===')
    #     try:
    #         self.anchordriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_invite").click()
    #         self.anchordriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/live_queue_invite").click()
    #         self.anchordriver.back()
    #         assert self.anchordriver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout[1]")
    #         logging.info('===断言成功，主播端同意上麦===')
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
    #
    #
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例11：主播移除嘉宾')
    # def test_TenParty_011(self):
    #     logging.info('===用例11：主播移除嘉宾===')
    #     try:
    #         audience_site = (MobileBy.XPATH,"//android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout[1]")
    #         self.anchordriver.find_element(*audience_site).click()
    #         self.anchordriver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_remove").click()
    #         message = self.multanchor.chat_area(-1)
    #         assert "已被主播移出房间" in message
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

    if __name__ == '__main__':
        pytest.main()

    '''
    pytest .\test_10party_mult.py -v -s --alluredir=..\result\2023_6_9_016
    allure serve  ..\result\2023_6_9_016
    pytest -s -v test_10party_mult.py::Test_multchamet::test_TenParty_001
    '''