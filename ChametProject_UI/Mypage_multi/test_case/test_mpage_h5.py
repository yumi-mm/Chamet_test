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
            global newName
            newName = 'Tom33364388mmm'
            global newIntro
            newIntro = 'oh!happy every 1 dammm'

            global man_sign_time
            man_sign_time = 1
            global woman_sign_time
            woman_sign_time = 1

            # 女生个人主页
            # 85手机
            # self.multiwoman.tap(930, 2123)
            # 126手机
            self.multiwoman.tap(963, 2268)
            self.multiwoman.tab_Mine_Btn_126()
            # self.multiwoman.tab_Mine_Head()
            # time.sleep(2)
            # global woman_pageSelfIntroduction, woman_pagePersonalName
            # woman_pageSelfIntroduction = self.multiwoman.user_ownPage_selfIntroductionEle()
            # woman_pagePersonalName = self.womandriver.find_element(*MultiWoman.user_own_pagePersonalName).text
            # assert self.womandriver.find_element(*MultiWoman.user_own_pagePersonalInformationText), "没有通过头像找到个人主页元素"
            # logging.info("断言成功")
            # self.womandriver.find_element(*MultiWoman.user_own_pageGobackBtn).click()
            # # print(woman_pageSelfIntroduction, woman_pagePersonalName)


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








    @allure.story('我的收入')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例165：我的收入-入口跳转')
    def test_homepage165(self):
        logging.info("===我的收入-入口跳转===")
        try:
            assert self.mandriver.find_element(*MultiMan.MyBalance_entry_manText).text=='提现'
            self.mandriver.find_element(*MultiMan.MyBalance_entry_man).click()
            time.sleep(3)
            self.multiman.native_to_h5()
            # self.mandriver.switch_to.frame('contentFrame')
            self.multiman.tap(545, 120)
            time.sleep(3)
            # logging.info("===男用户入口跳转成功===")
            assert self.mandriver.find_element(*MultiMan.MyBalance_earnText)
            self.multiman.system_goback_key()
            self.multiman.h5_to_native()
            logging.info("===男用户断言成功===")
            assert self.womandriver.find_element(*MultiWoman.MyBalance_entry_womanText).text == '提现'
            self.womandriver.find_element(*MultiWoman.MyBalance_entry_woman).click()
            time.sleep(3)
            self.multiwoman.native_to_h5()
            # self.womandriver.switch_to.frame('contentFrame')
            # logging.info("===女用户入口跳转成功===")
            self.multiwoman.tap(737,212)
            time.sleep(3)
            assert self.womandriver.find_element(*MultiWoman.MyBalance_earnText_price)
            # '//*[@id="app"]/div/div/div[2]/div[1]/div/div[1]/div'
            self.multiwoman.system_goback_key()
            self.multiwoman.h5_to_native()
            logging.info("===女用户断言成功===")


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
    @allure.title('用例166：我的邀请-男女入口显示及跳转')
    def test_homepage166(self):
        logging.info("===我的邀请-男女入口显示及跳转===")
        try:
            logging.info("===我的邀请-男用户-入口显示===")
            assert self.mandriver.find_element(*MultiMan.MyInvite_entry_FreeCardsText).text == '免费卡片'
            self.multiman.MyInvite_entry_AllEle()
            time.sleep(3)
            self.multiman.native_to_h5()
            self.multiman.tap(545, 120)
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
    @allure.title('用例167：我的邀请-男-问号按钮')
    def test_homepage167(self):
        logging.info("===我的邀请-男-问号按钮===")
        try:
            # time.sleep(3)
            self.multiman.tap(814,405)
            context = self.mandriver.contexts
            print(context)
            logging.info("===问号按钮===")
            # self.mandriver.switch_to.frame()
            # self.mandriver.find_element(*MultiMan.MyInvite_instructionsBtn).click()
            self.multiman.tap(814, 405)
            # self.multiman.tap(989, 186)
            item6=self.mandriver.find_element(*MultiMan.MyInvite_instructionsBtn)
            self.mandriver.execute_script("arguments[0].click();", item6)
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
    @allure.title('用例168：我的邀请-男-邀请好友按钮')
    def test_homepage168(self):
        logging.info("===我的邀请-男-邀请好友按钮===")
        try:
            logging.info("===邀请好友按钮===")
            context = self.mandriver.contexts
            print(context)
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
    @allure.title('用例169：我的邀请-邀请列表')
    def test_homepage169(self):
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
    @allure.title('用例170：我的邀请-周排行')
    def test_homepage170(self):
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





    @allure.story('我的背包')
    # @pytest.mark.skip(reason="本次不执行")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('用例171：我的背包-入口跳转')
    def test_homepage171(self):
        logging.info("===我的背包-入口跳转===")
        try:
            global backpack_entryNum
            backpack_entryNum=self.mandriver.find_element(*MultiMan.myBackpack_entryText).text
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


  #
    # @allure.story('我的背包')
    # # @pytest.mark.skip(reason="本次不执行")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例165：我的背包-入口跳转')
    # def test_homepage165(self):
    #     logging.info("===我的背包-入口跳转===")
    #     try:
    #         global backpack_entryNum
    #         backpack_entryNum=self.mandriver.find_element(*MultiMan.myBackpack_entryText).text
    #         self.mandriver.find_element(*MultiMan.myBackpack_entryAll).click()
    #         assert self.mandriver.find_element(*MultiMan.myBackpack_title).text=='我的背包'
    #         # self.multiman.system_goback_key()
    #         logging.info("===男用户入口跳转成功===")
    #         # assert self.womandriver.find_element(*MultiWoman.myBackpack_entryText)
    #         # self.womandriver.find_element(*MultiWoman.myBackpack_entryAll).click()
    #         # assert self.womandriver.find_element(*MultiWoman.myBackpack_title).text == '我的背包'
    #         # self.multiwoman.system_goback_key()
    #         # logging.info("===女用户入口跳转成功===")
    #
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multiman.screenshot('我的背包-入口跳转')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info("===执行失败===")
    #         screen_name = self.multiman.screenshot('我的背包-入口跳转')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #
    # @allure.story('我的背包')
    # # @pytest.mark.skip(reason="本次不执行")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例166：我的背包-内外数量显示')
    # def test_homepage166(self):
    #     logging.info("===我的背包-内外数量显示===")
    #     try:
    #         global backpack_FrameNum
    #         global backpack_EntranceNum
    #         backpack_FrameNum1 = self.mandriver.find_element(*MultiMan.myBackpack_Frame_Num).text
    #         backpack_EntranceNum1 = self.mandriver.find_element(*MultiMan.myBackpack_EntranceEffect_Num).text
    #         backpack_FrameNum = int(re.findall("\d+", backpack_FrameNum1)[0])
    #         backpack_EntranceNum = int(re.findall("\d+", backpack_EntranceNum1)[0])
    #         print(backpack_FrameNum,backpack_EntranceNum)
    #         inner_num=backpack_FrameNum+backpack_EntranceNum
    #         assert inner_num==int(backpack_entryNum)
    #         logging.info("===断言成功===")
    #
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multiman.screenshot('我的背包-内外数量显示')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info("===执行失败===")
    #         screen_name = self.multiman.screenshot('我的背包-内外数量显示')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #
    # @allure.story('我的背包')
    # # @pytest.mark.skip(reason="本次不执行")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例167：我的背包-当前使用—头像框显示')
    # def test_homepage167(self):
    #     logging.info("===我的背包-当前使用—头像框显示===")
    #     try:
    #         assert self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_NameText).text=='头像框'
    #         # backpack_FrameNum1 = self.mandriver.find_element(*MultiMan.myBackpack_Frame_Num).text
    #         # num1 = int(re.findall("\d+", backpack_FrameNum1)[0])
    #         # if num1 == 0:
    #         if backpack_FrameNum == 0:
    #             assert len(self.mandriver.find_elements(*MultiMan.myBackpack_Frame_inUse_Head))==0
    #             self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_NoneImage).click()
    #             time.sleep(1)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_NoneImage)
    #             logging.info("===头像框数量为0，断言成功===")
    #         else:
    #             self.mandriver.find_elements(*MultiMan.myBackpack_Frame_inUse_Head).click()
    #             time.sleep(1)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_PopTag)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_PopSourceLink)
    #             assert len(self.mandriver.find_elements(*MultiMan.myBackpack_Frame_inUse_PopFrame1))!=0 or len(self.mandriver.find_elements(*MultiMan.myBackpack_Frame_inUse_PopFrame2))!=0
    #             self.multiman.tap(929,685)
    #             logging.info("===有头像框，断言成功===")
    #
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multiman.screenshot('我的背包-当前使用—头像框显示')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info("===执行失败===")
    #         screen_name = self.multiman.screenshot('我的背包-当前使用—头像框显示')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #
    # @allure.story('我的背包')
    # # @pytest.mark.skip(reason="本次不执行")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例168：我的背包-当前使用—进场效果显示')
    # def test_homepage168(self):
    #     logging.info("===我的背包-当前使用—进场效果显示===")
    #     try:
    #         assert self.mandriver.find_element(*MultiMan.myBackpack_Entrance_inUse_NameText).text == '进场效果'
    #         # myBackpack_EntranceEffect_Num1 = self.mandriver.find_element(*MultiMan.myBackpack_EntranceEffect_Num).text
    #         # num2 = int(re.findall("\d+", myBackpack_EntranceEffect_Num1)[0])
    #         # if num2 == 0:
    #         if backpack_EntranceNum == 0:
    #             self.mandriver.find_element(*MultiMan.myBackpack_Entrance_inUse_NoneImage).click()
    #             time.sleep(2)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Entrance_inUse_NoneImage)
    #             logging.info("===进场效果数量为0，断言成功===")
    #         else:
    #             self.mandriver.find_elements(*MultiMan.myBackpack_Entrance_inUse_Image).click()
    #             time.sleep(2)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Entrance_inUse_PopTag)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Entrance_inUse_PopPreviewImg)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Entrance_inUse_PopSourceLink)
    #             self.mandriver.find_element(*MultiMan.myBackpack_Entrance_inUse_PopPreviewBtn).click()
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Entrance_inUse_PreviewEffect)
    #             self.multiman.system_goback_key()
    #             self.multiman.tap(929, 685)
    #             logging.info("===有进场效果，断言成功===")
    #
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multiman.screenshot('我的背包-当前使用—进场效果显示')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info("===执行失败===")
    #         screen_name = self.multiman.screenshot('我的背包-当前使用—进场效果显示')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #
    # @allure.story('我的背包')
    # # @pytest.mark.skip(reason="本次不执行")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.title('用例169：我的背包-所有道具—头像框预览')
    # def test_homepage169(self):
    #     logging.info("===我的背包-所有道具—头像框预览===")
    #     try:
    #         if backpack_FrameNum==0:
    #         assert self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_NameText).text == '头像框'
    #         backpack_FrameNum1 = self.mandriver.find_element(*MultiMan.myBackpack_Frame_Num).text
    #         num1 = int(re.findall("\d+", backpack_FrameNum1)[0])
    #         if num1 == 0:
    #             assert len(self.mandriver.find_elements(*MultiMan.myBackpack_Frame_inUse_Head)) == 0
    #             self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_NoneImage).click()
    #             time.sleep(1)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_NoneImage)
    #             logging.info("===头像框数量为0，断言成功===")
    #         else:
    #             self.mandriver.find_elements(*MultiMan.myBackpack_Frame_inUse_Head).click()
    #             time.sleep(1)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_PopTag)
    #             assert self.mandriver.find_element(*MultiMan.myBackpack_Frame_inUse_PopSourceLink)
    #             assert len(self.mandriver.find_elements(*MultiMan.myBackpack_Frame_inUse_PopFrame1)) != 0 or len(
    #                 self.mandriver.find_elements(*MultiMan.myBackpack_Frame_inUse_PopFrame2)) != 0
    #             self.multiman.tap(929, 685)
    #             logging.info("===有头像框，断言成功===")
    #
    #     except AssertionError as e:
    #         logging.info('===断言失败===')
    #         screen_name = self.multiman.screenshot('我的背包-所有道具—头像框预览')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #     except:
    #         logging.info("===执行失败===")
    #         screen_name = self.multiman.screenshot('我的背包-所有道具—头像框预览')
    #         logging.info(f'截图成功，图片为{screen_name}')
    #         raise
    #
    #





if __name__ == '__main__':
    pytest.main([".\test_case\test_mpage_h5.py","-vs","--alluredir=..\result\mypage_result\2023_h5_10_07_001"])


    #allure报告数据存放路径
    # pytest.main([".\test_case\test_mypage_multi.py","-vs","--alluredir",".\result\tmp\2023_08_24_001"])
    #运行源数据，生成操作，报告存放目录，每次运行删除上一次的数据
    # os.system("allure generate .\result\tmp\2023_08_24_001 -o ./report/mypage_reports  --clean")




''' pytest .\test_mpage_h5.py -s -v --alluredir=..\result\mypage_result\2023_h5_10_07_001'''
# '''pytest ./test_case/est_mypage_multi.py - vs --alluredir= D:\chamet_mypage_multi_testProject-8.10\result\mypage_result\2023_08_15_001'''
'''allure serve ..\result\mypage_result\2023_h5_10_07_001'''
# D:\chamet_mypage_multi_testProject-8.15.2\result\mypage_result\2023_8_17_001
# pytest .\test_mypage_multi.py -s -v --alluredir=..\result\mypage_result\2023_8_17