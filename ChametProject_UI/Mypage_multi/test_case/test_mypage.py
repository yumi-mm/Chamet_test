#_*_ coding:utf_8_*_
import os

from common.my_page_py_startend import StartEnd
from businessView.login_phoneView import LoginView
import time
from businessView.my_page import MyPage
import logging
import pytest
import allure


class TestMyPage(StartEnd):


    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例1：我的页面-个人头像-个人主页')
    def test_homepage01(self):
        logging.info("===我的页面-个人头像-个人主页===")
        try:
            # l = MyPage(self.driver)
            self.l.tap(930,2123)
            self.l.tab_Mine_Btn()
            self.l.tab_Mine_Head()
            time.sleep(2)
            global pageSelfIntroduction,pagePersonalName
            pageSelfIntroduction = self.l.user_ownPage_selfIntroductionEle()
            pagePersonalName = self.driver.find_element(*MyPage.user_own_pagePersonalName).text
            assert self.driver.find_element(*MyPage.user_own_pagePersonalInformationText), "没有通过头像找到个人主页元素"
            self.driver.find_element(*MyPage.user_own_pageGobackBtn).click()
            # 获取元素
            global user_gender,pageUserId
            user_gender=self.l.myProfile_Gender_ManorW()
            self.l.my_Profile_entry()
            pageUserId = self.driver.find_element(*MyPage.myProfile_ID_Number).text
            self.l.system_goback_key()
            print(pageSelfIntroduction,pagePersonalName,user_gender,pageUserId)
            print(type(user_gender))

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例2：我的页面-顶部空白区域')
    def test_homepage02(self):
        logging.info("===我的页面-顶部空白区域===")
        try:
            self.l.tab_Mine_Btn()
            assert self.driver.find_element(*MyPage.user_name).text==pagePersonalName
            # self.l.Check_RandomCall_PopoverEle()
            self.l.tap(261,245)
            assert self.driver.find_element(*MyPage.user_own_pagePersonalInformationText),"没有通过空白找到个人主页元素"
            self.l.system_goback_key()
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot(module='my_page_own')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot(module='my_page_own')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例3和4：我的页面-等级')
    def test_homepage03(self):
        logging.info("===我的页面-等级===")
        try:
            self.l.tab_Mine_Btn()
            self.l.tap(930, 2123)
            # self.l.Check_RandomCall_PopoverEle()
            global lel_ele
            lel_ele = self.l.tab_Mine_user_vip_level()
            if lel_ele != False:
                logging.info("有等级-点击确认")
                self.l.tap(930, 2123)
                lel_ele.click()
                self.driver.implicitly_wait(8)
                time.sleep(10)
                # c.native_to_h5()
                assert self.driver.find_element(*MyPage.level_title).text == '等级', '未进入我的等级页或者我的等级页标题不是"等级"'
                self.l.system_goback_key()
                # c.h5_to_native()
            else:
                logging.error("没有等级-等级元素再次确认")
                assert not self.driver.find_element(*MyPage.user_vipLevel), '没有等级，但是有等级元素'
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例5：我的页面-头像框')
    def test_homepage05(self):
        logging.info("===我的页面-头像框===")
        try:
            self.l.tab_Mine_Btn()
            if self.l.tab_Mine_Head_level_frame():
                logging.info("有头像框-等级确认")
                self.l.tap(930, 2123)
                assert self.driver.find_element(*MyPage.user_vipLevel)
            else:
                logging.error("没有头像框-等级确认")
                assert lel_ele==False
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例6：我的页面-国家')
    def test_homepage06(self):
        logging.info("===我的页面-国家===")
        try:
            self.l.tab_Mine_Btn()
            assert self.driver.find_element(*MyPage.user_nation), "页面没有国家图标"
            logging.info("===我的页面-有国家图标===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot(module='my_page_own')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot(module='my_page_own')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例7和8：我的页面-语言')
    def test_homepage07(self):
        logging.info("===我的页面-语言===")
        try:
            self. l.tab_Mine_Btn()
            lan_text=self.l.tab_Mine_user_language_LanEle()
            if lan_text ==1:
                logging.info("只有第一语言")
                self.driver.find_element(*MyPage.user_language).click()
                assert self.driver.find_element(*MyPage.myProfile_Language_title).text =='语言','只有第一语言。没跳转到语言页面'
                self.l.system_goback_key()
            elif lan_text==2:
                logging.info("有第二语言")
                self.driver.find_element(*MyPage.user_language).click()
                assert self.driver.find_element(*MyPage.myProfile_Title).text == '我的简介','有第二语言。没跳转到我的简介页面'
                self.l.system_goback_key()
            else:
                logging.error("没有语言")
                assert self.driver.find_element(*MyPage.tab_mine_btn),'没设置语言，没停留在我的页面'
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例9：我的页面-粉丝')
    def test_homepage09(self):
        logging.info("===我的页面-粉丝===")
        try:
            self.l.tab_Mine_Btn()
            # 该函数返回值有的话，返回粉丝数
            global followers_num
            followers_num =self.l.tab_Mine_user_followers()
            user_followers_entry=self.driver.find_element(*MyPage.user_followers)
            self.l.tap(930, 2123)
            if followers_num!=False:
                logging.info("有粉丝")
                user_followers_entry.click()
                assert self.driver.find_element(*MyPage.user_followers_Title).text == '粉丝', '有粉丝，但是点击没有进入粉丝页面'
                # self.driver.find_element(*MyPage.user_followers_GoBack).click()
            else:
                logging.error("没有粉丝")
                user_followers_entry.click()
                assert self.driver.find_element(*MyPage.user_followers_Title).text == '粉丝', '没有粉丝，但是点击没有进入粉丝页面'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot(module='my_page_followers')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot(module='my_page_followers')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例11：我的页面-粉丝头像')
    def test_homepage11(self):
        logging.info("===我的页面-粉丝头像===")
        try:
            # self.l.tab_Mine_Btn()
            # followers_ele = self.l.tab_Mine_user_followers_FollowersEle()
            # self.l.tap(930, 2123)
            if followers_num!=False and int(followers_num)>0:
                logging.info("===我的页面-粉丝头像人数不为0===")
                # self.driver.find_element(*MyPage.user_followers).click()
                followers_firstPerName=self.driver.find_element(*MyPage.user_followers_firstPerName).text
                self.driver.find_element(*MyPage.user_followers_firstPer).click()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == followers_firstPerName
                self.driver.find_element(*MyPage.user_own_pageGobackBtn).click()
                self.driver.find_element(*MyPage.user_followers_GoBack).click()
            elif followers_num!=False and int(followers_num)==0:
                logging.info("===我的页面-粉丝头像人数为0===")
                # # self.driver.find_element(*MyPage.user_followers).click()
                assert self.driver.find_element(*MyPage.user_followers_EmptyText).text=='你关注的用户将在这里'
                self.driver.find_element(*MyPage.user_followers_GoBack).click()
            else:
                logging.info("===我的页面-粉丝无该图标===")
                assert self.driver.find_element(*MyPage.user_followers_Title).text == '粉丝'
                self.driver.find_element(*MyPage.user_followers_GoBack).click()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例12：我的页面-关注')
    def test_homepage12(self):
        logging.info("===我的页面-关注===")
        try:
            self.l.tab_Mine_Btn()
            # 该函数返回值有的话，返回粉丝数
            global following_num
            following_num = self.l.tab_Mine_user_following()
            self.l.tap(930, 2123)
            user_following_Entry=self.driver.find_element(*MyPage.user_following)
            if following_num != False:
                logging.info("有关注")
                user_following_Entry.click()
                assert self.driver.find_element(*MyPage.user_following_Title).text == '关注'
                # self.driver.find_element(*MyPage.user_following_GoBack).click()
            else:
                logging.error("没有关注")
                user_following_Entry.click()
                assert self.driver.find_element(*MyPage.user_following_Title).text == '关注'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot(module='my_page_following')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot(module='my_page_following')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例14：我的页面-关注头像')
    def test_homepage14(self):
        logging.info("===我的页面-关注头像===")
        try:
            # self.l.tab_Mine_Btn()
            # following_ele = self.l.tab_Mine_user_following_FollowingEle()
            # self.l.tap(930, 2123)
            if following_num!=False and int(following_num)>0:
                logging.info("===我的页面-关注头像人数不为0===")
                following_firstPerName = self.driver.find_element(*MyPage.user_following_firstPerName).text
                self.driver.find_element(*MyPage.user_following_firstPer).click()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == following_firstPerName
                self.driver.find_element(*MyPage.user_own_pageGobackBtn).click()
                self.driver.find_element(*MyPage.user_following_GoBack).click()

            elif following_num!=False and int(following_num)==0:
                logging.info("===我的页面-关注头像人数为0===")
                assert self.driver.find_element(*MyPage.user_following_EmptyText).text=='你关注的用户将在这里'
                self.driver.find_element(*MyPage.user_followers_GoBack).click()

            else:
                logging.info("===我的页面-关注无该图标===")
                assert self.driver.find_element(*MyPage.user_following_Title).text == '关注'
                self.driver.find_element(*MyPage.user_following_GoBack).click()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例15：我的页面-朋友')
    def test_homepage15(self):
        logging.info("===我的页面-朋友===")
        try:
            self.l.tab_Mine_Btn()
            # 该函数返回值有的话，返回粉丝数
            global friend_num
            friend_num = self.l.tab_Mine_user_friend()
            self.l.tap(930, 2123)
            user_friend_Entry=self.driver.find_element(*MyPage.user_friend)
            if friend_num != False:
                logging.info("有朋友,进入朋友页面")
                user_friend_Entry.click()
                assert self.driver.find_element(*MyPage.user_friend_Title).text == '朋友'
                # self.driver.find_element(*MyPage.user_friend_GoBack).click()
            else:
                logging.error("没有朋友")
                user_friend_Entry.click()
                assert self.driver.find_element(*MyPage.user_friend_Title).text == '朋友'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('my_page_friendPer')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('my_page_friendPer')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例16,18：我的页面-朋友头像')
    def test_homepage16(self):
        logging.info("===我的页面-朋友头像===")
        try:
            if friend_num!=False and int(friend_num)>0:
                logging.info("===我的页面-朋友头像人数不为0===")
                friend_firstPerName = self.driver.find_element(*MyPage.user_friend_firstPerName).text
                self.driver.find_element(*MyPage.user_friend_firstPer).click()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == friend_firstPerName
                self.driver.find_element(*MyPage.user_own_pageGobackBtn).click()
                self.driver.find_element(*MyPage.user_friend_GoBack).click()
            elif friend_num!=False and int(friend_num)==0:
                assert self.driver.find_element(*MyPage.user_friend_EmptyText).text=='无用户', '朋友数为0，且没有第一位朋友，但是空图标的文字不匹配,断言失败'
                self.driver.find_element(*MyPage.user_friend_GoBack).click()
            else:
                logging.info("===我的页面-朋友无该图标===")
                assert self.driver.find_element(*MyPage.user_friend_Title).text == '朋友'
                self.driver.find_element(*MyPage.user_friend_GoBack).click()
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例19：我的页面-签到入口')
    def test_homepage19(self):
        logging.info("===我的页面-签到入口===")
        try:
            self. l.tab_Mine_Btn()
            global signInfoTopEle
            signInfoTopEle = self.l.tab_Mine_user_signInfoTop()
            self.l.tap(930, 2123)
            if signInfoTopEle != False:
                self.l.tap(930, 2123)
                signInfoTopEle.click()
                assert self.driver.find_element(*MyPage.sign_in_popover_dayInt1_7), '有签到入口未出现签到弹窗'
            else:
                logging.error("没有签到入口")
                assert self.driver.find_element(*MyPage.user_sign_infoTop),'没有签到入口再次寻找发现签到入口'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例20：我的页面-签到弹窗消失')
    def test_homepage20(self):
        logging.info("===我的页面-签到弹窗消失===")
        try:
            if signInfoTopEle != False:
                assert self.driver.find_element(*MyPage.sign_in_popover_dayInt1_7)
                self.l.tap(930, 2123)
                assert self.driver.find_element(*MyPage.tab_mine_btn), '签到弹窗消失后没有在我的界面'

            else:
                logging.error("没有签到入口")
                assert self.driver.find_element(*MyPage.user_sign_infoTop), '没有签到入口再次寻找发现签到入口'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-签到弹窗消失')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-签到弹窗消失')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例21-24：我的页面-去签到-跳转页面')
    def test_homepage21(self):
        logging.info("===我的页面-去签到===")
        try:
            self.l.tab_Mine_Btn()
            self.l.tap(930, 2123)
            # user_gender = self.l.myProfile_Gender_ManorW()
            if signInfoTopEle != False:
                signInfoTopEle.click()
                sign_btn_man = self.driver.find_element(*MyPage.sign_in_popover_SigninSubmitTextID)
                print(sign_btn_man.text)
                if sign_btn_man.text == '签到':
                    logging.info("===该用户-未签到===")
                    sign_btn_man.click()
                    assert signInfoTopEle != False
                elif sign_btn_man.text == '好的':
                    assert user_gender == 1
                    logging.info("===该用户为男生-已经签到===")
                    sign_btn_man.click()
                    assert self.driver.find_element(*MyPage.user_sign_infoTop), '签到弹窗已经点击消失但是没有停留在我的页面'
                elif sign_btn_man.text == '兑换奖励':
                    assert user_gender == 2
                    logging.info("===该用户为女生-已经签到===")
                    sign_btn_man.click()
                    task_CompletePopover = self.l.tab_Mine_user_signInfoTopEleTASK()
                    task_rewardBtn = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    if task_CompletePopover == False:
                        assert task_rewardBtn.get_attribute('selected') == 'true', '女生签到成功后跳转页面失败，不在任务-奖励页面'
                        self.l.system_goback_key()
                    else:
                        task_CompletePopover.click()
                        self.l.system_goback_key()

            else:
                logging.error("===该用户没有签到入口按钮===")
                assert signInfoTopEle==False



        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-去签到-跳转页面')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-去签到-跳转页面')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例25、26：留言-入口及消息未读数')
    def test_homepage25(self):
        logging.info("===留言-入口及消息未读数===")
        try:
            self.l.tab_Mine_Btn()
            self.l.tap(930, 2123)
            entry_UnReadNum_case=self.l.messages_entry_UnReadNumIDEle()
            # print(UnReadNum_case44)
            self.driver.find_element(*MyPage.messages_entry_All).click()
            assert self.driver.find_element(*MyPage.messages_title).text == '留言'
            if entry_UnReadNum_case != False:
            # if entry_UnReadNum_case!=False and len(entry_UnReadNum_case)!=0:
                logging.info("===留言-入口有消息未读数===")
                UnReadNum_case44 = entry_UnReadNum_case.text
                UnReadNum_lists=self.l.messages_UnReadNum_lists()
                # print(UnReadNum_lists)
                # print(UnReadNum_case44)
                assert UnReadNum_lists ==int(UnReadNum_case44)
                # assert self.l.messages_UnReadNum_lists() == int(entry_UnReadNum[0].text)
            else:
                logging.info("===留言-入口没有消息未读数===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-入口及消息未读数')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-入口及消息未读数')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例27、28：留言-返回后未读变已读返回')
    def test_homepage27(self):
        logging.info("===留言-返回后未读变已读返回===")
        try:
            system_UnReadNum=self.l.messages_system_UnReadNumXpathEle()
            self.driver.find_element(*MyPage.messages_goback).click()
            # self.l.system_goback_key()
            # self.driver.find_element(*MyPage.messages_goback).click()
            messages_entry_gobackNum = self.l.messages_entry_UnReadNumIDEle()
            self.driver.find_element(*MyPage.messages_entry_All).click()
            assert self.driver.find_element(*MyPage.messages_title).text == '留言'
            if system_UnReadNum!=False and len(system_UnReadNum)!=0:
                logging.info("===留言-有系统消息不消失消息为：{}===".format(system_UnReadNum.text))
                assert messages_entry_gobackNum!=False
                assert messages_entry_gobackNum.text>=system_UnReadNum.text
                assert self.l.messages_system_UnReadNumXpathEle()!=False and len(system_UnReadNum)!=0
            else:
                logging.info("===留言-没有系统消息===")
                if messages_entry_gobackNum!=False:
                    assert self.l.messages_system_UnReadNumXpathEle()==False or len(system_UnReadNum)==0
                else:
                    assert self.l.messages_UnReadNum_lists()==False

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-返回后未读变已读返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-返回后未读变已读返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例29：留言-chamet团队')
    def test_homepage29(self):
        logging.info("===留言-chamet团队===")
        try:
            entry_text=self.driver.find_element(*MyPage.messages_system_entryText).text
            self.driver.find_element(*MyPage.messages_system_EntryAll).click()
            assert self.driver.find_element(*MyPage.messages_system_title).text == 'Chamet团队'
            if entry_text=='没有消息':
                logging.info("===留言-chamet团队无消息===")
                assert self.driver.find_element(*MyPage.messages_system_emptyIcon)
                assert self.driver.find_element(*MyPage.messages_system_emptyText).text == '无消息'
                self.driver.find_element(*MyPage.messages_system_goback).click()
            else:
                logging.info("===留言-chamet团队有消息===")
                assert self.driver.find_element(*MyPage.messages_system_messagesContentAll)
                # assert self.driver.find_elements(*MyPage.messages_system_learnMoreText)
                self.driver.find_element(*MyPage.messages_system_goback).click()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-chamet团队')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-chamet团队')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例30：留言-chamet客服')
    def test_homepage30(self):
        logging.info("===留言-chamet客服===")
        try:
            entry_text = self.driver.find_element(*MyPage.messages_customerService_entryText).text
            self.driver.find_element(*MyPage.messages_customerService_EntryAll).click()
            assert self.driver.find_element(*MyPage.messages_customerService_title).text == '在线客服'
            assert entry_text == '任何问题？联络我'
            assert self.driver.find_element(*MyPage.messages_customerService_title)
            assert self.driver.find_element(*MyPage.messages_customerService_Container)
            assert self.driver.find_element(*MyPage.messages_customerService_problemChoice)
            assert self.driver.find_element(*MyPage.messages_customerService_InputText)
            self.driver.find_element(*MyPage.messages_customerService_goback).click()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-chamet客服')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-chamet客服')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例31-32：留言-群聊消息有无')
    def test_homepage31(self):
        logging.info("===留言-群聊消息有无===")
        try:
            global group_haveOrNot
            if self.l.messages_Group_entryGroupNameEle()!=False and len(self.l.messages_Group_entryGroupNameEle())!=0:
                group_haveOrNot=1
                logging.info("===留言-有群聊消息===")
                global name_text,count_text
                name_text = self.driver.find_element(*MyPage.messages_Group_entryGroupName).text
                count_text = self.driver.find_element(*MyPage.messages_Group_entryGroupCount).text
                self.driver.find_elements(*MyPage.messages_Group_entryGroupName)[0].click()
                self.l.driver.implicitly_wait(3)
                assert self.driver.find_element(*MyPage.messages_Group_titleGroupName).text== name_text
                assert '\x20''{}'.format(self.driver.find_element(*MyPage.messages_Group_titleGroupCount).text)==count_text
            else:
                group_haveOrNot = 0
                logging.info("===留言-无群聊消息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息有无')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息有无')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例33：留言-群聊消息-发言')
    def test_homepage33(self):
        logging.info("===留言-群聊消息-发言===")
        try:
            if group_haveOrNot==1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                name_text ="vndsiiovnhif VFSHTR"
                self.driver.find_element(*MyPage.messages_Group_inputBtn).send_keys(name_text)
                self.driver.find_element(*MyPage.messages_Group_inputSendBtn).click()
                time.sleep(1)
                assert self.driver.find_elements(*MyPage.messages_Group_TextInputContent)[-1].text==name_text
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无群聊消息,不在群聊页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-发言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-发言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例34：留言-群聊消息-表情')
    def test_homepage34(self):
        logging.info("===留言-群聊消息-表情===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_faceGifBtn).click()
                self.l.driver.implicitly_wait(25)
                # assert self.driver.find_elements(*MyPage.messages_Group_imgMotionList)
                self.driver.find_elements(*MyPage.messages_Group_imgMotionList)[2].click()
                self.l.driver.implicitly_wait(7)
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList))>=1
                # self.l.tap(337,1247)
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无群聊消息,不在群聊页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例35：留言-群聊消息-搜索表情')
    def test_homepage35(self):
        logging.info("===留言-群聊消息-搜索表情===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                # self.driver.find_element(*MyPage.messages_Group_faceGifBtn).click()
                # self.l.driver.implicitly_wait(25)
                # assert self.driver.find_elements(*MyPage.messages_Group_imgMotionClassList)
                self.driver.find_element(*MyPage.messages_Group_imgSearchBtn).click()
                time.sleep(5)
                # assert self.driver.find_element(*MyPage.messages_Group_imgSearchFirstPic)
                self.driver.find_element(*MyPage.messages_Group_imgSearchFirstPic).click()
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList)) >= 2
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无群聊消息,不在群聊页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-搜索表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-搜索表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例36：留言-群聊消息-语音消息')
    def test_homepage36(self):
        logging.info("===留言-群聊消息-语音消息===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_voiceBtn).click()
                self.l.get_permission_checkPopover()
                self.l.get_permission_checkPopover()
                message_group_sendVoicePress = self.driver.find_element(*MyPage.messages_Group_voiceAddBtn)
                self.l.longPress_action(message_group_sendVoicePress)
                assert self.driver.find_elements(*MyPage.messages_Group_TextVoiceTimes)
                assert self.driver.find_elements(*MyPage.messages_Group_TextVoiceIcon)
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无群聊消息,不在群聊页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-语音消息')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-语音消息')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例37：留言-群聊消息-图片信息')
    def test_homepage37(self):
        logging.info("===留言-群聊消息-图片信息===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_pictureMoreBtn).click()
                self.driver.find_element(*MyPage.messages_Group_pictureChooseBtn).click()
                time.sleep(2)
                self.l.get_permission_checkPopover()
                # assert self.driver.find_elements(*MyPage.messages_Group_pictureChooseList)
                self.driver.find_elements(*MyPage.messages_Group_pictureChooseList)[0].click()
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList)) >= 1
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无群聊消息,不在群聊页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-图片信息')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-图片信息')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例38：留言-群聊消息-上麦')
    def test_homepage38(self):
        logging.info("===留言-群聊消息-上麦===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_upMicBtn).click()
                self.l.get_permission_checkPopover()
                # time.sleep(1)
                # assert self.driver.find_elements(*MyPage.messages_Group_upMic10All)
                upMicUserHeadListNum=len(self.driver.find_elements(*MyPage.messages_Group_upMicUserHeadList))
                assert upMicUserHeadListNum>=1
                logging.info("===上麦已成功===")

            else:
                logging.info("===留言-无群聊消息,不在群聊页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-上麦')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-上麦')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例39：留言-群聊消息-上麦用户头像')
    def test_homepage39(self):
        logging.info("===留言-群聊消息-上麦用户头像===")
        try:
            if group_haveOrNot == 1:
                Group_upMicUserHeadListEle_case=self.l.messages_Group_upMicUserHeadListEle()
                if Group_upMicUserHeadListEle_case!=False and len(Group_upMicUserHeadListEle_case)!=0:
                    logging.info("===在上麦中===")
                    self.driver.find_elements(*MyPage.messages_Group_upMicUserHeadList)[0].click()
                    time.sleep(2)
                    upMic_userName=self.l.userHalfPagePopoverNameOrOneselfEle()
                    self.driver.find_element(*MyPage.messages_Group_userHalfPagePopoverHead).click()
                    assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text==upMic_userName
                    self.l.system_goback_key()
                    # assert self.l.messages_Group_detailMoreBtnEle()
                    logging.info("===执行断言成功===")
                else:
                    logging.info("===不在上麦中===")

            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-上麦用户头像')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-上麦用户头像')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例40：留言-群聊消息-麦位表情')
    def test_homepage40(self):
        logging.info("===留言-群聊消息-麦位表情===")
        try:
            if group_haveOrNot == 1:
                Group_upMicUserHeadListEle_case = self.l.messages_Group_upMicUserHeadListEle()
                if Group_upMicUserHeadListEle_case != False and len(Group_upMicUserHeadListEle_case) != 0:
                    logging.info("===在上麦中===")
                    # assert self.driver.find_elements(*MyPage.messages_Group_upMicUserHeadList)
                    self.driver.find_elements(*MyPage.messages_Group_upMicUserHeadList)[0].click()
                    # self.l.userHalfPagePopoverImgListEle_onebyone()
                    time.sleep(3)
                    userHalfPagePopoverImgList_case1=self.driver.find_elements(*MyPage.messages_Group_userHalfPagePopoverImgList)
                    print(len(userHalfPagePopoverImgList_case1))
                    userHalfPagePopoverImgList_case1[0].click()
                    # self.driver.find_element(*MyPage.messages_Group_userHalfPagePopoverImgFirst).click()
                    assert self.driver.find_elements(*MyPage.messages_Group_upMicBtn)
                    logging.info("===断言成功===")
                else:
                    logging.info("===不在上麦中===")

            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-麦位表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-麦位表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例41：留言-群聊消息-下麦')
    def test_homepage41(self):
        logging.info("===留言-群聊消息-下麦===")
        try:
            if group_haveOrNot == 1:
                Group_upMicUserHeadListEle_case = self.l.messages_Group_upMicUserHeadListEle()
                if Group_upMicUserHeadListEle_case != False and len(Group_upMicUserHeadListEle_case) != 0:
                    logging.info("===在上麦中===")
                    upMicLen_num=len(self.driver.find_elements(*MyPage.messages_Group_upMicUserHeadList))
                    messages_Group_upMicBtn_on=self.driver.find_element(*MyPage.messages_Group_upMicBtn)
                    messages_Group_upMicBtn_on.click()
                    self.driver.find_element(*MyPage.messages_Group_upMicTurnOffBtn).click()
                    if upMicLen_num==1:
                        assert self.driver.find_elements(*MyPage.messages_Group_BannerList)
                        # assert self.l.messages_Group_upMicUserHeadListEle()==False
                        # or len(self.driver.find_element(*MyPage.messages_Group_upMicUserHeadList)) == 0
                    else:
                        # assert self.driver.find_elements(*MyPage.messages_Group_upMicUserHeadList)
                        assert upMicLen_num > len(self.driver.find_elements(*MyPage.messages_Group_upMicUserHeadList))
                    logging.info('===断言成功===')
                else:
                    logging.info("===不在上麦中===")

            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-下麦')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-下麦')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例42-45：留言-群聊消息-钻石包发送-领取')
    def test_homepage42(self):
        logging.info("===留言-群聊消息-钻石包发送-领取===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_diamondsPacket).click()
                # assert self.driver.find_element(*MyPage.messages_Group_diamondsPacketPopTitle).text=='幸运红包'
                self.l.messages_Group_diamondsPacketSendAction(2,1000)
                self.l.tap(784,2083)
                assert self.driver.find_elements(*MyPage.messages_Group_TextDiamondsPacket)
                logging.info("===留钻石包已发送成功===")
                self.driver.find_elements(*MyPage.messages_Group_TextDiamondsPacket)[-1].click()
                if self.l.messages_Group_diamondsPacketStatusOpenEle():
                    self.driver.find_element(*MyPage.messages_Group_diamondsPacketStatusOpen).click()
                    time.sleep(1)
                    assert self.driver.find_element(*MyPage.messages_Group_diamondsPacketStatusReceived)
                    self.l.tap(784, 2083)
                    logging.info('===钻石包领取-断言成功===')
                elif self.l.messages_Group_diamondsPacketStatusReceivedEle():
                    assert self.driver.find_element(*MyPage.messages_Group_diamondsPacketStatusReceived)
                    self.l.tap(784, 2083)
                    logging.info('===钻石包已开启-断言成功===')
                elif self.l.messages_Group_diamondsPacketStatusExpiredEle():
                    assert self.driver.find_element(*MyPage.messages_Group_diamondsPacketStatusExpired).text=='已过期'
                    logging.info('===钻石包已过期-断言成功===')

            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-钻石包发送-领取')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-钻石包发送-领取')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例46：留言-群聊消息-游戏浮层')
    def test_homepage46(self):
        logging.info("===留言-群聊消息-游戏浮层===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_GameBtn).click()
                assert self.driver.find_element(*MyPage.messages_Group_GameLayerAll)
                self.l.tap(584,1804)
                logging.info('====游戏浮层-断言成功===')

            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-游戏浮层')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-游戏浮层')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例47、48：留言-群聊消息-礼物送礼')
    def test_homepage47(self):
        logging.info("===留言-群聊消息-礼物送礼===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_GiftBtn).click()
                # assert self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)
                self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)[0].click()
                if self.l.messages_Group_GiftLayerTypeListEle()==False:
                    logging.info('====第一组没有礼物，点击二组===')
                    self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)[1].click()
                logging.info('====第一组有礼物===')
                # self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeList)[0].click()
                GiftLayerGroupNumFirstEle = self.l.messages_Group_GiftLayerGroupNumFirstEle()
                if GiftLayerGroupNumFirstEle!=False and len(GiftLayerGroupNumFirstEle)!=0:
                    GiftLayerGroupNumFirstEle.click()
                self.driver.find_element(*MyPage.messages_Group_GiftLayerSendBtn).click()
                # self.l.messages_Group_GiftTreasuresAwesomeBtnEle()
                time.sleep(15)
                self.l.tap(475, 166)
                assert self.driver.find_element(*MyPage.messages_Group_TextGiftPicIcon)
                logging.info('====礼物送礼-断言成功===')

            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-礼物送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-礼物送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例49、50：留言-群聊消息-顶部banner入口')
    def test_homepage49(self):
        logging.info("===留言-群聊消息-顶部banner入口===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_BannerListLast).click()
                time.sleep(8)
                assert self.driver.find_elements(*MyPage.messages_Group_BannerListLayerClass)
                self.l.tap(475, 166)
                self.driver.find_element(*MyPage.messages_Group_BannerListPackupBtn).click()
                assert self.driver.find_elements(*MyPage.messages_Group_BannerListSmallBtn)
                logging.info('====顶部banner入口收起成功===')
                self.driver.find_element(*MyPage.messages_Group_BannerListSmallBtn).click()
                assert self.driver.find_elements(*MyPage.messages_Group_BannerList)
                logging.info('====顶部banner入口展开成功===')
            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-顶部banner入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-顶部banner入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例51-53：留言-群聊消息-更多按钮')
    def test_homepage51(self):
        logging.info("===留言-群聊消息-更多按钮===")
        try:
            if group_haveOrNot == 1:
            # if self.l.messages_Group_detailMoreBtnEle():
                logging.info("===留言-有群聊消息，在群聊页面===")
                self.driver.find_element(*MyPage.messages_Group_detailMoreBtn).click()
                self.driver.find_elements(*MyPage.messages_Group_MoreUserHeadList)[0].click()
                logging.info('===更多跳转详情页成功===')
                group_UserName=self.l.userHalfPagePopoverNameOrOneselfEle()
                self.driver.find_element(*MyPage.messages_Group_userHalfPagePopoverHead).click()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text==group_UserName
                self.l.system_goback_key()
                # assert self.driver.find_elements(*MyPage.messages_Group_MoreUserAll)
                logging.info('===头像跳转个人主页成功===')
                group_userlist1=len(self.driver.find_elements(*MyPage.messages_Group_MoreUserHeadList))
                if self.l.groupCount_number(count_text)<=20:
                    assert ' (''{}'')'.format(group_userlist1)==count_text
                else:
                    assert len(self.driver.find_elements(*MyPage.messages_Group_MoreUserHeadList))==20
                logging.info('===用户数据正常===')
            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-更多按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-更多按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例54-55：留言-群聊消息-更多-动态-更多详情页')
    def test_homepage54(self):
        logging.info("===留言-群聊消息-更多-动态-更多详情页===")
        try:
            if group_haveOrNot == 1:
                if self.driver.find_elements(*MyPage.messages_Group_MoreUserHeadList):
                    logging.info("===留言-有群聊消息，在群聊页面===")
                    if self.l.messages_Group_MoreMomentAllEle()==False:
                        logging.info('===没有动态元素===')
                    else:
                        logging.info('===有动态元素===')
                        self.driver.find_element(*MyPage.messages_Group_MoreMomentPicLast).click()
                        assert self.driver.find_element(*MyPage.messages_Group_MoreMomentMoreTitle).text=='动态'
                        assert self.driver.find_elements(*MyPage.messages_Group_MoreMomentMoreSendBtn)
                        self.driver.find_element(*MyPage.messages_Group_MoreMomentMoreGoback).click()
                        # assert self.l.messages_Group_MoreMomentAllEle()
                        logging.info('===更多跳转详情页成功===')
            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-更多-动态-更多详情页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-更多-动态-更多详情页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例56：留言-群聊消息-更多-动态-大图模式')
    def test_homepage56(self):
        logging.info("===留言-群聊消息-更多-动态-大图模式===")
        try:
            if group_haveOrNot == 1:
                if self.driver.find_elements(*MyPage.messages_Group_MoreUserHeadList):
                    logging.info("===留言-有群聊消息，在群聊页面===")
                    if self.l.messages_Group_MoreMomentAllEle() == False:
                        logging.info('===没有动态元素===')
                    else:
                        logging.info('===有动态元素===')
                        print(self.l.messages_Group_MoreMomentPicFrontEle())
                        group_MoreMomentPicFrontEle_case=self.l.messages_Group_MoreMomentPicFrontEle()
                        if group_MoreMomentPicFrontEle_case==False or len(group_MoreMomentPicFrontEle_case)==1:
                            logging.info('===只有一个动态===')
                        else:
                            logging.info('===多个动态===')
                            self.driver.find_elements(*MyPage.messages_Group_MoreMomentPicFront)[0].click()
                            assert self.driver.find_element(*MyPage.messages_Group_MoreMomentMaxZanBtn)
                            self.l.swipe(531,1776,531,900)
                            assert self.driver.find_element(*MyPage.messages_Group_MoreMomentMaxZanBtn)
                            self.l.system_goback_key()
                            # assert self.l.messages_Group_MoreMomentAllEle()
                            logging.info('===大图模式-断言成功===')
            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-更多-动态-大图模式')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-更多-动态-大图模式')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例57：留言-群聊消息-返回')
    def test_homepage57(self):
        logging.info("===留言-群聊消息-返回===")
        try:
            if group_haveOrNot == 1:
                if self.driver.find_elements(*MyPage.messages_Group_MoreUserHeadList):
                    logging.info("===留言-有群聊消息，在群聊页面===")
                    self.l.system_goback_key()
                    self.driver.find_element(*MyPage.messages_Group_goback).click()
                    assert self.driver.find_element(*MyPage.messages_title).text=='留言'
                    logging.info('===返回-断言成功===')
            else:
                logging.info("===不在群聊中===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-群聊消息-返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-群聊消息-返回')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例58-59：留言-陌生人留言有无')
    def test_homepage58(self):
        logging.info("===留言-陌生人留言有无===")
        try:
            global stranger_haveOrNot
            Stranger_entryHeadPicEle_case=self.l.messages_Stranger_entryHeadPicEle()
            if Stranger_entryHeadPicEle_case!=False and len(Stranger_entryHeadPicEle_case)!=0:
                stranger_haveOrNot = 1
                logging.info("===留言-有陌生人消息===")
                self.driver.find_element(*MyPage.messages_Stranger_entryHeadPic).click()
                assert self.driver.find_element(*MyPage.messages_Stranger_title).text=='陌生人留言'
                logging.info('===返回-断言成功===')
            else:
                stranger_haveOrNot =0
                logging.info("===没有陌生人消息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例60：留言-陌生人留言-陌生人列表')
    def test_homepage60(self):
        logging.info("===留言-陌生人留言===")
        try:
            if stranger_haveOrNot == 1:
                if self.driver.find_element(*MyPage.messages_Stranger_title).text=='陌生人留言':
                    logging.info("===留言-在陌生人消息列表===")
                    first_userName=self.driver.find_elements(*MyPage.messages_Stranger_UserNameList)[0].text
                    print(first_userName)
                    print(self.driver.find_elements(*MyPage.messages_Stranger_UserEntryList))
                    self.driver.find_elements(*MyPage.messages_Stranger_UserNameList)[0].click()
                    # assert self.driver.find_element(*MyPage.messages_Stranger_title).text=='陌生人留言'
                    assert self.driver.find_element(*MyPage.messages_Stranger_userTitleName).text==first_userName
                    logging.info('===返回-断言成功===')
            else:
                logging.info("===留言-没有陌生人消息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-陌生人列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-陌生人列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例61：留言-陌生人留言-一对一更多个人主页')
    def test_homepage61(self):
        logging.info("===留言-陌生人留言-一对一更多个人主页===")
        try:
            if stranger_haveOrNot == 1:
            # Stranger_userMoreBtn_case=self.l.messages_Stranger_userMoreBtnEle()
            # if Stranger_userMoreBtn_case!=False and len(Stranger_userMoreBtn_case)!=0:
                logging.info("===留言-在陌生人-一对一消息中===")
                self.driver.find_element(*MyPage.messages_Stranger_userMoreBtn).click()
                first_userName = self.driver.find_element(*MyPage.messages_Stranger_userHalfPagePopoverName).text
                self.driver.find_element(*MyPage.messages_Stranger_userHalfPagePopoverHead).click()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == first_userName
                self.l.system_goback_key()
                logging.info('===返回-断言成功===')
            else:
                logging.info("===留言-没有陌生人消息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-一对一更多个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-一对一更多个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例62：留言-陌生人留言-一对一更多个人浮层送礼')
    def test_homepage62(self):
        logging.info("===留言-陌生人留言-一对一更多个人浮层送礼===")
        try:
            if stranger_haveOrNot == 1:
            # if self.l.messages_Stranger_userMoreBtnEle():
                logging.info("===留言-有陌生人消息，在一对一页面===")
                self.driver.find_element(*MyPage.messages_Stranger_userMoreBtn).click()
                self.driver.find_element(*MyPage.messages_Stranger_SendGiftBtn).click()
                # assert self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)
                self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)[0].click()
                if self.l.messages_Group_GiftLayerTypeListEle() == False:
                    logging.info('====第一组没有礼物，点击二组===')
                    self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)[1].click()
                logging.info('====第一组有礼物===')
                # self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeList)[0].click()
                GiftLayerGroupNumFirstEle = self.l.messages_Group_GiftLayerGroupNumFirstEle()
                if GiftLayerGroupNumFirstEle != False and len(GiftLayerGroupNumFirstEle) != 0:
                    self.driver.find_element(*MyPage.messages_Group_GiftLayerGroupNumFirst).click()
                self.driver.find_element(*MyPage.messages_Group_GiftLayerSendBtn).click()
                self.l.messages_Group_GiftTreasuresAwesomeBtnEle()
                time.sleep(5)
                self.l.tap(475, 166)
                assert self.driver.find_element(*MyPage.messages_Group_TextGiftPicIcon)
                logging.info('====礼物送礼-断言成功===')
            else:
                logging.info("===留言-无陌生人消息,不在一对一页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-一对一更多个人浮层送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-一对一更多个人浮层送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例63-65：留言-陌生人留言-一对一更多个人浮层视频通话')
    def test_homepage63(self):
        logging.info("===留言-陌生人留言-一对一更多个人浮层视频通话===")
        try:
            if stranger_haveOrNot == 1:
            # if self.l.messages_Stranger_userMoreBtnEle():
                logging.info("===留言-有陌生人消息，在一对一页面===")
                self.driver.find_element(*MyPage.messages_Stranger_userMoreBtn).click()
                if self.l.messages_Stranger_videoCallEnableEle()==False:
                    logging.info("===视频聊不可拨打===")
                else:
                    self.driver.find_element(*MyPage.messages_Stranger_videoCallEnable).click()
                    self.l.get_permission_checkPopover()
                    # assert self.driver.find_element(*MyPage.messages_Stranger_callingInfo)
                    time.sleep(20)
                    assert self.driver.find_elements(*MyPage.messages_Stranger_TextCallNoAnswer)[-1].text == '用户没有回答'
                    print(self.driver.find_elements(*MyPage.messages_Stranger_TextCallNoAnswer)[-1].text)
                    self.driver.find_elements(*MyPage.messages_Stranger_TextCallNoAnswer)[-1].click()
                    if self.l.messages_Stranger_videoCallUnablePopAllEle():
                        self.driver.find_element(*MyPage.messages_Stranger_videoCallUnablePopConfirmBtn).click()
                        logging.info('存在不可拨打弹窗,已点击')
                    else:
                        time.sleep(20)
                        assert self.driver.find_elements(*MyPage.messages_Stranger_TextCallNoAnswer)[-1].text == '用户没有回答'
                        logging.info('====一对一更多个人浮层视频通话-断言成功===')

            else:
                logging.info("===留言-无陌生人消息,不在一对一页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例66：留言-陌生人留言-一对一输入框')
    def test_homepage66(self):
        logging.info("===留言-陌生人留言-一对一输入框===")
        try:
            if stranger_haveOrNot == 1:
            # if self.l.messages_Stranger_userMoreBtnEle():
                logging.info("===留言-有陌生人消息，在一对一页面===")
                name_text = "vndsiiovnhif VFvdfbgf43545646SHTR"
                InputEdit_case=self.driver.find_element(*MyPage.messages_Stranger_InputEdit)
                InputEdit_case.click()
                time.sleep(2)
                InputEdit_case.send_keys(name_text)
                # self.driver.find_element(*MyPage.messages_Stranger_InputEdit).send_keys(name_text)
                self.driver.find_element(*MyPage.messages_Stranger_InputSendBtn).click()
                time.sleep(2)
                assert self.driver.find_elements(*MyPage.messages_Stranger_TextInputContentText)[-1].text == name_text
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无陌生人消息,不在一对一页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-一对一输入框')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-一对一输入框')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例67：留言-陌生人留言-表情')
    def test_homepage67(self):
        logging.info("===留言-陌生人留言-表情===")
        try:
            if stranger_haveOrNot == 1:
            # if self.l.messages_Stranger_userMoreBtnEle():
                logging.info("===留言-有陌生人消息，在一对一页面===")
                self.driver.find_element(*MyPage.messages_Group_faceGifBtn).click()
                time.sleep(2)
                # assert self.driver.find_elements(*MyPage.messages_Group_imgMotionList)
                self.driver.find_elements(*MyPage.messages_Group_imgMotionList)[2].click()
                time.sleep(2)
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList)) >= 1
                self.l.tap(337, 1247)
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无陌生人消息,不在一对一页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例68：留言-陌生人留言-更多翻译')
    def test_homepage68(self):
        logging.info("===留言-陌生人留言-更多翻译===")
        try:
            if stranger_haveOrNot == 1:
            # if self.l.messages_Stranger_userMoreBtnEle():
                logging.info("===留言-有陌生人消息，在一对一页面===")
                self.driver.find_element(*MyPage.messages_Stranger_inputMoreBtn).click()
                # assert self.driver.find_elements(*MyPage.messages_Stranger_TranslateBtn)
                self.driver.find_element(*MyPage.messages_Stranger_TranslateBtn).click()
                # usermessage_Voice_chat_toast = self.l.toast_message('翻译已关闭')
                # assert usermessage_Voice_chat_toast.text == "翻译已关闭"
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无陌生人消息,不在一对一页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-更多翻译')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-更多翻译')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例69：留言-陌生人留言-更多相册')
    def test_homepage69(self):
        logging.info("===留言-陌生人留言-更多相册===")
        try:
            if stranger_haveOrNot == 1:
            # if self.l.messages_Stranger_userMoreBtnEle():
                logging.info("===留言-有陌生人消息，在一对一页面===")
                # assert self.driver.find_element(*MyPage.messages_Stranger_phonePictureBtn)
                self.driver.find_element(*MyPage.messages_Stranger_phonePictureBtn).click()
                self.l.get_permission_checkPopover()
                # assert self.driver.find_elements(*MyPage.messages_Group_pictureChooseList)
                self.driver.find_elements(*MyPage.messages_Stranger_phonePictureListSelect)[0].click()
                self.driver.find_element(*MyPage.messages_Stranger_phonePictureListConfirmBtn).click()
                time.sleep(2)
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList)) >= 1
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无陌生人消息,不在一对一页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-更多相册')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-更多相册')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    # 85手机相机问题
    @allure.story('留言')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例70：留言-陌生人留言-更多相机')
    def test_homepage70(self):
        logging.info("===留言-陌生人留言-更多相机===")
        try:
            if stranger_haveOrNot == 1:
            # if self.l.messages_Stranger_userMoreBtnEle():
                logging.info("===留言-有陌生人消息，在一对一页面===")
                # assert self.driver.find_elements(*MyPage.messages_Stranger_CameraBtn)
                self.driver.find_element(*MyPage.messages_Stranger_CameraBtn).click()
                self.l.get_permission_checkPopover()
                self.driver.find_element(*MyPage.messages_Stranger_CameraTakeBtn).click()
                self.driver.find_element(*MyPage.messages_Stranger_CameraTakeDoneBtn).click()
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList)) >= 1
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无陌生人消息,不在一对一页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-更多相机')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-更多相机')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例71：留言-陌生人留言-更多视频聊天')
    def test_homepage71(self):
        logging.info("===留言-陌生人留言-更多视频聊天===")
        try:
            if stranger_haveOrNot == 1:
            # if self.l.messages_Stranger_userMoreBtnEle():
                logging.info("===留言-有陌生人消息，在一对一页面===")
                # assert self.driver.find_elements(*MyPage.messages_Stranger_VideoCallBtn)
                self.driver.find_element(*MyPage.messages_Stranger_VideoCallBtn).click()
                self.l.get_permission_checkPopover()
                # assert self.driver.find_element(*MyPage.messages_Stranger_callingInfo)
                time.sleep(18)
                assert self.driver.find_elements(*MyPage.messages_Stranger_TextCallNoAnswer)[-1].text == '用户没有回答'
                self.driver.find_element(*MyPage.messages_Stranger_userGoback).click()
                self.l.system_goback_key()
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无陌生人消息,不在一对一页面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-陌生人留言-更多视频聊天')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-陌生人留言-更多视频聊天')
            logging.info(f'截图成功，图片为{screen_name}')
            raise








    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例72：留言-一对一列表-用户头像跳转')
    def test_homepage72(self):
        logging.info("===留言-一对一列表-用户头像跳转===")
        try:
            global user_haveOrNot
            User_EntryHeadEle_case=self.l.messages_User_EntryHeadEle()
            if User_EntryHeadEle_case!=False and len(User_EntryHeadEle_case)!=0:
                user_haveOrNot=1
                logging.info("===留言-有一对一消息，开始点击头像===")
                OneUserEntryUserNameList_case=self.l.messages_User_EntryUserNameEle()
                # print(type(OneUserEntryUserNameList))
                if OneUserEntryUserNameList_case!=False:
                    logging.info('===有用户头像且获取到了昵称元素===')
                    expected_name1=OneUserEntryUserNameList_case.text
                    # print(OneUserEntryUserNameList_case.text)
                    self.driver.find_elements(*MyPage.messages_User_EntryHead)[0].click()
                    expected_name2=self.driver.find_element(*MyPage.user_own_pagePersonalName).text
                    # print(self.driver.find_element(*MyPage.user_own_pagePersonalName).text)
                    assert expected_name2==expected_name1
                    self.l.system_goback_key()
                    assert self.driver.find_elements(*MyPage.messages_User_EntryHead)
                # else:
                #     logging.info('===有用户头像但是没有获取到昵称元素===')
            else:
                user_haveOrNot=0
                logging.info("===留言-没有一对一消息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一列表-用户头像跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一列表-用户头像跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例73：留言-一对一列表-列表跳转')
    def test_homepage73(self):
        logging.info("===留言-一对一列表-列表跳转===")
        try:
            if user_haveOrNot == 1:
                # OneUserEntryHead1 = self.l.messages_User_EntryHeadEle()
                # if OneUserEntryHead1 != False:
                logging.info("===留言-有一对一消息===")
                OneUserEntryUserNameList = self.l.messages_User_EntryUserNameEle()
                OneUserEntryUserNameList_text1=OneUserEntryUserNameList.text
                print(OneUserEntryUserNameList)
                if OneUserEntryUserNameList != False:
                    logging.info('===有用户头像且获取到了昵称元素===')
                    # self.driver.find_elements(*MyPage.messages_User_EntryHead)[0].click()
                    OneUserEntryUserNameList.click()
                    TitleName1=self.driver.find_element(*MyPage.messages_User_TitleName).text
                    assert TitleName1 == OneUserEntryUserNameList_text1
                    # else:
                    #     logging.info('===有用户头像但是没有获取到昵称元素===')
            else:
                logging.info("===留言-没有一对一消息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一列表-列表跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一列表-列表跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例74：留言-一对一-更多个人主页')
    def test_homepage74(self):
        logging.info("===留言-一对一-更多个人主页===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info("===留言-有一对一消息===")
                self.driver.find_element(*MyPage.messages_User_MoreBtn).click()
                first_userName = self.driver.find_element(*MyPage.messages_Stranger_userHalfPagePopoverName).text
                self.driver.find_element(*MyPage.messages_Stranger_userHalfPagePopoverHead).click()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == first_userName
                self.l.system_goback_key()
                # assert self.driver.find_element(*MyPage.messages_User_MoreBtn)
                logging.info('===返回-断言成功===')
            else:
                logging.info("===留言-没有一对一消息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-更多个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-更多个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例75：留言-一对一-更多个人浮层送礼')
    def test_homepage75(self):
        logging.info("===留言-一对一-更多个人浮层送礼===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info('====有私聊消息，在私聊消息界面===')
                self.driver.find_element(*MyPage.messages_User_MoreBtn).click()
                self.driver.find_element(*MyPage.messages_Stranger_SendGiftBtn).click()
                # assert self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)
                self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)[0].click()
                if self.l.messages_Group_GiftLayerTypeListEle() == False:
                    logging.info('====第一组没有礼物，点击二组===')
                    self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeTab)[1].click()
                logging.info('====第一组有礼物===')
                # self.driver.find_elements(*MyPage.messages_Group_GiftLayerTypeList)[0].click()
                GiftLayerGroupNumFirstEle = self.l.messages_Group_GiftLayerGroupNumFirstEle()
                if GiftLayerGroupNumFirstEle != False and len(GiftLayerGroupNumFirstEle) != 0:
                    self.driver.find_element(*MyPage.messages_Group_GiftLayerGroupNumFirst).click()
                self.driver.find_element(*MyPage.messages_Group_GiftLayerSendBtn).click()
                self.l.messages_Group_GiftTreasuresAwesomeBtnEle()
                time.sleep(5)
                self.l.tap(475, 166)
                assert self.driver.find_element(*MyPage.messages_Group_TextGiftPicIcon)
                logging.info('====礼物送礼-断言成功===')
            else:
                logging.info("===留言-没有一对一消息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-更多个人浮层送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-更多个人浮层送礼')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例76-78：留言-一对一-更多视频通话')
    def test_homepage76(self):
        logging.info("===留言-一对一-更多视频通话===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info('====有私聊消息，在私聊消息界面===')
                self.driver.find_element(*MyPage.messages_User_MoreBtn).click()
                if self.l.messages_Stranger_videoCallEnableEle() == False:
                    logging.info("===视频聊不可拨打===")
                else:
                    self.driver.find_element(*MyPage.messages_Stranger_videoCallEnable).click()
                    self.l.get_permission_checkPopover()
                    # assert self.driver.find_element(*MyPage.messages_Stranger_callingInfo)
                    time.sleep(20)
                    TextCallNoAnswer_case=self.driver.find_elements(*MyPage.messages_Stranger_TextCallNoAnswer)[-1]
                    assert TextCallNoAnswer_case.text == '用户没有回答'
                    print(TextCallNoAnswer_case.text)
                    TextCallNoAnswer_case.click()
                    if self.l.messages_Stranger_videoCallUnablePopAllEle():
                        self.driver.find_element(*MyPage.messages_Stranger_videoCallUnablePopConfirmBtn).click()
                        logging.info('存在不可拨打弹窗,已点击')
                    else:
                        time.sleep(20)
                        assert TextCallNoAnswer_case.text == '用户没有回答'
                        logging.info('====一对一更多个人浮层视频通话-断言成功===')
            else:
                logging.info("===留言-无私聊消息，不在私聊消息界面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-更多视频通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-更多视频通话')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例79：留言-一对一-输入框')
    def test_homepage79(self):
        logging.info("===留言-一对一-输入框===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info('====有私聊消息，在私聊消息界面===')
                name_text = "vndsiiovnhif VFvdfbgf43FHDEHZD并回复改掉哈545646SHTR"
                Stranger_InputEdit_case=self.driver.find_element(*MyPage.messages_Stranger_InputEdit)
                Stranger_InputEdit_case .click()
                Stranger_InputEdit_case.send_keys(name_text)
                self.driver.find_element(*MyPage.messages_Stranger_InputSendBtn).click()
                time.sleep(1)
                assert self.driver.find_elements(*MyPage.messages_Stranger_TextInputContentText)[-1].text == name_text
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无私聊消息，不在私聊消息界面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-输入框')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-输入框')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例80：留言-一对一-表情')
    def test_homepage80(self):
        logging.info("===留言-一对一-表情===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info('====有私聊消息，在私聊消息界面===')
                self.driver.find_element(*MyPage.messages_Group_faceGifBtn).click()
                time.sleep(5)
                # assert self.driver.find_elements(*MyPage.messages_Group_imgMotionList)
                self.driver.find_elements(*MyPage.messages_Group_imgMotionList)[2].click()
                time.sleep(2)
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList)) >= 1
                self.l.tap(337, 1247)
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无私聊消息，不在私聊消息界面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-表情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例81：留言-一对一-更多翻译')
    def test_homepage81(self):
        logging.info("===留言-一对一-更多翻译===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info('====有私聊消息，在私聊消息界面===')
                self.driver.find_element(*MyPage.messages_Stranger_inputMoreBtn).click()
                # assert self.driver.find_elements(*MyPage.messages_Stranger_TranslateBtn)
                # self.driver.find_elements(*MyPage.messages_Stranger_TranslateBtn).click()
                # usermessage_Voice_chat_toast = self.l.toast_message('翻译已关闭')
                # assert usermessage_Voice_chat_toast.text == "翻译已关闭"
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无私聊消息，不在私聊消息界面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-更多翻译')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-更多翻译')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例82：留言-一对一-更多相册')
    def test_homepage82(self):
        logging.info("===留言-一对一-更多相册===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info('====有私聊消息，在私聊消息界面===')
                self.driver.find_element(*MyPage.messages_Stranger_phonePictureBtn).click()
                self.l.get_permission_checkPopover()
                self.driver.find_elements(*MyPage.messages_Stranger_phonePictureListSelect)[0].click()
                self.driver.find_element(*MyPage.messages_Stranger_phonePictureListConfirmBtn).click()
                time.sleep(2)
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList)) >= 1
                logging.info('===断言成功===')

            else:
                logging.info("===留言-无私聊消息，不在私聊消息界面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-更多相册')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-更多相册')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例83：留言-一对一-更多相机')
    def test_homepage83(self):
        logging.info("===留言-一对一-更多相机===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info('====有私聊消息，在私聊消息界面===')
                # assert self.driver.find_elements(*MyPage.messages_Stranger_CameraBtn)
                self.driver.find_element(*MyPage.messages_Stranger_CameraBtn).click()
                self.l.get_permission_checkPopover()
                self.driver.find_element(*MyPage.messages_Stranger_CameraTakeBtn).click()
                self.driver.find_element(*MyPage.messages_Stranger_CameraTakeDoneBtn).click()
                assert len(self.driver.find_elements(*MyPage.messages_Group_TextImageList)) >= 1
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无私聊消息，不在私聊消息界面===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-更多相机')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-更多相机')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('留言')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例84：留言-一对一-更多视频聊天')
    def test_homepage84(self):
        logging.info("===留言-一对一-更多视频聊天===")
        try:
            if user_haveOrNot == 1:
            # if self.l.messages_User_MoreBtnEle():
                logging.info('====有私聊消息，在私聊消息界面===')
                # assert self.driver.find_elements(*MyPage.messages_Stranger_VideoCallBtn)
                self.driver.find_element(*MyPage.messages_Stranger_VideoCallBtn).click()
                self.l.get_permission_checkPopover()
                # assert self.driver.find_element(*MyPage.messages_Stranger_callingInfo)
                time.sleep(18)
                assert self.driver.find_elements(*MyPage.messages_Stranger_TextCallNoAnswer)[-1].text == '用户没有回答'
                self.driver.find_element(*MyPage.messages_Stranger_userGoback).click()
                self.l.system_goback_key()
                logging.info('===断言成功===')
            else:
                logging.info("===留言-无私聊消息，不在私聊消息界面===")
                self.l.system_goback_key()
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('留言-一对一-更多视频聊天')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('留言-一对一-更多视频聊天')
            logging.info(f'截图成功，图片为{screen_name}')
            raise






    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例85-86：我的等级外部显示和内部跳转')
    def test_homepage85(self):
        logging.info("===我的等级-我的等级外部显示和内部跳转===")
        self.l.tab_Mine_Btn()
        mylevel_value=self.l.myVipLevel_level_value()
        try:
            if mylevel_value==False:
                logging.error("===我的等级外部显示没有数值===")
            elif mylevel_value==None:
                logging.error("===我的等级-该用户性别未知===")
            else:
                logging.info("===我的等级-我的等外部显示不为空===")
                self.l.vip_Level_right_click()
                time.sleep(5)
                vipLevel_level_value=self.l.vipLevel_level_value()
                print(vipLevel_level_value)
                assert vipLevel_level_value == mylevel_value, "外部等级值显示和内部横条不一致"
                self.l.vip_Level_mylevel_goback()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的等级外部显示和内部跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的等级外部显示和内部跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例87：我的等级-男-立即充值')
    def test_homepage87(self):
        logging.info("===我的等级-男-立即充值===")
        self.l.tab_Mine_Btn()
        # level_Gender = self.l.myProfile_Gender_ManorW()
        try:
            self.l.vip_Level_right_click()
            topUpBtn=self.l.vipLevel_level_topUpBtn()
            if user_gender==1:
                logging.info("===男生===")
                # self.l.swipe(613, 2013, 544, 794)
                if topUpBtn!=False:
                    logging.info("===有充值按钮===")
                    topUpBtn[0].click()
                    self.c.h5_to_native()
                    time.sleep(5)
                    assert self.driver.find_element(*MyPage.myBalance_myDiamondText).text == '我的钻石', "点击立即充值未进入我的余额页面"
                    self.l.system_goback_key()
                    self.c.native_to_h5()
                    # self.l.tap(564,205)
                    # self.driver.find_element(*MyPage.level_goback).click()
                    # self.c.h5_to_native()
                else:
                    logging.info("===没有充值按钮===")
                    self.l.vip_Level_mylevel_goback()

            else:
                logging.info("===不是男生===")
                # self.l.swipe(613, 2013, 544, 794)
                assert topUpBtn == [] or False,'不是男生，但是有充值按钮'
                self.l.vip_Level_mylevel_goback()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的等级-男-立即充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的等级-男-立即充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例88：我的等级-等级横条')
    def test_homepage88(self):
        logging.info("===我的等级-等级横条===")
        # self.l.tab_Mine_Btn()
        # self.l.tap(930, 2123)
        try:
            # self.l.tap(914,2127)
            if user_gender==1:
                logging.info('===用户为男生===')
                # self.l.vip_Level_right_click()
                vipLevel_level_value = self.l.vipLevel_level_value()
                vipLevel_levelLeft_value=self.l.vipLevel_levelLeft_value()
                if vipLevel_level_value=='Lv0' and vipLevel_levelLeft_value=='Lv0':
                    logging.info('===等级为Lv0===')
                    assert self.driver.find_element(*MyPage.level_tabSelectedManCss).text == 'Lv1', "内部等级左边等级值显示和内部横条不一致"
                    logging.info('===开始断言等级特权弹窗===')
                    self.driver.find_element(*MyPage.level_privilege_DetailAllCss).click()
                    assert self.driver.find_element(*MyPage.level_privilege_detailPopoverHeadFrame).text == '进场气泡', "点击第二个，等级特权详情弹窗标题不是头像框"
                    logging.info('===开始断言等级特权弹窗是否消失===')
                    self.l.tap(760, 2036)
                    assert self.driver.find_element(*MyPage.level_privilege_DetailAllCss), "点击等级特权详情弹窗，未消失"
                    self.l.vip_Level_mylevel_goback()

                else:
                    logging.info('===等级不为Lv0，开始断言等级与横条等级内容===')
                    print(vipLevel_level_value)
                    assert self.driver.find_element(*MyPage.level_tabSelectedManCss).text == vipLevel_levelLeft_value, "内部等级值显示和内部横条不一致"
                    logging.info('===开始断言等级特权弹窗===')
                    self.driver.find_element(*MyPage.level_privilege_DetailAllCss).click()
                    assert self.driver.find_element(*MyPage.level_privilege_detailPopoverHeadFrame).text == '进场气泡', "点击第二个，等级特权详情弹窗标题不是头像框"
                    logging.info('===开始断言等级特权弹窗是否消失===')
                    self.l.tap(760, 2036)
                    assert self.driver.find_element(*MyPage.level_privilege_DetailAllCss), "点击等级特权详情弹窗，未消失"
                    self.l.vip_Level_mylevel_goback()

            elif user_gender==2:
                logging.info('===用户为女生===')
                self.l.vip_Level_right_click()
                vipLevel_level_value = self.l.vipLevel_level_value()
                logging.info('===开始断言等级与横条等级内容===')
                print(vipLevel_level_value)
                assert self.driver.find_element(*MyPage.level_tabSelectedWomanCss).text == vipLevel_level_value, "内部等级值显示和内部横条不一致"
                logging.info('===开始断言等级特权弹窗===')
                self.driver.find_element(*MyPage.level_detail_itemCheckRightClick).click()
                assert self.driver.find_element(*MyPage.level_privilege_detailPopoverHeadFrame).text == '进场气泡', "点击第二个，等级特权详情弹窗标题不是头像框"
                logging.info('===开始断言等级特权弹窗是否消失===')
                time.sleep(2)
                self.l.tap(760, 2036)
                assert self.driver.find_element(*MyPage.level_privilege_DetailAll), "点击等级特权详情弹窗，未消失"
                self.l.vip_Level_mylevel_goback()


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的等级-等级横条')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的等级-等级横条')
            logging.info(f'截图成功，图片为{screen_name}')
            raise






    #页面滑动 self.l.swipe(40, 387, 40, 1473,100)
    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例89，90,91，92：我的任务-男女-有奖励红点或积分')
    def test_homepage89(self):
        logging.info("===我的任务-有奖励红点或积分显示===")
        try:
            self.l.tab_Mine_Btn()
            self.l.tap(970, 2114)
            global my_Tasks_entryTwoText
            my_Tasks_entryTwoText = self.l.my_Tasks_entryTwoText()
            if my_Tasks_entryTwoText != False:
                logging.info("===我的任务-外部显示有数据===")
                if my_Tasks_entryTwoText=='新奖励':
                    logging.info("===我的任务-新奖励===")
                    self.driver.find_element(*MyPage.MyTasks_entry_RightClick).click()
                    # time.sleep(2)
                    # self.l.tap(1061, 111)
                    time.sleep(1)
                    self.l.swipe(40, 387, 40, 1473,100)
                    time.sleep(1)
                    self.l.swipe(40, 387, 40, 1473,100)
                    tasks_rewards_next=self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert tasks_rewards_next.get_attribute('selected') == 'true', '用户显示新奖励跳转后不在奖励页面'
                    assert self.driver.find_element(*MyPage.MyTasks_rewards_RedTagNew),'用户显示新奖励但奖励tab上没有新奖励红色tag'
                    # self.l.system_goback_key()
                else:
                    logging.info("===我的任务-具体积分===")
                    self.driver.find_element(*MyPage.MyTasks_entry_RightClick).click()
                    self.l.tap(1061, 111)
                    tasks_points_next = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                    assert tasks_points_next.get_attribute('selected') == 'true', '用户显示积分值跳转后不在任务页面'
                    MyTasks_tab_pointsNumber=self.driver.find_element(*MyPage.MyTasks_tab_pointsNumber).text
                    MyTasks_tab_pointsNumberIcon='{}''\x20''[points]'.format(MyTasks_tab_pointsNumber)
                    assert MyTasks_tab_pointsNumberIcon==my_Tasks_entryTwoText,'内外积分值不一致'
                    # self.l.system_goback_key()

            else:
                logging.error("===我的任务-外部显示没有积分数据===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-有奖励红点或积分显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-有奖励红点或积分显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    # 页面滑动未完成 self.l.swipe(40, 387, 40, 1473,100)
    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例93：我的任务--男女-兑换奖励按钮')
    def test_homepage93(self):
        logging.info("===我的任务-兑换奖励按钮===")
        # self.l.tab_Mine_Btn()
        # my_Tasks_entryTwoText = self.l.my_Tasks_entryTwoText()
        try:
            if my_Tasks_entryTwoText != False:
                logging.info("===我的任务-外部显示有数据===")
                if my_Tasks_entryTwoText == '新奖励':
                    logging.info("===我的任务-新奖励===")
                    # self.driver.find_element(*MyPage.MyTasks_entry_RightClick).click()
                    # self.l.tap(1061,111)
                    self.l.swipe(40, 387, 40, 1473,100)
                    self.l.swipe(40, 387, 40, 1473, 100)
                    self.l.swipe(40, 387, 40, 1473,100)
                    MyTasks_tab_rewards = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert MyTasks_tab_rewards.get_attribute('selected') == 'true', '跳转至奖励页面'
                    self.l.swipe(40, 387, 40, 1473, 100)
                    MyTasks_rewardstab_pointsSwitchBtn = self.driver.find_element(*MyPage.MyTasks_tab_pointsSwitchBtn)
                    logging.info("===兑换奖励-===")
                    assert MyTasks_rewardstab_pointsSwitchBtn.text == '更多积分'
                    MyTasks_rewardstab_pointsSwitchBtn.click()
                    assert MyTasks_rewardstab_pointsSwitchBtn.text == '兑换奖励'

                else:
                    logging.info("===我的任务-具体积分===")
                    # self.driver.find_element(*MyPage.MyTasks_entry_RightClick).click()
                    self.l.tap(1061,111)
                    MyTasks_tasktab_pointsSwitchBtn = self.driver.find_element(*MyPage.MyTasks_tab_pointsSwitchBtn)
                    assert MyTasks_tasktab_pointsSwitchBtn.text == '兑换奖励'
                    MyTasks_tasktab_pointsSwitchBtn.click()
                    assert MyTasks_tasktab_pointsSwitchBtn.text == '更多积分'


            else:
                logging.error("===我的任务-外部显示没有积分数据===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-兑换奖励按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-兑换奖励按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例94：我的任务-男-通行证历史')
    def test_homepage94(self):
        logging.info("====我的任务-男-通行证历史'===")
        try:
            if user_gender == 1:
                logging.info("===男生===")
                self.l.tap(1061,111)
                self.l.swipe(40, 387, 40, 1473, 100)
                # self.l.swipe(40, 387, 40, 1473, 100)
                # self.l.swipe(40, 387, 40, 1473, 100)
                monthlyHistory=self.l.my_Tasks_pointsMonthlyHistory()
                if monthlyHistory!=False:
                    logging.info("===有充值月卡，有记录===")
                    monthlyHistory.click()
                    time.sleep(2)
                    assert self.driver.find_element(*MyPage.MyTasks_tab_pointsMonthlyHistoryPopoverUserID).text == 'ID:''{}'.format(pageUserId), "充值月卡浮层该用户姓名不一致"
                    self.l.system_goback_key()

                else:
                    logging.info("===没有充值过月卡，无记录===")

            else:
                logging.info("===不是男生===")
                monthlyHistory = self.l.my_Tasks_pointsMonthlyHistory()
                assert monthlyHistory == False, '不是男生，但是有充值月卡记录'


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-通行证历史')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-通行证历史')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例95：我的任务-男女-签到入口')
    def test_homepage95(self):
        logging.info("====我的任务-男-签到入口'===")
        try:
            self.l.tap(1061, 111)
            self.driver.find_element(*MyPage.MyTasks_tab_tasks).click()
            if user_gender == 1:
                logging.info("===男生===")
                if self.l.my_Tasks_ManSignInSuccess():
                    logging.info("===已签到===")
                    MyTasks_tasks_signinEntry_case=self.driver.find_element(*MyPage.MyTasks_tasks_signinEntry)
                    MyTasks_tasks_signinEntry_case.click()
                    sign_btn_man = self.driver.find_element(*MyPage.sign_in_popover_SigninSubmitTextID)
                    assert sign_btn_man.text == '好的', "已签到，按钮不是好的"
                    sign_btn_man.click()
                    assert MyTasks_tasks_signinEntry_case
                    # tasks_points_next = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                    # # assert tasks_points_next.get_attribute('selected') == 'true'


                else:
                    logging.info("===未签到===")
                    MyTasks_tasks_signinEntry_case = self.driver.find_element(*MyPage.MyTasks_tasks_signinEntry)
                    MyTasks_tasks_signinEntry_case.click()
                    sign_btn_man = self.driver.find_element(*MyPage.sign_in_popover_SigninSubmitTextID)
                    assert sign_btn_man.text == '签到', "未签到，按钮不是签到"
                    sign_btn_man.click()
                    time.sleep(3)
                    assert self.l.my_Tasks_ManSignInSuccess()==True
                    # 签到完成会显示签到领取弹窗
                    # if self.l.MyTasks_task_completedPopoverOkBtnEle()!=False:
                    #     self.l.MyTasks_task_completedPopoverOkBtnEle().click()
                    # assert sign_btn_man.text == '好的', "已签到完成，签到按钮没变为好的"
                    # sign_btn_man.click()
                    # tasks_points_next = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                    # assert self.l.my_Tasks_ManSignInSuccess(), '已签到完成，签到实际没有完成'
            elif user_gender == 2:
                logging.error("===女生===")
                if self.l.MyTasks_womanTasks_LoginTomorrowAllEle()==False:
                    logging.info("===未签到===")
                    MyTasks_tasks_signinEntryW_case = self.driver.find_element(*MyPage.MyTasks_womanTasks_LoginAll)
                    MyTasks_tasks_signinEntryW_case.click()
                    # assert self.l.find_element(*MyPage.MyTasks_womanTasks_LoginAll)
                    # self.l.find_element(*MyPage.MyTasks_womanTasks_LoginAll).click()
                    # assert self.l.find_element(*MyPage.MyTasks_womanTasks_LoginAll)
                    sign_btn_woman = self.driver.find_element(*MyPage.sign_in_popover_SigninSubmitTextID)
                    assert sign_btn_woman.text == '签到'
                    sign_btn_woman.click()
                    time.sleep(3)
                    assert MyTasks_tasks_signinEntryW_case
                    # 签到完成会显示签到领取弹窗
                    # assert sign_btn_woman.text == '兑换奖励', "已签到完成，签到按钮没变为兑换奖励"
                    # sign_btn_woman.click()
                    # MyTasks_tab_rewards_next = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    # assert MyTasks_tab_rewards_next.get_attribute('selected') == 'true', '用户签到兑换奖励跳转后不在奖励页面'

                else:
                    logging.info("===已签到===")
                    self.driver.find_element(*MyPage.MyTasks_womanTasks_alreadyLoginAll).click()
                    sign_btn_man = self.driver.find_element(*MyPage.sign_in_popover_SigninSubmitTextID)
                    assert sign_btn_man.text == '兑换奖励', "已签到，按钮不是兑换奖励"
                    sign_btn_man.click()
                    MyTasks_tab_rewards_next = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert MyTasks_tab_rewards_next.get_attribute('selected') == 'true', '用户签到兑换奖励跳转后不在奖励页面'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例96：我的任务-男-邀请入口')
    def test_homepage96(self):
        logging.info("====我的任务-男-邀请入口'===")
        try:
            self.l.tap(1061, 111)
            MyTasks_tab_tasks_case1=self.driver.find_element(*MyPage.MyTasks_tab_tasks)
            MyTasks_tab_tasks_case1.click()
            if user_gender == 1:
                logging.info("===男生===")
                # assert self.driver.find_element(*MyPage.MyTasks_tasks_inviteEntryText).text == '邀请', "有邀请按钮，文字不是邀请"
                # self.driver.find_element(*MyPage.MyTasks_tasks_inviteEntry).click()
                self.driver.find_element(*MyPage.MyTasks_tasks_inviteEntryTextXpath).click()
                time.sleep(2)
                assert self.driver.find_element(*MyPage.MyTasks_tasks_invitePopoverAll), "有邀请按钮，邀请弹窗未出现"
                self.l.tap(1061, 111)
                # tasks_points_next = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                assert MyTasks_tab_tasks_case1.get_attribute('selected') == 'true', '邀请弹窗出现后点击空白未消失'
                logging.error("===断言成功===")

            else:
                logging.error("===不是男生===")
                # assert not self.l.MyTasks_tasks_inviteEntryTextEle(),'不是男生，但是有邀请入口'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-邀请入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-邀请入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例97：我的任务-男-Top Offers入口')
    def test_homepage97(self):
        logging.info("====我的任务-男-Top Offers入口'===")
        try:
            self.l.tap(1061, 111)
            MyTasks_tab_tasks_case1 = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
            MyTasks_tab_tasks_case1.click()
            if user_gender == 1:
                logging.info("===男生===")
                self.driver.find_element(*MyPage.MyTasks_tasks_TopOffersEntryTextXPATH).click()
                # assert self.driver.find_element(*MyPage.MyTasks_tasks_TopOffersEntryText).text == 'Top Offers', "有Top Offers入口，文字不是Top Offers"
                # self.driver.find_element(*MyPage.MyTasks_tasks_TopOffersEntry).click()
                assert self.driver.find_element(*MyPage.MyTasks_tasks_TopOffersTitle).text=='Top Offers', "邀请入口跳转页面不是Top Offers页面"
                self.driver.find_element(*MyPage.MyTasks_tasks_TopOffersGoback).click()
                # tasks_points_next = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                assert MyTasks_tab_tasks_case1.get_attribute('selected') == 'true', '邀请页面点击返回没有返回我的任务-任务页面'


            else:
                logging.error("===不是男生===")
                # assert not self.l.MyTasks_tasks_TopOffersEntryTextEle(), '不是男生，但是有Top Offers入口'


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-Top Offers入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-Top Offers入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例98-99：我的任务-男女-每日&月任务')
    def test_homepage98(self):
        logging.info("====我的任务-男女-每日&月任务'===")
        try:
            if user_gender == 1:
                logging.info("===男生===")
                self.l.tap(1061, 111)
                self.driver.find_element(*MyPage.MyTasks_tab_tasks).click()
                logging.info("====检查每日任务===")
                assert self.l.my_Tasks_ManDailyTasksAll(), "没有每日任务入口"
                self.l.swipe(40, 1473, 40, 387, 100)
                logging.info("====检查每月任务===")
                assert self.l.my_Tasks_ManMonthlyTasksAll(), "没有每月任务入口"

            elif user_gender == 2:
                logging.info("===女生===")
                self.driver.find_element(*MyPage.MyTasks_tab_tasks).click()
                self.l.tap(1061, 111)
                logging.info("====检查每日任务===")
                assert self.driver.find_element(*MyPage.MyTasks_womanTasks_dailyTasks), "没有每日任务入口"

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-每日&月任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-每日&月任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例100：我的任务-男-开通月卡')
    def test_homepage100(self):
        logging.info("====我的任务-男-开通月卡'===")
        try:
            self.l.tap(1061, 111)
            self.l.swipe(40, 387, 40, 1473,100)
            self.driver.find_element(*MyPage.MyTasks_tab_rewards).click()
            if user_gender == 1:
                logging.info("===男生===")
                self.l.swipe(40, 387, 40, 1473, 100)
                if self.l.myTasks_rewards_TopUpMonthCard():
                    logging.info("===男用户有充值月卡入口===")
                    self.driver.find_element(*MyPage.MyTasks_rewards_TopUpMonthCard).click()
                    assert self.driver.find_element(*MyPage.MyTasks_rewards_TopUpMonthCardPopoverCardText).text == '月卡', "有月卡弹窗，但是文字不是月卡字样"
                    self.l.tap(1061, 111)
                    MyTasks_tab_rewards = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert MyTasks_tab_rewards.get_attribute('selected') == 'true', '点击月卡空白处，未停留在奖励页面'
                    self.l.system_goback_key()
                else:
                    logging.info("===男用户没有充值月卡入口,已经开通完成===")
                    self.driver.find_element(*MyPage.MyTasks_rewards_TopUpMonthCard0Points).click()
                    assert self.l.MyTasks_rewards_CongratsPopoverAwesomeBtnEle() or self.l.MyTasks_rewards_RewardDetailsPopoverOkBtnEle()
                    self.l.tap(1061, 111)
                    self.l.system_goback_key()

            else:
                logging.error("===不是男生===")
                assert self.l.myTasks_rewards_TopUpMonthCard()==False, '不是男生，但是有月卡入口'
                self.l.system_goback_key()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-开通月卡')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-开通月卡')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例101-102：我的任务-男女-已完成-未领取奖励、已领取奖励')
    def test_homepage101(self):
        logging.info("====我的任务-男女-未领取奖励、已领取奖励'===")
        self.l.tap(930,2123)
        self.l.tab_Mine_Btn()
        try:
            self.l.tap(930, 2123)
            self.driver.find_element(*MyPage.MyTasks_entry_RightClick).click()
            self.l.tap(1061, 111)
            self.driver.find_element(*MyPage.MyTasks_tab_rewards).click()
            if user_gender == 1:
                logging.info("===男生===")
                if self.l.MyTasks_rewards_LeftClickGuideIDEle() or self.l.MyTasks_rewards_RightClickGuideIDEle():
                    logging.info("===有已完成未领取奖励===")
                    if self.l.MyTasks_rewards_LeftClickGuideIDEle():
                        ClickGuideID=self.driver.find_element(*MyPage.MyTasks_rewards_LeftClickGuideID).location
                        self.driver.find_element(*MyPage.MyTasks_rewards_LeftClickGuideID).click()
                    else:
                        ClickGuideID = self.driver.find_element(*MyPage.MyTasks_rewards_RightClickGuideID).location
                        self.driver.find_element(*MyPage.MyTasks_rewards_RightClickGuideID).click()
                    logging.info("===领取奖励中===")
                    assert self.driver.find_element(*MyPage.MyTasks_rewards_CongratsPopoverAwesomeBtn).text == '真棒！', "有领取弹窗，但是文字不是真棒字样"
                    self.driver.find_element(*MyPage.MyTasks_rewards_CongratsPopoverAwesomeBtn).click()
                    self.l.tap(ClickGuideID['x'], ClickGuideID['y'])
                    logging.info("===已领取奖励的弹窗===")
                    assert self.driver.find_element(*MyPage.MyTasks_rewards_RewardDetailsPopoverOkBtn).text == '完成任务获得更多奖励', "有详细弹窗，但是文字完成获得更多奖励不正确"
                    self.driver.find_element(*MyPage.MyTasks_rewards_RewardDetailsPopoverOkBtn).click()
                    logging.info("===已领取奖励的弹窗跳转===")
                    MyTasks_tab_tasks = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                    assert MyTasks_tab_tasks.get_attribute('selected') == 'true'


                elif self.l.MyTasks_rewards_first100Claimed_StatusEle()!=False:
                    logging.info("===奖励已全部领取完成,没有未领取奖励=====")

                else:
                    logging.info("===没有可以领取的奖励,没有未领取奖励===")

            else:
                logging.error("===不是男生===")
                if self.l.MyTasks_womanRewards_RewardsStatusClaimEle()!=False and len(self.l.MyTasks_womanRewards_RewardsStatusClaimEle())!=0:
                    logging.info("===有已完成未领取奖励===")
                    ClickGuideID = self.driver.find_element(*MyPage.MyTasks_rewards_LeftClickGuideID).location
                    self.driver.find_element(*MyPage.MyTasks_rewards_LeftClickGuideID).click()
                    logging.info("===领取奖励中===")
                    assert self.driver.find_element(*MyPage.MyTasks_rewards_CongratsPopoverAwesomeBtn).text == '真棒！', "有领取弹窗，但是文字不是真棒字样"
                    self.driver.find_element(*MyPage.MyTasks_rewards_CongratsPopoverAwesomeBtn).click()
                    self.l.tap(ClickGuideID['x'], ClickGuideID['y'])
                    logging.info("===已领取奖励的弹窗，点击无反应===")
                    MyTasks_tab_rewards = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert MyTasks_tab_rewards.get_attribute('selected') == 'true'


                elif self.l.MyTasks_womanRewards_RewardsStatusClaimedEle() != False and len(self.l.MyTasks_womanRewards_RewardsStatusClaimedEle()) != 0:
                    logging.info("===有已完成已领取奖励===")
                    self.driver.find_element(*MyPage.MyTasks_womanRewards_RewardsStatusClaimed).click()
                    MyTasks_tab_rewards = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert MyTasks_tab_rewards.get_attribute('selected') == 'true'


                elif self.l.MyTasks_womanRewards_RewardsStatusLockedEle():
                    logging.info("===有待解锁奖励===")
                    self.driver.find_element(*MyPage.MyTasks_womanRewards_RewardsStatusLocked).click()
                    MyTasks_tab_rewards = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert MyTasks_tab_rewards.get_attribute('selected') == 'true'




        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男女-领取奖励、已领取奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男女-已完成未领取奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例102：我的任务-男-已完成已领取奖励')
    def test_homepage102(self):
        logging.info("====我的任务-男-已完成已领取奖励'===")
        try:
            self.l.tap(1061, 111)
            self.driver.find_element(*MyPage.MyTasks_tab_rewards).click()
            if user_gender == 1:
                logging.info("===男生===")
                self.l.swipe(40, 387, 40, 1473, 100)
                if self.l.MyTasks_rewards_RewardClaimedIconEle()!=False:
                    logging.info("===有已完成已领取奖励===")
                    RewardClaimedIconEle_list=self.l.MyTasks_rewards_RewardClaimedIconEle()
                    RewardClaimedIconEle_list[0].click()
                    logging.info("===奖励已全部领取完成弹窗===")
                    assert self.driver.find_element(*MyPage.MyTasks_rewards_RewardDetailsPopoverOkBtn).text == '完成任务获得更多奖励', "有详细弹窗，但是文字完成获得更多奖励"
                    self.driver.find_element(*MyPage.MyTasks_rewards_RewardDetailsPopoverOkBtn).click()
                    MyTasks_tab_tasks = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                    assert MyTasks_tab_tasks.get_attribute('selected') == 'true', '点击完成任务获得更多奖励，未跳转至任务页面'

                else:
                    logging.info("===奖励没有已完成已领取奖励===")

            else:
                logging.error("===不是男生===")
                if self.l.MyTasks_womanRewards_RewardsStatusClaimedEle() != False and len(self.l.MyTasks_womanRewards_RewardsStatusClaimedEle()) != 0:
                    logging.info("===有已完成已领取奖励===")
                    self.driver.find_element(*MyPage.MyTasks_womanRewards_RewardsStatusClaimed).click()
                    MyTasks_tab_rewards = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert MyTasks_tab_rewards.get_attribute('selected') == 'true'


                else:
                    logging.info("===没有已完成已领取奖励===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-已完成已领取奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-已完成已领取奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例103：我的任务-男-未完成奖励')
    def test_homepage103(self):
        logging.info("====我的任务-男-未完成奖励'===")
        try:
            self.l.tap(1061, 111)
            self.driver.find_element(*MyPage.MyTasks_tab_tasks).click()
            self.driver.find_element(*MyPage.MyTasks_tab_rewards).click()
            if user_gender == 1:
                logging.info("===男生===")
                if int(self.driver.find_element(*MyPage.MyTasks_tab_pointsNumber).text)<6500:
                    logging.info("===有未完成奖励'===")
                    self.l.swipe(40, 1473, 40, 387, 100)
                    time.sleep(2)
                    self.l.swipe(40, 1473, 40, 387, 100)
                    self.driver.find_element(*MyPage.MyTasks_rewards_manLast6500NoClaim).click()
                    assert self.driver.find_element(*MyPage.MyTasks_rewards_RewardDetailsPopoverOkBtn).text == '完成任务获得更多奖励', "有详细弹窗，但是文字完成获得更多奖励"
                    self.driver.find_element(*MyPage.MyTasks_rewards_RewardDetailsPopoverOkBtn).click()
                    MyTasks_tab_tasks = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                    assert MyTasks_tab_tasks.get_attribute('selected') == 'true', '点击完成任务获得更多奖励，未跳转至任务页面'

                else:
                    logging.info("===有未完成奖励'===")
                    pytest.skip("===奖励没有已完成已领取奖励===")
            else:
                logging.error("===不是男生===")
                if int(self.driver.find_element(*MyPage.MyTasks_tab_pointsNumber).text)<7000:
                    logging.info("===有待解锁奖励'===")
                    self.l.swipe(40, 1473, 40, 387, 100)
                    self.l.swipe(40, 1473, 40, 387, 100)
                    self.l.swipe(40, 1473, 40, 387, 100)
                    self.driver.find_elements(*MyPage.MyTasks_womanRewards_RewardsStatusLocked)[-1].click()
                    MyTasks_tab_rewards = self.driver.find_element(*MyPage.MyTasks_tab_rewards)
                    assert MyTasks_tab_rewards.get_attribute('selected') == 'true'

                else:
                    logging.info("===没有待解锁奖励===")
                    pytest.skip("===没有待解锁奖励===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-未完成奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-未完成奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例104：我的任务-男女-现在做任务按钮')
    def test_homepage104(self):
        logging.info("====我的任务-男女-现在做任务按钮'===")
        try:
            self.l.tap(1061, 111)
            self.driver.find_element(*MyPage.MyTasks_tab_rewards).click()
            self.l.swipe(40, 1473, 40, 387, 100)
            self.l.swipe(40, 1473, 40, 387, 100)
            self.l.swipe(40, 1473, 40, 387, 100)
            if user_gender == 1:
                logging.info("===男生===")
                # assert self.driver.find_element(*MyPage.MyTasks_rewards_DoTasksNowBtn),'男用户没有现在做任务按钮'
                MyTasks_rewards_DoTasksNowBtn_case1=self.driver.find_element(*MyPage.MyTasks_rewards_DoTasksNowBtn)
                assert MyTasks_rewards_DoTasksNowBtn_case1.text == '现在做任务！'
                MyTasks_rewards_DoTasksNowBtn_case1.click()
                MyTasks_tab_tasks = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                assert MyTasks_tab_tasks.get_attribute('selected') == 'true', '做任务跳转页面不是任务页'
                self.l.system_goback_key()

            elif user_gender == 2:
                logging.error("===不是男生===")
                self.l.swipe(40, 1473, 40, 387, 100)
                self.l.swipe(40, 1473, 40, 387, 100)
                self.l.swipe(40, 1473, 40, 387, 100)
                self.l.swipe(40, 1473, 40, 387, 100)
                MyTasks_rewards_DoTasksNowBtn_case1 = self.driver.find_element(*MyPage.MyTasks_rewards_DoTasksNowBtn)
                assert MyTasks_rewards_DoTasksNowBtn_case1.text == '现在做任务！'
                MyTasks_rewards_DoTasksNowBtn_case1.click()
                MyTasks_tab_tasks = self.driver.find_element(*MyPage.MyTasks_tab_tasks)
                assert MyTasks_tab_tasks.get_attribute('selected') == 'true', '做任务跳转页面不是任务页'
                self.l.system_goback_key()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的任务-男-现在做任务按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的任务-男-现在做任务按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




    # 背包改版-等完成后再修改
    @allure.story('我的背包')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例105-109：我的背包-显示和数量')
    def test_homepage105(self):
        logging.info("===我的背包-显示和数量===")
        try:
            backpackNum = self.driver.find_element(*MyPage.myBackpack_entryText).text
            self.driver.find_element(*MyPage.myBackpack_entryAll).click()
            backpack_allNum = self.l.myBackpack_all_ClItemNum()
            if backpackNum== '0':
                logging.info("===背包道具为空===")
                assert self.driver.find_element(*MyPage.myBackpack_all_emptyIcon)
                assert self.driver.find_element(*MyPage.myBackpack_all_emptyText).text == '无道具'
                assert not self.l.myBackpack_now_frameIDEle()
                assert not self.l.myBackpack_now_frameSvgIDEle()

            else:
                logging.info("===背包道具不为空===")
                assert backpack_allNum!=False
                assert backpack_allNum==backpackNum
                assert self.l.myBackpack_now_frameIDEle() or self.l.myBackpack_now_frameSvgIDEle()


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的背包-显示和数量')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的背包-显示和数量')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的背包')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例110：我的背包-切换道具')
    def test_homepage110(self):
        logging.info("===我的背包-切换道具===")
        try:
            backpackNum = self.driver.find_element(*MyPage.myBackpack_entryText).text
            self.driver.find_element(*MyPage.myBackpack_entryAll).click()
            if backpackNum == '0':
                logging.info("===背包道具为空===")
                assert self.driver.find_element(*MyPage.myBackpack_all_emptyIcon)
                assert self.driver.find_element(*MyPage.myBackpack_all_emptyText).text == '无道具'

            else:
                logging.info("===背包道具不为空===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的背包-切换道具')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的背包-切换道具')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的背包')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例111-112：我的背包-已过期')
    def test_homepage111(self):
        logging.info("===我的背包-已过期===")
        try:
            self.driver.find_element(*MyPage.myBackpack_entryAll).click()
            self.driver.find_element(*MyPage.myBackpack_expiredEntry).click()
            assert self.driver.find_element(*MyPage.myBackpack_expiredTitle).text=='已过期'
            if self.l.myBackpack_expired_noTextEle()==False:
                logging.info("===我的背包-已过期-有道具===")
                assert self.driver.find_element(*MyPage.myBackpack_expiredList_First)
                assert self.driver.find_element(*MyPage.myBackpack_expiredList_FirstIcon)
                assert self.driver.find_element(*MyPage.myBackpack_expiredList_FirstName).text == '头像框' or '进场特效'
                assert self.driver.find_element(*MyPage.myBackpack_expiredList_FirstTime)

            else:
                logging.error("===我的背包-已过期-没有道具===")
                assert self.driver.find_element(*MyPage.myBackpack_expired_noText).text == '无道具'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的背包-已过期')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的背包-已过期')
            logging.info(f'截图成功，图片为{screen_name}')
            raise





    @allure.story('我的邀请')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例113、114、115：我的邀请-入口显示及按钮弹窗')
    def test_homepage113(self):

        try:
            logging.info("===我的邀请-入口显示===")
            if user_gender == 1:
                logging.info("===男用户，有我的邀请入口===")
                assert self.driver.find_element(*MyPage.MyInvite_entry_FreeCardsText).text == '免费卡片'
                self.l.MyInvite_entry_AllEle()
                # time.sleep(5)
                # assert self.driver.find_element(*MyPage.MyInvite_instructionsBtn)
                logging.info("===问号按钮===")
                self.driver.find_element(*MyPage.MyInvite_instructionsBtn).click()
                assert self.driver.find_element(*MyPage.MyInvite_instructionsPopover_rule1).text == '聊天卡免费用于视频聊天1分钟，每张卡有效期为5天'
                assert self.driver.find_element(*MyPage.MyInvite_instructionsPopover_rule2).text == '只有新的Chamet用户才能获得奖励'
                # assert self.driver.find_element(*MyPage.MyInvite_instructionsPopover)
                self.l.tap(609,197)
                logging.info("===邀请好友按钮===")
                self.driver.find_element(*MyPage.MyInvite_inviteFriendsBtnID).click()
                self.l.h5_to_native()
                assert self.driver.find_element(*MyPage.MyInvite_inviteFriendsPopover)
                self.l.tap(609, 197)
                self.l.native_to_h5()
                # self.l.MyInvite_gobackEle()

            elif user_gender == 2:
                logging.info("===女用户，没有我的邀请入口===")
                assert self.driver.find_element(*MyPage.MyInvite_entry_nameText).text != '我的邀请'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的邀请-入口显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的邀请-入口显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的邀请')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例116：我的邀请-邀请列表')
    def test_homepage116(self):
        logging.info("===我的邀请-邀请列表===")
        try:
            # self.l.tap(963,2120)
            if user_gender == 1:
                logging.info("===男用户，有我的邀请入口===")
                self.driver.find_element(*MyPage.MyInvite_myInvitees).click()
                inviteesListFirstNameText1 = self.driver.find_elements(*MyPage.MyInvite_my_inviteesListFirstName)[0].text
                # inviteesListFirstName =
                time.sleep(2)
                self.driver.find_elements(*MyPage.MyInvite_my_inviteesListFirstName)[0].click()
                self.l.h5_to_native()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text ==inviteesListFirstNameText1
                self.l.system_goback_key()
                self.l.native_to_h5()


                # no_user_ele=self.l.MyInvite_my_inviteesListNoUserEle()
                # if self.l.MyInvite_my_TotalRewardsBtnEle()!=False:
                #     # assert no_user_ele==False or len(no_user_ele)==0:
                #     global no_record
                #     no_record=0
                #     logging.info("===我的邀请-有用户===")
                #     inviteesListFirstName=self.driver.find_elements(*MyPage.MyInvite_my_inviteesListFirstName)[0].text
                #     self.driver.find_elements(*MyPage.MyInvite_my_inviteesList)[0].click()
                #     self.l.h5_to_native()
                #     assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text ==inviteesListFirstName
                #     self.l.system_goback_key()
                #     # self.l.MyInvite_gobackEle()
                # else:
                #     logging.info("===我的邀请-无用户===")
                #     no_record = 1
                #     assert self.driver.find_element(*MyPage.MyInvite_my_inviteesListNoUser).text != '没有记录'

            else:
                logging.info("===女用户，没有我的邀请入口===")
                assert self.driver.find_element(*MyPage.MyInvite_entry_nameText).text != '我的邀请'


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的邀请-邀请列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的邀请-邀请列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    # 周排行有数据的显示补充
    @allure.story('我的邀请')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例117：我的邀请-周排行')
    def test_homepage117(self):
        logging.info("===我的邀请-周排行===")
        try:
            # self.l.tap(963, 2120)
            if user_gender == 1:
                logging.info("===男用户，有我的邀请入口===")
                self.driver.find_element(*MyPage.MyInvite_weeklyRank).click()
                inviteesListFirstName = self.driver.find_elements(*MyPage.MyInvite_my_inviteesListFirstName)[0].text
                time.sleep(2)
                self.driver.find_elements(*MyPage.MyInvite_my_inviteesListFirstName)[0].click()
                self.l.h5_to_native()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == inviteesListFirstName
                self.l.system_goback_key()
                self.l.native_to_h5()
                self.l.MyInvite_gobackEle()

                # if no_record==0:
                #     logging.info("===我的邀请没有空图标===")
                #     if self.l.MyInvite_weekly_noUserEle() == False:
                #         logging.info("===周排行-有用户===")
                #         inviteesListFirstName = self.driver.find_elements(*MyPage.MyInvite_my_inviteesListFirstName)[0].text
                #         self.driver.find_elements(*MyPage.MyInvite_my_inviteesList)[0].click()
                #         self.l.h5_to_native()
                #         assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == inviteesListFirstName
                #         self.l.system_goback_key()
                #         self.l.MyInvite_gobackEle()
                #     else:
                #         logging.info("===周排行-没有记录===")
                #         assert self.driver.find_element(*MyPage.MyInvite_weekly_noUser).text != '没有记录'
                # else:
                #     logging.info("===我的邀请有空图标===")
                #     inviteesListFirstName = self.driver.find_elements(*MyPage.MyInvite_my_inviteesListFirstName)[0].text
                #     self.driver.find_elements(*MyPage.MyInvite_my_inviteesList)[0].click()
                #     self.l.h5_to_native()
                #     assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == inviteesListFirstName
                #     self.l.system_goback_key()
                #     self.l.MyInvite_gobackEle()

            else:
                logging.info("===女用户，没有我的邀请入口===")
                assert self.driver.find_element(*MyPage.MyInvite_entry_nameText).text != '我的邀请'


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的邀请-周排行')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的邀请-周排行')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例118：我的简介-入口')
    def test_homepage118(self):
        logging.info("===我的简介-入口===")
        try:
            if self.l.my_Profile_entry()==True:
                assert self.driver.find_element(*MyPage.myProfile_Title).text=='我的简介','没有进入我的等级页面'
                logging.info("===我的简介-进入成功===")
            else:
                logging.error('===没有找到我的简介入口元素===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例119：我的简介-头像')
    def test_homepage119(self):
        logging.info("===我的简介-头像===")
        try:
            self.driver.find_element(*MyPage.myProfile_MyAvatar_img).click()

            if user_gender==1:
                assert self.driver.find_element(*MyPage.myProfile_MyAvatar_title).text == '我的头像'
                assert self.driver.find_element(*MyPage.myProfile_MyAvatar_posterTipContents).text == '请上传你自己的清晰和漂亮的照片'
            else:
                assert self.driver.find_element(*MyPage.myProfile_MyAvatar_title).text == '我的封面'
                assert self.driver.find_element(*MyPage.myProfile_MyAvatar_posterScoreTitle).text == '封面评分'
            logging.info("===我的简介-头像断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-头像')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-头像')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例120：我的简介-头像-编辑')
    def test_homepage120(self):
        logging.info("===我的简介-头像-编辑===")
        try:
            MyAvatar_posterOld=self.driver.find_element(*MyPage.myProfile_MyAvatar_poster)
            self.driver.find_element(*MyPage.myProfile_MyAvatar_ChangePosterBtn).click()
            # assert self.driver.find_element(*MyPage.myProfile_MyAvatar_ChangePosterPopoverAll)
            self.driver.find_element(*MyPage.myProfile_MyAvatar_ChangePosterPopPictureBtn).click()
            self.l.get_permission_checkPopover()
            # assert self.driver.find_elements(*MyPage.messages_Group_pictureChooseList)
            self.driver.find_elements(*MyPage.messages_Group_pictureChooseList)[0].click()
            self.driver.find_element(*MyPage.myProfile_MyAvatar_ChangePosterUpdateConfirm).click()
            assert self.driver.find_element(*MyPage.myProfile_MyAvatar_PosterStateText).text=='审核中'
            print(self.driver.find_element(*MyPage.myProfile_MyAvatar_PosterStateText).text)
            MyAvatar_posterNew = self.driver.find_element(*MyPage.myProfile_MyAvatar_poster)
            assert MyAvatar_posterOld!=MyAvatar_posterNew
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-头像-编辑')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-头像-编辑')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例121：我的简介-头像-历史图集女用户')
    def test_homepage121(self):
        logging.info("===我的简介-头像-历史图集女用户===")
        try:
            if user_gender==2:
                logging.info("===女用户===")
                # assert self.driver.find_element(*MyPage.myProfile_MyAvatar_PosterHistoryBtn)
                self.driver.find_element(*MyPage.myProfile_MyAvatar_PosterHistoryBtn).click()
                assert self.driver.find_element(*MyPage.myProfile_MyAvatar_PosterHistoryTitle).text=='图集','图集名称不正确'
                self.driver.find_element(*MyPage.myProfile_MyAvatar_PosterHistoryGoback).click()
                assert self.driver.find_element(*MyPage.myProfile_MyAvatar_title).text == '我的封面'
                self.driver.find_element(*MyPage.myProfile_MyAvatar_goback).click()
                # self.l.system_goback_key()
            elif user_gender==1:
                logging.info("===男用户===")
                self.l.tap(1016,148)
                assert self.driver.find_element(*MyPage.myProfile_MyAvatar_title).text == '我的头像'
                self.driver.find_element(*MyPage.myProfile_MyAvatar_goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-头像-历史图集女用户')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-头像-历史图集女用户')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例122：我的简介-ID')
    def test_homepage122(self):
        logging.info("===我的简介-ID===")
        try:
            assert self.driver.find_element(*MyPage.myProfile_ID_Number)
            self.driver.find_element(*MyPage.myProfile_ID_CopyBtn).click()
            # print(self.l.toast_message('已拷贝'))
            assert self.driver.find_element(*MyPage.myProfile_ID_Number)
            logging.info("===断言成功===")

            # 获取已拷贝字样toast

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-ID')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-ID')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例123：我的简介-昵称')
    def test_homepage123(self):
        logging.info("===我的简介-昵称===")
        try:
            NickName_Text_aa=self.driver.find_element(*MyPage.myProfile_NickName_Text).text
            print(NickName_Text_aa)
            NickName_Text_aa1=NickName_Text_aa.rstrip('...')
            print(NickName_Text_aa1)
            assert pagePersonalName.find(NickName_Text_aa1)>=0
            self.driver.find_element(*MyPage.myProfile_NickName_Text).click()
            # assert self.driver.find_element(*MyPage.myProfile_NickName_title).text == '昵称','昵称的标题不正确'
            assert self.driver.find_element(*MyPage.myProfile_NickName_EditorContent).text==pagePersonalName,'用户昵称与个人主页不一致'

            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-昵称')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-昵称')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例124：我的简介-昵称-修改')
    def test_homepage124(self):
        logging.info("===我的简介-昵称-修改===")
        try:
            newName='20112494vsascbbdsdvfdnj:_bvsjvfd'
            self.driver.find_element(*MyPage.myProfile_NickName_EditorContent).clear()
            self.driver.find_element(*MyPage.myProfile_NickName_EditorContent).send_keys(newName)
            self.driver.find_element(*MyPage.myProfile_NickName_EditorCommit).click()
            assert self.driver.find_element(*MyPage.myProfile_Title).text == '我的简介', '我的简介名称不对'
            self.driver.find_element(*MyPage.myProfile_Goback).click()
            self.l.tab_Mine_Btn()
            self.l.tab_Mine_Head()
            assert newName.find(self.driver.find_element(*MyPage.user_own_pagePersonalName).text)>=0
            self.driver.find_element(*MyPage.user_own_pageGobackBtn).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-昵称-修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-昵称-修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例125：我的简介-性别')
    def test_homepage125(self):
        logging.info("===我的简介-性别===")
        try:
            self.l.tab_Mine_Btn()
            gender = self.l.myProfile_Gender_ManorW()
            if user_gender==1:
                assert gender ==1
            else:
                assert gender ==2
            logging.info("===断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-性别')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-性别')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例126：我的简介-年龄显示')
    def test_homepage126(self):
        logging.info("===我的简介-年龄显示===")
        try:
            self.l.tab_Mine_Btn()
            self.driver.find_element(*MyPage.myProfile_entry_man).click()
            Age=self.driver.find_element(*MyPage.myProfile_Age_Text).text
            assert int(Age) >= int('18'), '用户年龄小于18岁'
            self.driver.find_element(*MyPage.myProfile_Age_All).click()
            # assert self.driver.find_element(*MyPage.myProfile_Age_popoverDateCancelBtn)
            self.driver.find_element(*MyPage.myProfile_Age_popoverDateCancelBtn).click()
            logging.info("===断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-年龄显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-年龄显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例127：我的简介-年龄修改')
    def test_homepage127(self):
        logging.info("===我的简介-年龄修改===")
        try:
            Age = self.driver.find_element(*MyPage.myProfile_Age_Text).text
            self.driver.find_element(*MyPage.myProfile_Age_All).click()
            self.driver.find_element(*MyPage.myProfile_Age_popoverDateYear).click()
            self.driver.find_element(*MyPage.myProfile_Age_popoverDateYearSecond).click()
            time.sleep(2)
            self.l.tap(446,1398)
            self.driver.find_element(*MyPage.myProfile_Age_popoverDateConfirmBtn).click()
            assert self.driver.find_element(*MyPage.myProfile_Age_Text).text!=Age,'修改年龄后无变化'
            logging.info("===断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-年龄修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-年龄修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例128：我的简介-地区')
    def test_homepage128(self):
        logging.info("===我的简介-地区===")
        try:
            assert self.driver.find_element(*MyPage.myProfile_Region_Image), '国家图标未显示'
            assert self.driver.find_element(*MyPage.myProfile_Region_Text).text == '中国', '用户国家不是中国'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-地区')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-地区')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例129：我的简介-定位')
    def test_homepage129(self):
        logging.info("===我的简介-定位===")
        try:
            if self.l.myProfile_Location_TextContents()!=False:
                logging.info("===我的简介-定位有显示===")
                self.driver.find_element(*MyPage.myProfile_Location_All).click()
                assert self.driver.find_element(*MyPage.myProfile_Location_PopoverAll)
                self.driver.find_element(*MyPage.myProfile_Location_PopoverCancelBtn).click()
                logging.info("===断言成功===")
            else:
                logging.error("===我的简介-定位-没有显示任何信息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-定位')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-定位')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例130-131：我的简介-定位切换')
    def test_homepage130(self):
        logging.info("===我的简介-定位切换===")
        try:
            myProfile_Location_TextContents_case=self.l.myProfile_Location_TextContents()
            if myProfile_Location_TextContents_case!=False:
                logging.info("===我的简介-定位有显示===")
                location = myProfile_Location_TextContents_case.text
                print(location)
                if location=='隐藏':
                    self.driver.find_element(*MyPage.myProfile_Location_All).click()
                    if self.driver.find_element(*MyPage.myProfile_Location_Popover1stIcon_Text).text=='隐藏':
                        logging.info("===我的简介-定位隐藏无法获取===")
                        # assert not self.driver.find_element(*MyPage.myProfile_Location_Popover2edIcon)
                        self.driver.find_element(*MyPage.myProfile_Location_Popover1stIcon).click()
                        self.driver.find_element(*MyPage.myProfile_Location_PopoverConfirmBtn).click()
                        time.sleep(2)
                        # print(ord(self.driver.find_element(*MyPage.myProfile_Location_Text).text))
                        # print(ord('隐藏'))
                        assert self.driver.find_element(*MyPage.myProfile_Location_Text).text == '隐藏'
                        logging.info("===断言成功===")
                    else:
                        logging.info("===我的简介-定位有具体定位，为隐藏===")
                        print(self.driver.find_element(*MyPage.myProfile_Location_Popover2edIcon_Text).text)
                        assert self.driver.find_element(*MyPage.myProfile_Location_Popover2edIcon_Text).text == '隐藏'
                        self.driver.find_element(*MyPage.myProfile_Location_Popover1stIcon).click()
                        self.driver.find_element(*MyPage.myProfile_Location_PopoverConfirmBtn).click()
                        time.sleep(3)
                        # print(ord(self.driver.find_element(*MyPage.myProfile_Location_Text).text))
                        # print(ord('隐藏'))
                        assert self.driver.find_element(*MyPage.myProfile_Location_Text).text!='隐藏'
                        logging.info("===断言成功===")
                else:
                    logging.info("===我的简介-定位显示具体定位，准备切换成隐藏===")
                    self.driver.find_element(*MyPage.myProfile_Location_All).click()
                    assert self.driver.find_element(*MyPage.myProfile_Location_Popover2edIcon_Text).text == '隐藏', '隐藏不在第二个位置'
                    self.driver.find_element(*MyPage.myProfile_Location_Popover2edIcon).click()
                    self.driver.find_element(*MyPage.myProfile_Location_PopoverConfirmBtn).click()
                    time.sleep(2)
                    # print(ord(self.driver.find_element(*MyPage.myProfile_Location_Text).text))
                    # print(ord('隐藏'))
                    assert self.driver.find_element(*MyPage.myProfile_Location_Text).text == '隐藏'
                    logging.info("===断言成功===")
            else:
                logging.error("===我的简介-定位-没有显示任何信息===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-定位切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-定位切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例132：我的简介-语言')
    def test_homepage132(self):
        logging.info("===我的简介-语言===")
        try:
            myProfile_Language_Text_case=self.driver.find_element(*MyPage.myProfile_Language_Text)
            myProfile_Language_Text_caseName=myProfile_Language_Text_case.text
            myProfile_Language_Text_case.click()
            assert self.driver.find_element(*MyPage.myProfile_Language_title).text == '语言', '并没有跳转语言页面'
            myProfile_Language_ChooseLanguageText_case = self.driver.find_element(*MyPage.myProfile_Language_ChooseLanguageText).text
            assert myProfile_Language_ChooseLanguageText_case.find(myProfile_Language_Text_caseName)>=0
            self.driver.find_element(*MyPage.myProfile_Language_ChooseLanguage).click()
            # assert self.driver.find_element(*MyPage.myProfile_Language_PopoverContent)
            self.driver.find_element(*MyPage.myProfile_Language_PopoverCancelBtn).click()
            self.driver.find_element(*MyPage.myProfile_Language_goback).click()
            logging.info("===断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例133：我的简介-语言切换')
    def test_homepage133(self):
        logging.info("===我的简介-语言切换===")
        try:
            Language_Text_case=self.driver.find_element(*MyPage.myProfile_Language_Text).text
            self.driver.find_element(*MyPage.myProfile_Language_All).click()
            assert self.driver.find_element(*MyPage.myProfile_Language_title).text == '语言', '并没有跳转语言页面'
            self.driver.find_element(*MyPage.myProfile_Language_LanguageEnglish).click()
            # assert self.driver.find_element(*MyPage.myProfile_Language_PopoverContent)
            self.driver.find_element(*MyPage.myProfile_Language_PopoverConfirmBtn).click()
            assert self.driver.find_element(*MyPage.myProfile_Language_ChooseLanguageText).text == '英语(English)'
            self.driver.find_element(*MyPage.myProfile_Language_goback).click()
            assert self.driver.find_element(*MyPage.myProfile_Language_Text).text =='英语'
            logging.info("===断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-语言切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-语言切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例134-135：我的简介-第二语言显示和切换')
    def test_homepage134(self):
        logging.info("===我的简介-第二语言显示和切换===")
        try:
            SecondLanguage_textContents_case=self.l.myProfile_SecondLanguage_textContents()
            if SecondLanguage_textContents_case!=False:
                logging.info("===我的简介-第二语言有显示===")
                second_lan=SecondLanguage_textContents_case.text
                print(second_lan)
                SecondLanguage_textContents_case.click()
                assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_title).text == '第二语言', '并没有跳转第二语言页面'
                SecondLanguage_ChooseLanguageText_case2=self.driver.find_element(*MyPage.myProfile_SecondLanguage_ChooseLanguageText).text
                assert SecondLanguage_ChooseLanguageText_case2 != 'None(None)' and SecondLanguage_ChooseLanguageText_case2.find(second_lan) >= 0
                self.driver.find_element(*MyPage.myProfile_SecondLanguage_ChooseLanguageAll).click()
                # assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_PopoverContent)
                self.driver.find_element(*MyPage.myProfile_SecondLanguage_PopoverCancelBtn).click()
                time.sleep(2)
                if second_lan=='马来语':
                    logging.info("===是马来语，开始切换印度尼西亚语===")
                    self.driver.find_element(*MyPage.myProfile_SecondLanguage_LanguageIndonesia).click()
                    self.driver.find_element(*MyPage.myProfile_SecondLanguage_PopoverConfirmBtn).click()
                    assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_ChooseLanguageText).text == '印度尼西亚语(Bahasa Indonesia)'
                    self.driver.find_element(*MyPage.myProfile_SecondLanguage_goback).click()
                    assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_Text).text == '印度尼西亚语'
                    logging.info("===断言成功===")
                else:
                    logging.info("===不是马来语，开始切换成马来语===")
                    self.driver.find_element(*MyPage.myProfile_SecondLanguage_LanguageMalayu).click()
                    self.driver.find_element(*MyPage.myProfile_SecondLanguage_PopoverConfirmBtn).click()
                    assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_ChooseLanguageText).text == '马来语(bahasa Melayu)'
                    self.driver.find_element(*MyPage.myProfile_SecondLanguage_goback).click()
                    assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_Text).text == '马来语'
                    logging.info("===断言成功===")
            else:
                logging.info("===我的简介-第二语言没有===")
                self.driver.find_element(*MyPage.myProfile_SecondLanguage_All).click()
                assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_title).text == '第二语言', '并没有跳转第二语言页面'
                assert self.driver.find_element(*MyPage.myProfile_Language_ChooseLanguageText).text == 'None(None)'
                self.driver.find_element(*MyPage.myProfile_SecondLanguage_ChooseLanguageAll).click()
                # assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_PopoverContent)
                self.driver.find_element(*MyPage.myProfile_SecondLanguage_PopoverCancelBtn).click()
                logging.info("===没有语言，开始切换成马来语===")
                self.driver.find_element(*MyPage.myProfile_SecondLanguage_LanguageMalayu).click()
                self.driver.find_element(*MyPage.myProfile_SecondLanguage_PopoverConfirmBtn).click()
                assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_ChooseLanguageText).text == '马来语(bahasa Melayu)'
                self.driver.find_element(*MyPage.myProfile_SecondLanguage_goback).click()
                assert self.driver.find_element(*MyPage.myProfile_SecondLanguage_Text).text == '马来语'
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-第二语言显示和切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-第二语言显示和切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例136：我的简介-自我介绍')
    def test_homepage136(self):
        logging.info("===我的简介-自我介绍===")
        try:
            self.driver.find_element(*MyPage.myProfile_SelfIntroduction_All).click()
            assert self.driver.find_element(*MyPage.myProfile_SelfIntroduction_title).text == '自我介绍'
            if pageSelfIntroduction==False:
                assert self.driver.find_element(*MyPage.myProfile_SelfIntroduction_content).text =='输入你的自我介绍'
            else:
                assert self.driver.find_element(*MyPage.myProfile_SelfIntroduction_content).text == pageSelfIntroduction, '自我介绍的内容与个人主页不符合'
            # self.driver.find_element(*MyPage.myProfile_SelfIntroduction_goback).click()
            logging.info("===断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-自我介绍')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-自我介绍')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例137：我的简介-自我介绍修改')
    def test_homepage137(self):
        logging.info("===我的简介-自我介绍修改===")
        try:
            newIntro='greagergtrhfgbfbgrtnew,,khrf,,..._nbfd'
            # self.driver.find_element(*MyPage.myProfile_SelfIntroduction_All).click()
            # assert self.driver.find_element(*MyPage.myProfile_SelfIntroduction_title).text == '自我介绍', '并未跳转到自我介绍页面'
            SelfIntr = self.driver.find_element(*MyPage.myProfile_SelfIntroduction_content).text
            if pageSelfIntroduction != False:
                self.driver.find_element(*MyPage.myProfile_SelfIntroduction_content).clear()
            self.driver.find_element(*MyPage.myProfile_SelfIntroduction_content).send_keys(newIntro)
            # assert self.driver.find_element(*MyPage.myProfile_SelfIntroduction_content).text!=SelfIntr
            self.driver.find_element(*MyPage.myProfile_SelfIntroduction_CommitBtn).click()
            self.l.system_goback_key()
            self.l.tab_Mine_Btn()
            self.l.tab_Mine_Head()
            assert self.driver.find_element(*MyPage.user_ownPage_selfIntroduction).text==newIntro,'修改内容与个人主页显示不一致'
            self.l.system_goback_key()
            self.l.my_Profile_entry()
            # self.driver.find_element(*MyPage.myProfile_entry_man).click()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-自我介绍修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-自我介绍修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例138：我的简介-google弹窗')
    def test_homepage138(self):
        logging.info("===我的简介-google弹窗===")
        try:
            self.driver.find_element(*MyPage.myProfile_Google_All).click()
            assert self.driver.find_element(*MyPage.myProfile_Google_Popover)
            assert self.driver.find_element(*MyPage.myProfile_Google_PopoverFirstAccountAll)
            assert self.driver.find_element(*MyPage.myProfile_Google_PopoverAccountAddText).text == '再添加一个帐号'
            self.l.system_goback_key()
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-google弹窗')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-google弹窗')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例139：我的简介-手机号显示')
    def test_homepage139(self):
        logging.info("===我的简介-手机号显示===")
        try:
            global login_phone
            login_phone = self.driver.find_element(*MyPage.myProfile_Phone_entryText).text
            assert login_phone.find('***')>=0
            logging.info("===断言成功===")
            # self.driver.find_element(*MyPage.myProfile_Phone_entryAll).click()
            # self.driver.find_element(*MyPage.myProfile_Phone_ChangeCancelAll).click()
            # self.driver.find_element(*MyPage.myProfile_Phone_entryAll).click()
            # assert self.driver.find_element(*MyPage.myProfile_Phone_ChangeNumText).text=='请验证码原手机号'

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-手机号显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-手机号显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    # 手机号更换页面有错误！
    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例140：我的简介-手机号更换')
    def test_homepage140(self):
        logging.info("===我的简介-手机号更换===")
        try:
            self.driver.find_element(*MyPage.myProfile_Phone_entryAll).click()
            self.driver.find_element(*MyPage.myProfile_Phone_ChangeCancelAll).click()
            self.driver.find_element(*MyPage.myProfile_Phone_entryAll).click()
            self.driver.find_element(*MyPage.myProfile_Phone_ChangeNumText).click()
            assert self.driver.find_element(*MyPage.myProfile_Phone_ChangeTitle).text == '请验证原手机号'
            login_phone_num=login_phone.replace('*','')
            login_phone_area=self.driver.find_element(*MyPage.myProfile_Phone_ChangeAreaCode).text
            login_phone_area1=login_phone_area.lstrip('+')
            login_phoneNumber=login_phone_num.replace(login_phone_area1,'')
            assert login_phone_num.find(login_phone_area1)>=0
            assert self.driver.find_element(*MyPage.myProfile_Phone_ChangePhoneNum).text.find(login_phoneNumber)>=0
            self.driver.find_element(*MyPage.myProfile_Phone_ChangeVerCode).send_keys('3795')
            self.driver.find_element(*MyPage.myProfile_Phone_ChangeNextBtn).click()
            assert self.driver.find_element(*MyPage.myProfile_Phone_ChangeTitle).text == '更换手机号'
            assert self.driver.find_element(*MyPage.myProfile_Phone_ChangeAreaCode).text=='+99999'
            self.driver.find_element(*MyPage.myProfile_Phone_ChangeGoback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-手机号更换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-手机号更换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例141：我的简介-密码显示')
    def test_homepage141(self):
        logging.info("===我的简介-密码显示===")
        try:
            if self.l.myProfile_Password_entryTextEle():
                logging.info("===已经设置过密码，重置步骤===")
                assert self.driver.find_element(*MyPage.myProfile_Password_entryText).text == '重置'
                self.driver.find_element(*MyPage.myProfile_Password_entryAll).click()
                self.driver.find_element(*MyPage.myProfile_Password_popoverResetCancel).click()
                self.driver.find_element(*MyPage.myProfile_Password_entryAll).click()
                assert self.driver.find_element(*MyPage.myProfile_Password_popoverResetText).text == '重置密码'
                self.driver.find_element(*MyPage.myProfile_Password_popoverResetAll).click()
                assert self.driver.find_element(*MyPage.myProfile_Password_ResetTitle).text == '设置登录密码'
                logging.info("===断言成功===")

            elif self.driver.find_element(*MyPage.myProfile_Password_entryRedDot):
                logging.info("===没有密码，设置过程===")
                self.driver.find_element(*MyPage.myProfile_Password_entryAll).click()
                assert self.driver.find_element(*MyPage.myProfile_Password_ChangeTitle).text == '修改登录密码'
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-密码显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-密码显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    # 密码输入的格式（少于6位、不一致、一致）
    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例142：我的简介-密码更换')
    def test_homepage142(self):
        logging.info("===我的简介-密码更换===")
        try:
            if self.driver.find_element(*MyPage.myProfile_Password_ChangeTitle).text=='设置登录密码':
                logging.info("==有密码，重置界面==")
                # self.driver.find_element(*MyPage.myProfile_Password_ResetSendBtn).click()
                # pass_code=self.l.request_get_correct_code(86,4086111)
                # self.driver.find_element(*MyPage.myProfile_Password_ResetEditCode).send_keys(pass_code)
                # self.driver.find_element(*MyPage.myProfile_Password_ResetNextBtn).click()
                # assert self.driver.find_element(*MyPage.myProfile_Password_ChangeTitle).text=='修改登录密码','并未跳至修改密码页面'
                # firstPass = '222222'
                # firstSamePass = '222222'
                # firstDiffPass = '333333'
                # logging.info("==密码设置不一致==")
                # self.driver.find_element(*MyPage.myProfile_Password_ChangeEnterPw).send_keys(firstPass)
                # self.driver.find_element(*MyPage.myProfile_Password_ChangeReEnterPw).send_keys(firstDiffPass)
                # self.driver.find_element(*MyPage.myProfile_Password_ChangeConfirmBtn).click()
                # # 获取toast两次密码输入不一致
                # assert self.driver.find_element(*MyPage.myProfile_Password_ChangeTitle).text == '修改登录密码'
                # logging.info("==密码设置一致==")
                # self.driver.find_element(*MyPage.myProfile_Password_ChangeEnterPw).clear()
                # self.driver.find_element(*MyPage.myProfile_Password_ChangeReEnterPw).clear()
                # self.driver.find_element(*MyPage.myProfile_Password_ChangeEnterPw).send_keys(firstPass)
                # self.driver.find_element(*MyPage.myProfile_Password_ChangeReEnterPw).send_keys(firstSamePass)
                # self.driver.find_element(*MyPage.myProfile_Password_ChangeConfirmBtn).click()
                # assert self.driver.find_element(*MyPage.myProfile_Password_ChangeTitle).text == '我的简介'
                # assert self.driver.find_element(*MyPage.myProfile_Password_entryText).text == '重置', '密码已经重置好，重置文字显示不对'
                self.l.system_goback_key()
                self.l.system_goback_key()
                logging.info("===断言成功===")

            elif self.driver.find_element(*MyPage.myProfile_Password_ChangeTitle).text=='修改登录密码':
                logging.info("==无密码，设置界面==")
                assert self.driver.find_element(*MyPage.myProfile_Password_ChangeTipsText).text == '设置登录密码有助于提升账号安全', '无密码的页面提示文字有误，'
                firstPass='222222'
                firstSamePass='222222'
                firstDiffPass='333333'
                logging.info("==密码设置不一致==")
                self.driver.find_element(*MyPage.myProfile_Password_ChangeEnterPw).send_keys(firstPass)
                self.driver.find_element(*MyPage.myProfile_Password_ChangeReEnterPw).send_keys(firstDiffPass)
                self.driver.find_element(*MyPage.myProfile_Password_ChangeConfirmBtn).click()
                # 获取toast两次密码输入不一致
                assert self.driver.find_element(*MyPage.myProfile_Password_ChangeTitle).text=='修改登录密码'
                logging.info("==密码设置一致==")
                self.driver.find_element(*MyPage.myProfile_Password_ChangeEnterPw).clear()
                self.driver.find_element(*MyPage.myProfile_Password_ChangeReEnterPw).clear()
                self.driver.find_element(*MyPage.myProfile_Password_ChangeEnterPw).send_keys(firstPass)
                self.driver.find_element(*MyPage.myProfile_Password_ChangeReEnterPw).send_keys(firstSamePass)
                self.driver.find_element(*MyPage.myProfile_Password_ChangeConfirmBtn).click()
                assert self.driver.find_element(*MyPage.myProfile_Password_ChangeTitle).text == '我的简介'
                assert self.driver.find_element(*MyPage.myProfile_Password_entryText).text == '重置', '密码已经设置，重置文字显示不对'
                self.l.system_goback_key()
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的简介-密码更换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的简介-密码更换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    # 打招呼已发送给所有在线用户。
    @allure.story('我的打招呼')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例155：我的打招呼-进入显示')
    def test_homepage155(self):
        logging.info("===我的打招呼-进入显示===")
        try:
            if user_gender==2:
                self.driver.find_element(*MyPage.MyGreetingWords_entry).click()
                time.sleep(2)
                global GrWords_woman
                if self.l.MyGrWords_faceVerification_popoverAllEle():
                    GrWords_woman=0
                    logging.info("===我的打招呼-未通过真人检测===")
                    assert self.driver.find_element(*MyPage.MyGrWords_faceVerification_popoverText).text == '为保障安全性，你需要先通过真人检测'
                    # assert self.driver.find_element(*MyPage.MyGrWords_faceVerification_popoverConfirmBtn)
                    logging.info("===断言成功===")

                elif self.l.MyGrWords_edit_saveBtnEle():
                    GrWords_woman = 1
                    logging.info("===我的打招呼-已通过真人检测，没有消息记录===")
                    self.l.tap(1007, 1436)
                    self.driver.find_element(*MyPage.MyGrWords_edit_contentText).send_keys('hi,a nice day ,call me')
                    self.driver.find_element(*MyPage.MyGrWords_edit_albumPhoto).click()
                    self.l.tap(1007, 1436)
                    self.l.get_permission_checkPopover()
                    self.l.tap(522,427)
                    self.driver.find_element(*MyPage.MyGrWords_edit_saveBtn).click()
                    self.driver.find_element(*MyPage.MyGreetingWords_entry).click()
                    assert self.driver.find_element(*MyPage.MyGrWords_wordListNumTotal)
                    logging.info("===断言成功===")


                else:
                    GrWords_woman = 2
                    logging.info("===我的打招呼-已通过真人检测，有消息记录===")
                    assert self.driver.find_element(*MyPage.MyGrWords_Title).text == '我的打招呼'
                    assert self.l.MyGrWords_sendAllBtnEle()
                    logging.info("===断言成功===")

                    #
                    # print(self.driver.find_element(*MyPage.MyGrWords_wordListNumTotal))
                    # listNum=len(self.driver.find_elements(*MyPage.MyGrWords_wordListNumTotal))
                    # print('listNum''{}'.format(listNum))
                    # print(self.driver.find_elements(*MyPage.MyGrWords_wordList_StatusFailedAndIng))
                    # StatusFailedList=len(self.driver.find_elements(*MyPage.MyGrWords_wordList_StatusFailedAndIng))
                    # print('StatusFailedList''{}'.format(StatusFailedList))
                    # if StatusFailedList<listNum:
                    #     logging.info("===有已通过的打招呼消息===")
                    # else:
                    #     logging.info("===没有已通过的打招呼消息===")
                    # self.l.system_goback_key()
                    # logging.info("===断言成功===")


            else:
                logging.info("===男用户===")
                assert self.driver.find_element(*MyPage.MyGreetingWords_entryText).text!='我的打招呼'
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的打招呼-未通过真人检测')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的打招呼-未通过真人检测')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的打招呼')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例156：我的打招呼-已通过真人检测')
    def test_homepage156(self):
        logging.info("===我的打招呼-已通过真人检测===")
        # GrWords_woman=0,1,2=未通过真人检测，通过但没消息，通过且有消息
        try:
            if user_gender == 2:
                logging.info("===女用户===")
                print(GrWords_woman)
                if GrWords_woman ==0:
                    logging.info("===我的打招呼-未通过真人检测===")
                    # assert self.driver.find_element(*MyPage.MyGrWords_faceVerification_popoverText).text == '为保障安全性，你需要先通过真人检测'
                    self.driver.find_element(*MyPage.MyGrWords_faceVerification_popoverConfirmBtn).click()
                    assert self.driver.find_element(*MyPage.MyGrWords_faceVerification_cameraTipsXpath)
                    if self.driver.find_element(*MyPage.MyGrWords_faceVerification_cameraCloseBtn):
                        self.driver.find_element(*MyPage.MyGrWords_faceVerification_cameraCloseBtn).click()
                        logging.info("===断言成功===")
                    else:
                        self.driver.find_element(*MyPage.MyGrWords_faceVerification_cameraTryPopCancelBtn).click()
                        logging.info("===断言成功===")

                else:
                    logging.info("===我的打招呼-已通过真人检测===")
                    # self.driver.find_element(*MyPage.MyGreetingWords_entry).click()
                    print(self.driver.find_elements(*MyPage.MyGrWords_wordListNum))
                    listNum = len(self.driver.find_elements(*MyPage.MyGrWords_wordListNum))
                    print('listNum''{}'.format(listNum))
                    print(self.driver.find_elements(*MyPage.MyGrWords_wordList_StatusFailedAndIng))
                    StatusFailedList = len(self.driver.find_elements(*MyPage.MyGrWords_wordList_StatusFailedAndIng))
                    print('StatusFailedList''{}'.format(StatusFailedList))
                    if self.l.MyGrWords_MyWords_AddBtnEle() and StatusFailedList<listNum-1:
                        logging.info("===页面有增加按钮，有已通过的打招呼消息===")
                        self.driver.find_element(*MyPage.MyGrWords_sendAllBtn).click()
                        # 获取toast
                        assert self.driver.find_element(*MyPage.MyGrWords_sendAllBtn)
                        self.driver.find_element(*MyPage.MyGrWords_goback).click()
                    elif self.l.MyGrWords_MyWords_AddBtnEle()==False and StatusFailedList<listNum:
                        logging.info("===页面没有增加按钮，有已通过的打招呼消息===")
                        self.driver.find_element(*MyPage.MyGrWords_goback).click()
                    else:
                        logging.info("===没有已通过的打招呼消息===")
                        self.driver.find_element(*MyPage.MyGrWords_goback).click()
                    logging.info("===断言成功===")

            else:
                logging.info("===男用户===")
                assert self.driver.find_element(*MyPage.MyGreetingWords_entryText).text != '我的打招呼'
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的打招呼-已通过真人检测')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的打招呼-已通过真人检测')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例173：我的余额-我的钻石')
    def test_homepage173(self):
        logging.info("===我的简介-我的钻石===")
        try:
            if user_gender==1:
                entryDiamondNum = self.driver.find_element(*MyPage.myBalance_entryDiamondManNum).text
                self.driver.find_element(*MyPage.myBalance_entryManAll).click()
            else:
                entryDiamondNum = self.driver.find_element(*MyPage.myBalance_entryDiamondWomanNum).text
                self.driver.find_element(*MyPage.myBalance_entryWomanAll).click()
            myDiamondCount=self.driver.find_element(*MyPage.myBalance_myDiamondCountText).text
            assert '{}''[diamond]'.format(myDiamondCount) == entryDiamondNum,'内外钻石数不一致'
            assert self.driver.find_element(*MyPage.myBalance_agreeContent).text == '同意用户协议和隐私政策！'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的余额-我的钻石')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的余额-我的钻石')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例174：我的余额-free入口')
    def test_homepage174(self):
        logging.info("===我的余额-free入口===")
        try:
            self.driver.find_element(*MyPage.myBalance_topOffers_Entry).click()
            assert self.driver.find_element(*MyPage.myBalance_topOffers_Title).text == 'Top Offers'
            assert self.driver.find_element(*MyPage.myBalance_topOffers_AllOffers).text == 'All Offers'
            self.driver.find_element(*MyPage.myBalance_topOffers_Goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的余额-free入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的余额-free入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    # 充值档位需要谷歌套件才能显示
    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例175：我的余额-充值档位')
    def test_homepage175(self):
        logging.info("===我的余额-充值档位===")
        try:
            assert self.driver.find_element(*MyPage.myBalance_TopUpList_firstEle)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的余额-充值档位')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的余额-充值档位')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    # 充值档位需要谷歌套件才能显示
    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例176：我的余额-充值档位-充值')
    def test_homepage176(self):
        logging.info("===我的余额-充值档位-充值===")
        try:
            assert self.driver.find_element(*MyPage.myBalance_TopUpList_firstEle)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的余额-充值档位-充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的余额-充值档位-充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例177：我的余额-历史详情')
    def test_homepage177(self):
        logging.info("===我的余额-历史详情===")
        try:
            self.driver.find_element(*MyPage.myBalance_DiamondDetailEntry).click()
            time.sleep(15)
            assert self.driver.find_element(*MyPage.myBalance_DiamondDetail_TitleXpath)
            self.l.system_goback_key()
            # assert self.driver.find_element(*MyPage.myBalance_DiamondDetail_selectTab)
            # assert self.driver.find_element(*MyPage.myBalance_DiamondDetail_ContentBox)
            # self.driver.find_element(*MyPage.myBalance_DiamondDetail_Goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的余额-历史详情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的余额-历史详情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例178：我的余额-客服按钮')
    def test_homepage178(self):
        logging.info("===我的余额-客服按钮===")
        try:
            self.driver.find_element(*MyPage.myBalance_ServiceEntry).click()
            assert self.driver.find_element(*MyPage.myBalance_Service_title).text == '在线客服'
            assert self.driver.find_element(*MyPage.myBalance_Service_helpInput)
            self.driver.find_element(*MyPage.myBalance_Service_goback).click()
            self.driver.find_element(*MyPage.myBalance_entry_goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的余额-客服按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的余额-客服按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例179：我的页面-设置')
    def test_homepage179(self):
        logging.info("===我的页面-设置===")
        try:
            self.l.tab_Mine_Btn()
            time.sleep(2)
            self.l.tap(930,2123)
            self.l.swipe(626,1572,626,933)
            self.driver.find_element(*MyPage.settings_entry).click()
            assert self.driver.find_element(*MyPage.settings_title).text=='设置', "页面未跳转至设置页"
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例180：我的页面-设置-APP语言')
    def test_homepage180(self):
        logging.info("===我的页面-设置-APP语言===")
        try:
            # self.l.tab_Mine_Btn()
            # time.sleep(2)
            # self.l.swipe(626, 1572, 626, 933)
            App_lan=self.driver.find_element(*MyPage.settings_AppLanguage_selectedText).text
            print(App_lan)
            self.driver.find_element(*MyPage.settings_AppLanguage_All).click()
            assert self.driver.find_element(*MyPage.settings_AppLanguageTitle).text == 'APP语言', "页面未跳转至设置页"
            assert self.driver.find_element(*MyPage.settings_AppLanguage_AutomaticText).text == App_lan, "页面未跳转至设置页"
            self.driver.find_element(*MyPage.settings_AppLanguage_English).click()
            self.driver.find_element(*MyPage.settings_AppLanguage_saveBtn).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-APP语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-APP语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例181：我的页面-设置-切换APP语言')
    def test_homepage181(self):
        logging.info("===我的页面-设置-切换APP语言===")
        try:
            self.l.tab_Mine_Btn()
            time.sleep(2)
            self.l.swipe(626, 1572, 626, 933)
            self.driver.find_element(*MyPage.settings_entry).click()
            App_lan = self.driver.find_element(*MyPage.settings_AppLanguage_selectedText).text
            assert App_lan == 'English'
            self.driver.find_element(*MyPage.settings_AppLanguage_All).click()
            self.driver.find_element(*MyPage.settings_AppLanguage_Automatic).click()
            self.driver.find_element(*MyPage.settings_AppLanguage_saveBtn).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-切换APP语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-切换APP语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例182，183：我的页面-设置-黑名单')
    def test_homepage182(self):
        logging.info("===我的页面-设置-黑名单===")
        try:
            self.l.tab_Mine_Btn()
            time.sleep(2)
            self.l.swipe(626, 1572, 626, 933)
            self.driver.find_element(*MyPage.settings_entry_RightClick).click()
            self.driver.find_element(*MyPage.settings_blocklist).click()
            NoUserEle=self.l.settings_blockList_NoUserTextEle()
            if NoUserEle!=False:
                logging.info("===无用户===")
                assert NoUserEle == '无用户'
                self.driver.find_element(*MyPage.settings_blocklist_goback).click()
                logging.info("===断言成功===")
            # elif NoUserEle==False and self.l.settings_blocklist_oneUserClickEle():
            #     oneUserName = self.driver.find_element(*MyPage.settings_blocklist_oneUserName).text
            #     self.driver.find_element(*MyPage.settings_blocklist_oneUserClick).click()
            #     assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text ==oneUserName,'用户姓名前后不一致 '
            #     self.driver.find_element(*MyPage.user_own_pageFollowBtn).click()
            #     time.sleep(2)
            #     assert self.driver.find_element(*MyPage.user_own_pageFollowBtn)
            #     self.l.system_goback_key()
            #     self.l.system_goback_key()
            else:
                logging.info("===有用户===")
                firstUserName = self.driver.find_elements(*MyPage.settings_blocklist_UserNameList)[0].text
                self.driver.find_elements(*MyPage.settings_blocklist_UserClickList)[0].click()
                assert self.driver.find_element(*MyPage.user_own_pagePersonalName).text == firstUserName, '用户姓名前后不一致 '
                assert self.driver.find_element(*MyPage.user_own_pageFollowBtn)
                self.l.system_goback_key()
                assert self.driver.find_element(*MyPage.settings_blocklist_firstUserClick)
                self.l.system_goback_key()
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-黑名单')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-黑名单')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例184：我的页面-设置-隐私政策')
    def test_homepage184(self):
        logging.info("===我的页面-设置-隐私政策===")
        try:
            self.driver.find_element(*MyPage.settings_PrivacyPolicy).click()
            assert self.driver.find_element(*MyPage.settings_PrivacyPolicy_title).text == 'Privacy Policy', '隐私政策名称不一致'
            assert self.driver.find_element(*MyPage.settings_PrivacyPolicy_titleXpath)
            self.l.system_goback_key()
            # self.driver.find_element(*MyPage.settings_PrivacyPolicy_goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-隐私政策')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-隐私政策')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例185：我的页面-设置-用户协议')
    def test_homepage185(self):
        logging.info("===我的页面-设置-用户协议===")
        try:
            self.driver.find_element(*MyPage.settings_UserAgreement).click()
            assert self.driver.find_element(*MyPage.settings_UserAgreement_titleXpath)
            assert self.driver.find_element(*MyPage.settings_UserAgreement_Welcome)
            self.driver.find_element(*MyPage.settings_UserAgreement_titleAndGoback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-用户协议')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-用户协议')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例186：我的页面-设置-关于我们')
    def test_homepage186(self):
        logging.info("===我的页面-设置-关于我们===")
        try:
            self.driver.find_element(*MyPage.settings_AboutUs).click()
            assert self.driver.find_element(*MyPage.settings_AboutUs_title).text == '关于我们', '关于我们名称不一致'
            assert self.driver.find_element(*MyPage.settings_AboutUs_accountDeleteBtn)
            logging.info("===断言成功===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-关于我们')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-关于我们')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例187：我的页面-设置-关于我们删除账户')
    def test_homepage187(self):
        logging.info("===我的页面-设置-关于我们删除账户===")
        try:
            self.driver.find_element(*MyPage.settings_AboutUs_accountDeleteBtn).click()
            assert self.driver.find_element(*MyPage.settings_AboutUs_deleteUserName).text ==pagePersonalName , '用户名称不一致'
            assert self.driver.find_element(*MyPage.settings_AboutUs_deleteDeleteBtn)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-关于我们删除账户')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-关于我们删除账户')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例188：我的页面-设置-关于我们删除账户-提示弹窗')
    def test_homepage188(self):
        logging.info("===我的页面-设置-关于我们删除账户-提示弹窗===")
        try:
            delete_reason='i do not want to play anymore,i want to delete it'
            self.driver.find_element(*MyPage.settings_AboutUs_deleteEditReason).send_keys(delete_reason)
            time.sleep(2)
            self.l.tap(1015,1435)
            self.driver.find_element(*MyPage.settings_AboutUs_deleteDeleteBtn).click()
            self.driver.find_element(*MyPage.settings_AboutUs_deletePopoverCancel).click()
            assert self.driver.find_element(*MyPage.settings_AboutUs_deleteUserName).text == pagePersonalName
            self.driver.find_element(*MyPage.settings_AboutUs_deleteDeleteBtn).click()
            self.driver.find_element(*MyPage.settings_AboutUs_deletePopoverConfirm).click()
            assert self.driver.find_element(*LoginView.more_btn)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-关于我们删除账户-提示弹窗')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-关于我们删除账户-提示弹窗')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例189：我的页面-设置-关于我们删除账户-再次登录')
    def test_homepage189(self):
        logging.info("===我的页面-设置-关于我们删除账户-再次登录===")
        self.Login=LoginView(self.driver)
        try:
            # self.l.login_direct_phone(4086222, 111111)
            self.Login.more_Btn()
            self.Login.phonenumber_Btn()
            self.Login.login_input_phonenumber('4086222')
            self.driver.find_element(*LoginView.next_btn).click()
            assert self.driver.find_element(*MyPage.settings_AboutUs_deleteLoginPopoverTitle).text == '注意', '再次登录弹窗名称不是注意'
            self.driver.find_element(*MyPage.settings_AboutUs_deleteLoginPopoverCancel).click()
            self.driver.find_element(*LoginView.next_btn).click()
            self.driver.find_element(*MyPage.settings_AboutUs_deleteLoginPopoverConfirm).click()
            if LoginView(self.driver).find_pass_ele():
                LoginView(self.driver).login_input_phone_password('111111')
            self.l.tab_Mine_Btn()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-关于我们删除账户-再次登录')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-关于我们删除账户-再次登录')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例190：我的页面-设置-为Chamet评分')
    def test_homepage190(self):
        logging.info("===我的页面-设置-为Chamet评分===")
        self.Login = LoginView(self.driver)
        try:
            self.l.tab_Mine_Btn()
            time.sleep(2)
            self.l.swipe(626, 1572, 626, 933)
            self.driver.find_element(*MyPage.settings_entry_RightClick).click()
            self.driver.find_element(*MyPage.settings_RateChamet).click()
            assert self.driver.find_element(*MyPage.settings_RateChametText).text == '为Chamet评分', "页面点击后没停留设置页面"
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-为Chamet评分')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-为Chamet评分')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例191：我的页面-设置-清除缓存')
    def test_homepage191(self):
        logging.info("===我的页面-设置-清除缓存===")
        self.Login = LoginView(self.driver)
        try:
            self.driver.find_element(*MyPage.settings_ClearCache).click()
            # 获取缓存已清除的文字toast
            self.driver.find_element(*MyPage.settings_ClearCache).click()
            assert self.driver.find_element(*MyPage.settings_ClearCache_cache).text == '0B'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-清除缓存')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-清除缓存')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例192：我的页面-设置-版本')
    def test_homepage192(self):
        logging.info("===我的页面-设置-版本===")
        self.Login = LoginView(self.driver)
        try:
            self.driver.find_element(*MyPage.settings_versions).click()
            versions_versionText_case=self.driver.find_element(*MyPage.settings_versions_versionText).text
            assert versions_versionText_case.find('3.4.')>=0
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-版本')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-版本')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例193：我的页面-设置-登出按钮')
    def test_homepage193(self):
        logging.info("===我的页面-设置-登出按钮===")
        self.Login = LoginView(self.driver)
        try:
            assert self.driver.find_element(*MyPage.settings_logout_logoutText).text=='登出'
            self.driver.find_element(*MyPage.settings_logout).click()
            assert self.driver.find_element(*MyPage.settings_logout_popoverTitle).text == '确定退出？'
            self.l.tap(917,2010)
            self.driver.find_element(*MyPage.settings_logout).click()
            self.driver.find_element(*MyPage.settings_logout_popoverCancel).click()
            assert self.driver.find_element(*MyPage.settings_logout_logoutText).text == '登出'
            logging.info("===断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-登出按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-登出按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例194：我的页面-设置-登出按钮-登出再登入')
    def test_homepage194(self):
        logging.info("===我的页面-设置-登出按钮-登出再登入===")
        self.Login = LoginView(self.driver)
        try:
            self.driver.find_element(*MyPage.settings_logout).click()
            assert self.driver.find_element(*MyPage.settings_logout_popoverConfirm).text == '好的'
            self.driver.find_element(*MyPage.settings_logout_popoverConfirm).click()
            # assert self.driver.find_element(*LoginView.more_btn)
            self.l.login_step(4086222, 111111)
            self.l.tap(930,2123)
            assert self.driver.find_element(*MyPage.tab_mine_btn)
            # assert self.l.tab_Mine_Btn()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.c.screenshot('我的页面-设置-登出按钮-登出再登入')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.c.screenshot('我的页面-设置-登出按钮-登出再登入')
            logging.info(f'截图成功，图片为{screen_name}')
            raise





if __name__ == '__main__':
    pytest.main(["-vs","../test_case/test_mypage.py","--allure-stories==顶部个人主页,我的邀请,简介"])







    # command_line = ["-vs", "../test_case/test_mypage.py", "--alluredir=../result/2023_5_18_001",'--allure-stories', '打印韵母']
    # pytest.main(command_line)

    """    
    pytest.main(["-vs", "../test_case/test_mypage.py","--alluredir=../result/tmp/2023_06_15_002"])
    os.system('allure generate ../result/tmp -o ../reports/html --clean')
    os.system("allure open ./reports/html")
    """

    # # 执行测试用例生成测试数据，如果已经存在报告，那就先清空，然后再生成新的测试报告，使用命令： --clean-alluredir
    #     pytest.main([ '-vs','test.py','--clean-alluredir', '--alluredir', './allure-results'])
    """
    # 只运行 epic 名为 epic1 的测试用例
    pytest --alluredir ./report/allure --allure-epics=epic1
    
    # 只运行 feature 名为 模块级 的测试用例
    pytest --alluredir ./report/allure --allure-features=模块级
    
    # 只运行 story1、story2 的测试用例（也可以不用=号 空格即可）
    pytest tests.py --allure-stories story1,story2
    
    # 指定 feature和story
    pytest tests.py --allure-features feature1,feature2 --allure-stories story1
    """


    # pytest.main(['-s', 'test_mypage.py'])
    # pytest.main(['-pytest -vs --alluredir=./results'])

    # command_line = ["-s", "./tests/test1/test1.py", "--alluredir=./result/2023_5_31_001"]
    # pytest.main(command_line)
    '''
    pytest .\test_case\test_mypage.py -v -s --alluredir=..\result\tmp\2023_06_20_001 --allure-stories='顶部个人主页','我的等级'
    allure generate ../result/tmp/2023_06_15_002  -o ../reports/html --clean
    allure open ../report/html
    实验命令行
    pytest .\test_case\test_mypage.py -vs --alluredir=..\result\tmp\2023_06_15_001 
    pytest ./test_case/test_mypage.py - vs - -alluredir = .\result\2023_06_15_001
    allure serve D:/chamet_testProject1/result/tmp/2023_06_15_001
    '''

    # 宇敏terminal命令行输入
    # pytest .\test_10party.py -v -s --alluredir=..\result\2023_5_18_001
    # pytest .\test_10party.py - v - s - -alluredir =..\result\2023_5_18_001
    # allure serve..\result\2023_5_18_001
    # allure serve..\result\2023_6_14_002
    # 玉萍terminal命令行输入
    # pytest .\tespytest .\test_case\test_mypage.py -v -s --alluredir=..\result\tmp\2023_06_15_002 --allure-stories=="顶部个人主页","设置"st_case\test_mypage.py -v -s --alluredir=..\result\2023_06_08_002
    # pytest .\test_mypage.py - vs  -alluredir =..\result\2023_06_08_001

# python -m pytest ./test_case/test_mypage.py -v -s --alluredir=./result/2023_06_08_001
# pytest ./test_case/test_mypage.py -v -s --alluredir=./result/2023_06_08_001
#
# pytest .\test_case\test_mypage.py -v -s --alluredir=.\result\2023_5_31_001
# pytest test_case\test_mypage.py -v -s --alluredir=.\result\2023_5_31_001
# pytest ..\test_mypage.py -v -s --alluredir=..\result\2023_5_31_001