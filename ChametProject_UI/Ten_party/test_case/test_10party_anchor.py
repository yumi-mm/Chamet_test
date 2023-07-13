from common.partytencommon.party_Start import party_Start_End
from appium.webdriver.common.mobileby import MobileBy
import logging
import pytest
import allure
from time import sleep


@allure.epic("项目名称：10人交友房")
@allure.issue("BUG链接：http://zentao.floa.vip/index.php?m=project&f=build&projectID=243")
@allure.testcase("测试用例链接：http://zentao.floa.vip/index.php?m=testcase&f=browse&productID=3")
@allure.feature('交友房10人房——主播端功能')
class Test_chamet(party_Start_End):

    # @allure.story('创建交友房')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例1：进入创建交友房页面')
    def test_TenParty_001(self):
        logging.info('===用例1：进入创建交友房页面===')
        try:
            PreEnter_butname = self.driver.find_element(*self.partyten.partyPreviewPage_enter).text
            assert PreEnter_butname == "创建交友房"
            logging.info('===断言成功===')
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例2：默认交友房预览页为10人房')
    def test_TenParty_002(self):
        logging.info('===用例2：默认交友房预览页为10人房===')
        try:
            self.partyten.enter_party_PreviewPage()
            # 预览页出现十个交友位
            num1 = len(self.driver.find_elements(MobileBy.XPATH,"//android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout"))
            print(num1)
            assert num1 == 5
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例3：创建10人交友房')
    def test_TenParty_003(self):
        logging.info('===用例3：创建10人交友房===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            # 房主在交友位上
            assert self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/user_head")
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


    # @pytest.story('交友房消息区')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例4：交友房警告消息是否存在')
    def test_TenParty_004(self):
        logging.info('===用例4：交友房警告消息是否存在===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            # 警告消息是否存在
            assert self.driver.find_element(*self.partyten.warning_message)
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例5：交友房警告消息内容检查')
    def test_TenParty_005(self):
        logging.info('===用例5：交友房警告消息内容检查===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            # 警告消息内容是否正确
            warning_message_content = self.driver.find_element(*self.partyten.warning_message).text
            assert warning_message_content == "欢迎来到Chamet 交友房！警告：直播期间严禁出现色情、粗俗、暴力、未成年人等相关情况。人工智能系统每天24 小时对其进行审查。一旦违反规定，将受到严惩！"
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例6：交友房主播端发言')
    def test_TenParty_006(self):
        logging.info('===用例6：交友房主播端发言===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.anchor_speak_list("test")
            chat_area = self.partyten.chat_area(-1)
            # 断言发送的消息是否出现在消息区
            assert chat_area == "test"
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例7：发送文字正常向前滚动')
    def test_TenParty_007(self):
        logging.info('===用例7：发送文字正常向前滚动===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.anchor_speak_list(["test_1","test_2"])
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.title('用例8：消息区聊天消息可下滑')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_TenParty_008(self):
        logging.info('===用例8：消息区聊天消息可下滑===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.anchor_speak_list(["1","2","3","4","5","6","7","8","9","10","11"])
            self.partyten.swipe_xy(200, 900, 200, 1000)
            assert self.partyten.chat_area(-1) != "11"
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例9：消息区聊天消息可上滑')
    def test_TenParty_009(self):
        logging.info('===用例9：消息区聊天消息可上滑===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.anchor_speak_list(["1","2","3","4","5","6","7","8","9","10","11"])
            self.partyten.swipe_xy(200, 900, 200, 1000)
            self.partyten.swipe_xy(200, 1000, 200, 900)
            assert self.partyten.chat_area(-1) != "10"
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


    # @pytest.story('交友房送礼')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例10：打开送礼物弹窗')
    def test_TenParty_010(self):
        logging.info('===用例10：打开送礼物弹窗===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.open_gift_window()
            gift_lst = self.partyten.gift_lst()
            assert gift_lst
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例11：主播不可给自己送礼')
    def test_TenParty_011(self):
        logging.info('===用例11：主播不可给自己送礼===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.open_gift_window()
            gift_lst = self.partyten.gift_lst()
            gift_lst[0].click()
            send_butattr = self.partyten.get_attr("enabled", *self.partyten.send_gift_but)
            assert send_butattr == "false"
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例12：左滑动送礼弹窗')
    def test_TenParty_012(self):
        logging.info('===用例12：左滑动送礼弹窗===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.open_gift_window()
            gift_list_text = self.partyten.gift_lst()
            gift_list_text[0].click()
            nowgift_list_text = self.partyten.gift_lst()
            self.partyten.swipe_xy(600,1200,100,1200)
            newgift_list_text = self.partyten.gift_lst()
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例13：右滑动送礼弹窗')
    def test_TenParty_013(self):
        logging.info('===用例13：右滑动送礼弹窗===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.open_gift_window()
            gift_list_text = self.partyten.gift_lst()
            gift_list_text[0].click()
            self.partyten.swipe_xy(600,1200,100,1200)
            nowgift_list_text = self.partyten.gift_lst()
            self.partyten.swipe_xy(100,1200,600,1200)
            newgift_list_text = self.partyten.gift_lst()
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


    # @allure.story('交友房背景')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('用例14：打开交友房背景浮窗')
    def test_TenParty_014(self):
        logging.info('===用例14：打开交友房背景浮窗===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.background).click()
            background_title = self.driver.find_element(*self.partyten.background_title).text
            assert background_title == '交友房背景'
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('用例15：更换交友房背景(免费背景))')
    def test_TenParty_015(self):
        logging.info('===用例15：更换交友房背景===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.background).click()
            background_list = self.driver.find_elements(*self.partyten.background_list)
            background_list[2].click()
            logging.info('===断言成功===')
            screen_name = self.partyten.screenshot('party_ten')
            logging.info(f'截图成功，图片为{screen_name}')
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例16：更换交友房背景(等级限制背景)')
    def test_TenParty_016(self):
        logging.info('===用例16：更换交友房背景(等级限制背景)===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.background).click()
            background_list = self.driver.find_elements(*self.partyten.background_list)
            self.driver.scroll(background_list[4],background_list[0],100)
            now_background_list = self.driver.find_elements(*self.partyten.background_list)
            now_background_list[-1].click()
            assert self.driver.find_element(MobileBy.XPATH,"//android.view.ViewGroup[5]/android.widget.RelativeLayout/android.widget.ImageView[2]")
            # 获取toast提示
            # background_level_toast = self.partytencommon.toast_message('20级')
            # assert background_level_toast.text == "升级到20级可免费获得！"
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例17：交友房中打开消息列表')
    def test_TenParty_017(self):
        logging.info('===用例17：交友房中打开消息列表===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            # 存在Chamet客服则断言成功
            assert self.driver.find_element(*self.partyten.chamet_customer_service)
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


    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例18：进入私聊页面')
    def test_TenParty_018(self):
        logging.info('===用例18：进入私聊页面===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            message_page_namelaststr = self.driver.find_element(*self.partyten.message_page_name).text[-1]
            assert message_page_namelaststr != ")"
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
    @allure.title('用例19：私聊页面发送文字')
    def test_TenParty_019(self):
        logging.info('===用例19：私聊页面发送文字===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_send_text('hello')
            sleep(1)
            message_region = self.driver.find_elements(*self.partyten.usermessage_region_text)
            assert message_region[-1].text == 'hello'
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例20：私聊页面发送表情')
    def test_TenParty_020(self):
        logging.info('===用例20：私聊页面发送表情===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_send_expression(1)
            expression_list = self.driver.find_elements(*self.partyten.usermessage_region_expression)
            print(len(expression_list))
            assert len(expression_list) >= 1
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例21：私聊页面发送谷歌表情')
    def test_TenParty_021(self):
        logging.info('===用例21：私聊页面发送谷歌表情===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_send_expression(0)
            google_expression_list = self.driver.find_elements(*self.partyten.google_expression_list)
            assert len(google_expression_list) >= 1
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例22：展开私聊页面下拉按钮')
    def test_TenParty_022(self):
        logging.info('===用例22：展开私聊页面下拉按钮===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_drop_down()
            usermessage_translate = self.driver.find_element(*self.partyten.usermessage_translate)
            assert usermessage_translate
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例23：开启私聊界面翻译功能')
    def test_TenParty_023(self):
        logging.info('===用例23：开启私聊界面翻译功能===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_drop_down()
            self.partyten.usermessage_open_translate()
            # usermessage_open_translate_toast = self.partytencommon.toast_message('翻译已开启')
            # assert usermessage_open_translate_toast.text == "翻译已开启"
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



    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例24：私聊界面发送相册照片')
    def test_TenParty_024(self):
        logging.info('===用例24：私聊界面发送相册照片===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_drop_down()
            if self.partyten.usermessage_send_photo(2):
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例25：私聊界面发送相机照片')
    def test_TenParty_025(self):
        logging.info('===用例25：私聊界面发送相机照===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_drop_down()
            if self.partyten.usermessage_send_cameraphoto():
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例26：私聊界面发拨打语音聊天')
    def test_TenParty_026(self):
        logging.info('===用例26：私聊界面发拨打语音聊天===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_drop_down()
            self.partyten.usermessage_Voice_chat()
            usermessage_Voice_chat_toast = self.partyten.toast_message('交友房房主无法视频聊天')
            assert usermessage_Voice_chat_toast.text == "交友房房主无法视频聊天"
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例27：左右滑动私聊礼物页面')
    def test_TenParty_027(self):
        logging.info('===用例27：左右滑动私聊礼物页面===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_open_giftpage()
            nowgift_list_text,newgift_list_text = self.partyten.usermessage_scroll_gift()
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

    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例28：私聊页面送礼')
    def test_TenParty_028(self):
        logging.info('===用例28：私聊页面送礼===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            self.partyten.usermessage_open_giftpage()
            self.partyten.usermessage_sendgift()
            text = self.driver.find_elements(*self.partyten.usermessage_region_text)
            assert '送出' in text[-1].text
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例29：私聊页面打开个人主页浮窗')
    def test_TenParty_029(self):
        logging.info('===用例29：私聊页面打开个人主页浮窗===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_user_lists = self.partyten.message_user_list()
            if len(message_user_lists) == 0:
                pytest.skip("聊天列表中没有私聊记录，跳过该测试用例")
            self.partyten.message_user_enter()
            user_name=self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_name").text
            self.partyten.open_Profile_float()
            profile_name=self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/profile_name").text
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例30：10人交友房中进入群聊页面')
    def test_TenParty_030(self):
        logging.info('===用例30：10人交友房中进入群聊页面===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            groupmessage_pagenumber = self.driver.find_element(*self.partyten.groupmessage_number)
            groupmessage_pagenumberlast = groupmessage_pagenumber.text[-1]
            assert groupmessage_pagenumberlast == ")"
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
    @allure.title('用例31：群聊页面发送文字')
    def test_TenParty_031(self):
        logging.info('===用例31：群聊页面发送文字===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            self.partyten.groupmessage_send_text('hello')
            sleep(1)
            message_region = self.driver.find_elements(*self.partyten.usermessage_region_text)
            assert message_region[-1].text == 'hello'
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例32：群聊页面发送表情')
    def test_TenParty_032(self):
        logging.info('===用例32：群聊页面发送表情===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            self.partyten.usermessage_send_expression(1)
            expression_list = self.driver.find_elements(*self.partyten.groupmessage_region_expression)
            assert len(expression_list) >= 1
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例33：群聊页面发送google表情')
    def test_TenParty_033(self):
        logging.info('===用例33：群聊页面发送google表情===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            self.partyten.usermessage_send_expression(0)
            google_expression_list = self.driver.find_elements(*self.partyten.groupgoogle_expression_list)
            assert len(google_expression_list) >= 1
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例34：群聊页面发送语音')
    def test_TenParty_034(self):
        logging.info('===用例34：群聊页面发送语音===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            self.partyten.groupmessage_send_voice()
            voice_timelast = self.partyten.voice_text()[-1]
            print(voice_timelast)
            assert voice_timelast == 's'
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例35：群聊页面发送相册图片')
    def test_TenParty_035(self):
        logging.info('===用例35：群聊页面相册图片===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            if self.partyten.groupmessage_send_photo(2):
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例36：群聊页面发送拍摄图片')
    def test_TenParty_036(self):
        logging.info('===用例36：群聊页面发送拍摄图片===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            if self.partyten.groupmessage_send_cameraphoto():
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例37：群聊页面上麦')
    def test_TenParty_037(self):
        logging.info('===用例37：群聊页面上麦===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            self.partyten.up_microphone()
            toast_text = self.partyten.toast_message("直播间无法上麦").text
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例38：群聊页面发送钻石包')
    def test_TenParty_038(self):
        logging.info('===用例38：群聊页面发送钻石包===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            self.partyten.send_diamond_envelope(2,1000)
            envelope = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("幸运红包")')
            assert envelope
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例39：群聊页面领取钻石包')
    def test_TenParty_039(self):
        logging.info('===用例39：群聊页面领取钻石包===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            self.partyten.send_diamond_envelope(2,1000)
            self.partyten.get_diamond_envelope()
            user_head = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/civ_user_head")
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


    @allure.severity(allure.severity_level.MINOR)
    @allure.title('用例40：群聊页面送礼')
    def test_TenParty_040(self):
        logging.info('===用例40：群聊页面送礼===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.driver.find_element(*self.partyten.partymessage).click()
            message_group_lists = self.partyten.message_group_list()
            if len(message_group_lists) == 0:
                pytest.skip("聊天列表中没有群聊记录，跳过该测试用例")
            self.partyten.message_group_enter()
            self.partyten.groupmessage_send_gift(0)
            gift_messageimage = self.driver.find_elements(*self.partyten.group_giftmessageimage)
            assert gift_messageimage
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
    @allure.title('用例41：10人交友房主播端打开充值页面')
    def test_TenParty_041(self):
        logging.info('===用例41：10人交友房主播端打开充值页面===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.partyten.enter_recharge_page()
            assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("我的钻石")')
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
    @allure.title('用例42：10人交友房主播端充值')
    def test_TenParty_042(self):
        logging.info('===用例42：10人交友房主播端充值===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.partyten.enter_recharge_page()
            self.partyten.recharge_diamond()
            buy_success_page = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_card_icon")
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
    @allure.title('用例43：10人交友房主播端关闭麦克风')
    def test_TenParty_043(self):
        logging.info('===用例43：10人交友房主播端关闭麦克风===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            self.partyten.enter_setting_page()
            if self.partyten.close_voice():
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
    @allure.title('用例44：10人交友房主播端打开任务页')
    def test_TenParty_044(self):
        logging.info('===用例44：10人交友房主播端打开任务页===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.driver.find_element(*self.partyten.more_but).click()
            task = self.partyten.haveno_task_but()
            if task == False:
                pytest.skip("无任务按钮，跳过该测试用例")
            self.partyten.enter_task_page()
            task_page = self.driver.find_element(*self.partyten.task_page)
            assert task_page.text == "任务"
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
    @allure.title('用例45：打开观众列表')
    def test_TenParty_045(self):
        logging.info('===用例45：打开观众列表===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.enter_invit_window()
            audience_ele = self.driver.find_element(*self.partyten.audience_ele)
            assert audience_ele
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
    @allure.title('用例46：10人交友房主播端打开赛车游戏')
    def test_TenParty_046(self):
        logging.info('===用例46：10人交友房主播端打开赛车游戏===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.enter_game_window("Chamet赛车")
            race_rank = self.driver.find_element(*self.partyten.race_rank)
            assert race_rank
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
    @allure.title('用例47：10人交友房主播端打开幸运数字游戏')
    def test_TenParty_047(self):
        logging.info('===用例47：10人交友房主播端打开幸运数字游戏===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.enter_game_window("幸运数字")
            LuckyNumber_rank = self.driver.find_element(*self.partyten.LuckyNumber_rank)
            assert LuckyNumber_rank
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
    @allure.title('用例48：10人交友房主播端打开礼物冠名墙')
    def test_TenParty_048(self):
        logging.info('===用例48：10人交友房主播端打开礼物冠名墙===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.enter_giftnamingwall()
            giftwall_title = self.driver.find_element(*self.partyten.giftwall_title).text
            assert giftwall_title == "礼物荣誉墙"
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
    @allure.title('用例49：10人交友房主播端打开banner')
    def test_TenParty_049(self):
        logging.info('===用例49：10人交友房主播端打开banner===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            if self.partyten.enter_banner():
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
    @allure.title('用例50：退出10人交友房')
    def test_TenParty_050(self):
        logging.info('===用例50：退出10人交友房===')
        try:
            self.partyten.enter_party_PreviewPage()
            self.partyten.enter_tenparty()
            self.partyten.quit_party()
            assert self.driver.find_element(*self.partyten.partyPreviewPage_enter)
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
    pytest .\test_10party_anchor.py -v -s --alluredir=..\result\2023_6_9_016
    allure serve  ..\result\2023_6_9_016
    pytest -s -v test_10party_anchor.py::Test_chamet::test_TenParty_001
    '''
