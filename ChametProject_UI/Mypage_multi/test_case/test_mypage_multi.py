# -*- coding: utf-8 -*-

import os
import io
import re
import sys
from appium.webdriver.common.mobileby import MobileBy
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
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalInformationText), "没有通过头像找到个人主页元素"
            logging.info("断言成功")
            self.mandriver.find_element(*MultiMan.user_own_pageGobackBtn).click()
            # 获取元素
            global man_pageUserId
            # global man_user_gender
            # man_user_gender=self.multiman.myProfile_Gender_ManorW()
            self.multiman.my_Profile_entry()
            man_pageUserId = self.mandriver.find_element(*MultiMan.myProfile_ID_Number).text
            self.multiman.system_goback_key()
            # print(man_pageSelfIntroduction,man_pagePersonalName,man_pageUserId)
            # print(type(man_user_gender))


            # # 女生个人主页
            # self.multiwoman.tap(930, 2123)
            # self.multiwoman.tab_Mine_Btn()
            # self.multiwoman.tab_Mine_Head()
            # time.sleep(2)
            # global woman_pageSelfIntroduction, woman_pagePersonalName
            # woman_pageSelfIntroduction = self.multiwoman.user_ownPage_selfIntroductionEle()
            # woman_pagePersonalName = self.womandriver.find_element(*MultiWoman.user_own_pagePersonalName).text
            # assert self.womandriver.find_element(*MultiWoman.user_own_pagePersonalInformationText), "没有通过头像找到个人主页元素"
            # logging.info("断言成功")
            # self.womandriver.find_element(*MultiWoman.user_own_pageGobackBtn).click()
            # # print(woman_pageSelfIntroduction, woman_pagePersonalName)


            # 获取元素
            # global woman_pageUserId
            # global woman_user_gender
            # woman_user_gender = self.multiwoman.myProfile_Gender_ManorW()
            # self.multiwoman.my_Profile_entry()
            # woman_pageUserId = self.womandriver.find_element(*MultiWoman.myProfile_ID_Number).text
            # self.multiwoman.system_goback_key()
            # print(type(woman_user_gender))

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


    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例2：我的页面-顶部空白区域')
    def test_homepage02(self):
        logging.info("===我的页面-顶部空白区域===")
        try:
            self.multiman.tab_Mine_Btn()
            assert self.mandriver.find_element(*MultiMan.user_name).text==man_pagePersonalName
            self.multiman.tap(261,245)
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalInformationText),"没有通过空白找到个人主页元素"
            self.multiman.system_goback_key()
            logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('===我的页面-顶部空白区域===')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('===我的页面-顶部空白区域===')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例3和4：我的页面-等级')
    def test_homepage03(self):
        logging.info("===我的页面-等级===")
        try:
            self.multiman.tab_Mine_Btn()
            self.multiman.tap(960, 2262)
            global lel_ele
            lel_ele = self.multiman.tab_Mine_user_vip_level()
            global level_frame
            if lel_ele != False:
                logging.info("有等级-点击确认")
                level_frame = 1
                self.multiman.tap(960, 2262)
                lel_ele.click()
                time.sleep(3)
                self.multiman.native_to_h5()
                assert self.mandriver.find_element(*MultiMan.level_titleTextXpath)
                self.multiman.system_goback_key()
                self.multiman.h5_to_native()
                logging.info("断言成功")
            else:
                logging.info("没有等级-等级元素再次确认")
                assert self.mandriver.find_element(*MultiMan.my_vipLevel_NowLevelImgZeroAndWoman).text == 'Lv0'
                level_frame = 0
                logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例5：我的页面-头像框')
    def test_homepage05(self):
        logging.info("===我的页面-头像框===")
        try:
            self.multiman.tab_Mine_Btn()
            if level_frame == 1:
                logging.info("等级有,头像框-确认")
                self.multiman.tap(960, 2262)
                assert self.multiman.tab_Mine_Head_level_frame()
                logging.info("断言成功")
            else:
                logging.error("没有等级，没有头像框确认")
                assert self.multiman.tab_Mine_Head_level_frame()==False
                logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例6：我的页面-国家')
    def test_homepage06(self):
        logging.info("===我的页面-国家===")
        try:
            self.multiman.tab_Mine_Btn()
            assert self.mandriver.find_element(*MultiMan.user_nation), "页面没有国家图标"
            logging.info("===我的页面-有国家图标，断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot(module='my_page_own')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot(module='my_page_own')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例7和8：我的页面-语言')
    def test_homepage07(self):
        logging.info("===我的页面-语言===")
        try:
            self.multiman.tab_Mine_Btn()
            lan_text=self.multiman.tab_Mine_user_language_LanEle()
            if lan_text == 2:
                logging.info("有第二语言")
                self.mandriver.find_element(*MultiMan.user_language).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_Title).text == '我的简介', '有第二语言。没跳转到我的简介页面'
                self.multiman.system_goback_key()
                logging.info("断言成功")
            else:
                logging.info("只有第一语言")
                self.mandriver.find_element(*MultiMan.user_language).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_Language_title).text =='语言','只有第一语言。没跳转到语言页面'
                self.multiman.system_goback_key()
                logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例9：我的页面-粉丝')
    def test_homepage09(self):
        logging.info("===我的页面-粉丝===")
        try:
            self.multiman.tab_Mine_Btn()
            # 该函数返回值有的话，返回粉丝数
            global followers_num
            followers_num =self.multiman.tab_Mine_user_followers()
            user_followers_entry=self.mandriver.find_element(*MultiMan.user_followers)
            self.multiman.tap(960, 2262)
            user_followers_entry.click()
            assert self.mandriver.find_element(*MultiMan.user_followers_Title).text == '粉丝'
            assert followers_num!=False
            logging.info("有粉丝，断言成功")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-粉丝')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-粉丝')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例10：我的页面-粉丝列表')
    def test_homepage10(self):
        logging.info("===我的页面-粉丝列表===")
        try:
            if followers_num!=False and int(followers_num)>0:
                # 上下滑动
                followers_firstName = self.mandriver.find_elements(*MultiMan.user_followers_firstPerNameID)[0].text.encode('gbk', 'ignore')
                print(followers_firstName)
                self.multiman.swipe(340, 360, 340, 1340)
                time.sleep(3)
                assert self.mandriver.find_elements(*MultiMan.user_followers_firstPerNameID)[0].text.encode('gbk', 'ignore')==followers_firstName
                self.multiman.swipe(340, 1836, 340, 800)
                time.sleep(3)
                assert self.mandriver.find_elements(*MultiMan.user_followers_firstPerNameID)[0].text.encode('gbk', 'ignore') != followers_firstName
                # 检查国家、状态、等级元素有无
                assert self.mandriver.find_elements(*MultiMan.user_followers_country)
                assert self.mandriver.find_elements(*MultiMan.user_followers_countryName)
                assert self.mandriver.find_elements(*MultiMan.user_followers_level)
                assert self.mandriver.find_elements(*MultiMan.user_followers_status)
                assert self.mandriver.find_elements(*MultiMan.user_followers_loveImg)
                logging.info("断言成功")
            else:
                self.multiman.swipe(340, 360, 340, 1340)
                time.sleep(3)
                assert self.mandriver.find_element(*MultiMan.user_followers_EmptyText).text == '你关注的用户将在这里'
                self.multiman.swipe(340, 1870, 340, 340)
                assert self.mandriver.find_element(*MultiMan.user_followers_EmptyText).text == '你关注的用户将在这里'
                logging.info("断言成功")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-粉丝列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-粉丝列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例11：我的页面-粉丝头像')
    def test_homepage11(self):
        logging.info("===我的页面-粉丝头像===")
        try:
            if followers_num!=False and int(followers_num)>0:
                logging.info("===我的页面-粉丝头像人数不为0===")
                followers_firstPerName=self.mandriver.find_elements(*MultiMan.user_followers_firstPerNameID)[0].text.encode('gbk', 'ignore')
                self.mandriver.find_elements(*MultiMan.user_followers_firstPerHeadID)[0].click()
                time.sleep(2)
                assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName)
                # assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text.encode('gbk', 'ignore') == followers_firstPerName
                self.mandriver.find_element(*MultiMan.user_own_pageGobackBtn).click()
                self.mandriver.find_element(*MultiMan.user_followers_GoBack).click()
                logging.info("===断言成功===")
            else:
                logging.info("===我的页面-粉丝头像人数为0===")
                assert self.mandriver.find_element(*MultiMan.user_followers_EmptyText).text=='你关注的用户将在这里'
                self.mandriver.find_element(*MultiMan.user_followers_GoBack).click()
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例12：我的页面-关注')
    def test_homepage12(self):
        logging.info("===我的页面-关注===")
        try:
            self.multiman.tab_Mine_Btn()
            # 该函数返回值有的话，返回粉丝数
            global following_num
            following_num = self.multiman.tab_Mine_user_following()
            user_following_Entry=self.mandriver.find_element(*MultiMan.user_following)
            self.multiman.tap(960, 2262)
            user_following_Entry.click()
            assert self.mandriver.find_element(*MultiMan.user_following_Title).text == '关注'
            assert following_num != False
            logging.info("有关注，断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('===我的页面-关注==="')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('===我的页面-关注==="')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例13：我的页面-关注列表')
    def test_homepage13(self):
        logging.info("===我的页面-关注列表===")
        try:
            if following_num != False and int(following_num) > 0:
                # 上下滑动
                following_firstName = self.mandriver.find_elements(*MultiMan.user_following_firstPerNameID)[0].text.encode('gbk', 'ignore')
                print(following_firstName)
                self.multiman.swipe(340, 360, 340, 1340)
                time.sleep(3)
                assert self.mandriver.find_elements(*MultiMan.user_following_firstPerNameID)[0].text.encode('gbk', 'ignore') == following_firstName
                self.multiman.swipe(340, 1836, 340, 1020)
                time.sleep(2)
                self.multiman.swipe(340, 1836, 340, 1020)
                time.sleep(2)
                assert self.mandriver.find_elements(*MultiMan.user_following_firstPerNameID)[0].text.encode('gbk', 'ignore') != following_firstName
                # 检查国家、状态、等级元素有无
                assert self.mandriver.find_elements(*MultiMan.user_followers_country)
                assert self.mandriver.find_elements(*MultiMan.user_followers_countryName)
                assert self.mandriver.find_elements(*MultiMan.user_followers_level)
                assert self.mandriver.find_elements(*MultiMan.user_followers_status)
                assert self.mandriver.find_elements(*MultiMan.user_followers_loveImg)
                logging.info("断言成功")
            else:
                self.multiman.swipe(340, 360, 340, 1340)
                time.sleep(3)
                assert self.mandriver.find_element(*MultiMan.user_following_EmptyText).text == '你关注的用户将在这里'
                self.multiman.swipe(340, 1870, 340, 340)
                assert self.mandriver.find_element(*MultiMan.user_following_EmptyText).text == '你关注的用户将在这里'
                logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-关注列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-关注列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例14：我的页面-关注头像')
    def test_homepage14(self):
        logging.info("===我的页面-关注头像===")
        try:
            if following_num!=False and int(following_num)>0:
                logging.info("===我的页面-关注头像人数不为0===")
                following_firstPerName = self.mandriver.find_elements(*MultiMan.user_following_firstPerNameID)[0].text.encode('gbk', 'ignore')
                self.mandriver.find_elements(*MultiMan.user_following_firstPerHeadID)[0].click()
                time.sleep(2)
                assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName)
                # assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text.encode('gbk', 'ignore') == following_firstPerName
                self.multiman.system_goback_key()
                self.mandriver.find_element(*MultiMan.user_following_GoBack).click()
                logging.info("断言成功")
            else:
                logging.info("===我的页面-关注头像人数为0===")
                assert self.mandriver.find_element(*MultiMan.user_following_EmptyText).text=='你关注的用户将在这里'
                self.mandriver.find_element(*MultiMan.user_followers_GoBack).click()
                logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例15：我的页面-朋友')
    def test_homepage15(self):
        logging.info("===我的页面-朋友===")
        try:
            self.multiman.tab_Mine_Btn()
            # 该函数返回值有的话，返回粉丝数
            global friend_num
            friend_num = self.multiman.tab_Mine_user_friend()
            user_friend_Entry=self.mandriver.find_element(*MultiMan.user_friend)
            self.multiman.tap(930, 2123)
            user_friend_Entry.click()
            assert self.mandriver.find_element(*MultiMan.user_friend_Title).text == '朋友'
            assert followers_num != False
            logging.info("有朋友，断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('===我的页面-朋友===')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('===我的页面-朋友===')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例16：我的页面-朋友列表')
    def test_homepage16(self):
        logging.info("===我的页面-朋友列表===")
        try:
            if friend_num!=False and int(friend_num)>0:
                # 上下滑动
                friend_firstName = self.mandriver.find_elements(*MultiMan.user_friend_firstPerNameID)[0].text.encode('gbk', 'ignore')
                print(friend_firstName)
                self.multiman.swipe(340, 603, 340, 2000)
                time.sleep(3)
                assert self.mandriver.find_elements(*MultiMan.user_friend_firstPerNameID)[0].text.encode('gbk', 'ignore') == friend_firstName
                self.multiman.swipe(340, 2100, 340, 450)
                assert self.mandriver.find_elements(*MultiMan.user_friend_firstPerNameID)[0].text.encode('gbk', 'ignore') != friend_firstName
                # 检查搜索、密友值、国家图标、国家名称、等级元素有无
                assert self.mandriver.find_element(*MultiMan.user_friend_searchEle)
                assert self.mandriver.find_element(*MultiMan.user_friend_heartNum)
                assert self.mandriver.find_element(*MultiMan.user_friend_countryImg)
                assert self.mandriver.find_element(*MultiMan.user_friend_countryName)
                assert self.mandriver.find_element(*MultiMan.user_friend_levelImg)
                logging.info("断言成功")
            else:
                self.multiman.swipe(340, 360, 340, 1340)
                time.sleep(3)
                assert self.mandriver.find_element(*MultiMan.user_friend_EmptyText).text == '无用户'
                self.multiman.swipe(340, 1870, 340, 340)
                assert self.mandriver.find_element(*MultiMan.user_friend_EmptyText).text == '无用户'
                logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-关注列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-关注列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例17：我的页面-朋友头像')
    def test_homepage17(self):
        logging.info("===我的页面-朋友头像===")
        try:
            if friend_num!=False and int(friend_num)>0:
                logging.info("===我的页面-朋友头像人数不为0===")
                friend_firstPerName = self.mandriver.find_elements(*MultiMan.user_friend_firstPerNameID)[0].text.encode('gbk', 'ignore')
                self.mandriver.find_elements(*MultiMan.user_friend_firstPerHeadID)[0].click()
                time.sleep(2)
                assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName)
                # assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text.encode('gbk', 'ignore') == friend_firstPerName
                self.multiman.system_goback_key()
                self.mandriver.find_element(*MultiMan.user_friend_GoBack).click()
                logging.info("断言成功")
            else:
                logging.info("===我的页面-朋友无该图标===")
                assert self.mandriver.find_element(*MultiMan.user_friend_EmptyText).text=='无用户'
                self.mandriver.find_element(*MultiMan.user_friend_GoBack).click()
                logging.info("断言成功")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-个人头像-个人主页')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例18：我的页面-男-签到入口')
    def test_homepage18(self):
        logging.info("===我的页面-男-签到入口===")
        try:
            self.multiman.tab_Mine_Btn()
            global signInfoTopEle_man
            signInfoTopEle_man = self.multiman.tab_Mine_user_signInfoTop()
            self.multiman.tap(960, 2262)
            if signInfoTopEle_man != False:
                self.multiman.tap(960, 2262)
                signInfoTopEle_man.click()
                assert len(self.mandriver.find_elements(*MultiMan.sign_in_popover_dayNum1_7Ele))==7
                assert self.mandriver.find_element(*MultiMan.sign_in_popover_reminderText).text=='签到提醒'
                assert self.mandriver.find_element(*MultiMan.sign_in_popover_reminderBtn)
                # assert self.mandriver.find_element(*MultiMan.sign_in_popover_SigninSubmitTextID).text == '签到'
                # 测试点击空白处弹窗消失
                self.multiman.tap(960, 2262)
                assert self.mandriver.find_element(*MultiMan.tab_mine_btn)
                logging.info("断言成功")
            else:
                logging.error("没有签到入口")
                pytest.skip("没有签到入口，跳过该测试用例")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-男-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-男-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例19：我的页面-男-去签到-跳转页面')
    def test_homepage19(self):
        logging.info("===我的页面-男-去签到-跳转页面===")
        try:
            self.multiman.tab_Mine_Btn()
            self.multiman.tap(960, 2262)
            if signInfoTopEle_man != False:
                signInfoTopEle_man.click()
                sign_btn_man = self.mandriver.find_element(*MultiMan.sign_in_popover_SigninSubmitTextID)
                assert sign_btn_man.text == '签到'
                sign_btn_man.click()
                # 开始再次点击，测试跳转页面
                signInfoTopEle_man.click()
                sign_btn_man = self.mandriver.find_element(*MultiMan.sign_in_popover_SigninSubmitTextID)
                assert sign_btn_man.text == '好的'
                sign_btn_man.click()
                assert self.mandriver.find_element(*MultiMan.user_sign_infoTop)
                logging.info("断言成功")
            else:
                logging.error("没有签到入口")
                pytest.skip("没有签到入口，跳过该测试用例")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-男-去签到-跳转页面')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-男-去签到-跳转页面')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例20：我的页面-女-签到入口')
    def test_homepage20(self):
        logging.info("===我的页面-女-签到入口===")
        try:
            self.multiwoman.tab_Mine_Btn_126()
            global signInfoTopEle_woman
            signInfoTopEle_woman = self.multiwoman.tab_Mine_user_signInfoTop()
            self.multiwoman.tap(930, 2123)
            if signInfoTopEle_woman != False:
                self.multiwoman.tap(930, 2123)
                signInfoTopEle_woman.click()
                assert len(self.womandriver.find_elements(*MultiWoman.sign_in_popover_dayNum1_7Ele)) == 7
                assert self.womandriver.find_element(*MultiWoman.sign_in_popover_reminderText).text == '签到提醒'
                assert self.womandriver.find_element(*MultiWoman.sign_in_popover_reminderBtn)
                # assert self.womandriver.find_element(*MultiWoman.sign_in_popover_SigninSubmitTextID).text == '签到'
                # 测试点击空白处弹窗消失
                self.multiwoman.tap(930, 2123)
                assert self.womandriver.find_element(*MultiWoman.tab_mine_btn)
                logging.info("断言成功")
            else:
                logging.error("没有签到入口")
                pytest.skip("没有签到入口，跳过该测试用例")

        except AssertionError as e:
                logging.info('===断言失败===')
                screen_name = self.multiwoman.screenshot('我的页面-女-签到入口')
                logging.info(f'截图成功，图片为{screen_name}')
                raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的页面-女-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('顶部个人主页')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例21：我的页面-女-去签到-跳转页面')
    def test_homepage21(self):
        logging.info("===我的页面-女-去签到-跳转页面===")
        try:
            self.multiwoman.tab_Mine_Btn()
            self.multiwoman.tap(930, 2123)
            if signInfoTopEle_woman != False:
                signInfoTopEle_woman.click()
                sign_btn_woman = self.womandriver.find_element(*MultiWoman.sign_in_popover_SigninSubmitTextID)
                assert sign_btn_woman.text == '签到'
                sign_btn_woman.click()
                # 开始再次点击，测试跳转页面
                signInfoTopEle_woman.click()
                sign_btn_woman = self.womandriver.find_element(*MultiWoman.sign_in_popover_SigninSubmitTextID)
                assert sign_btn_woman.text =='兑换奖励'
                sign_btn_woman.click()
                task_CompletePopover = self.multiwoman.tab_Mine_user_signInfoTopEleTASK()
                task_rewardBtn = self.womandriver.find_element(*MultiWoman.MyTasks_tab_rewards)
                if task_CompletePopover == False:
                    assert task_rewardBtn.get_attribute('selected') == 'true'
                    self.multiwoman.system_goback_key()
                else:
                    task_CompletePopover.click()
                    self.multiwoman.system_goback_key()
                logging.info("断言成功")
            else:
                logging.error("没有签到入口")
                pytest.skip("没有签到入口，跳过该测试用例")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的页面-女-去签到-跳转页面')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的页面-女-去签到-跳转页面')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
















    # #
    # #
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例22、23：留言-列表及消息未读数')
    # # def test_homepage22(self):
    # #     logging.info("===留言-列表及消息未读数===")
    # #     try:
    # #         self.multiman.tab_Mine_Btn()
    # #         self.multiman.tap(930, 2123)
    # #         entry_UnReadNum_case=self.multiman.messages_entry_UnReadNumIDEle()
    # #         # print(UnReadNum_case44)
    # #         self.mandriver.find_element(*MultiMan.messages_entry_All).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_title).text == '留言'
    # #         assert self.mandriver.find_element(*MultiMan.messages_system_EntryTitle).text == 'Chamet团队'
    # #         assert self.mandriver.find_element(*MultiMan.messages_customerService_entryTitle).text == 'Chamet客服'
    # #         if entry_UnReadNum_case != False:
    # #         # if entry_UnReadNum_case!=False and len(entry_UnReadNum_case)!=0:
    # #             logging.info("===留言-入口有消息未读数===")
    # #             # UnReadNum_case44 = entry_UnReadNum_case.text
    # #             UnReadNum_lists=self.multiman.messages_UnReadNum_lists()
    # #             assert UnReadNum_lists ==int(entry_UnReadNum_case)
    # #             logging.info("断言成功")
    # #         else:
    # #             logging.info("===留言-入口没有消息未读数，断言成功===")
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-列表及消息未读数')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-列表及消息未读数')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例24：留言-chamet团队')
    # # def test_homepage24(self):
    # #     logging.info("===留言-chamet团队===")
    # #     try:
    # #         entry_text=self.mandriver.find_element(*MultiMan.messages_system_entryText).text
    # #         self.mandriver.find_element(*MultiMan.messages_system_EntryAll).click()
    # #         time.sleep(2)
    # #         assert self.mandriver.find_element(*MultiMan.messages_system_title).text == 'Chamet团队'
    # #         if entry_text=='没有消息':
    # #             logging.info("===留言-chamet团队无消息===")
    # #             assert self.mandriver.find_element(*MultiMan.messages_system_emptyIcon)
    # #             assert self.mandriver.find_element(*MultiMan.messages_system_emptyText).text == '无消息'
    # #             self.mandriver.find_element(*MultiMan.messages_system_goback).click()
    # #         else:
    # #             logging.info("===留言-chamet团队有消息===")
    # #             assert self.mandriver.find_element(*MultiMan.messages_system_messagesContentAll)
    # #             # assert self.mandriver.find_elements(*MultiMan.messages_system_learnMoreText)
    # #             self.mandriver.find_element(*MultiMan.messages_system_goback).click()
    # #         logging.info("断言成功")
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-chamet团队')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-chamet团队')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例25：留言-chamet客服')
    # # def test_homepage25(self):
    # #     logging.info("===留言-chamet客服===")
    # #     try:
    # #         assert self.mandriver.find_element(*MultiMan.messages_customerService_entryText).text== '任何问题？联络我'
    # #         self.mandriver.find_element(*MultiMan.messages_customerService_EntryAll).click()
    # #         time.sleep(2)
    # #         assert self.mandriver.find_element(*MultiMan.messages_customerService_title).text == '在线客服'
    # #         assert self.mandriver.find_element(*MultiMan.messages_customerService_Container)
    # #         assert self.mandriver.find_element(*MultiMan.messages_customerService_problemChoice)
    # #         assert self.mandriver.find_element(*MultiMan.messages_customerService_InputText)
    # #         self.mandriver.find_element(*MultiMan.messages_customerService_goback).click()
    # #         logging.info("断言成功")
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-chamet客服')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-chamet客服')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例26：留言-陌生人留言消息及未读数')
    # # def test_homepage26(self):
    # #     logging.info("===留言-陌生人留言消息及未读数===")
    # #     try:
    # #         self.multiwoman.find_search_id()
    # #         time.sleep(3)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Stranger_entryUserAndText).text=='Mary33470557…啊bbb哦哦哦: hhhhh'
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_entryHeadPic).click()
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_title).text=='陌生人留言'
    # #         self.multiman.system_goback_key()
    # #         assert self.multiman.messages_Stranger_entryUnread_Ele()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_entryHeadPic).click()
    # #         assert self.multiman.messages_Stranger_userListUnread_Ele()
    # #         logging.info('===返回-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言消息及未读数')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言消息及未读数')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例27：留言-陌生人留言-陌生人列表')
    # # def test_homepage27(self):
    # #     logging.info("===留言-陌生人列表===")
    # #     try:
    # #         assert self.mandriver.find_element(*MultiMan.messages_Stranger_title).text=='陌生人留言'
    # #         first_userName=self.mandriver.find_elements(*MultiMan.messages_Stranger_UserNameList)[0].text
    # #         print(first_userName)
    # #         print(self.mandriver.find_elements(*MultiMan.messages_Stranger_UserEntryList))
    # #         assert self.mandriver.find_element(*MultiMan.messages_Stranger_UserUnread)
    # #         self.mandriver.find_elements(*MultiMan.messages_Stranger_UserNameList)[0].click()
    # #         assert first_userName == 'Mary33470557…啊bbb哦哦哦'
    # #         assert self.mandriver.find_element(*MultiMan.messages_Stranger_userTitleName).text==first_userName
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-陌生人列表')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-陌生人列表')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例28：留言-陌生人留言-一对一更多个人主页')
    # # def test_homepage28(self):
    # #     logging.info("===留言-陌生人留言-一对一更多个人主页===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
    # #         first_userName = self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverName).text
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverHeadFrame)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverNation)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverNationName)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverLanguage)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverLevel)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverFollowBtn)
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverHead).click()
    # #         assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == first_userName
    # #         self.multiman.system_goback_key()
    # #         logging.info('===返回-断言成功===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人主页')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人主页')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例29：留言-陌生人留言-一对一个人浮层送礼滑动')
    # # def test_homepage29(self):
    # #     logging.info("===留言-陌生人留言-一对一个人浮层送礼滑动===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverSendGiftBtn).click()
    # #         nowgift_list_text, newgift_list_text = self.multiman.usermessage_scroll_gift()
    # #         self.multiman.tap(576, 543)
    # #         assert nowgift_list_text != newgift_list_text
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人浮层送礼滑动')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人浮层送礼滑动')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例30：留言-陌生人留言-一对一更多个人浮层视频通话')
    # # def test_homepage30(self):
    # #     logging.info("===留言-陌生人留言-一对一更多个人浮层视频通话===")
    # #     try:
    # #         self.multiman.tap(826,1000)
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
    # #         video_butele = (MobileBy.ANDROID_UIAUTOMATOR, 'text("视频通话")')
    # #         video_but = self.mandriver.find_element(*video_butele)
    # #         logging.info('===拨打语言聊天===')
    # #         video_but.click()
    # #         self.multiman.Phone114_getPermission_checkPopover()
    # #         self.multiman.Phone114_getPermission_checkPopover()
    # #         self.multiman.Permission_114Phone_MediaPopoverConfirmBtnEle()
    # #         self.multiman.not_available_win()
    # #         logging.info('====一对一更多个人浮层视频通话-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
    # #         screen_name = self.multiwoman.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
    # #         screen_name = self.multiwoman.screenshot('留言-陌生人留言-一对一更多个人浮层视频通话')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例31：留言-陌生人留言-一对一输入框')
    # # def test_homepage31(self):
    # #     logging.info("===留言-陌生人留言-一对一输入框===")
    # #     try:
    # #         name_text = "hello123"
    # #         InputEdit_case=self.mandriver.find_element(*MultiMan.messages_Stranger_InputEdit)
    # #         InputEdit_case.send_keys(name_text)
    # #         InputEdit_case.click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_InputSendBtn).click()
    # #         time.sleep(3)
    # #         assert self.mandriver.find_elements(*MultiMan.messages_Stranger_TextInputContentText)[-1].text == name_text
    # #         assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
    # #         assert self.multiwoman.messages_Stranger_translateContentEle()
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-一对一输入框')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-一对一输入框')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例32：留言-陌生人留言-表情')
    # # def test_homepage32(self):
    # #     logging.info("===留言-陌生人留言-表情===")
    # #     try:
    # #         self.multiman.audience_usermessage_sendexpression(1)
    # #         expression = self.multiman.watch_selfsendexpression()
    # #         assert expression
    # #         logging.info('===断言成功，发送chamet表情成功===')
    # #         head_frame, expression = self.multiwoman.watch_othersendexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到chamet表情===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例33：留言-陌生人留言-搜索表情')
    # # def test_homepage33(self):
    # #     logging.info("===留言-陌生人留言-搜索表情===")
    # #     try:
    # #         self.multiman.audience_usermessage_sendexpression(0)
    # #         expression = self.multiman.watch_selfsendgooglexpression()
    # #         assert expression
    # #         logging.info('===断言成功，发送Facebook表情成功===')
    # #         head_frame, expression = self.multiwoman.watch_othersendgoogleexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到Facebook表情===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-搜索表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-搜索表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例34：留言-陌生人留言-更多翻译')
    # # def test_homepage34(self):
    # #     logging.info("===留言-陌生人留言-更多翻译===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_inputMoreBtn).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_TranslateBtn).click()
    # #         # usermessage_Voice_chat_toast = self.multiman.toast_message('翻译已关闭')
    # #         # assert usermessage_Voice_chat_toast.text == "翻译已关闭"
    # #         name_text = "hehehehe"
    # #         InputEdit_case = self.womandriver.find_element(*MultiWoman.messages_Stranger_InputEdit)
    # #         InputEdit_case.send_keys(name_text)
    # #         InputEdit_case.click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Stranger_InputSendBtn).click()
    # #         assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
    # #         time.sleep(3)
    # #         assert self.mandriver.find_elements(*MultiMan.messages_Stranger_TextInputContentText)[-1].text == name_text
    # #         assert self.multiman.messages_Stranger_translateContentEle()==False or self.multiman.messages_Stranger_translateContentEle()!=name_text
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-更多翻译')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-更多翻译')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例35：留言-陌生人留言-更多相册')
    # # def test_homepage35(self):
    # #     logging.info("===留言-陌生人留言-更多相册===")
    # #     try:
    # #         # self.mandriver.find_element(*MultiMan.messages_Stranger_inputMoreBtn).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_phonePictureBtn).click()
    # #         self.mandriver.find_elements(*MultiMan.messages_Stranger_phonePictureListSelect)[0].click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_phonePictureListConfirmBtn).click()
    # #         time.sleep(2)
    # #         photo = self.multiman.watch_selfsendexpression()
    # #         assert photo
    # #         logging.info('===断言成功，发送相册照片成功===')
    # #         head_frame, expression = self.multiwoman.watch_othersendexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到相册照片===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-更多相册')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-更多相册')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例36：留言-陌生人留言-更多相机')
    # # def test_homepage36(self):
    # #     logging.info("===留言-陌生人留言-更多相机===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_CameraBtn).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_114CameraTakeBtn).click()
    # #         time.sleep(5)
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_114CameraTakeDoneBtn).click()
    # #         photo = self.multiman.watch_selfsendexpression()
    # #         assert photo
    # #         logging.info('===断言成功，发送相机照片成功===')
    # #         head_frame, expression = self.multiwoman.watch_othersendexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到相机照片===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-更多相机')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-更多相机')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例37：留言-陌生人留言-更多视频聊天')
    # # def test_homepage37(self):
    # #     logging.info("===留言-陌生人留言-更多视频聊天===")
    # #     try:
    # #         self.multiman.usermessage_video_but()
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-更多视频聊天')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-更多视频聊天')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例38：留言-陌生人留言-送礼')
    # # def test_homepage38(self):
    # #     logging.info('===留言-陌生人留言-送礼===')
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_SendGiftBtn).click()
    # #         # global sendgift_assertcondition_4
    # #         sendgift_assertcondition_4 = self.multiman.audience_sendgift_bymessage("热门", "棒棒糖")
    # #         if sendgift_assertcondition_4 == 0:
    # #             pytest.skip("送礼方未送礼")
    # #         else:
    # #             last_text = self.multiman.get_usermessage_textcontent(-1)
    # #             assert '送出' in last_text
    # #             logging.info('===断言成功，送礼方成功发送礼物===')
    # #             head_frame, gift_content = self.multiwoman.watch_othersendgift()
    # #             assert head_frame
    # #             assert '送出' in gift_content
    # #             logging.info('===断言成功，收到私聊礼物===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info('===执行失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言-送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例39：留言-陌生人留言返回')
    # # def test_homepage39(self):
    # #     logging.info("===留言-陌生人留言返回===")
    # #     try:
    # #         self.multiman.find_element(*MultiMan.messages_Stranger_userGoback).click()
    # #         time.sleep(2)
    # #         assert self.multiman.messages_Stranger_userListUnread_Ele()==False
    # #         # self.mandriver.find_element(*MultiMan.messages_Stranger_goback).click()
    # #         # assert self.mandriver.find_element(*MultiMan.messages_title).text == '留言'
    # #         logging.info('===返回-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言返回')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-陌生人留言返回')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例40：留言-一对一列表-用户头像跳转')
    # # def test_homepage40(self):
    # #     logging.info("===留言-一对一列表-用户头像跳转===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_User_33470557Strange).click()
    # #         self.mandriver.find_element(*MultiMan.messages_User_StrangeTopName).click()
    # #         self.mandriver.find_element(*MultiMan.user_own_pageFollowBtn).click()
    # #         self.multiman.system_goback_key()
    # #         self.multiman.system_goback_key()
    # #         self.multiman.system_goback_key()
    # #         new_text = "NotStrange"
    # #         InputEdit_case = self.womandriver.find_element(*MultiWoman.messages_Stranger_InputEdit)
    # #         InputEdit_case.send_keys(new_text)
    # #         InputEdit_case.click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Stranger_InputSendBtn).click()
    # #         assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text==new_text
    # #         time.sleep(3)
    # #         assert self.mandriver.find_element(*MultiMan.messages_User_ListCountryIcon)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_User_ListLevelIcon)
    # #         assert self.mandriver.find_element(*MultiMan.messages_User_userContentText).text==new_text
    # #         assert self.multiman.messages_User_userContentUnreadDotEle()
    # #         expected_name1=self.mandriver.find_elements(*MultiMan.messages_User_EntryUserName)[0].text
    # #         self.mandriver.find_elements(*MultiMan.messages_User_EntryHead)[0].click()
    # #         expected_name2 = self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text
    # #         assert expected_name2==expected_name1
    # #         self.multiman.system_goback_key()
    # #         logging.info('===断言成功===')
    # #
    # #
    # #
    # #         # global user_haveOrNot
    # #         # User_EntryHeadEle_case=self.multiman.messages_User_EntryHeadEle()
    # #         # if User_EntryHeadEle_case!=False and len(User_EntryHeadEle_case)!=0:
    # #         #     user_haveOrNot=1
    # #         #     logging.info("===留言-有一对一消息，开始点击头像===")
    # #         #     OneUserEntryUserNameList_case=self.multiman.messages_User_EntryUserNameEle()
    # #         #     # print(type(OneUserEntryUserNameList))
    # #         #     if OneUserEntryUserNameList_case!=False:
    # #         #         logging.info('===有用户头像且获取到了昵称元素===')
    # #         #         expected_name1=OneUserEntryUserNameList_case.text
    # #         #         # print(OneUserEntryUserNameList_case.text)
    # #         #         self.mandriver.find_elements(*MultiMan.messages_User_EntryHead)[0].click()
    # #         #         expected_name2=self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text
    # #         #         # print(self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text)
    # #         #         assert expected_name2==expected_name1
    # #         #         self.multiman.system_goback_key()
    # #         #         assert self.mandriver.find_elements(*MultiMan.messages_User_EntryHead)
    # #         #     # else:
    # #         #     #     logging.info('===有用户头像但是没有获取到昵称元素===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一列表-用户头像跳转')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一列表-用户头像跳转')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例41：留言-一对一列表-列表跳转')
    # # def test_homepage41(self):
    # #     logging.info("===留言-一对一列表-列表跳转===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_User_33470557Strange).click()
    # #         assert  self.mandriver.find_element(*MultiMan.messages_User_StrangeTopName).text=='Mary33470557…啊bbb哦哦哦'
    # #         self.multiman.system_goback_key()
    # #         assert self.multiman.messages_User_userContentUnreadDotEle()==False
    # #         self.mandriver.find_element(*MultiMan.messages_User_33470557Strange).click()
    # #         logging.info('===断言成功===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一列表-列表跳转')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一列表-列表跳转')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例42：留言-一对一-更多个人主页')
    # # def test_homepage42(self):
    # #     logging.info("===留言-一对一-更多个人主页===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
    # #         first_userName = self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverName).text
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverHeadFrame)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverNation)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverNationName)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverLanguage)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverLevel)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverFollowBtn)
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverHead).click()
    # #         assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == first_userName
    # #         self.multiman.system_goback_key()
    # #         logging.info('===返回-断言成功===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多个人主页')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多个人主页')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例43：留言-一对一-更多个人浮层送礼滑动')
    # # def test_homepage43(self):
    # #     logging.info("===留言-一对一-更多个人浮层送礼滑动===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userHalfPagePopoverSendGiftBtn).click()
    # #         nowgift_list_text, newgift_list_text = self.multiman.usermessage_scroll_gift()
    # #         self.multiman.tap(576, 543)
    # #         print(nowgift_list_text)
    # #         print(newgift_list_text)
    # #         assert nowgift_list_text != newgift_list_text
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多个人浮层送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多个人浮层送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例44：留言-一对一-更多视频通话')
    # # def test_homepage44(self):
    # #     logging.info("===留言-一对一-更多视频通话===")
    # #     try:
    # #         self.multiman.tap(826,1000)
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_userMoreBtn).click()
    # #         video_butele = (MobileBy.ANDROID_UIAUTOMATOR, 'text("视频通话")')
    # #         video_but = self.mandriver.find_element(*video_butele)
    # #         logging.info('===拨打语言聊天===')
    # #         video_but.click()
    # #         self.multiman.Phone114_getPermission_checkPopover()
    # #         self.multiman.Phone114_getPermission_checkPopover()
    # #         self.multiman.Permission_114Phone_MediaPopoverConfirmBtnEle()
    # #         self.multiman.not_available_win()
    # #         logging.info('====一对一更多个人浮层视频通话-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多视频通话')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多视频通话')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例45：留言-一对一-输入框')
    # # def test_homepage45(self):
    # #     logging.info("===留言-一对一-输入框===")
    # #     try:
    # #         name_text = "userHello123"
    # #         InputEdit_case=self.mandriver.find_element(*MultiMan.messages_Stranger_InputEdit)
    # #         InputEdit_case.send_keys(name_text)
    # #         InputEdit_case.click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_InputSendBtn).click()
    # #         time.sleep(3)
    # #         assert self.mandriver.find_elements(*MultiMan.messages_Stranger_TextInputContentText)[-1].text == name_text
    # #         assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
    # #         assert self.multiwoman.messages_Stranger_translateContentEle()
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-输入框')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-输入框')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例46：留言-一对一-表情')
    # # def test_homepage46(self):
    # #     logging.info("===留言-一对一-表情===")
    # #     try:
    # #         self.multiman.audience_usermessage_sendexpression(1)
    # #         expression = self.multiman.watch_selfsendexpression()
    # #         assert expression
    # #         logging.info('===断言成功，发送chamet表情成功===')
    # #         head_frame, expression = self.multiwoman.watch_othersendexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到chamet表情===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例47：留言-一对一-搜索表情')
    # # def test_homepage47(self):
    # #     logging.info("===留言-一对一-搜索表情===")
    # #     try:
    # #         self.multiman.audience_usermessage_sendexpression(0)
    # #         expression = self.multiman.watch_selfsendgooglexpression()
    # #         assert expression
    # #         logging.info('===断言成功，发送Facebook表情成功===')
    # #         head_frame, expression = self.multiwoman.watch_othersendgoogleexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到Facebook表情===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-搜索表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-搜索表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例48：留言-一对一-更多翻译')
    # # def test_homepage48(self):
    # #     logging.info("===留言-一对一-更多翻译===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_inputMoreBtn).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_TranslateBtn).click()
    # #         # usermessage_Voice_chat_toast = self.multiman.toast_message('翻译已开启')
    # #         # assert usermessage_Voice_chat_toast.text == "翻译已开启"
    # #         name_text = "userTranslate"
    # #         InputEdit_case = self.womandriver.find_element(*MultiWoman.messages_Stranger_InputEdit)
    # #         InputEdit_case.send_keys(name_text)
    # #         InputEdit_case.click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Stranger_InputSendBtn).click()
    # #         assert self.womandriver.find_elements(*MultiWoman.messages_Stranger_TextInputContentText)[-1].text == name_text
    # #         time.sleep(3)
    # #         assert self.mandriver.find_elements(*MultiMan.messages_Stranger_TextInputContentText)[-1].text == name_text
    # #         assert self.multiman.messages_Stranger_translateContentEle()!=False
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多翻译')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多翻译')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例49：留言-一对一-更多相册')
    # # def test_homepage49(self):
    # #     logging.info("===留言-一对一-更多相册===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_phonePictureBtn).click()
    # #         self.mandriver.find_elements(*MultiMan.messages_Stranger_phonePictureListSelect)[0].click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_phonePictureListConfirmBtn).click()
    # #         time.sleep(2)
    # #         photo = self.multiman.watch_selfsendexpression()
    # #         assert photo
    # #         logging.info('===断言成功，发送相册照片成功===')
    # #         head_frame, expression = self.multiwoman.watch_othersendexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到相册照片===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多相册')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多相册')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例50：留言-一对一-更多相机')
    # # def test_homepage50(self):
    # #     logging.info("===留言-一对一-更多相机===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_CameraBtn).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_114CameraTakeBtn).click()
    # #         time.sleep(5)
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_114CameraTakeDoneBtn).click()
    # #         photo = self.multiman.watch_selfsendexpression()
    # #         assert photo
    # #         logging.info('===断言成功，发送相机照片成功===')
    # #         head_frame, expression = self.multiwoman.watch_othersendexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到相机照片===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多相机')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多相机')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例51：留言-一对一-更多视频聊天')
    # # def test_homepage51(self):
    # #     logging.info("===留言-一对一-更多视频聊天===")
    # #     try:
    # #         self.multiman.usermessage_video_but()
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多视频聊天')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-更多视频聊天')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例52：留言-一对一-送礼')
    # # def test_homepage52(self):
    # #     logging.info("===留言-一对一-送礼===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Stranger_SendGiftBtn).click()
    # #         global sendgift_assertcondition_5
    # #         sendgift_assertcondition_5 = self.multiman.audience_sendgift_bymessage("热门", "棒棒糖")
    # #         if sendgift_assertcondition_5 == 0:
    # #             pytest.skip("送礼方未送礼")
    # #         else:
    # #             last_text = self.multiman.get_usermessage_textcontent(-1)
    # #             assert '送出' in last_text
    # #             logging.info('===断言成功，送礼方成功发送礼物===')
    # #             head_frame, gift_content = self.multiwoman.watch_othersendgift()
    # #             assert head_frame
    # #             assert '送出' in gift_content
    # #             logging.info('===断言成功，收到私聊礼物===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例53：留言-一对一-返回')
    # # def test_homepage53(self):
    # #     logging.info("===留言-一对一-返回===")
    # #     try:
    # #         self.multiman.find_element(*MultiMan.messages_Stranger_userGoback).click()
    # #         time.sleep(2)
    # #         assert self.mandriver.find_element(*MultiMan.messages_title).text == '留言'
    # #         logging.info("断言成功")
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-一对一-送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-一对一-送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例54：留言-群聊消息显示')
    # # def test_homepage54(self):
    # #     logging.info("===留言-群聊消息显示===")
    # #     try:
    # #         self.womandriver.find_elements(*MultiWoman.messages_Stranger_UserHeadList)[-1].click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Stranger_userHalfPagePopoverHead).click()
    # #         self.multiwoman.swipe(506, 1832, 506, 400)
    # #         self.multiwoman.swipe(506, 1832, 506, 400)
    # #         self.multiwoman.swipe(506, 1832, 506, 400)
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_pageGroupName).click()
    # #         group_text='gHello'
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_inputBtn).send_keys(group_text)
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_inputBtn).click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_inputSendBtn).click()
    # #         logging.info('===女生发言，准备成功===')
    # #         self.multiwoman.system_goback_key()
    # #         self.multiwoman.system_goback_key()
    # #         self.multiwoman.system_goback_key()
    # #         self.multiwoman.system_goback_key()
    # #         # 加点击
    # #         self.womandriver.find_element(*MultiWoman.messages_entry_All).click()
    # #         self.womandriver.find_elements(*MultiWoman.messages_Group_entryGroupName)[0].click()
    # #         time.sleep(3)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_ContentText).text.find(group_text)>=0
    # #         time.sleep(3)
    # #         # assert self.multiman.messages_User_userContentUnreadDotEle()
    # #         global groupName_text, groupCount_text
    # #         groupName_text = self.mandriver.find_element(*MultiMan.messages_Group_entryGroupName).text
    # #         groupCount_text = self.mandriver.find_element(*MultiMan.messages_Group_entryGroupCount).text
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_entryGroupName)[0].click()
    # #         time.sleep(2)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_titleGroupName).text == groupName_text
    # #         assert '\x20''{}'.format(
    # #         self.mandriver.find_element(*MultiMan.messages_Group_titleGroupCount).text) == groupCount_text
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息显示')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息显示')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例55：留言-群聊消息未读数')
    # # def test_homepage55(self):
    # #     logging.info("===留言-群聊消息未读数===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_goback).click()
    # #         assert self.multiman.messages_User_userContentUnreadDotEle()==False
    # #         self.mandriver.find_element(*MultiMan.messages_Group_entryGroupHead).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_titleGroupName).text == groupName_text
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息未读数')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息未读数')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例56：留言-群聊消息-发言')
    # # def test_homepage56(self):
    # #     logging.info("===留言-群聊消息-发言===")
    # #     try:
    # #         name_text ="vndsiiovnhif VFSHTR"
    # #         self.mandriver.find_element(*MultiMan.messages_Group_inputBtn).send_keys(name_text)
    # #         self.mandriver.find_element(*MultiMan.messages_Group_inputBtn).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_inputSendBtn).click()
    # #         time.sleep(1)
    # #         assert self.mandriver.find_elements(*MultiMan.messages_Group_TextInputContent)[-1].text==name_text
    # #         assert self.womandriver.find_elements(*MultiWoman.messages_Group_TextInputContent)[-1].text == name_text
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-发言')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-发言')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例57：留言-群聊消息-表情')
    # # def test_homepage57(self):
    # #     logging.info("===留言-群聊消息-表情===")
    # #     try:
    # #         self.multiman.audience_groupmessage_sendexpression(1)
    # #         expression = self.multiman.watchgroup_selfsendexpression()
    # #         assert expression
    # #         logging.info('===断言成功，成功发送chamet表情===')
    # #         head_frame, expression = self.multiwoman.watchgroup_othersendexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，收到chamet表情消息===')
    # #
    # #     except AssertionError as e:
    # #             logging.info('===断言失败===')
    # #             screen_name = self.multiman.screenshot('留言-群聊消息-表情')
    # #             logging.info(f'截图成功，图片为{screen_name}')
    # #             raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例58：留言-群聊消息-搜索表情')
    # # def test_homepage58(self):
    # #     logging.info("===留言-群聊消息-搜索表情===")
    # #     try:
    # #         self.multiman.groupmessage_send_expression(0)
    # #         expression = self.multiman.watchgroup_selfsendgooglexpression()
    # #         assert expression
    # #         logging.info('===断言成功，成功发送google表情===')
    # #         user_name, expression = self.multiwoman.watchgroup_othersendgoogleexpression()
    # #         assert user_name
    # #         assert expression
    # #         logging.info('===断言成功，收到google表情消息===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-搜索表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-搜索表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例59：留言-群聊消息-语音消息')
    # # def test_homepage59(self):
    # #     logging.info("===留言-群聊消息-语音消息===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_voiceBtn).click()
    # #         self.multiman.Phone114_getPermission_checkPopover()
    # #         self.multiman.Permission_114Phone_MediaPopoverConfirmBtnEle()
    # #         message_group_sendVoicePress = self.mandriver.find_element(*MultiMan.messages_Group_voiceAddBtn)
    # #         self.multiman.longPress_action(message_group_sendVoicePress)
    # #         assert self.mandriver.find_elements(*MultiMan.messages_Group_TextVoiceIcon)
    # #         assert self.womandriver.find_elements(*MultiWoman.messages_Group_TextVoiceIcon)
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-语音消息')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-语音消息')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例60：留言-群聊消息-图片信息')
    # # def test_homepage60(self):
    # #     logging.info("===留言-群聊消息-图片信息===")
    # #     try:
    # #         self.multiman.groupmessage_send_photo(2)
    # #         expression = self.multiman.watchgroup_selfsendexpression()
    # #         assert expression
    # #         logging.info('===断言成功，成功发送相册图片===')
    # #         head_frame, expression = self.multiwoman.watchgroup_othersendexpression()
    # #         assert head_frame
    # #         assert expression
    # #         logging.info('===断言成功，成功收到相册图片===')
    # #
    # #         # self.mandriver.find_element(*MultiMan.messages_Group_pictureMoreBtn).click()
    # #         # self.mandriver.find_element(*MultiMan.messages_Group_pictureChooseBtn).click()
    # #         # time.sleep(2)
    # #         # self.multiman.Permission_114Phone_PopoverConfirmOnlyBtn()
    # #         # # assert self.mandriver.find_elements(*MultiMan.messages_Group_pictureChooseList)
    # #         # self.mandriver.find_elements(*MultiMan.messages_Group_pictureChooseList)[0].click()
    # #         # assert len(self.mandriver.find_elements(*MultiMan.messages_Group_TextImageList)) >= 1
    # #         # logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-图片信息')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-图片信息')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例：61留言-群聊消息-上麦')
    # # def test_homepage61(self):
    # #     logging.info("===留言-群聊消息-上麦===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_upMicBtn).click()
    # #         self.multiman.Phone114_getPermission_checkPopover()
    # #         self.multiman.Permission_114Phone_MediaPopoverConfirmBtnEle()
    # #         # time.sleep(1)
    # #         # assert self.mandriver.find_elements(*MultiMan.messages_Group_upMic10All)
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_upMicBtn).click()
    # #         self.multiwoman.get_permission_checkPopover()
    # #         self.multiwoman.get_permission_checkPopover()
    # #         upMicUserHeadListNum=len(self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList))
    # #         assert upMicUserHeadListNum>=2
    # #         logging.info("===上麦已成功===")
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-上麦')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-上麦')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例62：留言-群聊消息-上麦用户头像-查看自己')
    # # def test_homepage62(self):
    # #     logging.info("===留言-群聊消息-上麦用户头像-查看自己===")
    # #     try:
    # #         time.sleep(2)
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[0].click()
    # #         global man_upMicName,woman_upMicName
    # #         man_upMicName=self.mandriver.find_element(*MultiMan.messages_Group_OneSelfHalfPagePopoverName).text
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHeadFrame)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverLev)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverCouName)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverLan)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_OneSelfHalfPagePopoverMomentList)
    # #         self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHead).click()
    # #         assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == man_upMicName
    # #         self.multiman.system_goback_key()
    # #         logging.info("===男群主上麦，查看自己，断言成功===")
    # #         self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList)[1].click()
    # #         woman_upMicName = self.womandriver.find_element(*MultiWoman.messages_Group_OneSelfHalfPagePopoverName).text
    # #         # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverHeadFrame)
    # #         # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverLev)
    # #         # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverCouName)
    # #         # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverLan)
    # #         # assert self.womandriver.find_element(*MultiMan.messages_Group_OneSelfHalfPagePopoverMomentList)
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverHead).click()
    # #         assert self.womandriver.find_element(*MultiWoman.user_own_pagePersonalName).text == woman_upMicName
    # #         self.multiwoman.system_goback_key()
    # #         logging.info("===女成员上麦，查看自己，断言成功===")
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-查看自己')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-查看自己')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例63：留言-群聊消息-麦位表情')
    # # def test_homepage63(self):
    # #     logging.info("===留言-群聊消息-麦位表情===")
    # #     try:
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[0].click()
    # #         time.sleep(3)
    # #         userHalfPagePopoverImgList_case1=self.mandriver.find_elements(*MultiMan.messages_Group_userHalfPagePopoverImgList)
    # #         userHalfPagePopoverImgList_case1[0].click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_upMicBtn)
    # #         logging.info("===男群主麦位表情，断言成功===")
    # #         self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList)[1].click()
    # #         time.sleep(3)
    # #         userHalfPagePopoverImgList_case2 = self.womandriver.find_elements(*MultiWoman.messages_Group_userHalfPagePopoverImgList)
    # #         userHalfPagePopoverImgList_case2[0].click()
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_upMicBtn)
    # #         logging.info("===女成员麦位表情，断言成功===")
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-麦位表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-麦位表情')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # #
    # #
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例64：留言-群聊消息-上麦用户头像-查看他人')
    # # def test_homepage64(self):
    # #     logging.info("===留言-群聊消息-上麦用户头像-查看他人===")
    # #     try:
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[1].click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverName).text==woman_upMicName
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHeadFrame)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverLev)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverCouName)
    # #         # assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverLan)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverAtHer)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverReport)
    # #         # assert self.multiman.messages_Group_userHalfPagePopoverMomentListEle() ==False
    # #         self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHead).click()
    # #         assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == woman_upMicName
    # #         self.multiman.system_goback_key()
    # #         logging.info("===男群主上麦，查看他人，断言成功===")
    # #         self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList)[0].click()
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverName).text == man_upMicName
    # #         # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverHeadFrame)
    # #         # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverLev)
    # #         # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverCouName)
    # #         # assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverLan)
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverAtHer)
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverReport)
    # #         # assert self.multiwoman.messages_Group_userHalfPagePopoverMomentListEle() == False
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverHead).click()
    # #         assert self.womandriver.find_element(*MultiWoman.user_own_pagePersonalName).text == man_upMicName
    # #         self.multiwoman.system_goback_key()
    # #         logging.info("===女成员上麦，查看他人，断言成功===")
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-查看他人')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-查看他人')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例65：留言-群聊消息-上麦用户头像-他人送礼和通话')
    # # def test_homepage65(self):
    # #     logging.info("===留言-群聊消息-上麦用户头像-他人送礼和通话===")
    # #     try:
    # #         time.sleep(2)
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[1].click()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverGifBtn).click()
    # #         assert self.mandriver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("热门")')
    # #         self.multiman.tap (751,925)
    # #         logging.info("===男群主上麦给他人送礼，断言成功===")
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[1].click()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverCallBtn).click()
    # #         if self.multiman.messages_Group_CallMoneyNotEnoughEle():
    # #             self.multiman.tap(941, 2027)
    # #         else:
    # #             time.sleep(5)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_upMicBtn)
    # #         logging.info("===男群主上麦给他人通话，断言成功===")
    # #         self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList)[0].click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverGifBtn).click()
    # #         assert self.womandriver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("热门")')
    # #         self.multiwoman.tap(906, 798)
    # #         logging.info("===女成员上麦上麦给他人送礼，断言成功===")
    # #         self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList)[1].click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_userHalfPagePopoverCallBtn).click()
    # #         if self.multiwoman.messages_Group_CallMoneyNotEnoughEle():
    # #             self.multiwoman.tap(892, 2027)
    # #         else:
    # #             time.sleep(5)
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_upMicBtn)
    # #         logging.info("===女成员上麦上麦给他人通话，断言成功===")
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-他人送礼和通话')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-上麦用户头像-他人送礼和通话')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例66：留言-群聊消息-下麦')
    # # def test_homepage66(self):
    # #     logging.info("===留言-群聊消息-下麦===")
    # #     try:
    # #
    # #         upMicLen_num1=len(self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList))
    # #         messages_Group_upMicBtn_on=self.mandriver.find_element(*MultiMan.messages_Group_upMicBtn)
    # #         messages_Group_upMicBtn_on.click()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_upMicTurnOffBtn).click()
    # #         assert upMicLen_num1 > len(self.mandriver.find_elements(*MultiMan.messages_Group_upMicUserHeadList))
    # #         upMicLen_num2 = len(self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList))
    # #         messages_Group_upMicBtn_on = self.womandriver.find_element(*MultiWoman.messages_Group_upMicBtn)
    # #         messages_Group_upMicBtn_on.click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_upMicTurnOffBtn).click()
    # #         if upMicLen_num2==1:
    # #             assert self.womandriver.find_element(*MultiWoman.messages_Group_BannerListLast)
    # #         else:
    # #             assert upMicLen_num2 > len(self.womandriver.find_elements(*MultiWoman.messages_Group_upMicUserHeadList))
    # #         logging.info('===下麦-断言成功===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-下麦')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-下麦')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例67：留言-群聊消息-钻石包发送-领取')
    # # def test_homepage67(self):
    # #     logging.info("===留言-群聊消息-钻石包发送-领取===")
    # #     try:
    # #         self.multiman.audience_send_diamondenvelope(2, 200)
    # #         envelope = self.multiman.messageregion_getenvelope()
    # #         assert envelope
    # #         logging.info('===断言成功，成功发送钻石包===')
    # #         self.multiwoman.audience_get_diamondenvelope()
    # #         user_head = self.multiwoman.getenvelope_userhead()
    # #         assert user_head
    # #         logging.info('===断言成功,女生成功领取钻石包===')
    # #         self.multiman.get_diamond_envelope()
    # #         user_head = self.multiman.getenvelope_userhead()
    # #         assert user_head
    # #         logging.info('===断言成功，男生成功领取钻石包===')
    # #         thank_ele = self.multiwoman.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_thanking_1")
    # #         thank_text = thank_ele.text
    # #         thank_ele.click()
    # #         self.multiman.tap(335,1903)
    # #         audience_messageregion = self.multiman.groupmessage_text(-1)
    # #         assert thank_text in audience_messageregion
    # #         logging.info('===断言成功,男生成功收到主播发送的感谢语===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-钻石包发送-领取')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-钻石包发送-领取')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例68：留言-群聊消息-游戏浮层')
    # # def test_homepage68(self):
    # #     logging.info("===留言-群聊消息-游戏浮层===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_GameBtn).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer1).text=='Chamet赛车'
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer2).text=='顶级赛车'
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer3).text=='幸运盒子'
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer4).text=='幸运转盘'
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer5).text=='幸运数字'
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_GameLayer6).text=='幸运抽奖机'
    # #         self.multiman.tap(584,1804)
    # #         logging.info('====游戏浮层-断言成功===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-游戏浮层')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-游戏浮层')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例69：留言-群聊消息-礼物送礼')
    # # def test_homepage69(self):
    # #     logging.info("===留言-群聊消息-礼物送礼===")
    # #     try:
    # #         self.multiman.group_opengiftwin()
    # #         global sendgift_assertcondition_6
    # #         sendgift_assertcondition_6 = self.multiman.audience_groupmessage_sendgift("热门", "幸运之吻")
    # #         if sendgift_assertcondition_6 == 0:
    # #             pytest.skip("观众端未送礼")
    # #         gift_text = self.multiman.watchgroup_selfsendgift()
    # #         assert "送出" in gift_text
    # #         logging.info('===断言成功，观众群聊页面成功送礼===')
    # #         if sendgift_assertcondition_6 == 0:
    # #             pytest.skip("观众端未送礼")
    # #         user_name, gift_text = self.multiwoman.watchgroup_othersendgift()
    # #         assert user_name
    # #         assert "送出" in gift_text
    # #         logging.info('===断言成功，主播收到送礼消息===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-礼物送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-礼物送礼')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例70：留言-群聊消息-顶部banner入口')
    # # def test_homepage70(self):
    # #     logging.info("===留言-群聊消息-顶部banner入口===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_BannerListLast).click()
    # #         time.sleep(8)
    # #         assert self.mandriver.find_elements(*MultiMan.messages_Group_BannerListLayer)
    # #         self.multiman.tap(577, 617)
    # #         self.mandriver.find_element(*MultiMan.messages_Group_BannerListPackupBtn).click()
    # #         time.sleep(3)
    # #         self.mandriver.find_element(*MultiMan.messages_Group_BannerListSmallBtn).click()
    # #         logging.info('====顶部banner入口收起成功===')
    # #         assert self.mandriver.find_elements(*MultiMan.messages_Group_BannerList)
    # #         logging.info('====顶部banner入口展开成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-顶部banner入口')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-顶部banner入口')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例71：留言-群聊消息-更多按钮')
    # # def test_homepage71(self):
    # #     logging.info("===留言-群聊消息-更多按钮===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_detailMoreBtn).click()
    # #         HeadList_test1=self.mandriver.find_elements(*MultiMan.messages_Group_MoreUserHeadList)
    # #         group_userlist1 = len(HeadList_test1)
    # #         HeadList_test1[0].click()
    # #         logging.info('===更多跳转详情页成功===')
    # #         group_UserName=self.multiman.userHalfPagePopoverNameOrOneselfEle()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_userHalfPagePopoverHead).click()
    # #         assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text==group_UserName
    # #         self.multiman.system_goback_key()
    # #         logging.info('===头像跳转个人主页成功===')
    # #         if self.multiman.groupCount_number(groupCount_text)<=20:
    # #             assert ' (''{}'')'.format(group_userlist1)==groupCount_text
    # #         else:
    # #             assert len(self.mandriver.find_elements(*MultiMan.messages_Group_MoreUserHeadList))==20
    # #         logging.info('===用户数据正常===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-更多按钮')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-更多按钮')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例72：留言-群聊消息-更多-动态-更多详情页')
    # # def test_homepage72(self):
    # #     logging.info("===留言-群聊消息-更多-动态-更多详情页===")
    # #     try:
    # #         if self.mandriver.find_elements(*MultiMan.messages_Group_MoreUserHeadList):
    # #             logging.info("===留言-有群聊消息，在群聊页面===")
    # #             MoreMomentAllEle=self.multiman.messages_Group_MoreMomentAllEle()
    # #             global moment_ele
    # #             if MoreMomentAllEle!=False and len(MoreMomentAllEle)!=0:
    # #                 moment_ele=1
    # #                 logging.info('===有动态元素===')
    # #                 self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentPicLast).click()
    # #                 assert self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentMoreTitle).text=='动态'
    # #                 assert self.mandriver.find_elements(*MultiMan.messages_Group_MoreMomentMoreSendBtn)
    # #                 self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentMoreGoback).click()
    # #                 # assert self.l.messages_Group_MoreMomentAllEle()
    # #                 logging.info('===更多跳转详情页成功===')
    # #             else:
    # #                 moment_ele = 0
    # #                 logging.info('===没有动态元素===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-更多-动态-更多详情页')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-更多-动态-更多详情页')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例73：留言-群聊消息-更多-动态-大图模式')
    # # def test_homepage73(self):
    # #     logging.info("===留言-群聊消息-更多-动态-大图模式===")
    # #     try:
    # #         if moment_ele==0:
    # #             logging.info('===没有动态元素===')
    # #         else:
    # #             logging.info('===有动态元素===')
    # #             print(self.multiman.messages_Group_MoreMomentPicFrontEle())
    # #             group_MoreMomentPicFrontEle_case=self.multiman.messages_Group_MoreMomentPicFrontEle()
    # #             if group_MoreMomentPicFrontEle_case==False or len(group_MoreMomentPicFrontEle_case)==1:
    # #                 logging.info('===只有一个动态===')
    # #             else:
    # #                 logging.info('===多个动态===')
    # #                 self.mandriver.find_elements(*MultiMan.messages_Group_MoreMomentPicFront)[0].click()
    # #                 assert self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentMaxZanBtn)
    # #                 self.multiman.swipe(531,1776,531,900)
    # #                 assert self.mandriver.find_element(*MultiMan.messages_Group_MoreMomentMaxZanBtn)
    # #                 self.multiman.system_goback_key()
    # #                 # assert self.l.messages_Group_MoreMomentAllEle()
    # #                 logging.info('===大图模式-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-更多-动态-大图模式')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-更多-动态-大图模式')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例74：留言-群聊消息-群组类型')
    # # def test_homepage74(self):
    # #     logging.info("===留言-群聊消息-群组类型===")
    # #     try:
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_detailMoreBtn).click()
    # #         time.sleep(3)
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupType).text=='普通群组'
    # #         time.sleep(2)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupType).text == '普通群组'
    # #         logging.info('===返回-断言成功===')
    # #
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-群组类型')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-群组类型')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例75：留言-群聊消息-群组封面')
    # # def test_homepage75(self):
    # #     logging.info("===留言-群聊消息-群组封面===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupHeadPic).click()
    # #         assert self.multiman.messages_Group_MoreGroupHeadPic_picStatusEle()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupHeadPic_pic).click()
    # #         assert self.multiman.messages_Group_MoreGroupHeadPic_ChangeEle()
    # #         self.multiman.tap(389,1583)
    # #         self.multiman.system_goback_key()
    # #         logging.info('===群主-断言成功===')
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupHeadPic).click()
    # #         assert self.multiwoman.messages_Group_MoreGroupHeadPic_picStatusEle()==False
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupHeadPic_pic).click()
    # #         assert self.multiwoman.messages_Group_MoreGroupHeadPic_ChangeEle()==False
    # #         self.multiwoman.system_goback_key()
    # #         logging.info('===群成员-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-群组封面')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-群组封面')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例76：留言-群聊消息-群组名')
    # # def test_homepage76(self):
    # #     logging.info("===留言-群聊消息-群组名===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSet).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSetContent).text==groupName_text
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSetContentGoback).click()
    # #         logging.info('===群主-断言成功===')
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupNameSet).click()
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupNameSet).text == groupName_text
    # #         logging.info('===群成员-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-群组名')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-群组名')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例77：留言-群聊消息-群组介绍')
    # # def test_homepage77(self):
    # #     logging.info("===留言-群聊消息-群组介绍===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntro).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroContent).clear()
    # #         group_intro='hhhhhhh7'
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroContent).send_keys(group_intro)
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroContent).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupNameSetContentSave).click()
    # #         time.sleep(2)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroDes).text==group_intro
    # #         logging.info('===群主-断言成功===')
    # #         self.multiwoman.system_goback_key()
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_detailMoreBtn).click()
    # #         time.sleep(2)
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupIntroDes).text == group_intro
    # #         logging.info('===群成员-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-群组介绍')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-群组介绍')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例78：留言-群聊消息-管理群组')
    # # def test_homepage78(self):
    # #     logging.info("===留言-群聊消息-管理群组===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupMana).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaVisConText)
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaPriConText)
    # #         logging.info("===模式-断言完成===")
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaNextHost).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaNextHostTitle).text=='选择新群主'
    # #         self.multiman.system_goback_key()
    # #         logging.info("===群组所有权转让-断言完成===")
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaAdmin).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaNextHostTitle).text =='群管理员'
    # #         self.multiman.system_goback_key()
    # #         logging.info("===群管理员-断言完成===")
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisband).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisPopCon).text == '解散后，所有成员（包括群主）将被移出组'
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisPopCancel).click()
    # #         logging.info("===解散群组-断言完成===")
    # #         logging.info("===群主-断言完成===")
    # #         assert self.multiwoman.messages_Group_MoreGroupManaEle()==False
    # #         logging.info('===群成员-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-管理群组')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-管理群组')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例79：留言-群聊消息-删除并离开')
    # # def test_homepage79(self):
    # #     logging.info("===留言-群聊消息-删除并离开===")
    # #     try:
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDeAndLeave).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisPopCon).text == '退出此群组后没有群组消息'
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupManaDisPopCancel).click()
    # #         logging.info("===群主-断言完成===")
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupManaDeAndLeave).click()
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupManaDisPopCon).text == '退出此群组后没有群组消息'
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupManaDisPopCancel).click()
    # #         logging.info('===群成员-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-删除并离开')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-删除并离开')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例80：留言-群聊消息-添加成员')
    # # def test_homepage80(self):
    # #     logging.info("===留言-群聊消息-添加成员===")
    # #     try:
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_MoreGroupAddBtn)[0].click()
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_MoreGroupAddIcon)[0].click()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupRemovePerSave).click()
    # #         assert  self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupTitle).text == groupName_text
    # #         logging.info('===断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-添加成员')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-添加成员')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例81：留言-群聊消息-移除成员')
    # # def test_homepage81(self):
    # #     logging.info("===留言-群聊消息-移除成员===")
    # #     try:
    # #         self.mandriver.find_elements(*MultiMan.messages_Group_MoreGroupAddBtn)[-1].click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupIntroTitle).text == '移除成员'
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupRemovePer).click()
    # #         self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupRemovePerSave).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_MoreGroupRemoveTips).text == '“你移除了”Mary33470557…啊bb...“来自群组”'
    # #         self.multiman.system_goback_key()
    # #         logging.info("===群主-断言完成===")
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_MoreGroupRemovePTips)
    # #         self.multiwoman.system_goback_key()
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_pageGroupName).click()
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_joinBtn).click()
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_joinPopCon).text=='等待群主同意'
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_joinPopConfirm).click()
    # #         self.multiwoman.system_goback_key()
    # #         time.sleep(8)
    # #         self.mandriver.find_element(*MultiMan.messages_Group_Notification).click()
    # #         assert self.mandriver.find_element(*MultiMan.messages_Group_NotiJoinCon).text =='Mary33470557…啊bb... 申请加入群组: 今日也莫人陪我'
    # #         self.mandriver.find_element(*MultiMan.messages_Group_joinAgree).click()
    # #         time.sleep(2)
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_pageGroupName).click()
    # #         assert self.womandriver.find_element(*MultiWoman.messages_Group_joinInTips)
    # #         logging.info('===群成员-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-移除成员')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-移除成员')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #
    # #
    # #
    # # @allure.story('留言')
    # # # @pytest.mark.skip(reason="本次不执行")
    # # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.title('用例82：留言-群聊消息-返回')
    # # def test_homepage82(self):
    # #     logging.info("===留言-群聊消息-返回===")
    # #     try:
    # #         self.multiman.system_goback_key()
    # #         assert self.mandriver.find_element(*MultiMan.messages_title).text == '留言'
    # #         self.womandriver.find_element(*MultiWoman.messages_Group_goback).click()
    # #         assert self.womandriver.find_element(*MultiWoman.messages_title).text=='留言'
    # #         self.multiman.system_goback_key()
    # #         self.multiwoman.system_goback_key()
    # #         logging.info('===返回-断言成功===')
    # #
    # #     except AssertionError as e:
    # #         logging.info('===断言失败===')
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-返回')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    # #     except:
    # #         logging.info("===执行失败===")
    # #         screen_name = self.multiman.screenshot('留言-群聊消息-返回')
    # #         logging.info(f'截图成功，图片为{screen_name}')
    # #         raise
    #
    #
    #
    #
    #
    #
    #












    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例83-84：我的等级-男-外部显示和内部跳转')
    def test_homepage83(self):
        logging.info("===我的等级-我的等级外部显示和内部跳转===")
        self.multiman.tab_Mine_Btn()
        try:
            if self.multiman.my_vipLevel_UpLevelImgManAllEle():
                logging.error("===我的等级外部显示不为0===")
                man_now_level=self.mandriver.find_element(*MultiMan.my_vipLevel_UpLevelImgManLevel).text
                print(man_now_level)
                self.multiman.vip_Level_right_click()
                self.multiman.native_to_h5()
                level_top=self.multiman.vipLevel_level_value()
                assert level_top==man_now_level
                logging.error("===断言成功===")

            else:
                logging.info("===我的等外部显示为0===")
                assert self.mandriver.find_element(*MultiMan.my_vipLevel_NowLevelImgZeroAndWoman).text=='Lv0'
                man_now_diamond = self.mandriver.find_element(*MultiMan.myBalance_entryDiamondManNum).text
                assert int(self.multiman.string_find_num(man_now_diamond))<=int(2000)
                self.multiman.vip_Level_right_click()
                assert self.multiman.vipLevel_level_value =='Lv0'
                logging.error("===断言成功===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的等级外部显示和内部跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的等级外部显示和内部跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例85：我的等级-男-等级tab栏')
    def test_homepage85(self):
        logging.info("===我的等级-男-等级tab栏===")
        try:
            vipLevel_level_value = self.multiman.vipLevel_level_value()
            vipLevel_levelLeft_value=self.multiman.vipLevel_levelLeft_value()
            if vipLevel_level_value=='Lv0' and vipLevel_levelLeft_value=='Lv0':
                logging.info('===等级为Lv0===')
                assert self.mandriver.find_element(*MultiMan.level_tabSelectedManCss).text == 'Lv1'
                logging.info('===开始断言等级特权弹窗===')
                self.mandriver.find_element(*MultiMan.level_privilege_DetailAllCss).click()
                assert self.mandriver.find_element(*MultiMan.level_privilege_detailPopoverHeadFrameCss).text == '进场气泡'
                # self.multiman.swipe(780,1000,348,1000)
                # assert self.mandriver.find_element(*MultiMan.level_privilege_detailPopoverHeadFrameCss).text  == '头像框'
                self.multiman.tap(972, 1830)
                logging.info('===开始断言等级特权tab切换===')
                self.mandriver.find_elements(*MultiMan.level_tabItem)[1].click()
                assert len(self.mandriver.find_elements(*MultiMan.level_privilege_DetailList)) == 2
                # assert self.mandriver.find_element(*MultiMan.level_tabSelectedManCss).text == 'Lv2'
                logging.info('===断言成功===')
            else:
                logging.info('===等级不为Lv0，开始断言等级与横条等级内容===')
                print(vipLevel_level_value)
                assert self.mandriver.find_element(*MultiMan.level_tabSelectedManCss).text == vipLevel_levelLeft_value
                logging.info('===开始断言等级特权弹窗===')
                self.mandriver.find_element(*MultiMan.level_privilege_DetailAllCss).click()
                assert self.mandriver.find_element(*MultiMan.level_privilege_detailPopoverHeadFrameCss).text == '进场气泡'
                time.sleep(3)
                # print(self.mandriver.window_handles)
                # print(len(self.mandriver.window_handles))
                # self.multiman.swipe(780,1000,348,1000)
                # self.mandriver.swipe(348,1000,780,1000,2000)
                # assert self.mandriver.find_element(*MultiMan.level_privilege_detailPopoverHeadFrameCss).text == '头像框'
                self.multiman.tap(972, 1830)
                logging.info('===开始断言等级特权tab切换===')
                # self.mandriver.find_elements(*MultiMan.level_tabItem)[0].click()
                self.mandriver.find_elements(*MultiMan.level_tabItem)[0].click()
                time.sleep(1)
                assert len(self.mandriver.find_elements(*MultiMan.level_privilege_DetailList))==2
                logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的等级-男-等级tab栏')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的等级-男-等级tab栏')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例86：我的等级-男-立即充值')
    def test_homepage86(self):
        logging.info("===我的等级-男-立即充值===")
        try:
            # self.multiman.swipe(622,2000,622,600)
            assert self.mandriver.find_element(*MultiMan.level_rules_text).text == '充值/消费'
            topUpBtn=self.multiman.vipLevel_level_topUpBtn()
            topUpBtn[0].click()
            self.multiman.h5_to_native()
            time.sleep(3)
            assert self.mandriver.find_element(*MultiMan.myBalance_myDiamondText).text == '余额'
            self.multiman.system_goback_key()
            self.multiman.native_to_h5()
            self.multiman.vip_Level_mylevel_goback()
            # self.l.tap(564,205)
            # self.mandriver.find_element(*MultiMan.level_goback).click()
            # self.c.h5_to_native()

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的等级-男-立即充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的等级-男-立即充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例87-88：我的等级-女-外部显示和内部跳转')
    def test_homepage87(self):
        logging.info("===我的等级-女-外部显示和内部跳转===")
        # self.multiwoman.tap(980,2155)
        self.multiwoman.tab_Mine_Btn_126()
        try:
            my_vipLevel_NowLevelImgWomanZero = self.womandriver.find_element(*MultiWoman.my_vipLevel_NowLevelImgZeroAndWoman).text
            self.multiwoman.vip_Level_right_click()
            self.multiwoman.native_to_h5()
            assert self.multiwoman.vipLevel_level_value() == my_vipLevel_NowLevelImgWomanZero
            logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的等级-女-外部显示和内部跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的等级-女-外部显示和内部跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例89：我的等级-女-等级tab栏')
    def test_homepage89(self):
        logging.info("===我的等级-女-等级tab栏===")
        try:
            vipLevel_level_value = self.multiwoman.vipLevel_level_value()
            vipLevel_levelLeft_value = self.multiwoman.vipLevel_levelLeft_value()
            if vipLevel_level_value == 'Lv0' and vipLevel_levelLeft_value == 'Lv0':
                logging.info('===等级为Lv0===')
                assert self.womandriver.find_element(*MultiWoman.level_tabSelectedManCss).text == 'Lv1'
                logging.info('===开始断言等级特权弹窗===')
                self.womandriver.find_element(*MultiWoman.level_privilege_DetailAllCss).click()
                assert self.womandriver.find_element(*MultiWoman.level_privilege_detailPopoverHeadFrameCss).text == '进场气泡'
                # self.multiwoman.swipe(780,1000,348,1000)
                # assert self.womandriver.find_element(*MultiWoman.level_privilege_detailPopoverHeadFrameCss).text  == '头像框'
                self.multiwoman.tap(870, 2036)
                logging.info('===开始断言等级特权tab切换===')
                self.womandriver.find_elements(*MultiWoman.level_tabItem)[1].click()
                assert len(self.womandriver.find_elements(*MultiWoman.level_privilege_DetailList))==3
                logging.info('===断言成功===')
            else:
                logging.info('===等级不为Lv0，开始断言等级与横条等级内容===')
                print(vipLevel_level_value)
                assert self.womandriver.find_element(*MultiWoman.level_tabSelectedWomanCss).text == vipLevel_levelLeft_value
                logging.info('===开始断言等级特权弹窗===')
                self.womandriver.find_element(*MultiWoman.level_privilege_DetailAllCss).click()
                assert self.womandriver.find_element(*MultiWoman.level_privilege_detailPopoverHeadFrameCss).text == '进场气泡'
                # self.multiwoman.swipe(780,1000,348,1000)
                # assert self.womandriver.find_element(*MultiWoman.level_privilege_detailPopoverHeadFrameCss).text  == '头像框'
                self.multiwoman.tap(870, 2036)
                logging.info('===开始断言等级特权tab切换===')
                self.womandriver.find_elements(*MultiWoman.level_tabItem)[0].click()
                assert len(self.womandriver.find_elements(*MultiWoman.level_privilege_DetailList))==2
                logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的等级-女-等级tab栏')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的等级-女-等级tab栏')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的等级')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例90：我的等级-女-立即充值')
    def test_homepage90(self):
        logging.info("===我的等级-女-立即充值==")
        try:
            # self.multiwoman.swipe(622, 2000, 622, 600)
            assert self.womandriver.find_element(*MultiWoman.level_rules_text_woman).text == '赚取金额'
            topUpBtn = self.multiwoman.vipLevel_level_topUpBtn()
            assert topUpBtn == [] or False
            self.multiwoman.vip_Level_mylevel_goback()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的等级-女-立即充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的等级-女-立即充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise







    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例91-92：我的任务-男-有奖励红点或积分及未领取和领取奖励')
    def test_homepage91(self):
        logging.info("===我的任务-男-有奖励红点或积分及未领取和领取奖励===")
        try:
            self.multiman.tab_Mine_Btn()
            self.multiman.tap(970, 2114)
            global my_Tasks_entryTwoText
            my_Tasks_entryTwoText = self.multiman.my_Tasks_entryTwoText()
            if my_Tasks_entryTwoText=='新奖励':
                logging.info("===我的任务-新奖励===")
                self.mandriver.find_element(*MultiMan.MyTasks_entry_RightClick).click()
                time.sleep(2)
                self.multiman.tap(1061, 111)
                logging.info("===已完成未领取奖励，开始领取===")
                if self.multiman.MyTasks_rewards_LeftClickGuideIDEle():
                    ClickGuideID=self.mandriver.find_element(*MultiMan.MyTasks_rewards_LeftClickGuideID).location
                    self.mandriver.find_element(*MultiMan.MyTasks_rewards_LeftClickGuideID).click()
                else:
                    ClickGuideID = self.mandriver.find_element(*MultiMan.MyTasks_rewards_RightClickGuideID).location
                    self.mandriver.find_element(*MultiMan.MyTasks_rewards_RightClickGuideID).click()
                logging.info("===领取奖励中===")
                assert self.mandriver.find_element(*MultiMan.MyTasks_rewards_CongratsPopoverAwesomeBtn).text == '真棒！'
                self.mandriver.find_element(*MultiMan.MyTasks_rewards_CongratsPopoverAwesomeBtn).click()
                time.sleep(2)
                self.multiman.tap(ClickGuideID['x'], ClickGuideID['y'])
                logging.info("===已完成已领取奖励，弹窗跳转确认===")
                assert self.mandriver.find_element(*MultiMan.MyTasks_rewards_RewardDetailsPopoverOkBtn).text == '完成任务获得更多奖励'
                self.mandriver.find_element(*MultiMan.MyTasks_rewards_RewardDetailsPopoverOkBtn).click()
                logging.info("===已领取奖励的弹窗跳转===")
                MyTasks_tab_tasks = self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks)
                assert MyTasks_tab_tasks.get_attribute('selected') == 'true'
                logging.info("===断言成功===")
            else:
                logging.info("===我的任务-具体积分===")
                self.mandriver.find_element(*MultiMan.MyTasks_entry_RightClick).click()
                self.multiman.tap(1061, 111)
                tasks_points_next = self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks)
                assert tasks_points_next.get_attribute('selected') == 'true'
                MyTasks_tab_pointsNumber=self.mandriver.find_element(*MultiMan.MyTasks_tab_pointsNumber).text
                MyTasks_tab_pointsNumberIcon='{}''\x20''[points]'.format(MyTasks_tab_pointsNumber)
                assert MyTasks_tab_pointsNumberIcon==my_Tasks_entryTwoText
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-有奖励红点或积分及未领取和领取奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-有奖励红点或积分及未领取和领取奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例93：我的任务-男-未完成奖励')
    def test_homepage93(self):
        logging.info("====我的任务-男-未完成奖励'===")
        try:
            self.multiman.tap(1061, 111)
            self.mandriver.find_element(*MultiMan.MyTasks_tab_rewards).click()
            logging.info("===未完成奖励'===")
            self.multiman.swipe(40, 1473, 40, 387, 100)
            self.multiman.swipe(40, 1473, 40, 387, 100)
            self.multiman.swipe(40, 1473, 40, 387, 100)
            self.mandriver.find_elements(*MultiMan.MyTasks_rewards_manLast6500NoClaim)[-1].click()
            RewardDetailsPopoverOkBtn_test=self.mandriver.find_element(*MultiMan.MyTasks_rewards_RewardDetailsPopoverOkBtn)
            assert RewardDetailsPopoverOkBtn_test.text == '完成任务获得更多奖励'
            RewardDetailsPopoverOkBtn_test.click()
            MyTasks_tab_tasks = self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks)
            assert MyTasks_tab_tasks.get_attribute('selected') == 'true'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-未完成奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-未完成奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例94：我的任务-男-现在做任务按钮')
    def test_homepage94(self):
        logging.info("====我的任务-男-现在做任务按钮'===")
        try:
            self.multiman.tap(899, 161)
            self.mandriver.find_element(*MultiMan.MyTasks_tab_rewards).click()
            self.multiman.swipe(40, 1473, 40, 387, 100)
            self.multiman.swipe(40, 1473, 40, 387, 100)
            self.multiman.swipe(40, 1473, 40, 387, 100)
            MyTasks_rewards_DoTasksNowBtn_case1=self.mandriver.find_element(*MultiMan.MyTasks_rewards_DoTasksNowBtn)
            assert MyTasks_rewards_DoTasksNowBtn_case1.text == '现在做任务！'
            MyTasks_rewards_DoTasksNowBtn_case1.click()
            MyTasks_tab_tasks = self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks)
            assert MyTasks_tab_tasks.get_attribute('selected') == 'true'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-现在做任务按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-现在做任务按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例95：我的任务--男-兑换奖励按钮')
    def test_homepage95(self):
        logging.info("===我的任务--男-兑换奖励按钮===")
        try:
            self.multiman.tap(899, 161)
            self.multiman.swipe(40, 387, 40, 1473, 100)
            self.multiman.swipe(40, 387, 40, 1473, 100)
            MyTasks_tasktab_pointsSwitchBtn = self.mandriver.find_element(*MultiMan.MyTasks_tab_pointsSwitchBtn)
            if MyTasks_tasktab_pointsSwitchBtn.text == '兑换奖励':
                MyTasks_tasktab_pointsSwitchBtn.click()
                assert MyTasks_tasktab_pointsSwitchBtn.text == '更多积分'
            else:
                MyTasks_tasktab_pointsSwitchBtn.click()
                assert MyTasks_tasktab_pointsSwitchBtn.text == '兑换奖励'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务--男-兑换奖励按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务--男-兑换奖励按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例96：我的任务-男-通行证历史')
    def test_homepage96(self):
        logging.info("====我的任务-男-通行证历史'===")
        try:
            self.multiman.tap(899, 161)
            self.multiman.swipe(40, 387, 40, 1473, 100)
            monthlyHistory=self.multiman.my_Tasks_pointsMonthlyHistory()
            if monthlyHistory!=False:
                logging.info("===有充值月卡，有记录===")
                monthlyHistory.click()
                time.sleep(2)
                assert self.mandriver.find_element(*MultiMan.MyTasks_tab_pointsMonthlyHistoryPopoverUserID).text == 'ID:''{}'.format(man_pageUserId)
                self.multiman.system_goback_key()
                logging.info("===断言成功===")
            else:
                pytest.skip("===没有充值过月卡，无记录===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-通行证历史')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-通行证历史')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例97：我的任务-男-签到入口')
    def test_homepage97(self):
        logging.info("====我的任务-男-签到入口'===")
        try:
            self.multiman.tap(899, 161)
            self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks).click()
            assert self.multiman.my_Tasks_ManSignInSuccess()
            MyTasks_tasks_signinEntry_case=self.mandriver.find_element(*MultiMan.MyTasks_tasks_signinEntry)
            MyTasks_tasks_signinEntry_case.click()
            sign_btn_man = self.mandriver.find_element(*MultiMan.sign_in_popover_SigninSubmitTextID)
            assert sign_btn_man.text == '好的', "已签到，按钮不是好的"
            sign_btn_man.click()
            # assert MyTasks_tasks_signinEntry_case
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例98：我的任务-男-邀请入口')
    def test_homepage98(self):
        logging.info("====我的任务-男-邀请入口'===")
        try:
            self.multiman.tap(899, 161)
            MyTasks_tab_tasks_case1=self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks)
            MyTasks_tab_tasks_case1.click()
            self.mandriver.find_element(*MultiMan.MyTasks_tasks_inviteEntryTextXpath).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.MyTasks_tasks_invitePopoverAll), "有邀请按钮，邀请弹窗未出现"
            self.multiman.tap(899, 161)
            # assert MyTasks_tab_tasks_case1.get_attribute('selected') == 'true', '邀请弹窗出现后点击空白未消失'
            logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-邀请入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-邀请入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例99：我的任务-男-Top Offers入口')
    def test_homepage99(self):
        logging.info("====我的任务-男-Top Offers入口'===")
        try:
            self.multiman.tap(899, 161)
            MyTasks_tab_tasks_case1 = self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks)
            MyTasks_tab_tasks_case1.click()
            self.mandriver.find_element(*MultiMan.MyTasks_tasks_TopOffersEntryTextXPATH).click()
            # assert self.mandriver.find_element(*MultiMan.MyTasks_tasks_TopOffersEntryText).text == 'Top Offers'
            # self.mandriver.find_element(*MultiMan.MyTasks_tasks_TopOffersEntry).click()
            assert self.mandriver.find_element(*MultiMan.MyTasks_tasks_TopOffersTitle).text=='Top Offers'
            self.mandriver.find_element(*MultiMan.MyTasks_tasks_TopOffersGoback).click()
            # tasks_points_next = self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks)
            # assert self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks).get_attribute('selected') == 'true'
            logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-Top Offers入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-Top Offers入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例100：我的任务-男-每日任务')
    def test_homepage100(self):
        logging.info("====我的任务-男-每日任务'===")
        try:
            logging.info("====检查每日任务===")
            self.multiman.tap(899, 161)
            # self.mandriver.find_element(*MultiMan.MyTasks_tab_tasks).click()
            self.multiman.swipe(200, 1772, 200, 1251)
            assert len(self.mandriver.find_elements(*MultiMan.MyTasks_tasks_DailyTasksList))==6
            logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-每日任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-每日任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例101：我的任务-男-每月任务')
    def test_homepage101(self):
        logging.info("====我的任务-男-每月任务'===")
        try:
            self.multiman.swipe(200, 1473, 200, 387, 100)
            logging.info("====检查每月任务===")
            assert len(self.mandriver.find_elements(*MultiMan.MyTasks_tasks_MonthlyTasksList))==5
            logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-每月任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-每月任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例102：我的任务-男-开通月卡')
    def test_homepage102(self):
        logging.info("====我的任务-男-开通月卡'===")
        try:
            # self.multiman.tap(899, 161)
            self.multiman.swipe(40, 387, 40, 1473,100)
            self.mandriver.find_element(*MultiMan.MyTasks_tab_rewards).click()
            self.multiman.swipe(40, 387, 40, 1473, 100)
            if self.multiman.myTasks_rewards_TopUpMonthCard():
                logging.info("===男用户有充值月卡入口===")
                self.mandriver.find_element(*MultiMan.MyTasks_rewards_TopUpMonthCard).click()
                assert self.mandriver.find_element(*MultiMan.MyTasks_rewards_TopUpMonthCardPopoverCardText).text == '月卡'
                self.multiman.tap(899, 161)
                MyTasks_tab_rewards = self.mandriver.find_element(*MultiMan.MyTasks_tab_rewards)
                assert MyTasks_tab_rewards.get_attribute('selected') == 'true', '点击月卡空白处，未停留在奖励页面'
                self.multiman.system_goback_key()
                logging.error("===断言成功===")
            else:
                logging.info("===男用户没有充值月卡入口,已经开通完成===")
                self.mandriver.find_element(*MultiMan.MyTasks_rewards_TopUpMonthCard0Points).click()
                assert self.multiman.MyTasks_rewards_CongratsPopoverAwesomeBtnEle()!=False or self.multiman.MyTasks_rewards_RewardDetailsPopoverOkBtnEle()!=False
                # self.multiman.tap(899, 161)
                self.multiman.system_goback_key()
                time.sleep(1)
                self.multiman.system_goback_key()
                logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的任务-男-开通月卡')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的任务-男-开通月卡')
            logging.info(f'截图成功，图片为{screen_name}')
            raise








    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例103-104：我的任务-女-有奖励红点或积分及未领取和领取奖励')
    def test_homepage103(self):
        logging.info("===我的任务-女-有奖励红点或积分及未领取和领取奖励===")
        try:
            self.multiwoman.tab_Mine_Btn_126()
            self.multiwoman.tap(970, 2114)
            global my_Tasks_entryTwoText
            my_Tasks_entryTwoText1 = self.multiwoman.my_Tasks_entryTwoText()
            my_Tasks_entryTwoText=my_Tasks_entryTwoText1.replace(',','')
            print(my_Tasks_entryTwoText)
            if my_Tasks_entryTwoText=='新奖励':
                logging.info("===我的任务-新奖励===")
                self.womandriver.find_element(*MultiWoman.MyTasks_entry_RightClick).click()
                time.sleep(2)
                self.multiwoman.tap(1061, 111)
                logging.info("===有已完成未领取奖励,开始领取===")
                ClickGuideID = self.womandriver.find_element(*MultiWoman.MyTasks_rewards_LeftClickGuideID).location
                self.womandriver.find_element(*MultiWoman.MyTasks_rewards_LeftClickGuideID).click()
                logging.info("===领取奖励中===")
                assert self.womandriver.find_element(*MultiWoman.MyTasks_rewards_CongratsPopoverAwesomeBtn).text == '真棒！', "有领取弹窗，但是文字不是真棒字样"
                self.womandriver.find_element(*MultiWoman.MyTasks_rewards_CongratsPopoverAwesomeBtn).click()
                self.multiwoman.tap(ClickGuideID['x'], ClickGuideID['y'])
                logging.info("===已领取奖励的弹窗，点击无反应===")
                MyTasks_tab_rewards = self.womandriver.find_element(*MultiWoman.MyTasks_tab_rewards)
                assert MyTasks_tab_rewards.get_attribute('selected') == 'true'
                logging.info("===已完成已领取奖励,开始查看===")
                self.womandriver.find_element(*MultiWoman.MyTasks_womanRewards_RewardsStatusClaimed).click()
                MyTasks_tab_rewards = self.womandriver.find_element(*MultiWoman.MyTasks_tab_rewards)
                assert MyTasks_tab_rewards.get_attribute('selected') == 'true'
                logging.info("===断言成功===")
            else:
                logging.info("===我的任务-具体积分===")
                self.womandriver.find_element(*MultiWoman.MyTasks_entry_RightClick).click()
                self.multiwoman.tap(1061, 111)
                tasks_points_next = self.womandriver.find_element(*MultiWoman.MyTasks_tab_tasks)
                assert tasks_points_next.get_attribute('selected') == 'true'
                MyTasks_tab_pointsNumber=self.womandriver.find_element(*MultiWoman.MyTasks_tab_pointsNumber).text
                MyTasks_tab_pointsNumberIcon='{}''\x20''[points]'.format(MyTasks_tab_pointsNumber)
                assert MyTasks_tab_pointsNumberIcon==my_Tasks_entryTwoText
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-有奖励红点或积分及未领取和领取奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-有奖励红点或积分及未领取和领取奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例105：我的任务-女-未完成奖励')
    def test_homepage105(self):
        logging.info("====我的任务-女-未完成奖励'===")
        try:
            self.multiwoman.tap(1061, 111)
            self.womandriver.find_element(*MultiWoman.MyTasks_tab_rewards).click()
            logging.error("===女生===")
            logging.info("===待解锁奖励'===")
            self.multiwoman.swipe(40, 1473, 40, 387, 100)
            self.multiwoman.swipe(40, 1473, 40, 387, 100)
            self.multiwoman.swipe(40, 1473, 40, 387, 100)
            self.womandriver.find_elements(*MultiWoman.MyTasks_womanRewards_RewardsStatusLocked)[-1].click()
            MyTasks_tab_rewards = self.womandriver.find_element(*MultiWoman.MyTasks_tab_rewards)
            assert MyTasks_tab_rewards.get_attribute('selected') == 'true'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-未完成奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-未完成奖励')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例106：我的任务-女-现在做任务按钮')
    def test_homepage106(self):
        logging.info("====我的任务-女-现在做任务按钮'===")
        try:
            self.multiwoman.tap(1061, 111)
            self.womandriver.find_element(*MultiWoman.MyTasks_tab_rewards).click()
            self.multiwoman.swipe(40, 1473, 40, 387, 100)
            self.multiwoman.swipe(40, 1473, 40, 387, 100)
            self.multiwoman.swipe(40, 1473, 40, 387, 100)
            self.multiwoman.swipe(40, 1473, 40, 387, 100)
            MyTasks_rewards_DoTasksNowBtn_case1 = self.womandriver.find_element(*MultiWoman.MyTasks_rewards_DoTasksNowBtn)
            assert MyTasks_rewards_DoTasksNowBtn_case1.text == '立即做任务！'
            MyTasks_rewards_DoTasksNowBtn_case1.click()
            MyTasks_tab_tasks = self.womandriver.find_element(*MultiWoman.MyTasks_tab_tasks)
            assert MyTasks_tab_tasks.get_attribute('selected') == 'true'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-现在做任务按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-现在做任务按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例107：我的任务--女-兑换奖励按钮')
    def test_homepage107(self):
        logging.info("===我的任务--女-兑换奖励按钮===")
        try:
            self.multiwoman.tap(1061, 111)
            self.multiwoman.swipe(40, 387, 40, 1473, 100)
            self.multiwoman.swipe(40, 387, 40, 1473, 100)
            MyTasks_tasktab_pointsSwitchBtn = self.womandriver.find_element(*MultiWoman.MyTasks_tab_pointsSwitchBtn)
            assert MyTasks_tasktab_pointsSwitchBtn.text == '兑换奖励'
            MyTasks_tasktab_pointsSwitchBtn.click()
            assert MyTasks_tasktab_pointsSwitchBtn.text == '更多积分'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务--女-兑换奖励按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务--女-兑换奖励按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例108：我的任务-女-通行证历史')
    def test_homepage108(self):
        logging.info("====我的任务-女-通行证历史'===")
        try:
            monthlyHistory = self.multiwoman.my_Tasks_pointsMonthlyHistory()
            assert monthlyHistory == False
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-通行证历史')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-通行证历史')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例109：我的任务-女-签到入口')
    def test_homepage109(self):
        logging.info("====我的任务-女-签到入口'===")
        try:
            self.multiwoman.tap(1061, 111)
            self.womandriver.find_element(*MultiWoman.MyTasks_tab_tasks).click()
            assert self.womandriver.find_element(*MultiWoman.MyTasks_womanTasks_LoginTomorrowText).text=='签到'
            self.womandriver.find_element(*MultiWoman.MyTasks_womanTasks_alreadyLoginAll).click()
            sign_btn_man = self.womandriver.find_element(*MultiWoman.sign_in_popover_SigninSubmitTextID)
            assert sign_btn_man.text == '兑换奖励', "已签到，按钮不是兑换奖励"
            sign_btn_man.click()
            # MyTasks_tab_rewards_next = self.womandriver.find_element(*MultiWoman.MyTasks_tab_rewards)
            # assert MyTasks_tab_rewards_next.get_attribute('selected') == 'true'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-签到入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例110：我的任务-女-邀请入口')
    def test_homepage110(self):
        logging.info("====我的任务-女-邀请入口'===")
        try:
            self.multiwoman.tap(1061, 111)
            MyTasks_tab_tasks_case1=self.womandriver.find_element(*MultiWoman.MyTasks_tab_tasks)
            MyTasks_tab_tasks_case1.click()
            assert self.multiwoman.MyTasks_tasks_inviteEntryTextEle()==False
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-邀请入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-邀请入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例111：我的任务-女-Top Offers入口')
    def test_homepage111(self):
        logging.info("====我的任务-女-Top Offers入口'===")
        try:
            self.multiwoman.tap(1061, 111)
            MyTasks_tab_tasks_case1 = self.womandriver.find_element(*MultiWoman.MyTasks_tab_tasks)
            MyTasks_tab_tasks_case1.click()
            assert self.multiwoman.MyTasks_tasks_TopOffersEntryTextEle()==False
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-Top Offers入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-Top Offers入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例112：我的任务-女-每日任务')
    def test_homepage112(self):
        logging.info("====我的任务-女-每日任务'===")
        try:
            logging.info("====检查每日任务===")
            # self.womandriver.find_element(*MultiWoman.MyTasks_tab_tasks).click()
            self.multiwoman.tap(1061, 111)
            self.multiwoman.swipe(160,2000,190,1000)
            assert len(self.womandriver.find_elements(*MultiWoman.MyTasks_tasks_DailyTasksList))==6
            logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-每日任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-每日任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例113：我的任务-女-每月任务')
    def test_homepage113(self):
        logging.info("====我的任务-女-每月任务'===")
        try:
            logging.info("====检查每月任务===")
            self.multiwoman.swipe(160, 2000, 190, 1000)
            assert self.multiwoman.my_Tasks_ManMonthlyTasksAll()==False
            logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-每月任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-每月任务')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的任务')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例114：我的任务-女-开通月卡')
    def test_homepage114(self):
        logging.info("====我的任务-女-开通月卡'===")
        try:
            self.multiwoman.tap(1061, 111)
            self.multiwoman.swipe(40, 387, 40, 1473,100)
            self.womandriver.find_element(*MultiWoman.MyTasks_tab_rewards).click()
            assert self.multiwoman.myTasks_rewards_TopUpMonthCard()==False
            self.multiwoman.system_goback_key()
            logging.error("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的任务-女-开通月卡')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的任务-女-开通月卡')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的背包')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例115：我的背包-入口跳转')
    def test_homepage115(self):
        logging.info("===我的背包-入口跳转===")
        try:
            assert self.mandriver.find_element(*MultiMan.myBackpack_entryText)
            self.mandriver.find_element(*MultiMan.myBackpack_entryAll).click()
            assert self.mandriver.find_element(*MultiMan.myBackpack_title).text=='我的背包'
            self.multiman.system_goback_key()
            logging.info("===男用户入口跳转成功===")
            assert self.womandriver.find_element(*MultiWoman.myBackpack_entryText)
            self.womandriver.find_element(*MultiWoman.myBackpack_entryAll).click()
            assert self.womandriver.find_element(*MultiWoman.myBackpack_title).text == '我的背包'
            self.multiwoman.system_goback_key()
            logging.info("===女用户入口跳转成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的背包-入口跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的背包-入口跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的背包')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例116：我的收入-入口跳转')
    def test_homepage116(self):
        logging.info("===我的收入-入口跳转===")
        try:
            assert self.mandriver.find_element(*MultiMan.MyBalance_entry_manText).text=='提现'
            self.mandriver.find_element(*MultiMan.MyBalance_entry_man).click()
            time.sleep(3)
            self.multiman.native_to_h5()
            assert self.mandriver.find_element(*MultiMan.MyBalance_title).text == '我的赚取'
            self.multiman.system_goback_key()
            self.multiman.h5_to_native()
            logging.info("===男用户入口跳转成功===")
            assert self.womandriver.find_element(*MultiWoman.MyBalance_entry_womanText).text == '提现'
            self.womandriver.find_element(*MultiWoman.MyBalance_entry_woman).click()
            time.sleep(3)
            self.multiwoman.native_to_h5()
            assert self.womandriver.find_element(*MultiWoman.MyBalance_title).text == '我的赚取'
            self.multiwoman.system_goback_key()
            self.multiwoman.h5_to_native()
            logging.info("===男用户入口跳转成功===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的收入-入口跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的收入-入口跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的邀请')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例117：我的邀请-男女入口显示及跳转')
    def test_homepage117(self):
        logging.info("===我的邀请-男女入口显示及跳转===")
        try:
            logging.info("===我的邀请-男用户-入口显示===")
            assert self.mandriver.find_element(*MultiMan.MyInvite_entry_FreeCardsText).text == '免费卡片'
            self.multiman.MyInvite_entry_AllEle()
            self.multiman.native_to_h5()
            self.mandriver.implicitly_wait(2)
            # assert self.mandriver.find_element(*MultiMan.MyInvite_inviteRewardsTextName)
            # assert self.mandriver.find_element(*MultiMan.MyInvite_inviteRewardsTextXpath).text == '邀请奖励'
            logging.info("===女用户，没有我的邀请入口===")
            assert self.womandriver.find_element(*MultiWoman.MyInvite_entry_nameText).text != '我的邀请'
            # self.mandriver.quit()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的邀请-男女入口显示及跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的邀请-男女入口显示及跳转')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的邀请')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例118：我的邀请-男-问号按钮')
    def test_homepage118(self):
        logging.info("===我的邀请-男-问号按钮===")
        try:

            logging.info("===问号按钮===")
            self.mandriver.find_element(*MultiMan.MyInvite_instructionsBtn).click()
            assert self.mandriver.find_element(*MultiMan.MyInvite_instructionsPopover_rule1).text == '聊天卡免费用于视频聊天1分钟，每张卡有效期为5天'
            assert self.mandriver.find_element(*MultiMan.MyInvite_instructionsPopover_rule2).text == '只有新的Chamet用户才能获得奖励'
            self.multiman.tap(609,197)
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的邀请-男-问号按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的邀请-男-问号按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的邀请')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例119：我的邀请-男-邀请好友按钮')
    def test_homepage119(self):
        logging.info("===我的邀请-男-邀请好友按钮===")
        try:
            logging.info("===邀请好友按钮===")
            self.mandriver.find_element(*MultiMan.MyInvite_inviteFriendsBtnID).click()
            self.multiman.h5_to_native()
            assert self.mandriver.find_element(*MultiMan.MyInvite_inviteFriendsPopover_whats)
            assert self.mandriver.find_element(*MultiMan.MyInvite_inviteFriendsPopover_mess)
            self.multiman.tap(609, 197)
            self.multiman.native_to_h5()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的邀请-男-邀请好友按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的邀请-男-邀请好友按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




    @allure.story('我的邀请')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例120：我的邀请-邀请列表')
    def test_homepage120(self):
        logging.info("===我的邀请-邀请列表===")
        try:
            self.mandriver.find_element(*MultiMan.MyInvite_myInvitees).click()
            time.sleep(3)
            assert self.mandriver.find_elements(*MultiMan.MyInvite_weekly_noUser)
            # if len(self.mandriver.find_elements(*MultiMan.MyInvite_weekly_noUser))!=0:
            #     assert len(self.mandriver.find_elements(*MultiMan.MyInvite_my_inviteesListNameXpath))==0
            # else:
            #     inviteesListFirstNameText1 = self.mandriver.find_elements(*MultiMan.MyInvite_my_inviteesListNameXpath)[0].text
            #     time.sleep(2)
            #     self.mandriver.find_elements(*MultiMan.MyInvite_my_inviteesListNameXpath)[0].click()
            #     self.multiman.h5_to_native()
            #     assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text.encode('gbk', 'ignore') in inviteesListFirstNameText1
            #     self.multiman.system_goback_key()
            #     self.multiman.native_to_h5()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的邀请-邀请列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的邀请-邀请列表')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的邀请')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例121：我的邀请-周排行')
    def test_homepage121(self):
        logging.info("===我的邀请-周排行===")
        try:
            self.mandriver.find_element(*MultiMan.MyInvite_weeklyRank).click()
            inviteesListFirstName = self.mandriver.find_elements(*MultiMan.MyInvite_my_inviteesListNameXpath)[3].text.encode('gbk', 'ignore')
            time.sleep(2)
            self.mandriver.find_elements(*MultiMan.MyInvite_my_inviteesListNameXpath)[3].click()
            self.multiman.h5_to_native()
            assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName)
            self.multiman.system_goback_key()
            self.multiman.native_to_h5()
            self.multiman.MyInvite_gobackEle()
            logging.info('===断言成功===')

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的邀请-周排行')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的邀请-周排行')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    # 打招呼已发送给所有在线用户。
    @allure.story('我的打招呼')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例122：我的打招呼-男女入口显示-进入显示')
    def test_homepage122(self):
        logging.info("===我的打招呼-男女入口显示-进入显示===")
        try:
            logging.info("===我的打招呼-女入口显示-进入显示===")
            self.multiwoman.tab_Mine_Btn()
            self.womandriver.find_element(*MultiWoman.MyGreetingWords_entry).click()
            time.sleep(2)
            global GrWords_woman
            if self.multiwoman.MyGrWords_faceVerification_popoverAllEle():
                GrWords_woman=0
                logging.info("===我的打招呼-未通过真人检测===")
                assert self.womandriver.find_element(*MultiWoman.MyGrWords_faceVerification_popoverText).text == '为保障安全性，你需要先通过真人检测'
            elif self.multiwoman.MyGrWords_edit_saveBtnEle():
                GrWords_woman = 1
                logging.info("===我的打招呼-已通过真人检测，没有消息记录===")
                self.multiwoman.tap(1007, 1436)
                self.womandriver.find_element(*MultiWoman.MyGrWords_edit_contentText).send_keys('hi,a nice day ,call me')
                self.womandriver.find_element(*MultiWoman.MyGrWords_edit_albumPhoto).click()
                self.multiwoman.tap(1007, 1436)
                self.multiwoman.get_permission_checkPopover()
                self.multiwoman.tap(522,427)
                self.womandriver.find_element(*MultiWoman.MyGrWords_edit_saveBtn).click()
                self.womandriver.find_element(*MultiWoman.MyGreetingWords_entry).click()
                assert self.womandriver.find_element(*MultiWoman.MyGrWords_wordListNumTotal)
            else:
                GrWords_woman = 2
                logging.info("===我的打招呼-已通过真人检测，有消息记录===")
                assert self.womandriver.find_element(*MultiWoman.MyGrWords_Title).text == '我的打招呼'
                assert self.multiwoman.MyGrWords_sendAllBtnEle()
                logging.info("===女用户-断言成功===")

                logging.info("===我的打招呼-男女入口显示-进入显示===")
                assert self.mandriver.find_element(*MultiMan.MyGreetingWords_entryText).text!='我的打招呼'
                logging.info("===男用户-断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的打招呼-男女入口显示-进入显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的打招呼-男女入口显示-进入显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的打招呼')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例123-124：我的打招呼-女-已通过真人检测')
    def test_homepage123(self):
        logging.info("===我的打招呼-女-已通过真人检测===")
        # GrWords_woman=0,1,2=未通过真人检测，通过但没消息，通过且有消息
        try:
            print(GrWords_woman)
            if GrWords_woman ==0:
                logging.info("===我的打招呼-未通过真人检测===")
                # assert self.mandriver.find_element(*MultiMan.MyGrWords_faceVerification_popoverText).text == '为保障安全性，你需要先通过真人检测'
                self.womandriver.find_element(*MultiWoman.MyGrWords_faceVerification_popoverConfirmBtn).click()
                assert self.womandriver.find_element(*MultiWoman.MyGrWords_faceVerification_cameraTipsXpath)
                if self.womandriver.find_element(*MultiWoman.MyGrWords_faceVerification_cameraCloseBtn):
                    self.womandriver.find_element(*MultiWoman.MyGrWords_faceVerification_cameraCloseBtn).click()
                    logging.info("===断言成功===")
                else:
                    self.womandriver.find_element(*MultiWoman.MyGrWords_faceVerification_cameraTryPopCancelBtn).click()
                    logging.info("===断言成功===")
            else:
                logging.info("===我的打招呼-已通过真人检测===")
                # self.mandriver.find_element(*MultiMan.MyGreetingWords_entry).click()
                print(self.womandriver.find_elements(*MultiWoman.MyGrWords_wordListNum))
                listNum = len(self.womandriver.find_elements(*MultiWoman.MyGrWords_wordListNum))
                print('listNum''{}'.format(listNum))
                print(self.womandriver.find_elements(*MultiWoman.MyGrWords_wordList_StatusFailedAndIng))
                StatusFailedList = len(self.womandriver.find_elements(*MultiWoman.MyGrWords_wordList_StatusFailedAndIng))
                print('StatusFailedList''{}'.format(StatusFailedList))
                if self.multiwoman.MyGrWords_MyWords_AddBtnEle() and StatusFailedList<listNum-1:
                    logging.info("===页面有增加按钮，有已通过的打招呼消息===")
                    self.womandriver.find_element(*MultiWoman.MyGrWords_sendAllBtn).click()
                    self.multiwoman.MyGrWords_sendAllBtn_3levelPopConEle()
                    # 获取toast
                    assert self.womandriver.find_element(*MultiWoman.MyGrWords_sendAllBtn)
                    self.womandriver.find_element(*MultiWoman.MyGrWords_goback).click()
                elif self.multiwoman.MyGrWords_MyWords_AddBtnEle()==False and StatusFailedList<listNum:
                    logging.info("===页面没有增加按钮，有已通过的打招呼消息===")
                    self.womandriver.find_element(*MultiWoman.MyGrWords_goback).click()
                else:
                    logging.info("===没有已通过的打招呼消息===")
                    self.womandriver.find_element(*MultiWoman.MyGrWords_goback).click()
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的打招呼-女-已通过真人检测')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的打招呼-女-已通过真人检测')
            logging.info(f'截图成功，图片为{screen_name}')
            raise








    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例125：我的简介-入口')
    def test_homepage125(self):
        logging.info("===我的简介-入口===")
        try:
            self.mandriver.find_element(*MultiMan.myProfile_entry_man).click()
            assert self.mandriver.find_element(*MultiMan.myProfile_Title).text=='我的简介','没有进入我的等级页面'
            logging.info("===男-进入简介-断言成功===")
            self.multiwoman.tab_Mine_Btn()
            self.womandriver.find_element(*MultiWoman.myProfile_entry_woman).click()
            assert self.womandriver.find_element(*MultiWoman.myProfile_Title).text == '我的简介', '没有进入我的等级页面'
            logging.info("===女-进入简介-断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例126：我的简介-男-头像')
    def test_homepage126(self):
        logging.info("===我的简介-男-头像===")
        try:
            self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_img).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_title).text == '我的头像'
            assert self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_posterTipContents).text == '请上传你自己的清晰和漂亮的照片'
            logging.info("===我的简介-头像断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-男-头像')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-男-头像')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例127：我的简介-男-头像-编辑')
    def test_homepage127(self):
        logging.info("===我的简介-头像-编辑===")
        try:
            MyAvatar_posterOld=self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_poster)
            self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_ChangePosterBtn).click()
            self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_ChangePosterPopPictureBtn).click()
            self.multiman.get_permission_checkPopover()
            self.mandriver.find_elements(*MultiMan.messages_Group_pictureChooseList)[0].click()
            self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_ChangePosterUpdateConfirm).click()
            assert self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_PosterStateText).text=='审核中' or '已通过'or'失败'
            print(self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_PosterStateText).text)
            MyAvatar_posterNew = self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_poster)
            assert MyAvatar_posterOld!=MyAvatar_posterNew
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-头像-编辑')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-头像-编辑')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例128：我的简介-头像-男-无历史图集')
    def test_homepage128(self):
        logging.info("===我的简介-头像-男-无历史图集==")
        try:
            self.multiman.tap(1016,148)
            assert self.multiman.myProfile_MyAvatar_PosterHistoryBtn_Ele()==False
            assert self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_title).text == '我的头像'
            self.mandriver.find_element(*MultiMan.myProfile_MyAvatar_goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-头像-历史图集女用户')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-头像-历史图集女用户')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例129：我的简介-女-头像')
    def test_homepage129(self):
        logging.info("===我的简介-女-头像===")
        try:
            self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_img).click()
            time.sleep(2)
            assert self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_title).text == '我的封面'
            # assert self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_posterScoreTitle).text == '封面评分'
            logging.info("===我的简介-头像断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的简介-女-头像')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的简介-女-头像')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例130：我的简介-头像-女-有历史图集')
    def test_homepage130(self):
        logging.info("===我的简介-头像-女-有历史图集===")
        try:
            time.sleep(2)
            # poster_score_out=self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_PosterScore).text
            history_btn_woman = self.multiwoman.myProfile_MyAvatar_PosterHistoryBtn_Ele()
            history_btn_woman.click()
            time.sleep(3)
            assert self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_PosterHistoryTitle).text == '图集'
            # 需要遍历list的分数
            assert len(self.womandriver.find_elements(*MultiWoman.myProfile_MyAvatar_PosterHistoryScore)) >= 1
            self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_PosterHistoryGoback).click()
            time.sleep(2)
            # assert self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_title).text == '我的封面'
            # self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的简介-头像-女-有历史图集')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的简介-头像-女-有历史图集')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例131：我的简介-女-头像-编辑')
    def test_homepage131(self):
        logging.info("===我的简介-女-头像-编辑===")
        try:
            MyAvatar_posterOld=self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_poster)
            self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_ChangePosterBtn).click()
            self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_ChangePosterPopPictureBtn).click()
            self.multiwoman.get_permission_checkPopover()
            self.womandriver.find_elements(*MultiWoman.messages_Group_pictureChooseList)[0].click()
            self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_ChangePosterUpdateConfirm).click()
            time.sleep(3)
            self.multiwoman.tap(952, 2200)
            time.sleep(3)
            self.multiwoman.tap(952, 2200)
            assert self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_PosterStateText).text=='审核中' or '已通过'or'失败'
            print(self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_PosterStateText).text)
            MyAvatar_posterNew = self.womandriver.find_element(*MultiWoman.myProfile_MyAvatar_poster)
            assert MyAvatar_posterOld!=MyAvatar_posterNew
            self.multiwoman.system_goback_key()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiwoman.screenshot('我的简介-女-头像-编辑')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiwoman.screenshot('我的简介-女-头像-编辑')
            logging.info(f'截图成功，图片为{screen_name}')
            raise






    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例132：我的简介-ID')
    def test_homepage132(self):
        logging.info("===我的简介-ID===")
        try:
            assert self.mandriver.find_element(*MultiMan.myProfile_ID_Number)
            self.mandriver.find_element(*MultiMan.myProfile_ID_CopyBtn).click()
            # print(self.l.toast_message('已拷贝'))
            assert self.mandriver.find_element(*MultiMan.myProfile_ID_Number)
            logging.info("===断言成功===")
            # 获取已拷贝字样toast

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-ID')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-ID')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例133：我的简介-昵称')
    def test_homepage133(self):
        logging.info("===我的简介-昵称===")
        try:
            NickName_Text_aa=self.mandriver.find_element(*MultiMan.myProfile_NickName_Text).text
            print(NickName_Text_aa)
            NickName_Text_aa1=NickName_Text_aa.rstrip('...')
            print(NickName_Text_aa1)
            assert man_pagePersonalName.find(NickName_Text_aa1)>=0
            self.mandriver.find_element(*MultiMan.myProfile_NickName_Text).click()
            # assert self.mandriver.find_element(*MultiMan.myProfile_NickName_title).text == '昵称','昵称的标题不正确'
            assert self.mandriver.find_element(*MultiMan.myProfile_NickName_EditorContent).text==man_pagePersonalName,'用户昵称与个人主页不一致'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-昵称')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-昵称')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例134：我的简介-昵称-修改')
    def test_homepage134(self):
        logging.info("===我的简介-昵称-修改===")
        try:
            global newName
            newName='Tom33364388yyy'
            self.mandriver.find_element(*MultiMan.myProfile_NickName_EditorContent).clear()
            self.mandriver.find_element(*MultiMan.myProfile_NickName_EditorContent).send_keys(newName)
            self.multiman.system_goback_key()
            self.multiman.myProfile_NickName_EditorCommitBtnEle()
            self.multiman.myProfile_NickName_EditorCommitBtnEle()
            # self.mandriver.find_element(*MultiMan.myProfile_NickName_EditorCommit).click()
            assert self.mandriver.find_element(*MultiMan.myProfile_Title).text == '我的简介'
            self.mandriver.find_element(*MultiMan.myProfile_Goback).click()
            self.multiman.tab_Mine_Btn()
            self.multiman.tab_Mine_Head()
            assert newName.find(self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text)>=0
            self.mandriver.find_element(*MultiMan.user_own_pageGobackBtn).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-昵称-修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-昵称-修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例135：我的简介-男女-性别')
    def test_homepage135(self):
        logging.info("===我的简介-性别===")
        try:
            self.multiman.tab_Mine_Btn()
            self.mandriver.find_element(*MultiMan.myProfile_entry_man).click()
            myProfile_Gender_sex_man = self.mandriver.find_element(*MultiMan.myProfile_GenderTextWoman).text
            assert myProfile_Gender_sex_man=='男'
            logging.info("===男-断言成功===")
            myProfile_Gender_sex_woman = self.womandriver.find_element(*MultiWoman.myProfile_GenderTextWoman).text
            assert myProfile_Gender_sex_woman ==  '性别' or '女'
            logging.info("===女-断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-男女-性别')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-男女-性别')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例136：我的简介-年龄显示')
    def test_homepage136(self):
        logging.info("===我的简介-年龄显示===")
        try:
            Age=self.mandriver.find_element(*MultiMan.myProfile_Age_Text).text
            assert int(Age) >= int('18'), '用户年龄小于18岁'
            self.mandriver.find_element(*MultiMan.myProfile_Age_All).click()
            self.mandriver.find_element(*MultiMan.myProfile_Age_popoverDateCancelBtn).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-年龄显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-年龄显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例137：我的简介-年龄修改')
    def test_homepage137(self):
        logging.info("===我的简介-年龄修改===")
        try:
            Age = self.mandriver.find_element(*MultiMan.myProfile_Age_Text).text
            self.mandriver.find_element(*MultiMan.myProfile_Age_All).click()
            self.mandriver.find_element(*MultiMan.myProfile_Age_popoverDateYear).click()
            self.mandriver.find_element(*MultiMan.myProfile_Age_popoverDateYearSecond).click()
            time.sleep(2)
            # self.multiman.tap(446,1398)
            self.multiman.tap(455,1480)
            self.mandriver.find_element(*MultiMan.myProfile_Age_popoverDateConfirmBtn).click()
            assert self.mandriver.find_element(*MultiMan.myProfile_Age_Text).text!=Age
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-年龄修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-年龄修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例138：我的简介-地区')
    def test_homepage138(self):
        logging.info("===我的简介-地区===")
        try:
            assert self.mandriver.find_element(*MultiMan.myProfile_Region_Image), '国家图标未显示'
            assert self.mandriver.find_element(*MultiMan.myProfile_Region_Text).text == '阿曼'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-地区')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-地区')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例139：我的简介-定位')
    def test_homepage139(self):
        logging.info("===我的简介-定位===")
        try:
            assert self.multiman.myProfile_Location_TextContents()!=False
            logging.info("===我的简介-定位有显示===")
            self.mandriver.find_element(*MultiMan.myProfile_Location_All).click()
            assert self.mandriver.find_element(*MultiMan.myProfile_Location_PopoverAll)
            self.mandriver.find_element(*MultiMan.myProfile_Location_PopoverCancelBtn).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-定位')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-定位')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例140-141：我的简介-定位切换')
    def test_homepage140(self):
        logging.info("===我的简介-定位切换===")
        try:
            myProfile_Location_TextContents_case=self.multiman.myProfile_Location_TextContents()
            assert myProfile_Location_TextContents_case!=False
            logging.info("===我的简介-定位有显示===")
            location = myProfile_Location_TextContents_case.text
            print(location)
            if location=='隐藏':
                self.mandriver.find_element(*MultiMan.myProfile_Location_All).click()
                if self.mandriver.find_element(*MultiMan.myProfile_Location_Popover1stIcon_Text).text=='隐藏':
                    logging.info("===我的简介-定位隐藏无法获取===")
                    self.mandriver.find_element(*MultiMan.myProfile_Location_Popover1stIcon).click()
                    self.mandriver.find_element(*MultiMan.myProfile_Location_PopoverConfirmBtn).click()
                    time.sleep(2)
                    assert self.mandriver.find_element(*MultiMan.myProfile_Location_Text).text == '隐藏'
                    logging.info("===断言成功===")
                else:
                    logging.info("===我的简介-定位有具体定位，为隐藏===")
                    print(self.mandriver.find_element(*MultiMan.myProfile_Location_Popover2edIcon_Text).text)
                    assert self.mandriver.find_element(*MultiMan.myProfile_Location_Popover2edIcon_Text).text == '隐藏'
                    self.mandriver.find_element(*MultiMan.myProfile_Location_Popover1stIcon).click()
                    self.mandriver.find_element(*MultiMan.myProfile_Location_PopoverConfirmBtn).click()
                    time.sleep(3)
                    assert self.mandriver.find_element(*MultiMan.myProfile_Location_Text).text!='隐藏'
                    logging.info("===断言成功===")
            else:
                logging.info("===我的简介-定位显示具体定位，准备切换成隐藏===")
                self.mandriver.find_element(*MultiMan.myProfile_Location_All).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_Location_Popover2edIcon_Text).text == '隐藏', '隐藏不在第二个位置'
                self.mandriver.find_element(*MultiMan.myProfile_Location_Popover2edIcon).click()
                self.mandriver.find_element(*MultiMan.myProfile_Location_PopoverConfirmBtn).click()
                time.sleep(2)
                assert self.mandriver.find_element(*MultiMan.myProfile_Location_Text).text == '隐藏'
                logging.info("===断言成功===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-定位切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-定位切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例142：我的简介-语言')
    def test_homepage142(self):
        logging.info("===我的简介-语言===")
        try:
            myProfile_Language_Text_case=self.mandriver.find_element(*MultiMan.myProfile_Language_Text)
            myProfile_Language_Text_caseName=myProfile_Language_Text_case.text
            myProfile_Language_Text_case.click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.myProfile_Language_title).text == '语言', '并没有跳转语言页面'
            myProfile_Language_ChooseLanguageText_case = self.mandriver.find_element(*MultiMan.myProfile_Language_ChooseLanguageText).text
            assert myProfile_Language_ChooseLanguageText_case.find(myProfile_Language_Text_caseName)>=0
            self.mandriver.find_element(*MultiMan.myProfile_Language_ChooseLanguage).click()
            self.mandriver.find_element(*MultiMan.myProfile_Language_PopoverCancelBtn).click()
            # self.mandriver.find_element(*MultiMan.myProfile_Language_goback).click()
            logging.info("===断言成功===")
        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例143：我的简介-语言切换')
    def test_homepage143(self):
        logging.info("===我的简介-语言切换===")
        try:
            # Language_Text_case=self.mandriver.find_element(*MultiMan.myProfile_Language_Text).text
            # self.mandriver.find_element(*MultiMan.myProfile_Language_All).click()
            # assert self.mandriver.find_element(*MultiMan.myProfile_Language_title).text == '语言', '并没有跳转语言页面'
            self.mandriver.find_element(*MultiMan.myProfile_Language_LanguageEnglish).click()
            self.mandriver.find_element(*MultiMan.myProfile_Language_PopoverConfirmBtn).click()
            assert self.mandriver.find_element(*MultiMan.myProfile_Language_ChooseLanguageText).text == '英语(English)'
            self.mandriver.find_element(*MultiMan.myProfile_Language_goback).click()
            assert self.mandriver.find_element(*MultiMan.myProfile_Language_Text).text =='英语'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-语言切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-语言切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例144-145：我的简介-第二语言显示和切换')
    def test_homepage144(self):
        logging.info("===我的简介-第二语言显示和切换===")
        try:
            SecondLanguage_textContents_case=self.multiman.myProfile_SecondLanguage_textContents()
            if SecondLanguage_textContents_case!=False:
                logging.info("===我的简介-第二语言有显示===")
                second_lan=SecondLanguage_textContents_case.text
                print(second_lan)
                SecondLanguage_textContents_case.click()
                time.sleep(2)
                assert self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_title).text == '第二语言', '并没有跳转第二语言页面'
                SecondLanguage_ChooseLanguageText_case2=self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_ChooseLanguageText).text
                assert SecondLanguage_ChooseLanguageText_case2 != 'None(None)' and SecondLanguage_ChooseLanguageText_case2.find(second_lan) >= 0
                self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_ChooseLanguageAll).click()
                self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_PopoverCancelBtn).click()
                time.sleep(2)
                if second_lan=='马来语':
                    logging.info("===是马来语，开始切换印度尼西亚语===")
                    self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_LanguageIndonesia).click()
                    self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_PopoverConfirmBtn).click()
                    assert self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_ChooseLanguageText).text == '印度尼西亚语(bahasa Indonesia)'
                    self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_goback).click()
                    assert self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_Text).text == '印度尼西亚语'
                    logging.info("===断言成功===")
                else:
                    logging.info("===不是马来语，开始切换成马来语===")
                    self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_LanguageMalayu).click()
                    self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_PopoverConfirmBtn).click()
                    assert self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_ChooseLanguageText).text == '马来语(bahasa Melayu)'
                    self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_goback).click()
                    assert self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_Text).text == '马来语'
                    logging.info("===断言成功===")
            else:
                logging.info("===我的简介-第二语言没有===")
                self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_All).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_title).text == '第二语言', '并没有跳转第二语言页面'
                assert self.mandriver.find_element(*MultiMan.myProfile_Language_ChooseLanguageText).text == 'None(None)'
                self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_ChooseLanguageAll).click()
                self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_PopoverCancelBtn).click()
                logging.info("===没有语言，开始切换成马来语===")
                self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_LanguageMalayu).click()
                self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_PopoverConfirmBtn).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_ChooseLanguageText).text == '马来语(bahasa Melayu)'
                self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_goback).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_SecondLanguage_Text).text == '马来语'
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-第二语言显示和切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-第二语言显示和切换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例146：我的简介-自我介绍')
    def test_homepage146(self):
        logging.info("===我的简介-自我介绍===")
        try:
            self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_All).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_title).text == '自我介绍'
            if man_pageSelfIntroduction==False:
                assert self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_content).text =='输入你的自我介绍'
            else:
                assert self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_content).text == man_pageSelfIntroduction, '自我介绍的内容与个人主页不符合'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-自我介绍')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-自我介绍')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例147：我的简介-自我介绍修改')
    def test_homepage147(self):
        logging.info("===我的简介-自我介绍修改===")
        try:
            newIntro='oh!happy every 1 dayyy'
            # self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_All).click()
            # assert self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_title).text == '自我介绍', '并未跳转到自我介绍页面'
            SelfIntr = self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_content).text
            if man_pageSelfIntroduction != False:
                self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_content).clear()
            self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_content).send_keys(newIntro)
            # assert self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_content).text!=SelfIntr
            self.mandriver.find_element(*MultiMan.myProfile_SelfIntroduction_CommitBtn).click()
            self.multiman.system_goback_key()
            self.multiman.tab_Mine_Btn()
            self.multiman.tab_Mine_Head()
            assert self.mandriver.find_element(*MultiMan.user_ownPage_selfIntroduction).text==newIntro
            self.multiman.system_goback_key()
            self.mandriver.find_element(*MultiMan.myProfile_entry_man).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-自我介绍修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-自我介绍修改')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例148：我的简介-google弹窗')
    def test_homepage148(self):
        logging.info("===我的简介-google弹窗===")
        try:
            self.mandriver.find_element(*MultiMan.myProfile_Google_All).click()
            # assert self.mandriver.find_element(*MultiMan.myProfile_Google_Popover)
            assert self.mandriver.find_element(*MultiMan.myProfile_Google_PopoverFirstAccountAll)
            assert self.mandriver.find_element(*MultiMan.myProfile_Google_PopoverAccountAddText).text == '再添加一个帐号'
            self.multiman.system_goback_key()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-google弹窗')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-google弹窗')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例149：我的简介-手机号显示')
    def test_homepage149(self):
        logging.info("===我的简介-手机号显示===")
        try:
            global login_phone
            login_phone = self.mandriver.find_element(*MultiMan.myProfile_Phone_entryText).text
            assert login_phone=='8618****00000'
            # assert login_phone.find('****')>=0
            logging.info("===断言成功===")

            # # 兼容未手机号注册
            # time.sleep(3)
            # if len(self.mandriver.find_elements(*MultiMan.myProfile_Phone_entryText)) == 0:
            #     logging.info("===手机号未绑定-进绑定页面===")
            #     self.mandriver.find_element(*MultiMan.myProfile_Gmail_entry).click()
            #     time.sleep(8)
            #     assert self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindTitle).text == '绑定Gmail邮箱'
            #     assert self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindMailTips).text == '@gmail.com'
            #     assert self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindConfirmBtn)
            #     self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindGoback).click()
            # else:
            #     logging.info("===手机号已绑定-进换绑界面===")
            #     entry_test1 = self.mandriver.find_element(*MultiMan.myProfile_Gmail_entryText)
            #     assert entry_test1.text.find('@gmail.com') >= 0
            #     entry_test1.click()
            #     self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindChangePopConf).click()
            #     time.sleep(3)
            #     assert self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindTitle).text == '换绑Gmail邮箱'
            #     self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindGoback).click()
            # logging.info("===断言成功===")









        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-手机号显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-手机号显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例150：我的简介-手机号更换')
    def test_homepage150(self):
        logging.info("===我的简介-手机号更换===")
        try:
            time.sleep(3)
            self.mandriver.find_element(*MultiMan.myProfile_Phone_entryAll).click()
            self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeCancelAll).click()
            self.mandriver.find_element(*MultiMan.myProfile_Phone_entryAll).click()
            self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeNumText).click()
            assert self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeTitle).text == '请验证原手机号'
            login_phone_area = self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeAreaCode).text
            assert login_phone_area=='+86'
            assert self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangePhoneNum).text=='18868100000'
            self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeVerCode).send_keys('3795')
            self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeNextBtn).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeTitle).text == '更换手机号'
            assert self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeAreaCode).text == '+99999'
            self.mandriver.find_element(*MultiMan.myProfile_Phone_ChangeGoback).click()
            logging.info("===断言成功===")


        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-手机号更换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-手机号更换')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例151：我的简介-Gmail')
    def test_homepage151(self):
        logging.info("===我的简介-Gmail===")
        try:
            time.sleep(3)
            if len(self.mandriver.find_elements(*MultiMan.myProfile_Gmail_entryText))==0:
                logging.info("===Gmail未绑定-进绑定页面===")
                self.mandriver.find_element(*MultiMan.myProfile_Gmail_entry).click()
                time.sleep(8)
                assert self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindTitle).text == '绑定Gmail邮箱'
                assert self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindMailTips).text == '@gmail.com'
                assert self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindConfirmBtn)
                self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindGoback).click()
            else:
                logging.info("===Gmail已绑定-进换绑界面===")
                entry_test1=self.mandriver.find_element(*MultiMan.myProfile_Gmail_entryText)
                assert entry_test1.text.find('@gmail.com')>=0
                entry_test1.click()
                self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindChangePopConf).click()
                time.sleep(3)
                assert self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindTitle).text == '换绑Gmail邮箱'
                self.mandriver.find_element(*MultiMan.myProfile_Gmail_BindGoback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-Gmail')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-Gmail')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的简介')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例152-153：我的简介-密码显示')
    def test_homepage152(self):
        logging.info("===我的简介-密码显示===")
        try:
            if self.multiman.myProfile_Password_entryTextEle():
                logging.info("===已经设置过密码，重置步骤===")
                assert self.mandriver.find_element(*MultiMan.myProfile_Password_entryText).text == '重置'
                self.mandriver.find_element(*MultiMan.myProfile_Password_entryAll).click()
                self.mandriver.find_element(*MultiMan.myProfile_Password_popoverResetCancel).click()
                self.mandriver.find_element(*MultiMan.myProfile_Password_entryAll).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_Password_popoverResetText).text == '重置密码'
                self.mandriver.find_element(*MultiMan.myProfile_Password_popoverResetAll).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_Password_ResetTitle).text == '设置登录密码'
                self.multiman.system_goback_key()
                self.multiman.system_goback_key()
                self.multiwoman.system_goback_key()
                logging.info("===断言成功===")
            elif self.mandriver.find_element(*MultiMan.myProfile_Password_entryRedDot):
                logging.info("===没有密码，设置过程===")
                self.mandriver.find_element(*MultiMan.myProfile_Password_entryAll).click()
                assert self.mandriver.find_element(*MultiMan.myProfile_Password_ChangeTitle).text == '修改登录密码'
                self.multiman.system_goback_key()
                self.multiman.system_goback_key()
                self.multiwoman.system_goback_key()
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的简介-密码显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的简介-密码显示')
            logging.info(f'截图成功，图片为{screen_name}')
            raise






    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例154-155：我的余额-入口-我的钻石')
    def test_homepage154(self):
        logging.info("===我的简介-入口-我的钻石===")
        try:
            time.sleep(3)
            global entryDiamondNum_man
            entryDiamondNum_man = self.mandriver.find_element(*MultiMan.myBalance_entryDiamondManNum).text
            self.mandriver.find_element(*MultiMan.myBalance_entryManAll).click()
            time.sleep(2)
            global myDiamondCount
            myDiamondCount = self.mandriver.find_element(*MultiMan.myBalance_myDiamondCountText).text
            print(myDiamondCount)
            print(type(myDiamondCount))
            assert '{}''[diamond]'.format(myDiamondCount) == entryDiamondNum_man
            assert self.mandriver.find_element(*MultiMan.myBalance_agreeContent).text == '同意用户协议和隐私政策！'
            logging.info("===男用户-我的余额入口-断言成功===")
            self.multiwoman.tab_Mine_Btn()
            entryDiamondNum_woman = self.womandriver.find_element(*MultiWoman.myBalance_entryDiamondWomanNum).text
            self.womandriver.find_element(*MultiWoman.myBalance_entryWomanAll).click()
            myDiamondCount=self.womandriver.find_element(*MultiWoman.myBalance_myDiamondCountText).text
            assert '{}''[diamond]'.format(myDiamondCount) == entryDiamondNum_woman
            self.multiwoman.system_goback_key()
            logging.info("===女用户-我的余额入口-断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的余额-入口-我的钻石')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的余额-入口-我的钻石')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例156：我的余额-free入口')
    def test_homepage156(self):
        logging.info("===我的余额-free入口===")
        try:
            self.mandriver.find_element(*MultiMan.myBalance_topOffers_Entry).click()
            assert self.mandriver.find_element(*MultiMan.myBalance_topOffers_Title).text == 'Top Offers'
            assert self.mandriver.find_element(*MultiMan.myBalance_topOffers_AllOffers).text == 'All Offers'
            self.mandriver.find_element(*MultiMan.myBalance_topOffers_Goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的余额-free入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的余额-free入口')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例157：我的余额-充值档位')
    def test_homepage157(self):
        logging.info("===我的余额-充值档位===")
        try:
            assert len(self.mandriver.find_elements(*MultiMan.myBalance_TopUpList5Id))==5
            assert self.mandriver.find_elements(*MultiMan.myBalance_TopUpListmoreBtn)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的余额-充值档位')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的余额-充值档位')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的余额')
    @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例158：我的余额-充值档位-充值')
    def test_homepage158(self):
        logging.info("===我的余额-充值档位-充值===")
        try:
            result_old1 = self.mandriver.find_element(*MultiMan.myBalance_myDiamondCountText).text
            result_old = self.multiman.string_find_num(result_old1)
            self.mandriver.find_elements(*MultiMan.myBalance_TopUpList5Id)[0].click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.myBalance_TopUp_googleTestCardXpath)
            self.mandriver.find_element(*MultiMan.myBalance_TopUp_googleBuyBtnXpath).click()
            time.sleep(5)
            assert self.mandriver.find_element(*MultiMan.myBalance_TopUp_successText).text=='恭喜！你得到4,500[diamond]'
            self.mandriver.find_element(*MultiMan.myBalance_TopUp_successKnowBtn).click()
            result_new=self.mandriver.find_element(*MultiMan.myBalance_myDiamondCountText).text
            result_NEW = self.multiman.string_find_num(result_new)
            assert int(result_NEW)==int(result_old)+int('4500')
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的余额-充值档位-充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的余额-充值档位-充值')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例159：我的余额-充值档位-more')
    def test_homepage159(self):
        logging.info("===我的余额-充值档位-more===")
        try:
            if len(self.mandriver.find_elements(*MultiMan.myBalance_TopUpListmoreBtn))==0:
                pytest.skip('该用户没有第三方充值')
            else:
                self.mandriver.find_element(*MultiMan.myBalance_TopUpListmoreBtn).click()
                time.sleep(5)
                assert self.mandriver.find_element(*MultiMan.myBalance_TopUpListmoreTitle)
                self.multiman.system_goback_key()
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的余额-充值档位-more')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的余额-充值档位-more')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例160：我的余额-历史详情')
    def test_homepage160(self):
        logging.info("===我的余额-历史详情===")
        try:
            self.mandriver.find_element(*MultiMan.myBalance_DiamondDetailEntry).click()
            time.sleep(5)
            assert self.mandriver.find_element(*MultiMan.myBalance_DiamondDetail_TitleXpath)
            self.multiman.system_goback_key()
            # assert self.mandriver.find_element(*MultiMan.myBalance_DiamondDetail_selectTab)
            # assert self.mandriver.find_element(*MultiMan.myBalance_DiamondDetail_ContentBox)
            # self.mandriver.find_element(*MultiMan.myBalance_DiamondDetail_Goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的余额-历史详情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的余额-历史详情')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('我的余额')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例161：我的余额-客服按钮')
    def test_homepage161(self):
        logging.info("===我的余额-客服按钮===")
        try:
            self.mandriver.find_element(*MultiMan.myBalance_ServiceEntry).click()
            assert self.mandriver.find_element(*MultiMan.myBalance_Service_title).text == '在线客服'
            assert self.mandriver.find_element(*MultiMan.myBalance_Service_helpInput)
            self.mandriver.find_element(*MultiMan.myBalance_Service_goback).click()
            self.mandriver.find_element(*MultiMan.myBalance_entry_goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的余额-客服按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的余额-客服按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise



    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例162：我的页面-设置')
    def test_homepage162(self):
        logging.info("===我的页面-设置===")
        try:
            self.multiman.tab_Mine_Btn()
            time.sleep(2)
            self.multiman.tap(930,2123)
            self.multiman.swipe(626,1000,626,933)
            self.mandriver.find_element(*MultiMan.settings_entry).click()
            assert self.mandriver.find_element(*MultiMan.settings_title).text=='设置'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例163：我的页面-设置-APP语言')
    def test_homepage163(self):
        logging.info("===我的页面-设置-APP语言===")
        try:
            # self.l.tab_Mine_Btn()
            # time.sleep(2)
            # self.l.swipe(626, 1572, 626, 933)
            App_lan=self.mandriver.find_element(*MultiMan.settings_AppLanguage_selectedText).text
            print(App_lan)
            self.mandriver.find_element(*MultiMan.settings_AppLanguage_All).click()
            time.sleep(2)
            assert self.mandriver.find_element(*MultiMan.settings_AppLanguageTitle).text == 'APP语言'
            assert self.mandriver.find_element(*MultiMan.settings_AppLanguage_AutomaticText).text == App_lan
            self.mandriver.find_element(*MultiMan.settings_AppLanguage_English).click()
            self.mandriver.find_element(*MultiMan.settings_AppLanguage_saveBtn).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-APP语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-APP语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例164：我的页面-设置-切换APP语言')
    def test_homepage164(self):
        logging.info("===我的页面-设置-切换APP语言===")
        try:
            self.multiman.tab_Mine_Btn()
            time.sleep(1)
            self.multiman.swipe(626, 1100, 626, 933)
            self.mandriver.find_element(*MultiMan.settings_entry).click()
            App_lan = self.mandriver.find_element(*MultiMan.settings_AppLanguage_selectedText).text
            assert App_lan == 'English'
            self.mandriver.find_element(*MultiMan.settings_AppLanguage_All).click()
            self.mandriver.find_element(*MultiMan.settings_AppLanguage_Automatic).click()
            self.mandriver.find_element(*MultiMan.settings_AppLanguage_saveBtn).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-切换APP语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-切换APP语言')
            logging.info(f'截图成功，图片为{screen_name}')
            raise






    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例165-166：我的页面-设置-黑名单')
    def test_homepage165(self):
        logging.info("===我的页面-设置-黑名单===")
        try:
            self.multiman.tab_Mine_Btn()
            time.sleep(2)
            # self.multiman.swipe(626, 1572, 626, 933)
            self.mandriver.find_element(*MultiMan.settings_entry).click()
            self.mandriver.find_element(*MultiMan.settings_blocklist).click()
            NoUserEle=self.multiman.settings_blockList_NoUserTextEle()
            if NoUserEle!=False:
                logging.info("===无用户===")
                assert NoUserEle == '无用户'
                self.mandriver.find_element(*MultiMan.settings_blocklist_goback).click()
                logging.info("===断言成功===")
            else:
                logging.info("===有用户===")
                firstUserName = self.mandriver.find_elements(*MultiMan.settings_blocklist_UserNameList)[0].text
                self.mandriver.find_elements(*MultiMan.settings_blocklist_UserClickList)[0].click()
                assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName)
                # assert self.mandriver.find_element(*MultiMan.user_own_pagePersonalName).text == firstUserName
                self.mandriver.find_element(*MultiMan.user_own_pageFollowBtn).click()
                assert self.mandriver.find_element(*MultiMan.user_own_pageFollowBtn)
                self.multiman.system_goback_key()
                time.sleep(2)
                assert self.mandriver.find_element(*MultiMan.settings_blocklist_title).text=='黑名单'
                self.mandriver.find_element(*MultiMan.settings_blocklist_goback).click()
                logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-黑名单')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-黑名单')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例167：我的页面-设置-隐私政策')
    def test_homepage167(self):
        logging.info("===我的页面-设置-隐私政策===")
        try:
            self.mandriver.find_element(*MultiMan.settings_PrivacyPolicy).click()
            time.sleep(3)
            self.multiman.native_to_h5()
            assert self.mandriver.find_element(*MultiMan.settings_PrivacyPolicy_titleXpath).text == 'Privacy Policy', '隐私政策名称不一致'
            assert self.mandriver.find_element(*MultiMan.settings_PrivacyPolicy_HeadlineXpath)
            self.multiman.system_goback_key()
            self.multiman.h5_to_native()
            # self.mandriver.find_element(*MultiMan.settings_PrivacyPolicy_goback).click()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-隐私政策')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-隐私政策')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例168：我的页面-设置-用户协议')
    def test_homepage168(self):
        logging.info("===我的页面-设置-用户协议===")
        try:
            self.mandriver.find_element(*MultiMan.settings_UserAgreement).click()
            time.sleep(3)
            self.multiman.native_to_h5()
            # assert self.mandriver.find_element(*MultiMan.settings_UserAgreement_titleXpath).text=='User Agreement'
            assert self.mandriver.find_element(*MultiMan.settings_UserAgreement_titleXpath)
            # assert self.mandriver.find_element(*MultiMan.settings_UserAgreement_titleTextXpath)
            assert self.mandriver.find_element(*MultiMan.settings_UserAgreement_Welcome)
            self.mandriver.find_element(*MultiMan.settings_UserAgreement_titleAndGoback).click()
            self.multiman.h5_to_native()
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-用户协议')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-用户协议')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例169：我的页面-设置-关于我们')
    def test_homepage169(self):
        logging.info("===我的页面-设置-关于我们===")
        try:
            self.mandriver.find_element(*MultiMan.settings_AboutUs).click()
            time.sleep(3)
            assert self.mandriver.find_element(*MultiMan.settings_AboutUs_title).text == '关于我们', '关于我们名称不一致'
            assert self.mandriver.find_element(*MultiMan.settings_AboutUs_accountDeleteBtn)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-关于我们')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-关于我们')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例170：我的页面-设置-关于我们删除账户')
    def test_homepage170(self):
        logging.info("===我的页面-设置-关于我们删除账户===")
        try:
            self.mandriver.find_element(*MultiMan.settings_AboutUs_accountDeleteBtn).click()
            assert self.mandriver.find_element(*MultiMan.settings_AboutUs_deleteUserName).text ==man_pagePersonalName or newName
            assert self.mandriver.find_element(*MultiMan.settings_AboutUs_deleteDeleteBtn)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-关于我们删除账户')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-关于我们删除账户')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例171：我的页面-设置-关于我们删除账户-提示弹窗')
    def test_homepage171(self):
        logging.info("===我的页面-设置-关于我们删除账户-提示弹窗===")
        try:
            delete_reason='i do not want to play anymore,i want to delete it'
            self.mandriver.find_element(*MultiMan.settings_AboutUs_deleteEditReason).send_keys(delete_reason)
            time.sleep(1)
            self.mandriver.find_element(*MultiMan.settings_AboutUs_deleteDeleteBtn).click()
            assert self.mandriver.find_element(*MultiMan.settings_AboutUs_deletePopoverContentText).text=='删除账号后，你可以在14天内重新登录并恢复账号。14天后，你的账号将被永久删除且无法恢复。 请慎重考虑！'
            self.mandriver.find_element(*MultiMan.settings_AboutUs_deletePopoverCancel).click()
            assert self.mandriver.find_element(*MultiMan.settings_AboutUs_deleteUserName).text == man_pagePersonalName or newName
            self.multiman.system_goback_key()
            self.multiman.system_goback_key()
            # self.mandriver.find_element(*MultiMan.settings_AboutUs_deleteGoback).click()
            # self.mandriver.find_element(*MultiMan.settings_AboutUs_goback).click()

            # self.mandriver.find_element(*MultiMan.settings_AboutUs_deletePopoverConfirm).click()
            # assert self.mandriver.find_element(*LoginView.more_btn)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-关于我们删除账户-提示弹窗')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-关于我们删除账户-提示弹窗')
            logging.info(f'截图成功，图片为{screen_name}')
            raise


    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例172：我的页面-设置-为Chamet评分')
    def test_homepage172(self):
        logging.info("===我的页面-设置-为Chamet评分===")
        self.Login = LoginView(self.mandriver)
        try:
            # self.multiman.tab_Mine_Btn()
            # time.sleep(2)
            # self.multiman.swipe(626, 1572, 626, 933)
            # self.mandriver.find_element(*MultiMan.settings_entry_RightClick).click()
            self.mandriver.find_element(*MultiMan.settings_RateChamet).click()
            assert self.mandriver.find_element(*MultiMan.settings_RateChametText).text == '为Chamet评分', "页面点击后没停留设置页面"
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-为Chamet评分')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-为Chamet评分')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例173：我的页面-设置-清除缓存')
    def test_homepage173(self):
        logging.info("===我的页面-设置-清除缓存===")
        self.Login = LoginView(self.mandriver)
        try:
            self.mandriver.find_element(*MultiMan.settings_ClearCache).click()
            # 获取缓存已清除的文字toast
            self.mandriver.find_element(*MultiMan.settings_ClearCache).click()
            assert self.mandriver.find_element(*MultiMan.settings_ClearCache_cache).text == '0B'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-清除缓存')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-清除缓存')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例174：我的页面-设置-版本')
    def test_homepage174(self):
        logging.info("===我的页面-设置-版本===")
        self.Login = LoginView(self.mandriver)
        try:
            self.mandriver.find_element(*MultiMan.settings_versions).click()
            versions_versionText_case=self.mandriver.find_element(*MultiMan.settings_versions_versionText).text
            assert versions_versionText_case.find('3.5.')>=0
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-版本')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-版本')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例175：我的页面-设置-登出按钮')
    def test_homepage175(self):
        logging.info("===我的页面-设置-登出按钮===")
        self.Login = LoginView(self.mandriver)
        try:
            assert self.mandriver.find_element(*MultiMan.settings_logout_logoutText).text=='退出'
            self.mandriver.find_element(*MultiMan.settings_logout).click()
            assert self.mandriver.find_element(*MultiMan.settings_logout_popoverTitle).text == '确定退出？'
            self.multiman.tap(917,2010)
            self.mandriver.find_element(*MultiMan.settings_logout).click()
            self.mandriver.find_element(*MultiMan.settings_logout_popoverCancel).click()
            assert self.mandriver.find_element(*MultiMan.settings_logout_logoutText).text == '退出'
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-登出按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-登出按钮')
            logging.info(f'截图成功，图片为{screen_name}')
            raise

    @allure.story('设置')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例176：我的页面-设置-登出按钮-登出')
    def test_homepage176(self):
        logging.info("===我的页面-设置-登出按钮-登出===")
        try:
            self.mandriver.find_element(*MultiMan.settings_logout).click()
            settings_logout_popoverConfirm2=self.mandriver.find_element(*MultiMan.settings_logout_popoverConfirm)
            assert settings_logout_popoverConfirm2.text == '好的'
            settings_logout_popoverConfirm2.click()
            assert self.mandriver.find_element(*MultiMan.more_btn)
            logging.info("===断言成功===")

        except AssertionError as e:
            logging.info('===断言失败===')
            screen_name = self.multiman.screenshot('我的页面-设置-登出按钮-登出')
            logging.info(f'截图成功，图片为{screen_name}')
            raise
        except:
            logging.info("===执行失败===")
            screen_name = self.multiman.screenshot('我的页面-设置-登出按钮-登出')
            logging.info(f'截图成功，图片为{screen_name}')
            raise




if __name__ == '__main__':
    pytest.main([".\test_case\test_mypage_multi.py","-vs","--alluredir=.\result\mypage_result\2023_08_24_001"])


    #allure报告数据存放路径
    # pytest.main([".\test_case\test_mypage_multi.py","-vs","--alluredir",".\result\tmp\2023_08_24_001"])
    #运行源数据，生成操作，报告存放目录，每次运行删除上一次的数据
    # os.system("allure generate .\result\tmp\2023_08_24_001 -o ./report/mypage_reports  --clean")




''' pytest .\test_mypage_multi.py -s -v --alluredir=..\result\mypage_result\2023_8_24_001'''
# '''pytest ./test_case/est_mypage_multi.py - vs --alluredir= D:\chamet_mypage_multi_testProject-8.10\result\mypage_result\2023_08_15_001'''
'''allure serve ..\result\mypage_result\2023_8_24_001'''
# D:\chamet_mypage_multi_testProject-8.15.2\result\mypage_result\2023_8_17_001
# pytest .\test_mypage_multi.py -s -v --alluredir=..\result\mypage_result\2023_8_17