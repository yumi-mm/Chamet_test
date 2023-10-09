# -*- coding: utf-8 -*-

import os
import io
import re
import sys
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

#改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import time
from businessView.login_phoneView import LoginView
from common.mypage_multi.mypage_multi_Start_End import mypage_multi_Start_End
# from appium.webmandriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import logging
import pytest
import allure
from time import sleep
from businessView.login_phoneView import LoginView
from common.mypage_multi.multiMypage_man import MultiMan
from common.mypage_multi.multiMypage_woman import MultiWoman
# if data[:3] == codecs.BOM_UTF8:
#     data = data[3:]
#     print(data.decode('utf-8'))


class Test_multi_mypage(mypage_multi_Start_End):

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例1：我的页面-个人头像-个人主页')
    def test_homepage01(self):
        logging.info("===我的页面-个人头像-个人主页===")
        try:
            # 男生个人主页
            self.multiman.tap(960, 2262)
            self.multiman.tab_Mine_Btn()
            self.multiman.tab_Mine_Head()
            global man_pageSelfIntroduction,man_pagePersonalName
            man_pageSelfIntroduction = self.multiman.user_ownPage_selfIntroductionEle()
            man_pagePersonalName = self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName)
            logging.info("断言成功")
            self.mandriver.find_element(*MultiMan.user_own_pageGobackBtn).click()
            # 获取元素
            global man_pageUserId
            self.multiman.my_Profile_entry()
            man_pageUserId = self.mandriver.find_element(*MultiMan.myProfile_ID_Number).text
            self.multiman.system_goback_key()
            global man_groupNameText
            man_groupNameText='今日也莫人陪我'
            global group_intro
            group_intro = 'hhhhyyygg'


            # 女生个人主页
            # 85手机
            # self.multiwoman.tap(930, 2123)
            # 126手机
            self.multiwoman.tap(963, 2268)
            self.multiwoman.tab_Mine_Btn_126()
            self.multiwoman.tap(116, 486)
            time.sleep(2)
            global woman_pagePersonalName
            woman_pagePersonalName = self.womandriver.find_element(*MultiWoman.user_own_pagePersonalName).text
            assert self.womandriver.find_element(*MultiWoman.user_own_pagePersonalInformationText), "没有通过头像找到个人主页元素"
            logging.info("断言成功")
            self.womandriver.find_element(*MultiWoman.user_own_pageGobackBtn).click()
            global group_remove_womanName
            group_remove_womanName = 'Mary33470557…啊bb...'


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-个人头像男-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            screen_name = self.multiwoman.screenshot('我的页面-个人头像女-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise





    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例22、23：留言-列表及消息未读数')
    def test_homepage22(self):
        logging.info("===留言-列表及消息未读数===")
        try:
            self.multiwoman.find_search_id(man_pageUserId)
            time.sleep(5)
            self.multiman.tab_Mine_Btn()
            self.multiman.tap(930, 2123)
            entry_UnReadNum_case=self.multiman.messages_entry_UnReadNumIDEle()
            # print(UnReadNum_case44)
            self.mandriver.find_element(*MultiMan.messages_entry_All).click()
            assert self.mandriver.find_element(*MultiMan.messages_title).text == '消息'
            assert self.mandriver.find_element(*MultiMan.messages_system_EntryTitle).text == 'Chamet团队'
            assert self.mandriver.find_element(*MultiMan.messages_customerService_entryTitle).text == 'Chamet客服'
            if entry_UnReadNum_case != False:
                logging.info("===留言-入口有消息未读数===")
                UnReadNum_lists=self.multiman.messages_UnReadNum_lists()
                assert UnReadNum_lists ==int(entry_UnReadNum_case)
                logging.info("断言成功")
            else:
                logging.info("===留言-入口没有消息未读数，断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-列表及消息未读数')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-列表及消息未读数')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例24：留言-chamet团队')
    def test_homepage24(self):
        logging.info("===留言-chamet团队===")
        try:
            entry_text=self.mandriver.find_element(*MultiMan.messages_system_entryText).text
            self.mandriver.find_element(*MultiMan.messages_system_EntryAll).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_system_title).text == 'Chamet团队'
            if entry_text=='没有消息':
                logging.info("===留言-chamet团队无消息===")
                assert self.mandriver.find_element(*MultiMan.messages_system_emptyIcon)
                assert self.mandriver.find_element(*MultiMan.messages_system_emptyText).text == '无消息'
                self.mandriver.find_element(*MultiMan.messages_system_goback).click()
            else:
                logging.info("===留言-chamet团队有消息===")
                assert self.mandriver.find_element(*MultiMan.messages_system_messagesContentAll)
                # assert self.mandriver.find_elements(*MultiMan.messages_system_learnMoreText)
                self.mandriver.find_element(*MultiMan.messages_system_goback).click()
            logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-chamet团队')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-chamet团队')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例25：留言-chamet客服')
    def test_homepage25(self):
        logging.info("===留言-chamet客服===")
        try:
            assert self.mandriver.find_element(*MultiMan.messages_customerService_entryText).text== '任何问题？联络我'
            self.mandriver.find_element(*MultiMan.messages_customerService_EntryAll).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_customerService_title).text == '在线客服'
            assert self.mandriver.find_element(*MultiMan.messages_customerService_Container)
            assert self.mandriver.find_element(*MultiMan.messages_customerService_problemChoice)
            assert self.mandriver.find_element(*MultiMan.messages_customerService_InputText)
            self.mandriver.find_element(*MultiMan.messages_customerService_goback).click()
            logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-chamet客服')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-chamet客服')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例26：留言-陌生人留言消息及未读数')
    def test_homepage26(self):
        logging.info("===留言-陌生人留言消息及未读数===")
        try:
            # self.multiwoman.find_search_id()
            time.sleep(1)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_entryUserAndText).text=='{}: hhhhh'.format(woman_pagePersonalName)
            assert '{}: '.format(woman_pagePersonalName) in self.mandriver.find_element(*MultiMan.messages_Stranger_entryUserAndText).text
            self.mandriver.find_element(*MultiMan.messages_Stranger_entryHeadPic).click()
            self.multiman.system_goback_key()
            assert self.multiman.messages_Stranger_entryUnread_Ele()
            self.mandriver.find_element(*MultiMan.messages_Stranger_entryHeadPic).click()
            assert self.multiman.messages_Stranger_userListUnread_Ele()
            logging.info('===返回-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言消息及未读数')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言消息及未读数')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例27：留言-陌生人留言-陌生人列表')
    def test_homepage27(self):
        logging.info("===留言-陌生人列表===")
        try:
            assert self.mandriver.find_element(*MultiMan.messages_Stranger_title).text=='陌生人消息'
            first_userName=self.mandriver.find_elements(*MultiMan.messages_Stranger_UserNameList)[0].text
            # print(first_userName)
            # print(self.mandriver.find_elements(*MultiMan.messages_Stranger_UserEntryList))
            assert self.mandriver.find_element(*MultiMan.messages_Stranger_UserUnread)
            self.mandriver.find_elements(*MultiMan.messages_Stranger_UserNameList)[0].click()
            assert first_userName == woman_pagePersonalName
            assert self.mandriver.find_element(*MultiMan.messages_Stranger_userTitleName).text==first_userName
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-陌生人列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-陌生人列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例28：留言-陌生人留言-一对一更多个人主页')
    def test_homepage28(self):
        logging.info("===留言-陌生人留言-一对一更多个人主页===")
        try:
            self.mandriver.find_elements(*MultiMan.messages_Stranger_userHalfPagePopoverHead)[0].click()
            # self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
            first_userName = self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverName).text
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverHeadFrame)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverNation)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverNationName)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverLanguage)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverLevel)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverFollowBtn)
            self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverHead).click()
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == first_userName
            self.multiman.system_goback_key()
            logging.info('===返回-断言成功===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例29：留言-陌生人留言-一对一个人浮层送礼')
    def test_homepage29(self):
        logging.info("===留言-陌生人留言-一对一个人浮层送礼===")
        try:
            time.sleep(3)
            self.mandriver.find_elements(*MultiMan.messages_Stranger_userHalfPagePopoverHead)[0].click()
            self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverSendGiftBtn).click()
            nowgift_list_text, newgift_list_text = self.multiman.usermessage_scroll_gift()
            assert nowgift_list_text != newgift_list_text
            sendgift_assertcondition_4 = self.multiman.audience_sendgift_bymessage("热门", "4th Anniversary")
            if sendgift_assertcondition_4 == 0:
                pytest.skip("送礼方未送礼")
            else:
                last_text = self.multiman.get_usermessage_textcontent(-1)
                assert '送出' in last_text
                logging.info('===断言成功，送礼方成功发送礼物===')
                head_frame, gift_content = self.multiwoman.watch_othersendgift()
                assert head_frame
                assert '送出' in gift_content
                logging.info('===断言成功，收到私聊礼物===')
            # self.multiman.tap(576, 543)
            logging.info('===断言成功===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人浮层送礼滑动')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人浮层送礼滑动')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例30：留言-陌生人留言-一对一更多个人浮层视频通话')
    def test_homepage30(self):
        logging.info("===留言-陌生人留言-一对一更多个人浮层视频通话===")
        try:
            # self.multiman.tap(826,1000)
            self.multiwoman.tap(912,149)
            self.mandriver.find_elements(*MultiMan.messages_Stranger_userHalfPagePopoverHead)[0].click()
            # self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
            video_butele = (MobileBy.ANDROID_UIAUTOMATOR, 'text("视频通话")')
            video_but = self.mandriver.find_element(*video_butele)
            logging.info('===拨打语言聊天===')
            video_but.click()
            if self.multiman.Phone114_getPermission_checkPopover():
                self.multiman.Phone114_getPermission_checkPopover()
                self.multiman.Permission_114Phone_MediaPopoverConfirmBtnEle()
            if self.multiwoman.get_permission_checkPopover():
                self.multiwoman.get_permission_checkPopover()
                self.multiwoman.get_permission_checkPopover()
            time.sleep(2)
            self.multiman.not_available_win()
            logging.info('====一对一更多个人浮层视频通话-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
            screen_name = self.multiwoman.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
            screen_name = self.multiwoman.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例31：留言-陌生人留言-一对一输入框')
    def test_homepage31(self):
        logging.info("===留言-陌生人留言-一对一输入框===")
        try:
            name_text = "hello123"
            InputEdit_case=self.mandriver.find_element(*MultiMan.messages_Stranger_InputEdit)
            InputEdit_case.send_keys(name_text)
            InputEdit_case.click()
            self.mandriver.find_element(*MultiMan.messages_Stranger_InputSendBtn).click()
            time.sleep(3)
            assert self.mandriver.find_elements(*MultiMan.messages_Stranger_TextInputContentText)[-1].text == name_text
            time.sleep(2)
            assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
            # assert self.multiwoman.messages_Stranger_translateContentEle()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-一对一输入框')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-一对一输入框')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例32：留言-陌生人留言-表情')
    def test_homepage32(self):
        logging.info("===留言-陌生人留言-表情===")
        try:
            self.multiman.audience_usermessage_sendexpression(1)
            expression = self.multiman.watch_selfsendexpression()
            assert expression
            logging.info('===断言成功，发送chamet表情成功===')
            head_frame, expression = self.multiwoman.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到chamet表情===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例33：留言-陌生人留言-搜索表情')
    def test_homepage33(self):
        logging.info("===留言-陌生人留言-搜索表情===")
        try:
            self.multiman.audience_usermessage_sendexpression(0)
            expression = self.multiman.watch_selfsendgooglexpression()
            assert expression
            logging.info('===断言成功，发送Facebook表情成功===')
            head_frame, expression = self.multiwoman.watch_othersendgoogleexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到Facebook表情===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-搜索表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-搜索表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例34：留言-陌生人留言-更多翻译')
    def test_homepage34(self):
        logging.info("===留言-陌生人留言-更多翻译===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Stranger_inputMoreBtn).click()
            self.mandriver.find_element(*MultiMan.messages_Stranger_TranslateBtn).click()
            # usermessage_Voice_chat_toast = self.multiman.toast_message('翻译已关闭')
            # assert usermessage_Voice_chat_toast.text == "翻译已关闭"
            name_text = "hehehehe"
            InputEdit_case = self.womandriver.find_element(*MultiWoman.messages_Stranger_InputEdit)
            InputEdit_case.send_keys(name_text)
            InputEdit_case.click()
            self.womandriver.find_element(*MultiWoman.messages_Stranger_InputSendBtn).click()
            # assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
            assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
            time.sleep(3)
            assert self.mandriver.find_elements(*MultiMan.messages_Stranger_TextInputContentText)[-1].text == name_text
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-更多翻译')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-更多翻译')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例35：留言-陌生人留言-更多相册')
    def test_homepage35(self):
        logging.info("===留言-陌生人留言-更多相册===")
        try:
            self.multiwoman.tap(912,149)
            # self.mandriver.find_element(*MultiMan.messages_Stranger_inputMoreBtn).click()
            self.mandriver.find_element(*MultiMan.messages_Stranger_phonePictureBtn).click()
            if len(self.mandriver.find_elements(*MultiMan.messages_Stranger_phonePictureListSelect))==0:
                pytest.skip("用户相册为空")
            self.mandriver.find_elements(*MultiMan.messages_Stranger_phonePictureListSelect)[0].click()
            time.sleep(2)
            self.mandriver.find_element(*MultiMan.messages_Stranger_phonePictureListConfirmBtn).click()
            time.sleep(2)
            photo = self.multiman.watch_selfsendexpression()
            assert photo
            logging.info('===断言成功，发送相册照片成功===')
            head_frame, expression = self.multiwoman.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到相册照片===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-更多相册')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-更多相册')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例36：留言-陌生人留言-更多相机')
    def test_homepage36(self):
        logging.info("===留言-陌生人留言-更多相机===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Stranger_CameraBtn).click()
            time.sleep(2)
            self.mandriver.find_element(*MultiMan.messages_Stranger_114CameraTakeBtn).click()
            time.sleep(5)
            self.mandriver.find_element(*MultiMan.messages_Stranger_114CameraTakeDoneBtn).click()
            photo = self.multiman.watch_selfsendexpression()
            assert photo
            logging.info('===断言成功，发送相机照片成功===')
            head_frame, expression = self.multiwoman.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到相机照片===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-更多相机')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-更多相机')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例37：留言-陌生人留言-更多视频聊天')
    def test_homepage37(self):
        logging.info("===留言-陌生人留言-更多视频聊天===")
        try:
            self.multiman.usermessage_video_but()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-更多视频聊天')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言-更多视频聊天')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例38：留言-陌生人留言-送礼')
    def test_homepage38(self):
        logging.info('===留言-陌生人留言-送礼===')
        try:
            self.mandriver.find_element(*MultiMan.messages_Stranger_SendGiftBtn).click()
            # global sendgift_assertcondition_4
            sendgift_assertcondition_4 = self.multiman.audience_sendgift_bymessage("热门", "4th Anniversary")
            if sendgift_assertcondition_4 == 0:
                pytest.skip("送礼方未送礼")
            else:
                last_text = self.multiman.get_usermessage_textcontent(-1)
                assert '送出' in last_text
                logging.info('===断言成功，送礼方成功发送礼物===')
                head_frame, gift_content = self.multiwoman.watch_othersendgift()
                assert head_frame
                assert '送出' in gift_content
                logging.info('===断言成功，收到私聊礼物===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info('===执行失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言-送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例39：留言-陌生人留言返回')
    def test_homepage39(self):
        logging.info("===留言-陌生人留言返回===")
        try:
            self.multiman.find_element(*MultiMan.messages_Stranger_userGoback).click()
            time.sleep(2)
            assert len(self.multiman.find_elements(*MultiMan.messages_Stranger_userListUnread1))==0
            # assert self.multiman.messages_Stranger_userListUnread_Ele()==False
            # self.mandriver.find_element(*MultiMan.messages_Stranger_goback).click()
            # assert self.mandriver.find_element(*MultiMan.messages_title).text == '留言'
            logging.info('===返回-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-陌生人留言返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-陌生人留言返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise





    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例40：留言-好友一对一列表-用户头像跳转')
    def test_homepage40(self):
        logging.info("===留言-好友一对一列表-用户头像跳转===")
        try:
            woman_st_name = self.mandriver.find_element(By.XPATH,"//*[@text='{}']".format(woman_pagePersonalName))
            woman_st_name.click()
            # self.mandriver.find_element(*MultiMan.messages_User_33470557Strange).click()
            self.mandriver.find_element(*MultiMan.messages_User_StrangeTopName).click()
            self.mandriver.find_element(*MultiMan.user_own_pageFollowBtn).click()
            self.multiman.system_goback_key()
            self.multiman.system_goback_key()
            self.multiman.system_goback_key()
            self.multiman.system_goback_key()
            new_text = "user2223"
            InputEdit_case = self.womandriver.find_element(*MultiWoman.messages_Stranger_InputEdit)
            InputEdit_case.send_keys(new_text)
            InputEdit_case.click()
            self.womandriver.find_element(*MultiWoman.messages_Stranger_InputSendBtn).click()
            time.sleep(3)
            assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text==new_text
            # self.multiman.system_goback_key()
            self.multiman.tap(960, 2262)
            self.mandriver.find_element(*MultiMan.messages_entry_All).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_User_ListCountryIcon)
            # assert self.mandriver.find_element(*MultiMan.messages_User_ListLevelIcon)
            assert self.mandriver.find_element(*MultiMan.messages_User_userContentText).text==new_text
            assert self.multiman.messages_User_userContentUnreadDotEle()
            expected_name1=self.mandriver.find_elements(*MultiMan.messages_User_EntryUserName)[0].text
            self.mandriver.find_elements(*MultiMan.messages_User_EntryHead)[0].click()
            expected_name2 = self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text
            assert expected_name2==expected_name1
            self.multiman.system_goback_key()
            logging.info('===断言成功===')



            # global user_haveOrNot
            # User_EntryHeadEle_case=self.multiman.messages_User_EntryHeadEle()
            # if User_EntryHeadEle_case!=False and len(User_EntryHeadEle_case)!=0:
            #     user_haveOrNot=1
            #     logging.info("===留言-有一对一消息，开始点击头像===")
            #     OneUserEntryUserNameList_case=self.multiman.messages_User_EntryUserNameEle()
            #     # print(type(OneUserEntryUserNameList))
            #     if OneUserEntryUserNameList_case!=False:
            #         logging.info('===有用户头像且获取到了昵称元素===')
            #         expected_name1=OneUserEntryUserNameList_case.text
            #         # print(OneUserEntryUserNameList_case.text)
            #         self.mandriver.find_elements(*MultiMan.messages_User_EntryHead)[0].click()
            #         expected_name2=self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text
            #         # print(self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text)
            #         assert expected_name2==expected_name1
            #         self.multiman.system_goback_key()
            #         assert self.mandriver.find_elements(*MultiMan.messages_User_EntryHead)
            #     # else:
            #     #     logging.info('===有用户头像但是没有获取到昵称元素===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一列表-用户头像跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一列表-用户头像跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例41：留言-好友一对一列表-列表跳转')
    def test_homepage41(self):
        logging.info("===留言-好友一对一列表-列表跳转===")
        try:
            expected_name1 = self.mandriver.find_elements(*MultiMan.messages_User_EntryUserName)
            expected_name2=expected_name1[0].text
            expected_name1[0].click()
            assert self.mandriver.find_element(*MultiMan.messages_User_StrangeTopName).text == expected_name2

            # self.mandriver.find_element(*MultiMan.messages_User_33470557Strange).click()
            # assert  self.mandriver.find_element(*MultiMan.messages_User_StrangeTopName).text=='Mary33470557…啊bbb哦哦哦'
            # self.multiman.system_goback_key()
            # assert self.multiman.messages_User_userContentUnreadDotEle()==False
            # self.mandriver.find_element(*MultiMan.messages_User_33470557Strange).click()
            # logging.info('===断言成功===')
            #
            # assert self.mandriver.find_element(*MultiMan.messages_User_userContentText).text == new_text
            # assert self.multiman.messages_User_userContentUnreadDotEle()
            # expected_name1 = self.mandriver.find_elements(*MultiMan.messages_User_EntryUserName)[0].text
            # self.mandriver.find_elements(*MultiMan.messages_User_EntryHead)[0].click()
            # expected_name3 = self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一列表-列表跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一列表-列表跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例42：留言-好友一对一-更多个人主页')
    def test_homepage42(self):
        logging.info("===留言-好友一对一-更多个人主页===")
        try:
            self.mandriver.find_elements(*MultiMan.messages_Stranger_userHalfPagePopoverHead)[0].click()
            # self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
            first_userName = self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverName).text
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverHeadFrame)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverNation)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverNationName)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverLanguage)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverLevel)
            # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverFollowBtn)
            self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverHead).click()
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == first_userName
            self.multiman.system_goback_key()
            logging.info('===返回-断言成功===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-更多个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-更多个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例43：留言-好友一对一-更多个人浮层送礼滑动')
    def test_homepage43(self):
        logging.info("===留言-好友一对一-更多个人浮层送礼滑动===")
        try:
            time.sleep(3)
            self.mandriver.find_elements(*MultiMan.messages_Stranger_userHalfPagePopoverHead)[0].click()
            # self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
            self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverSendGiftBtn).click()
            nowgift_list_text, newgift_list_text = self.multiman.usermessage_scroll_gift()
            # self.multiman.tap(29, 543)
            # self.multiman.system_goback_key()
            # print(nowgift_list_text)
            # print(newgift_list_text)
            assert nowgift_list_text != newgift_list_text
            sendgift_assertcondition_4 = self.multiman.audience_sendgift_bymessage("热门", "4th Anniversary")
            if sendgift_assertcondition_4 == 0:
                pytest.skip("送礼方未送礼")
            else:
                last_text = self.multiman.get_usermessage_textcontent(-1)
                assert '送出' in last_text
                logging.info('===断言成功，送礼方成功发送礼物===')
                head_frame, gift_content = self.multiwoman.watch_othersendgift()
                assert head_frame
                assert '送出' in gift_content
                logging.info('===断言成功，收到私聊礼物===')
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-更多个人浮层送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-更多个人浮层送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例44：留言-好友一对一-更多视频通话')
    def test_homepage44(self):
        logging.info("===留言-好友一对一-更多视频通话===")
        try:
            self.multiman.tap(882,170)
            self.mandriver.find_elements(*MultiMan.messages_Stranger_userHalfPagePopoverHead)[0].click()
            # self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
            video_butele = (MobileBy.ANDROID_UIAUTOMATOR, 'text("视频通话")')
            video_but = self.mandriver.find_element(*video_butele)
            logging.info('===拨打语言聊天===')
            video_but.click()
            if self.multiman.Phone114_getPermission_checkPopover():
                self.multiman.Phone114_getPermission_checkPopover()
                self.multiman.Permission_114Phone_MediaPopoverConfirmBtnEle()
            self.multiman.not_available_win()
            logging.info('====一对一更多个人浮层视频通话-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-更多视频通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-更多视频通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例45：留言-好友一对一-输入框')
    def test_homepage45(self):
        logging.info("===留言-好友一对一-输入框===")
        try:
            name_text = "userHello123"
            InputEdit_case=self.mandriver.find_element(*MultiMan.messages_Stranger_InputEdit)
            InputEdit_case.send_keys(name_text)
            InputEdit_case.click()
            self.mandriver.find_element(*MultiMan.messages_Stranger_InputSendBtn).click()
            time.sleep(3)
            assert self.mandriver.find_elements(*MultiMan.messages_Stranger_TextInputContentText)[-1].text == name_text
            assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
            # assert self.multiwoman.messages_Stranger_translateContentEle()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-输入框')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-输入框')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例46：留言-好友一对一-表情')
    def test_homepage46(self):
        logging.info("===留言-好友一对一-表情===")
        try:
            self.multiwoman.tap(912, 149)
            self.multiman.audience_usermessage_sendexpression(1)
            expression = self.multiman.watch_selfsendexpression()
            assert expression
            logging.info('===断言成功，发送chamet表情成功===')
            head_frame, expression = self.multiwoman.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到chamet表情===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例47：留言-好友一对一-搜索表情')
    def test_homepage47(self):
        logging.info("===留言-好友一对一-搜索表情===")
        try:
            self.multiman.audience_usermessage_sendexpression(0)
            expression = self.multiman.watch_selfsendgooglexpression()
            assert expression
            logging.info('===断言成功，发送Facebook表情成功===')
            head_frame, expression = self.multiwoman.watch_othersendgoogleexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到Facebook表情===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-搜索表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-搜索表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例48：留言-好友一对一-更多翻译')
    def test_homepage48(self):
        logging.info("===留言-好友一对一-更多翻译===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Stranger_inputMoreBtn).click()
            self.mandriver.find_element(*MultiMan.messages_Stranger_TranslateBtn).click()
            # usermessage_Voice_chat_toast = self.multiman.toast_message('翻译已开启')
            # assert usermessage_Voice_chat_toast.text == "翻译已开启"
            name_text = "userTranslate"
            InputEdit_case = self.womandriver.find_element(*MultiWoman.messages_Stranger_InputEdit)
            InputEdit_case.send_keys(name_text)
            InputEdit_case.click()
            self.womandriver.find_element(*MultiWoman.messages_Stranger_InputSendBtn).click()
            assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
            time.sleep(5)
            assert self.mandriver.find_elements(*MultiMan.messages_Stranger_TextInputContentText)[-1].text == name_text
            # assert self.multiman.messages_Stranger_translateContentEle()!=False
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-更多翻译')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-更多翻译')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例49：留言-好友一对一-更多相册')
    def test_homepage49(self):
        logging.info("===留言-好友一对一-更多相册===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Stranger_phonePictureBtn).click()
            if len(self.mandriver.find_elements(*MultiMan.messages_Stranger_phonePictureListSelect))==0:
                pytest.skip("用户相册为空")
            self.mandriver.find_elements(*MultiMan.messages_Stranger_phonePictureListSelect)[0].click()
            time.sleep(2)
            self.mandriver.find_element(*MultiMan.messages_Stranger_phonePictureListConfirmBtn).click()
            time.sleep(2)
            photo = self.multiman.watch_selfsendexpression()
            assert photo
            logging.info('===断言成功，发送相册照片成功===')
            head_frame, expression = self.multiwoman.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到相册照片===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-更多相册')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-更多相册')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例50：留言-好友一对一-更多相机')
    def test_homepage50(self):
        logging.info("===留言-好友一对一-更多相机===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Stranger_CameraBtn).click()
            self.mandriver.find_element(*MultiMan.messages_Stranger_114CameraTakeBtn).click()
            time.sleep(5)
            self.mandriver.find_element(*MultiMan.messages_Stranger_114CameraTakeDoneBtn).click()
            photo = self.multiman.watch_selfsendexpression()
            assert photo
            logging.info('===断言成功，发送相机照片成功===')
            head_frame, expression = self.multiwoman.watch_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到相机照片===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-更多相机')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-更多相机')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例51：留言-好友一对一-更多视频聊天')
    def test_homepage51(self):
        logging.info("===留言-好友一对一-更多视频聊天===")
        try:
            self.multiman.usermessage_video_but()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-更多视频聊天')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-更多视频聊天')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例52：留言-好友一对一-送礼')
    def test_homepage52(self):
        logging.info("===留言-好友一对一-送礼===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Stranger_SendGiftBtn).click()
            global sendgift_assertcondition_5
            sendgift_assertcondition_5 = self.multiman.audience_sendgift_bymessage("热门", "4th Anniversary")
            if sendgift_assertcondition_5 == 0:
                pytest.skip("送礼方未送礼")
            else:
                last_text = self.multiman.get_usermessage_textcontent(-1)
                assert '送出' in last_text
                logging.info('===断言成功，送礼方成功发送礼物===')
                head_frame, gift_content = self.multiwoman.watch_othersendgift()
                assert head_frame
                assert '送出' in gift_content
                logging.info('===断言成功，收到私聊礼物===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例53：留言-好友一对一-返回')
    def test_homepage53(self):
        logging.info("===留言-好友一对一-返回===")
        try:
            self.multiman.find_element(*MultiMan.messages_Stranger_userGoback).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_title).text == '消息'
            logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-好友一对一-返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-好友一对一-返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例54：留言-群聊消息显示')
    def test_homepage54(self):
        logging.info("===留言-群聊消息显示===")
        try:
            self.womandriver.find_elements(*MultiWoman.messages_Stranger_UserHeadList)[-1].click()
            self.womandriver.find_element(*MultiWoman.messages_Stranger_userHalfPagePopoverHead).click()
            self.multiwoman.swipe(506, 1832, 506, 400)
            self.multiwoman.swipe(506, 1832, 506, 400)
            self.multiwoman.swipe(506, 1832, 506, 400)
            # self.multiwoman.swipe(1000, 929, 500, 929)
            self.multiwoman.swipe(1000, 929, 110, 929)
            group_man_na=self.womandriver.find_element(By.XPATH, "//*[@text='{}']".format(man_groupNameText))
            group_man_na.click()
            # self.womandriver.find_element(*MultiWoman.messages_Group_pageGroupName).click()
            group_text='gHello'
            self.womandriver.find_element(*MultiWoman.messages_Group_inputBtn).send_keys(group_text)
            self.womandriver.find_element(*MultiWoman.messages_Group_inputBtn).click()
            self.womandriver.find_element(*MultiWoman.messages_Group_inputSendBtn).click()
            logging.info('===女生发言，准备成功===')
            self.multiwoman.system_goback_key()
            self.multiwoman.system_goback_key()
            self.multiwoman.system_goback_key()
            self.multiwoman.system_goback_key()
            time.sleep(2)
            # self.multiwoman.system_goback_key()
            self.multiwoman.system_goback_key()
            # 加点击
            self.multiwoman.tab_Mine_Btn_85()
            self.multiwoman.tap(956, 2124)
            self.womandriver.find_element(*MultiWoman.messages_entry_All).click()
            self.womandriver.find_elements(*MultiWoman.messages_Group_entryGroupName)[0].click()
            time.sleep(3)
            assert self.mandriver.find_element(*MultiMan.messages_Group_ContentText).text.find(group_text)>=0
            time.sleep(3)
            # assert self.multiman.messages_User_userContentUnreadDotEle()
            global groupName_text, groupCount_text
            groupName_text = self.mandriver.find_element(*MultiMan.messages_Group_entryGroupName).text
            groupCount_text = self.mandriver.find_element(*MultiMan.messages_Group_entryGroupCount).text
            self.mandriver.find_elements(*MultiMan.messages_Group_entryGroupName)[0].click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_Group_titleGroupName).text == groupName_text
            assert '\x20''{}'.format(
            self.mandriver.find_element(*MultiMan.messages_Group_titleGroupCount).text) == groupCount_text
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例55：留言-群聊消息未读数')
    def test_homepage55(self):
        logging.info("===留言-群聊消息未读数===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Group_goback).click()
            assert self.multiman.messages_User_userContentUnreadDotEle()==False
            self.mandriver.find_element(*MultiMan.messages_Group_entryGroupHead).click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_titleGroupName).text == groupName_text
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息未读数')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息未读数')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例56：留言-群聊消息-发言')
    def test_homepage56(self):
        logging.info("===留言-群聊消息-发言===")
        try:
            name_text ="vndsiiovnhif VFSHTR"
            self.mandriver.find_element(*MultiMan.messages_Group_inputBtn).send_keys(name_text)
            self.mandriver.find_element(*MultiMan.messages_Group_inputBtn).click()
            self.mandriver.find_element(*MultiMan.messages_Group_inputSendBtn).click()
            time.sleep(1)
            assert self.mandriver.find_elements(*MultiMan.messages_Group_TextInputContent)[-1].text==name_text
            assert self.womandriver.find_elements(*MultiWoman.messages_Group_TextInputContent)[-1].text == name_text
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-发言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-发言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例57：留言-群聊消息-表情')
    def test_homepage57(self):
        logging.info("===留言-群聊消息-表情===")
        try:
            self.multiman.audience_groupmessage_sendexpression(1)
            expression = self.multiman.watchgroup_selfsendexpression()
            assert expression
            logging.info('===断言成功，成功发送chamet表情===')
            time.sleep(2)
            head_frame, expression = self.multiwoman.watchgroup_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，收到chamet表情消息===')

        except AssertionError as e:
                logging.info('===断言失败===')
                screen_name = self.multiman.screenshot('留言-群聊消息-表情')
                logging.info(f'截图成功，图片为{screen_name}')
                raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例58：留言-群聊消息-搜索表情')
    def test_homepage58(self):
        logging.info("===留言-群聊消息-搜索表情===")
        try:
            time.sleep(3)
            self.multiman.audience_groupmessage_sendexpression(0)
            # self.multiman.groupmessage_send_expression(0)
            expression = self.multiman.watchgroup_selfsendgooglexpression()
            assert expression
            logging.info('===断言成功，成功发送google表情===')
            user_name, expression = self.multiwoman.watchgroup_othersendgoogleexpression()
            assert user_name
            assert expression
            logging.info('===断言成功，收到google表情消息===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-搜索表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-搜索表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例59：留言-群聊消息-语音消息')
    def test_homepage59(self):
        logging.info("===留言-群聊消息-语音消息===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Group_voiceBtn).click()
            self.multiman.Phone114_getPermission_checkPopover()
            self.multiman.Permission_114Phone_MediaPopoverConfirmBtnEle()
            message_group_sendVoicePress = self.mandriver.find_element(*MultiMan.messages_Group_voiceAddBtn)
            self.multiman.longPress_action(message_group_sendVoicePress)
            assert self.mandriver.find_elements(*MultiMan.messages_Group_TextVoiceIcon)
            assert self.womandriver.find_elements(*MultiWoman.messages_Group_TextVoiceIcon)
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-语音消息')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-语音消息')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例60：留言-群聊消息-图片信息')
    def test_homepage60(self):
        logging.info("===留言-群聊消息-图片信息===")
        try:
            self.multiman.groupmessage_send_photo(2)
            expression = self.multiman.watchgroup_selfsendexpression()
            assert expression
            logging.info('===断言成功，成功发送相册图片===')
            head_frame, expression = self.multiwoman.watchgroup_othersendexpression()
            assert head_frame
            assert expression
            logging.info('===断言成功，成功收到相册图片===')

            # self.mandriver.find_element(*MultiMan.messages_Group_pictureMoreBtn).click()
            # self.mandriver.find_element(*MultiMan.messages_Group_pictureChooseBtn).click()
            # time.sleep(2)
            # self.multiman.Permission_114Phone_PopoverConfirmOnlyBtn()
            # # assert self.mandriver.find_elements(*MultiMan.messages_Group_pictureChooseList)
            # self.mandriver.find_elements(*MultiMan.messages_Group_pictureChooseList)[0].click()
            # assert len(self.mandriver.find_elements(*MultiMan.messages_Group_TextImageList)) >= 1
            # logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-图片信息')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-图片信息')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例61：留言-群聊消息-上麦')
    def test_homepage61(self):
        logging.info("===留言-群聊消息-上麦===")
        try:
            time.sleep(4)
            self.mandriver.find_element(*MultiMan.messages_Group_upMicBtn).click()
            if self.multiman.Phone114_getPermission_checkPopover():
                self.multiman.Permission_114Phone_MediaPopoverConfirmBtnEle()
            # time.sleep(1)
            # assert self.mandriver.find_elements(*MultiMan.messages_Group_upMic10All)
            self.womandriver.find_element(*MultiWoman.messages_Group_upMicBtn).click()
            # self.multiwoman.get_permission_checkPopover()
            # self.multiwoman.get_permission_checkPopover()
            time.sleep(3)
            global upMicUserHeadList1
            upMicUserHeadList1=self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)
            upMicUserHeadListNum=len(upMicUserHeadList1)
            assert upMicUserHeadListNum>=2
            logging.info("===上麦已成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-上麦')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-上麦')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例62：留言-群聊消息-上麦用户头像-查看自己')
    def test_homepage62(self):
        logging.info("===留言-群聊消息-上麦用户头像-查看自己===")
        try:
            time.sleep(2)
            # self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[0].click()
            self.mandriver.find_element(*MultiMan.messages_Group_upMicUserHeadList1).click()
            global man_upMicName,woman_upMicName
            man_upMicName=self.mandriver.find_element(*MultiMan.messages_Group_OneSelfHalfPagePopoverName).text
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHeadFrame)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverLev)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverCouName)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverLan)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_OneSelfHalfPagePopoverMomentList)
            self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHead).click()
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == man_upMicName
            self.multiman.system_goback_key()
            logging.info("===男群主上麦，查看自己，断言成功===")
            # self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList)[1].click()
            self.womandriver.find_element(*MultiWoman.messages_Group_upMicUserHeadList2).click()
            # upMicUserHeadList1[1].click()
            woman_upMicName = self.womandriver.find_element(*MultiWoman.messages_Group_OneSelfHalfPagePopoverName).text
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverHeadFrame)
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverLev)
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverCouName)
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverLan)
            # assert self.womandriver.find_element(*MultiMan.messages_Group_OneSelfHalfPagePopoverMomentList)
            self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverHead).click()
            assert self.womandriver.find_element(*MultiWoman.user_own_pagePersonalName).text == woman_upMicName
            self.multiwoman.system_goback_key()
            logging.info("===女成员上麦，查看自己，断言成功===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-查看自己')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-查看自己')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例63：留言-群聊消息-麦位表情')
    def test_homepage63(self):
        logging.info("===留言-群聊消息-麦位表情===")
        try:
            # self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[0].click()
            self.mandriver.find_element(*MultiMan.messages_Group_upMicUserHeadList1).click()
            time.sleep(3)
            userHalfPagePopoverImgList_case1=self.mandriver.find_elements(*MultiMan.messages_Group_userHalfPagePopoverImgList)
            userHalfPagePopoverImgList_case1[0].click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_upMicBtn)
            logging.info("===男群主麦位表情，断言成功===")
            self.womandriver.find_element(*MultiWoman.messages_Group_upMicUserHeadList2).click()
            time.sleep(3)
            userHalfPagePopoverImgList_case2 = self.womandriver.find_elements(*MultiWoman.messages_Group_userHalfPagePopoverImgList)
            userHalfPagePopoverImgList_case2[0].click()
            assert self.womandriver.find_element(*MultiWoman.messages_Group_upMicBtn)
            logging.info("===女成员麦位表情，断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-麦位表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-麦位表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例64：留言-群聊消息-上麦用户头像-查看他人')
    def test_homepage64(self):
        logging.info("===留言-群聊消息-上麦用户头像-查看他人===")
        try:
            # self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[1].click()
            self.mandriver.find_element(*MultiMan.messages_Group_upMicUserHeadList2).click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverName).text==woman_upMicName
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHeadFrame)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverLev)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverCouName)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverLan)
            assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverAtHer)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverReport)
            # assert self.multiman.messages_Group_userHalfPagePopoverMomentListEle() ==False
            self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHead).click()
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == woman_upMicName
            self.multiman.system_goback_key()
            logging.info("===男群主上麦，查看他人，断言成功===")
            self.womandriver.find_element(*MultiWoman.messages_Group_upMicUserHeadList1).click()
            assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverName).text == man_upMicName
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverHeadFrame)
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverLev)
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverCouName)
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverLan)
            assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverAtHer)
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverReport)
            # assert self.multiwoman.messages_Group_userHalfPagePopoverMomentListEle() == False
            self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverHead).click()
            assert self.womandriver.find_element(*MultiWoman.user_own_pagePersonalName).text == man_upMicName
            self.multiwoman.system_goback_key()
            logging.info("===女成员上麦，查看他人，断言成功===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-查看他人')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-查看他人')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例65：留言-群聊消息-上麦用户头像-他人送礼和通话')
    def test_homepage65(self):
        logging.info("===留言-群聊消息-上麦用户头像-他人送礼和通话===")
        try:
            time.sleep(2)
            self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[1].click()
            time.sleep(1)
            self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverGifBtn).click()
            sendgift_assertcondition_6 = self.multiman.audience_groupmessage_sendgift("热门", "幸运之吻")
            if sendgift_assertcondition_6 == 0:
                pytest.skip("送礼方未送礼")
            gift_text = self.multiman.watchgroup_selfsendgift()
            assert "送出" in gift_text
            logging.info('===断言成功，男生群聊页面成功送礼===')
            user_name, gift_text = self.multiwoman.watchgroup_othersendgift()
            assert user_name
            assert "送出" in gift_text
            logging.info('===断言成功，女生收到送礼消息===')
            logging.info("===男群主上麦给他人送礼，断言成功===")
            self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[1].click()
            self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverCallBtn).click()
            if self.multiman.messages_Group_CallMoneyNotEnoughEle():
                self.multiman.tap(941, 2027)
            else:
                time.sleep(5)
            assert self.mandriver.find_element(*MultiMan.messages_Group_upMicBtn)
            logging.info("===男群主上麦给他人通话，断言成功===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-他人送礼和通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-他人送礼和通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例66：留言-群聊消息-下麦')
    def test_homepage66(self):
        logging.info("===留言-群聊消息-下麦===")
        try:
            upMicLen_num1=len(self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList))
            messages_Group_upMicBtn_on=self.mandriver.find_element(*MultiMan.messages_Group_upMicBtn)
            messages_Group_upMicBtn_on.click()
            self.mandriver.find_element(*MultiMan.messages_Group_upMicTurnOffBtn).click()
            assert upMicLen_num1 > len(self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList))
            upMicLen_num2 = len(self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList))
            messages_Group_upMicBtn_on = self.womandriver.find_element(*MultiWoman.messages_Group_upMicBtn)
            messages_Group_upMicBtn_on.click()
            self.womandriver.find_element(*MultiWoman.messages_Group_upMicTurnOffBtn).click()
            time.sleep(3)
            assert len(self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList))==0

            # if upMicLen_num2==1:
            #     assert len(self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList))==0
            #     # assert self.womandriver.find_element(*MultiWoman.messages_Group_BannerListLast)
            # else:
            #     assert upMicLen_num2 > len(self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList))
            logging.info('===下麦-断言成功===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-下麦')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-下麦')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例67：留言-群聊消息-钻石包发送-领取')
    def test_homepage67(self):
        logging.info("===留言-群聊消息-钻石包发送-领取===")
        try:
            self.multiwoman.audience_send_diamondenvelope(2, 200)
            envelope = self.multiwoman.messageregion_getenvelope()
            assert envelope
            logging.info('===断言成功，成功发送钻石包===')
            self.multiman.audience_get_diamondenvelope()
            user_head = self.multiman.getenvelope_userhead()
            assert user_head
            logging.info('===断言成功,男生成功领取钻石包===')
            self.multiwoman.get_diamond_envelope()
            user_head = self.multiwoman.getenvelope_userhead()
            assert user_head
            logging.info('===断言成功，女生成功领取钻石包===')
            thank_ele = self.multiman.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_thanking_1")
            thank_text = thank_ele.text.encode("utf-8")
            thank_ele.click()
            self.multiwoman.tap(335,1903)
            time.sleep(5)
            audience_messageregion = self.multiwoman.groupmessage_text(-1)
            print(thank_text,audience_messageregion)
            # print(thank_text.encode("utf-8"))
            # print(audience_messageregion.encode("utf-8"))
            assert thank_text in audience_messageregion
            logging.info('===断言成功,女生成功收到男生发送的感谢语===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-钻石包发送-领取')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-钻石包发送-领取')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例68：留言-群聊消息-游戏浮层')
    def test_homepage68(self):
        logging.info("===留言-群聊消息-游戏浮层===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Group_GameBtn).click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer1).text=='Chamet赛车'
            assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer2).text=='顶级赛车'
            assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer3).text=='幸运盒子'
            assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer4).text=='幸运转盘'
            assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer5).text=='幸运数字'
            assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer6).text=='幸运抽奖机'
            self.multiman.tap(584,1804)
            logging.info('====游戏浮层-断言成功===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-游戏浮层')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-游戏浮层')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例69：留言-群聊消息-礼物送礼')
    def test_homepage69(self):
        logging.info("===留言-群聊消息-礼物送礼===")
        try:
            self.multiman.group_opengiftwin()
            global sendgift_assertcondition_6
            sendgift_assertcondition_6 = self.multiman.audience_groupmessage_sendgift("热门", "幸运之吻")
            if sendgift_assertcondition_6 == 0:
                pytest.skip("群主未送礼")
            gift_text = self.multiman.watchgroup_selfsendgift()
            assert "送出" in gift_text
            logging.info('===断言成功，群主群聊页面成功送礼===')
            if sendgift_assertcondition_6 == 0:
                pytest.skip("群主未送礼")
            user_name, gift_text = self.multiwoman.watchgroup_othersendgift()
            assert user_name
            assert "送出" in gift_text
            logging.info('===断言成功，女生收到送礼消息===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-礼物送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-礼物送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例70：留言-群聊消息-顶部banner入口')
    def test_homepage70(self):
        logging.info("===留言-群聊消息-顶部banner入口===")
        try:
            if len(self.mandriver.find_elements(*MultiMan.messages_Group_BannerListLast)) == 0:
                pytest.skip("顶部banner入口不存在，跳过")
            else:
                self.mandriver.find_element(*MultiMan.messages_Group_BannerListLast).click()
                time.sleep(8)
                assert self.mandriver.find_elements(*MultiMan.messages_Group_BannerListLayer)
                self.multiman.tap(577, 617)
                self.mandriver.find_element(*MultiMan.messages_Group_BannerListPackupBtn).click()
                time.sleep(3)
                self.mandriver.find_element(*MultiMan.messages_Group_BannerListSmallBtn).click()
                logging.info('====顶部banner入口收起成功===')
                assert self.mandriver.find_elements(*MultiMan.messages_Group_BannerList)
                logging.info('====顶部banner入口展开成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-顶部banner入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-顶部banner入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例71：留言-群聊消息-更多按钮')
    def test_homepage71(self):
        logging.info("===留言-群聊消息-更多按钮===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Group_detailMoreBtn).click()
            HeadList_test1=self.mandriver.find_elements(*MultiMan.messages_Group_MoreUserHeadList)
            group_userlist1 = len(HeadList_test1)
            HeadList_test1[1].click()
            logging.info('===更多跳转详情页成功===')
            group_UserName=self.multiman.userHalfPagePopoverNameOrOneselfEle()
            self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHead).click()
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text==group_UserName
            self.multiman.system_goback_key()
            logging.info('===头像跳转个人主页成功===')
            if self.multiman.groupCount_number(groupCount_text)<=18:
                assert ' (''{}'')'.format(group_userlist1)==groupCount_text
            else:
                assert len(self.mandriver.find_elements(*MultiMan.messages_Group_MoreUserHeadList))==18
            logging.info('===用户数据正常===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-更多按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-更多按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例72：留言-群聊消息-更多-动态-更多详情页')
    def test_homepage72(self):
        logging.info("===留言-群聊消息-更多-动态-更多详情页===")
        try:
            if self.mandriver.find_elements(*MultiMan.messages_Group_MoreUserHeadList):
                logging.info("===留言-有群聊消息，在群聊页面===")
                MoreMomentAllEle=self.multiman.messages_Group_MoreMomentAllEle()
                global moment_ele
                if MoreMomentAllEle!=False and len(MoreMomentAllEle)!=0:
                    moment_ele=1
                    logging.info('===有动态元素===')
                    self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentPicLast).click()
                    time.sleep(2)
                    assert self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentMoreTitle).text=='动态'
                    assert self.mandriver.find_elements(*MultiMan.messages_Group_MoreMomentGiftSendBtn)
                    self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentMoreGoback).click()
                    # assert self.l.messages_Group_MoreMomentAllEle()
                    logging.info('===更多跳转详情页成功===')
                else:
                    moment_ele = 0
                    logging.info('===没有动态元素===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-更多-动态-更多详情页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-更多-动态-更多详情页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例73：留言-群聊消息-更多-动态-大图模式')
    def test_homepage73(self):
        logging.info("===留言-群聊消息-更多-动态-大图模式===")
        try:
            if moment_ele==0:
                pytest.skip("===没有动态元素===")
            else:
                logging.info('===有动态元素===')
                print(self.multiman.messages_Group_MoreMomentPicFrontEle())
                group_MoreMomentPicFrontEle_case=self.multiman.messages_Group_MoreMomentPicFrontEle()
                if group_MoreMomentPicFrontEle_case==False or len(group_MoreMomentPicFrontEle_case)==1:
                    logging.info('===只有一个动态===')
                else:
                    logging.info('===多个动态===')
                    self.mandriver.find_elements(*MultiMan.messages_Group_MoreMomentPicFront)[0].click()
                    assert self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentMaxCommentBtn)
                    self.multiman.swipe(531,1776,531,900)
                    assert self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentMaxCommentBtn)
                    self.multiman.system_goback_key()
                    # assert self.l.messages_Group_MoreMomentAllEle()
                    logging.info('===大图模式-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-更多-动态-大图模式')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-更多-动态-大图模式')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例74：留言-群聊消息-群组类型')
    def test_homepage74(self):
        logging.info("===留言-群聊消息-群组类型===")
        try:
            self.womandriver.find_element(*MultiWoman.messages_Group_detailMoreBtn).click()
            time.sleep(3)
            assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupType).text=='普通群组'
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupType).text == '普通群组'
            logging.info('===返回-断言成功===')


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-群组类型')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-群组类型')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例75：留言-群聊消息-群组封面')
    def test_homepage75(self):
        logging.info("===留言-群聊消息-群组封面===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupHeadPic).click()
            assert self.multiman.messages_Group_MoreGroupHeadPic_picStatusEle()
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupHeadPic_pic).click()
            assert self.multiman.messages_Group_MoreGroupHeadPic_ChangeEle()
            self.multiman.tap(389,1583)
            self.multiman.system_goback_key()
            logging.info('===群主-断言成功===')
            self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupHeadPic).click()
            assert self.multiwoman.messages_Group_MoreGroupHeadPic_picStatusEle()==False
            self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupHeadPic_pic).click()
            assert self.multiwoman.messages_Group_MoreGroupHeadPic_ChangeEle()==False
            self.multiwoman.system_goback_key()
            logging.info('===群成员-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-群组封面')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-群组封面')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例76：留言-群聊消息-群组名')
    def test_homepage76(self):
        logging.info("===留言-群聊消息-群组名===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSet).click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSetContent).text==groupName_text
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSetContentGoback).click()
            logging.info('===群主-断言成功===')
            self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupNameSet).click()
            assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupNameSet).text == groupName_text
            logging.info('===群成员-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-群组名')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-群组名')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例77：留言-群聊消息-群组介绍')
    def test_homepage77(self):
        logging.info("===留言-群聊消息-群组介绍===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntro).click()
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroContent).clear()
            # group_intro='hhhhyyyy7'
            group_intro_con=self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroContent)
            group_intro_con.send_keys(group_intro)
            group_intro_con.click()
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSetContentSave).click()
            # time.sleep(6)
            self.multiman.system_goback_key()
            self.mandriver.find_element(*MultiMan.messages_Group_detailMoreBtn).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroDes).text==group_intro
            logging.info('===群主-断言成功===')
            self.multiwoman.system_goback_key()
            self.womandriver.find_element(*MultiWoman.messages_Group_detailMoreBtn).click()
            time.sleep(2)
            assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupIntroDes).text == group_intro
            logging.info('===群成员-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-群组介绍')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-群组介绍')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例78：留言-群聊消息-管理群组')
    def test_homepage78(self):
        logging.info("===留言-群聊消息-管理群组===")
        try:
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupMana).click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaVisConTextXPATH).text=='非群组用户可以查看消息和送礼，但不能发送消息、进行语音聊天或玩游戏。 \n 开启访客模式的群组将更容易被看到，群组将变得更加活跃。'
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaPriConTextXPATH).text=='不在群组内的用户不能申请加入。用户只能通过群主或管理员的邀请加入'
            logging.info("===模式内容-断言完成===")
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaNextHost).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaNextHostTitle).text=='选择新群主'
            self.multiman.system_goback_key()
            logging.info("===群组所有权转让-断言完成===")
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaAdmin).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaNextHostTitle).text =='群管理员'
            self.multiman.system_goback_key()
            logging.info("===群管理员-断言完成===")
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisband).click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisPopCon).text == '解散后，所有成员（包括群主）将被移出群组'
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisPopCancel).click()
            time.sleep(2)
            self.multiman.system_goback_key()
            logging.info("===解散群组-断言完成===")
            logging.info("===群主-断言完成===")
            assert self.multiwoman.messages_Group_MoreGroupManaEle()==False
            logging.info('===群成员-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-管理群组')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-管理群组')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例79：留言-群聊消息-删除并离开')
    def test_homepage79(self):
        logging.info("===留言-群聊消息-删除并离开===")
        try:
            time.sleep(3)
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDeAndLeaveID).click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisPopCon).text == '退出此群组后将不再接收群组消息'
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisPopCancel).click()
            logging.info("===群主-断言完成===")
            self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupManaDeAndLeaveID).click()
            assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupManaDisPopCon).text == '退出此群组后将不再接收群组消息'
            self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupManaDisPopCancel).click()
            logging.info('===群成员-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-删除并离开')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-删除并离开')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例80：留言-群聊消息-添加成员')
    def test_homepage80(self):
        logging.info("===留言-群聊消息-添加成员===")
        try:
            self.mandriver.find_elements(*MultiMan.messages_Group_MoreGroupAddBtn)[0].click()
            time.sleep(2)
            self.mandriver.find_elements(*MultiMan.messages_Group_MoreGroupAddIcon)[0].click()
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSetContentGoback).click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupTitle).text == groupName_text
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-添加成员')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-添加成员')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例81：留言-群聊消息-移除成员')
    def test_homepage81(self):
        logging.info("===留言-群聊消息-移除成员===")
        try:
            self.mandriver.find_elements(*MultiMan.messages_Group_MoreGroupAddBtn)[-1].click()
            assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroTitle).text == '移除成员'
            self.multiman.swipe(590,1792,590,927)
            remove_name=self.mandriver.find_element(By.XPATH, "//*[@text='{}']".format(woman_pagePersonalName))
            remove_name.click()
            # self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupRemovePer).click()
            time.sleep(2)
            self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupRemovePerSave).click()
            time.sleep(3)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupRemoveTips).text == '“你移除了”Mary33470557…啊bb...“来自群组”'
            # assert self.mandriver.find_element(By.XPATH,  "//*[@text='“你移除了”{}“来自群组”']".format(group_remove_womanName))
            print( "//*[@text='“你移除了”{}“来自群组”']".format(group_remove_womanName))
            assert self.mandriver.find_element(By.XPATH,  "//*[@text='“你移除了”{}“来自群组”']".format(group_remove_womanName))
            # print(self.mandriver.find_elements(*MultiMan.messages_Group_MoreGroupRemoveTips)[-1].text)
            # assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupRemoveTipsText)
            self.multiwoman.system_goback_key()
            assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupRemovePTips)
            logging.info('===群成员-断言成功===')



            # 后续的添加用户
            # self.multiman.system_goback_key()
            # self.multiman.system_goback_key()
            # logging.info("===群主-断言完成,已返回至我的页面===")
            # # logging.info("===群主-断言完成===")
            # self.multiwoman.system_goback_key()
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupRemovePTips)
            # self.multiwoman.system_goback_key()
            # self.womandriver.find_element(*MultiWoman.messages_Group_pageGroupName).click()
            # self.womandriver.find_element(*MultiWoman.messages_Group_joinBtn).click()
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_joinPopCon).text=='等待群主同意'
            # self.womandriver.find_element(*MultiWoman.messages_Group_joinPopConfirm).click()
            # self.multiwoman.system_goback_key()
            # self.multiwoman.system_goback_key()
            # time.sleep(2)
            # self.multiman.swipe(572,816,572,5778)
            # self.mandriver.find_element(*MultiMan.messages_entry_All).click()
            # self.mandriver.find_element(*MultiMan.messages_Group_Notification).click()
            # assert self.mandriver.find_element(*MultiMan.messages_Group_NotiJoinCon).text =='Mary33470557…啊bb... 申请加入群组: 今日也莫人陪我'
            # self.mandriver.find_element(*MultiMan.messages_Group_joinAgree).click()
            # time.sleep(2)
            # self.womandriver.find_element(*MultiWoman.messages_entry_All).click()
            # self.womandriver.find_element(*MultiWoman.messages_Group_pageGroupName).click()
            # assert self.womandriver.find_element(*MultiWoman.messages_Group_joinInTips)
            # logging.info('===群成员-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-移除成员')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-移除成员')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例82：留言-群聊消息-返回')
    def test_homepage82(self):
        logging.info("===留言-群聊消息-返回===")
        try:
            self.multiman.system_goback_key()
            assert self.mandriver.find_element(*MultiMan.messages_title).text == '消息'
            self.womandriver.find_element(*MultiWoman.messages_Group_goback).click()
            assert self.womandriver.find_element(*MultiWoman.messages_title).text=='消息'
            self.multiman.system_goback_key()
            self.multiwoman.system_goback_key()
            logging.info('===返回-断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('留言-群聊消息-返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('留言-群聊消息-返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




if __name__ == '__main__':
    pytest.main(["-vs","..\test_case\test_mypage_message_multi.py","--alluredir=..\result\mypage_result\2023_09_11_m_002"])

''' pytest .\test_mypage_message_multi.py -s -v --alluredir=..\result\mypage_result\2023_m_10_07_001'''
# '''pytest ./test_case/est_mypage_multi.py - vs --alluredir= D:\chamet_mypage_multi_testProject-8.10\result\mypage_result\2023_08_15_001'''
'''allure serve ..\result\mypage_result\2023_m_10_07_001'''
# D:\chamet_mypage_multi_testProject-8.15.2\result\mypage_result\2023_8_17_001
# pytest .\test_mypage_multi.py -s -v --alluredir=..\result\mypage_result\2023_8_17