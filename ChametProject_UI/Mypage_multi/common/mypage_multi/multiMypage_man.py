# -*- coding: utf-8 -*-

import logging
import re

from appium.webdriver.common.appiumby import AppiumBy

from common.mypage_multi.mypage_common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from businessView.login_phoneView import LoginView
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import time


class MultiMan(Common):

    randomCall_popover=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout')
    my_list_man = {
        "留言": "(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]')"
        ,"我的等级":  "(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout')"
        ,"我的余额":  "(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]')"
        , "我的任务": "(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]')"
        , "我的背包": "(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[5]')"
        , "我的邀请": "(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[6]')"
        , "我的简介": "(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[7]')"
        , "我的收入":" (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[8]')"
        , "设置": "(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[9]')"
    }

    my_list_woman={
        "我的收入": "(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]')"
        , "我的简介": "(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[6]')"
        , "我的打招呼": " (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[7]')"
        , "我的余额": "(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[8]')"

    }

    my_list_womanText = {
      "我的收入": "(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.TextView')"
    , "我的余额": "(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[8]/android.widget.LinearLayout/android.widget.TextView')"

    }


    # =========个人主页顶部=========
    tab_mine_btn = (By.ID, 'com.hkfuliao.chamet:id/rl_tab_mine')
    tab_mine_head = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    user_own_pagePersonalInformationText = (By.XPATH, '//android.widget.LinearLayout[@content-desc="个人信息"]/android.widget.FrameLayout/android.widget.TextView')
    user_own_pagePersonalName = (By.ID, 'com.hkfuliao.chamet:id/tv_user_name')
    user_own_pageGobackBtn = (By.ID, 'com.hkfuliao.chamet:id/img_go_back_btn')
    user_own_pageFollowBtn = (By.ID,'com.hkfuliao.chamet:id/img_follow')
    user_ownPage_selfIntroduction = (By.ID,'com.hkfuliao.chamet:id/tv_message_board')
    user_head_levelFrame = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head_level_frame')
    user_head_levelFrameSvg = (By.ID, 'com.hkfuliao.chamet:id/svga_user_head_level_frame')
    user_head_levelFrameAll=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]')
    user_name = (By.ID, 'com.hkfuliao.chamet:id/userNameTv')
    user_vip_level = (By.ID, 'com.hkfuliao.chamet:id/iv_vip_level')
    user_vipLevel=(By.ID, 'com.hkfuliao.chamet:id/vipdrawable')
    user_nation = (By.ID, 'com.hkfuliao.chamet:id/layout_nation')
    user_nationText=(By.ID,'com.hkfuliao.chamet:id/tv_countryname')
    user_language = (By.ID, 'com.hkfuliao.chamet:id/ll_language')
    user_language_Text=(By.ID,'com.hkfuliao.chamet:id/tv_language')
    # 朋友
    user_friend = (By.ID, 'com.hkfuliao.chamet:id/friendsLl')
    user_friendNumText = (By.ID, 'com.hkfuliao.chamet:id/friendsNumTv')
    user_friendNameText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]')
    user_friend_Title = (By.ID, 'com.hkfuliao.chamet:id/title')
    user_friend_GoBack = (By.ID, 'com.hkfuliao.chamet:id/back')
    user_friend_firstPer = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
    user_friend_firstPerHeadID = (By.ID, 'com.hkfuliao.chamet:id/civ_user_head')
    user_friend_firstPerNameID = (By.ID, 'com.hkfuliao.chamet:id/tv_user_name')
    user_friend_firstPerName = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    user_friend_SearchNameText =(By.ID,'com.hkfuliao.chamet:id/et_search_name')
    user_friend_EmptyText = (By.ID,'com.hkfuliao.chamet:id/emptyContentTv')
    user_friend_heartNum = (By.ID, 'com.hkfuliao.chamet:id/svga_love')
    user_friend_countryImg = (By.ID, 'com.hkfuliao.chamet:id/iv_national_flag')
    user_friend_countryName = (By.ID, 'com.hkfuliao.chamet:id/tv_country_name')
    user_friend_levelImg = (By.ID, 'com.hkfuliao.chamet:id/iv_vip_level')
    user_friend_searchEle = (By.ID, 'com.hkfuliao.chamet:id/et_search_name')
    # 关注
    user_following = (By.ID, 'com.hkfuliao.chamet:id/followingLl')
    user_followingNumText = (By.ID, 'com.hkfuliao.chamet:id/followingNumTv')
    user_followingNameText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView[2]')
    user_following_Title = (By.ID, 'com.hkfuliao.chamet:id/title')
    user_following_GoBack = (By.ID, 'com.hkfuliao.chamet:id/back')
    user_following_firstPer = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]')
    user_following_firstPerHeadID = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    user_following_firstPerNameID = (By.ID, 'com.hkfuliao.chamet:id/tv_user_name')
    user_following_firstPerName = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
    user_following_EmptyText = (By.ID,'com.hkfuliao.chamet:id/tv_empty_content')
    # 粉丝
    user_followers = (By.ID, 'com.hkfuliao.chamet:id/followersLl')
    user_followers_NumText = (By.ID, 'com.hkfuliao.chamet:id/followersNumTv')
    user_followers_NameText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.TextView[2]')
    user_followers_Title = (By.ID, 'com.hkfuliao.chamet:id/title')
    user_followers_GoBack = (By.ID, 'com.hkfuliao.chamet:id/back')
    user_followers_firstPer = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]')
    user_followers_firstPerHeadID = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    user_followers_firstPerNameID = (By.ID, 'com.hkfuliao.chamet:id/tv_user_name')
    user_followers_firstPerName = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
    user_followers_EmptyText = (By.ID, 'com.hkfuliao.chamet:id/tv_empty_content')
    user_followers_country = (By.ID, 'com.hkfuliao.chamet:id/img_country')
    user_followers_countryName = (By.ID, 'com.hkfuliao.chamet:id/tv_country_name')
    user_followers_level = (By.ID,  'com.hkfuliao.chamet:id/iv_vip_level')
    user_followers_status = (By.ID,  'com.hkfuliao.chamet:id/ll_status')
    user_followers_loveImg = (By.ID, 'com.hkfuliao.chamet:id/img_love')
    # 签到
    user_sign_infoTop = (By.ID, 'com.hkfuliao.chamet:id/iv_sign_info_top')
    sign_in_popover_dayInt1_7 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView')

    sign_in_popover_dayNum1_7Ele = (By.ID, 'com.hkfuliao.chamet:id/tvTitle')
    sign_in_popover_dayNumLight=(By.ID, 'com.hkfuliao.chamet:id/ivGiftLight')
    sign_in_popover_reminderText=(By.ID, 'com.hkfuliao.chamet:id/tv_task_reminder')
    sign_in_popover_reminderBtn=(By.ID, 'com.hkfuliao.chamet:id/ivRemindSwitch')
    sign_in_popover_dayInt1_7ID = (By.ID, 'com.hkfuliao.chamet:id/rv_sign_in')
    sign_in_popover_dayInt1_7Xpath = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView')
    sign_in_popover_RemindSwitchSelected = (By.ID, 'com.hkfuliao.chamet:id/ivRemindSwitch')
    sign_in_popover_SigninSubmitTextID = (By.ID, 'com.hkfuliao.chamet:id/tvSubmit')
    sign_in_popover_SigninSubmitTextXpath=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]')
    sign_in_popoverDayInt1_7Complete = (By.ID, 'com.hkfuliao.chamet:id/ivComplete')



    # 权限请求弹窗============================================
    # “Chamet”请求使用摄像头权限，是否允许？
    # “Chamet”请求存储权限，是否允许？
    # “Chamet”请求录音权限，是否允许？
    Permission_popoverTitle = (By.ID,'com.android.permissioncontroller:id/permission_message')
    Permission_popoverConfirmBtn = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')


    Permission_popoverTitle1 = '“Chamet”请求使用摄像头权限，是否允许？'
    Permission_popoverTitle2 ='“Chamet”请求存储权限，是否允许？'
    Permission_popoverTitle3 ='“Chamet”请求录音权限，是否允许？'


    # 85-phone的权限弹窗询问
    # "Chamet" 请求打开前置摄像头，是否允许？
    Permission_85Phone_PopoverTitle = (By.ID, 'vivo:id/confirm_msg')
    Permission_85Phone_PopoverConfirmBtn = (By.ID, 'android:id/button1')

    # 114-phone
    # 要允许“Chamet”拍摄照片和录制视频吗？
    Permission_114Phone_PopoverConfirmOnlyBtn = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    # 仅在使用该应用时允许='com.android.permissioncontroller:id/permission_allow_foreground_only_button'
    Permission_114Phone_MediaPopoverConfirmBtn = (By.ID,'com.android.permissioncontroller:id/permission_allow_button')

    # 通过查找找到该用户
    tab_discoverEle = (By.ID,'com.hkfuliao.chamet:id/rl_tab_discover')
    tab_discoverEle_selectedEntry = (By.ID, 'com.hkfuliao.chamet:id/ll_select_country')
    tab_discoverEle_moreEntry = (By.XPATH,"//*[@text='更多']")
    tab_discoverEle_searchInput = (By.ID, 'com.hkfuliao.chamet:id/et_search_id')
    tab_discoverEle_searchBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_search')
    otherPage_messageBtn = (By.ID, 'com.hkfuliao.chamet:id/ll_send_message')
    message_editEle = (By.ID, 'com.hkfuliao.chamet:id/editEt')
    message_sendBtn = (By.ID, 'com.hkfuliao.chamet:id/btn_send')





    # ========留言==========================
    messages_entry_All=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]')
    messages_entry_UnReadNumID = (By.ID,'com.hkfuliao.chamet:id/unReadNumTv')
    messages_entry_UnReadNumXpath= (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView')
    messages_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    messages_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    messages_UnReadNumID = (By.ID, 'com.hkfuliao.chamet:id/unReadNumTv')
    # Chamet团队
    messages_system_UnReadNumXpath= (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[2]')
    messages_system_UnReadNumID= (By.ID, 'com.hkfuliao.chamet:id/system_unReadNumTv')
    messages_system_EntryAll = (By.ID, 'com.hkfuliao.chamet:id/rl_system_content')
    messages_system_EntryTitle = (By.ID,'com.hkfuliao.chamet:id/system_userNameTv')
    messages_system_entryText = (By.ID, 'com.hkfuliao.chamet:id/system_messageContentTv')
    messages_system_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    messages_system_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    messages_system_emptyIcon = (By.ID, 'com.hkfuliao.chamet:id/emptyIv')
    messages_system_emptyText = (By.ID, 'com.hkfuliao.chamet:id/emptyContentTv')
    messages_system_messagesContentAll = (By.ID, 'com.hkfuliao.chamet:id/ll_msg_translate_root')
    messages_system_learnMoreText = (By.ID, 'android.widget.TextView')
    # Chamet客服
    messages_customerService_EntryAll = (By.ID, 'com.hkfuliao.chamet:id/rl_customer_service_content')
    messages_customerService_entryText = (By.ID, 'com.hkfuliao.chamet:id/cs_messageContentTv')
    messages_customerService_entryTitle = (By.ID, 'com.hkfuliao.chamet:id/cs_userNameTv')
    messages_customerService_title = (By.ID, 'com.hkfuliao.chamet:id/aihelp_tv_title')
    messages_customerService_goback = (By.ID, 'com.hkfuliao.chamet:id/aihelp_iv_back')
    messages_customerService_Container = (By.ID, 'com.hkfuliao.chamet:id/aihelp_agent_message_container')
    messages_customerService_problemChoice = (By.ID, 'com.hkfuliao.chamet:id/aihelp_root_layout')
    messages_customerService_InputText = (By.ID, 'com.hkfuliao.chamet:id/aihelp_et_input')
    # 群聊消息
    messages_Group_entryAllLists = (By.CLASS_NAME, 'android.widget.RelativeLayout')
    messages_Group_entryGroupNameAll = (By.ID, 'com.hkfuliao.chamet:id/userNameLl')
    messages_Group_entryGroupName = (By.ID, 'com.hkfuliao.chamet:id/tv_group_name')
    messages_Group_entryGroupCount = (By.ID, 'com.hkfuliao.chamet:id/tv_group_count')
    messages_Group_entryGroupHead = (By.ID, 'com.hkfuliao.chamet:id/groupIv')
    messages_Group_entryGroupType = (By.ID, 'com.hkfuliao.chamet:id/iv_visitor_group')
    messages_Group_titleGroupName = (By.ID, 'com.hkfuliao.chamet:id/tv_group_name')
    messages_Group_titleGroupCount = (By.ID, 'com.hkfuliao.chamet:id/tv_group_number')
    messages_Group_goback = (By.ID, 'com.hkfuliao.chamet:id/iv_back')
    messages_Group_detailMoreBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_group_detail')
    messages_Group_inputBtn = (By.ID, 'com.hkfuliao.chamet:id/et_edit_chat_info')
    messages_Group_inputSendBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_send_message')
    messages_Group_TextInputContent = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    messages_Group_faceGifBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_face_gif')
    messages_Group_imgMotionList = (By.ID, 'com.hkfuliao.chamet:id/img_motion')
    messages_Group_imgMotionClassList = (By.CLASS_NAME, 'android.widget.ImageView')
    messages_Group_imgSearchBtn = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView')
    messages_Group_imgSearchFirstPic = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView')
    messages_Group_imgSearchLogo = (By.ID,'com.hkfuliao.chamet:id/img_giphy_logo')
    messages_Group_TextImageList = (By.ID, 'com.hkfuliao.chamet:id/iv_pic')
    messages_Group_GifsList = (By.CLASS_NAME, 'android.widget.ImageView')
    messages_Group_voiceBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_voice')
    messages_Group_voiceAddBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_add_voice')
    messages_Group_TextVoiceTimes = (By.ID, 'com.hkfuliao.chamet:id/tv_voice_times')
    messages_Group_TextVoiceIcon = (By.ID, 'com.hkfuliao.chamet:id/icon_voice')
    messages_Group_pictureMoreBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_more_pic')
    messages_Group_pictureChooseBtn = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')
    messages_Group_pictureCameraBtn = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView')
    messages_Group_pictureChooseList = (By.ID, 'com.hkfuliao.chamet:id/iv_photo')
    messages_Group_upMicBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_bottom_up_mic')
    messages_Group_upMic10All = (By.ID, 'com.hkfuliao.chamet:id/recycler_group_video')
    messages_Group_upMicUserHeadList = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    messages_Group_upMicUserHeadList1 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]')
    messages_Group_upMicUserHeadList2 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]')
    messages_Group_upMicEmptyList = (By.ID, 'com.hkfuliao.chamet:id/emptyView')
    messages_Group_upMicSwitchMicBtn = (By.ID, 'com.hkfuliao.chamet:id/switch_microphone')
    messages_Group_upMicTurnOffBtn = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]')
    messages_Group_pageGroupName = (By.XPATH, "//*[@text='今日也莫人陪我']")
    messages_Group_ContentText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]')

    # 个人主页半屏浮层
    messages_Group_userHalfPagePopoverHead = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    messages_Group_userHalfPagePopoverHeadFrame = (By.ID,'com.hkfuliao.chamet:id/iv_user_head_level_frame')
    messages_Group_userHalfPagePopoverName = (By.ID, 'com.hkfuliao.chamet:id/profile_name')
    messages_Group_userHalfPagePopoverLev = (By.ID,'com.hkfuliao.chamet:id/iv_vip_level')
    messages_Group_userHalfPagePopoverCouName = (By.ID, 'com.hkfuliao.chamet:id/tv_country_name')
    messages_Group_userHalfPagePopoverLan = (By.ID, 'com.hkfuliao.chamet:id/tv_language')
    messages_Group_userHalfPagePopoverMomentList = (By.ID, 'com.hkfuliao.chamet:id/cv_user_moment_list')
    # messages_Group_userHalfPagePopoverGifBtn = (By.ID, 'com.hkfuliao.chamet:id/profile_gift')
    messages_Group_userHalfPagePopoverGifBtn = (By.XPATH, "//*[@text='送礼物']")
    messages_Group_userHalfPagePopoverCallBtn = (By.ID, 'com.hkfuliao.chamet:id/ll_enable')
    messages_Group_userHalfPagePopoverAtHer = (By.ID, 'com.hkfuliao.chamet:id/tv_atHer')
    messages_Group_userHalfPagePopoverReport = (By.ID, 'com.hkfuliao.chamet:id/tv_report')
    messages_Group_userHalfPagePopover_UpMicRemove = (By.ID, 'com.hkfuliao.chamet:id/tv_remove')
    # 用户自己
    messages_Group_OneSelfHalfPagePopoverMomentList = (By.ID, 'com.hkfuliao.chamet:id/recycler_moment_oneself')
    messages_Group_OneSelfHalfPagePopoverName = (By.ID,'com.hkfuliao.chamet:id/oneself_profile_name')
    messages_Group_CallMoneyNotEnough = (By.XPATH, "//*[@text='余额不足']")
    messages_Group_userHalfPagePopoverImgList = (By.ID, 'com.hkfuliao.chamet:id/img_expression')
    messages_Group_userHalfPagePopoverImgFirst = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView')
    messages_Group_userHalfPagePopoverGiftSendBtn = (By.ID, 'com.hkfuliao.chamet:id/ll_send_gift')
    messages_Group_diamondsPacket = (By.ID, 'com.hkfuliao.chamet:id/iv_packet')
    messages_Group_diamondsPacketPopTitle = (By.ID, 'com.hkfuliao.chamet:id/tv_title')
    messages_Group_diamondsPacketPopCount = (By.ID, 'com.hkfuliao.chamet:id/ed_packet_count')
    messages_Group_diamondsPacketPopTotalNum = (By.ID, 'com.hkfuliao.chamet:id/ed_packet_total_energy')
    messages_Group_diamondsPacketPopSendBtn = (By.ID, 'com.hkfuliao.chamet:id/btn_send_packet')
    messages_Group_TextDiamondsPacket = (By.ID, 'com.hkfuliao.chamet:id/ll_diamond_packet_content')
    messages_Group_diamondsPacketStatusOpen = (By.ID, 'com.hkfuliao.chamet:id/iv_open_diamond_packet')
    messages_Group_diamondsPacketStatusReceived = (By.ID, 'com.hkfuliao.chamet:id/tv_receive_energy')
    messages_Group_diamondsPacketStatusExpired = (By.ID, 'com.hkfuliao.chamet:id/tv_status')
    messages_Group_GameBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_play_game')
    messages_Group_GameLayerAll = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
    messages_Group_GameLayer1 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    messages_Group_GameLayer2 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')
    messages_Group_GameLayer3 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView')
    messages_Group_GameLayer4 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView')
    messages_Group_GameLayer5 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView')
    messages_Group_GameLayer6 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView')


    messages_Group_GiftBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_gift_tip')
    messages_Group_GiftLayerTypeTab = (By.ID, 'com.hkfuliao.chamet:id/tv_type')
    messages_Group_GiftLayerTypeList = (By.CLASS_NAME, 'android.view.ViewGroup')
    messages_Group_GiftLayerGroupNum = (By.ID, 'com.hkfuliao.chamet:id/item_group_count_text')
    messages_Group_GiftLayerGroupNumFirst = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView')
    messages_Group_GiftLayerSendBtn = (By.ID, 'com.hkfuliao.chamet:id/sendTv')
    messages_Group_GiftTreasuresAwesomeBtn = (By.ID, 'com.hkfuliao.chamet:id/finish')
    messages_Group_TextGiftPicIcon = (By.ID, 'com.hkfuliao.chamet:id/giftPicIv')
    messages_Group_BannerList = (By.CLASS_NAME, 'android.widget.ImageView')
    messages_Group_BannerListLast = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.ImageView')
    messages_Group_BannerListLayer = (By.ID, 'com.hkfuliao.chamet:id/webview')
    messages_Group_BannerListLayerClass = (By.CLASS_NAME, 'android.view.View')
    messages_Group_BannerListPackupBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_group_inbox_up_btn')
    messages_Group_BannerListSmallBtn = (By.ID, 'com.hkfuliao.chamet:id/mic_play')
    messages_Group_MoreUserAll = (By.ID, 'com.hkfuliao.chamet:id/recycler_group')
    messages_Group_MoreUserList = (By.ID, 'com.hkfuliao.chamet:id/rootView')
    messages_Group_MoreUserHeadList = (By.ID, 'com.hkfuliao.chamet:id/rl_head')
    messages_Group_MoreMomentAll = (By.ID, 'com.hkfuliao.chamet:id/rl_moment')
    messages_Group_MoreMomentList = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    messages_Group_MoreMomentPicFront = (By.ID,'com.hkfuliao.chamet:id/img_moment_pic')
    messages_Group_MoreMomentPicLast = (By.ID, 'com.hkfuliao.chamet:id/img_moment_pic2')
    messages_Group_MoreMomentMoreTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    messages_Group_MoreMomentMoreGoback = (By.ID, 'com.hkfuliao.chamet:id/back')
    # messages_Group_MoreMomentMoreSendBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_send_moment')
    messages_Group_MoreMomentGiftSendBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_gift_select')
    messages_Group_MoreMomentMaxZanBtn = (By.ID, 'com.hkfuliao.chamet:id/ivZan_unSelect')
    messages_Group_MoreMomentMaxCommentBtn = (By.ID, 'com.hkfuliao.chamet:id/ivComment')
    messages_Group_MoreGroupType = (By.ID, 'com.hkfuliao.chamet:id/tv_group_type')
    messages_Group_MoreGroupHeadPic = (By.ID, 'com.hkfuliao.chamet:id/img_group_head_pic')
    messages_Group_MoreGroupHeadPic_Change = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout')
    messages_Group_MoreGroupHeadPic_pic = (By.ID, 'com.hkfuliao.chamet:id/iv_cover_pic')
    messages_Group_MoreGroupHeadPic_picStatus = (By.ID, 'com.hkfuliao.chamet:id/iv_cover_status')
    messages_Group_MoreGroupNameSet = (By.ID, 'com.hkfuliao.chamet:id/tv_group_name')
    messages_Group_MoreGroupNameSetContent = (By.ID, 'com.hkfuliao.chamet:id/et_create_group_name')
    messages_Group_MoreGroupNameSetContentSave = (By.ID, 'com.hkfuliao.chamet:id/right')
    messages_Group_MoreGroupNameSetContentGoback = (By.ID, 'com.hkfuliao.chamet:id/back')
    messages_Group_MoreGroupIntro = (By.XPATH, "//*[@text='群组介绍']")
    messages_Group_MoreGroupIntroDes = (By.ID,'com.hkfuliao.chamet:id/tv_group_description')
    messages_Group_MoreGroupIntroContent = (By.ID, 'com.hkfuliao.chamet:id/et_create_group_name')
    messages_Group_MoreGroupIntroTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    messages_Group_MoreGroupTitle = (By.ID, 'com.hkfuliao.chamet:id/tv_title')
    messages_Group_MoreGroupMana = (By.XPATH, "//*[@text='管理群组']")
    messages_Group_MoreGroupManaVis = (By.ID, 'com.hkfuliao.chamet:id/tv_title')
    messages_Group_MoreGroupManaVisCon = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[4]')
    # messages_Group_MoreGroupManaVisConText = (By.XPATH, "//*[@text='非群组用户可以查看消息和送礼，但不能发送消息、进行语音聊天或玩游戏。 开启访客模式的群组将更容易被看到，群组将变得更加活跃。']")
    messages_Group_MoreGroupManaVisConTextXPATH = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[4]')
    messages_Group_MoreGroupManaPriCon = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView[4]')
    # messages_Group_MoreGroupManaPriConText = (By.XPATH, "//*[@text='不在群组内的用户不能申请加入。用户只能通过群主或管理员的邀请加入']")
    messages_Group_MoreGroupManaPriConTextXPATH = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView[4]')
    messages_Group_MoreGroupManaNextHost = (By.XPATH, "//*[@text='群组所有权转让']")
    messages_Group_MoreGroupManaNextHostTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    messages_Group_MoreGroupManaAdmin =(By.XPATH, "//*[@text='群管理员']")
    messages_Group_MoreGroupManaDisband =(By.XPATH, "//*[@text='解散群组']")
    messages_Group_MoreGroupManaDisPopCon = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    messages_Group_MoreGroupManaDisPopCancel = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')
    messages_Group_MoreGroupManaDisPopConfirm = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    # messages_Group_MoreGroupManaDeAndLeave = (By.XPATH, "//*[@text='删除并离开']")
    messages_Group_MoreGroupManaDeAndLeaveID = (By.ID, 'com.hkfuliao.chamet:id/tv_group_delete')
    messages_Group_MoreGroupAddBtn = (By.ID, 'com.hkfuliao.chamet:id/rl_add')
    # messages_Group_MoreGroupRemovePer = (By.XPATH, "//*[@text='Mary33470557…啊bbb哦哦哦']")
    messages_Group_MoreGroupRemovePerSave = (By.ID, 'com.hkfuliao.chamet:id/tv_done')
    messages_Group_MoreGroupRemoveTips = (By.ID, 'com.hkfuliao.chamet:id/tv_tip_default_msg')
    # messages_Group_MoreGroupRemoveTipsText = (By.XPATH,  "//*[@text='“你移除了”Mary33470557…啊bb...“来自群组”']")
    messages_Group_MoreGroupRemovePTips = (By.XPATH, "//*[@text='你已被移出群组']")
    messages_Group_MoreGroupRemovePTips2 = (By.XPATH, "//*[@text='该群组已被解散']")
    messages_Group_joinBtn = (By.ID,'com.hkfuliao.chamet:id/btn_join_group')
    messages_Group_joinPopCon = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    messages_Group_joinPopConfirm = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    messages_Group_Notification = (By.ID, 'com.hkfuliao.chamet:id/group_userNameTv')
    messages_Group_NotiJoinCon = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    messages_Group_joinAgree = (By.ID, 'com.hkfuliao.chamet:id/tv_agree')
    messages_Group_joinIgnore = (By.ID, 'com.hkfuliao.chamet:id/tv_ignore')
    # messages_Group_joinInTips =  (By.XPATH, "//*[@text='Mary33470557…啊bb... 加入了群组']")
    messages_Group_MoreGroupAddIcon = (By.ID, 'com.hkfuliao.chamet:id/tv_select_icon')




    # 陌生人消息
    messages_Stranger_entryHeadPic = (By.ID, 'com.hkfuliao.chamet:id/headIv')
    messages_Stranger_entryUserAndText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[1]')
    messages_Stranger_entryUnread = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]')
    messages_Stranger_userListUnread = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[3]')
    messages_Stranger_userListUnread1 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[3]')
    messages_Stranger_entryTitleName = (By.ID, 'com.hkfuliao.chamet:id/userNameTv')
    messages_Stranger_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    messages_Stranger_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    messages_Stranger_UserHeadList = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    messages_Stranger_UserUnread = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[3]')
    messages_Stranger_UserNameList = (By.ID, 'com.hkfuliao.chamet:id/userNameTv')
    messages_Stranger_UserEntryList = (By.CLASS_NAME, 'android.widget.LinearLayout')
    messages_Stranger_userTitleName = (By.ID, 'com.hkfuliao.chamet:id/tv_name')
    messages_Stranger_userGoback = (By.ID, 'com.hkfuliao.chamet:id/iv_back')
    messages_Stranger_userMoreBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_more')
    messages_Stranger_userHalfPagePopoverHead = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    messages_Stranger_userHalfPagePopoverHeadFrame = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head_level_frame')
    messages_Stranger_userHalfPagePopoverLevel = (By.ID, 'com.hkfuliao.chamet:id/iv_vip_level')
    messages_Stranger_userHalfPagePopoverNation = (By.ID, 'com.hkfuliao.chamet:id/nationalFlagIv')
    messages_Stranger_userHalfPagePopoverNationName = (By.ID, 'com.hkfuliao.chamet:id/tv_country_name')
    messages_Stranger_userHalfPagePopoverLanguage = (By.ID, 'com.hkfuliao.chamet:id/tv_language')
    messages_Stranger_userHalfPagePopoverFollowBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_follow')
    messages_Stranger_userHalfPagePopoverName = (By.ID, 'com.hkfuliao.chamet:id/profile_name')
    messages_Stranger_SendGiftBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_chat_gift')
    messages_Stranger_userHalfPagePopoverSendGiftBtn = (By.ID, 'com.hkfuliao.chamet:id/ll_send_gift')
    messages_Stranger_GiftFirstTabFirst = (By.CLASS_NAME, 'android.widget.TextView')

    # 视频聊按钮状态
    messages_Stranger_videoCallEnable = (By.ID, 'com.hkfuliao.chamet:id/ll_enable')
    messages_Stranger_videoCallUnable = (By.ID, 'com.hkfuliao.chamet:id/ll_uneable')
    messages_Stranger_videoCallUnablePopAll = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup')
    messages_Stranger_videoCallUnablePopTitle = (By.ID, 'com.hkfuliao.chamet:id/dialog_msg')
    messages_Stranger_videoCallUnablePopConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/single_btn')
    # 视频聊拨打中元素
    messages_Stranger_callingInfo = (By.ID, 'com.hkfuliao.chamet:id/cl_calling_info')
    messages_Stranger_callingSvg = (By.ID, 'com.hkfuliao.chamet:id/svga_call_ing')
    messages_Stranger_callingMineHead = (By.ID, 'com.hkfuliao.chamet:id/iv_user_mine_header')
    messages_Stranger_callingUserHead = (By.ID, 'com.hkfuliao.chamet:id/iv_call_user_0')
    messages_Stranger_callingStopBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_stop_call')
    # 接收方
    messages_Stranger_callingName = (By.ID,'com.hkfuliao.chamet:id/call_name')

    # 用户没有回答
    # '请不要轻信陌生人的转账、抽奖、免费钻石等诈骗信息。 请不要与陌生人分享任何重要信息，如密码、手机号码、短信验证码。'
    messages_Stranger_TextCallNoAnswer = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    # 输入框其他内容
    messages_Stranger_InputEdit = (By.ID, 'com.hkfuliao.chamet:id/editEt')
    messages_Stranger_TextInputContentText = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    messages_Stranger_InputSendBtn = (By.ID, 'com.hkfuliao.chamet:id/btn_send')
    messages_Stranger_inputMoreBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_more_bottom')
    messages_Stranger_translateContent = (By.ID, 'com.hkfuliao.chamet:id/tv_translate_content')
    messages_Stranger_moreFourBtn = (By.CLASS_NAME, 'android.widget.ImageView')
    messages_Stranger_TranslateBtn = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView')
    messages_Stranger_phonePictureBtn = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView')
    messages_Stranger_CameraBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_take_camera')
    messages_Stranger_VideoCallBtn = (By.ID, 'com.hkfuliao.chamet:id/videoView')
    messages_Stranger_phonePictureListSelect = (By.ID, 'com.hkfuliao.chamet:id/iv_select')
    messages_Stranger_phonePictureListSelectFirst = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[2]')
    messages_Stranger_phonePictureListConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/btn_confirm')
    messages_Stranger_phonePictureListUnselectedBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_unselect')
    # 114手机
    messages_Stranger_114CameraBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_take_camera')
    messages_Stranger_114VideoCallBtn = (By.ID, 'com.hkfuliao.chamet:id/videoView')
    messages_Stranger_114phonePictureListSelectFirst = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[2]')

    # 85手机相机
    messages_Stranger_CameraTakeBtn= (By.ID, 'com.android.camera:id/shutter_button')
    messages_Stranger_CameraTakeBtnXpath= (By.XPATH,'//android.widget.ImageView[@content-desc="快门"]')
    messages_Stranger_CameraTakeDoneBtn = (By.ID, 'com.android.camera:id/done_button')
    messages_Stranger_CameraTakeDoneBtnXpath = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[7]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button[2]')

    # 114手机相机
    messages_Stranger_114CameraTakeBtn = (By.ID, 'com.android.camera:id/shutter_button_horizontal')
    messages_Stranger_114CameraTakeDoneBtn = (By.ID, 'com.android.camera:id/done_button')

    # 留言_私聊消息（一对一消息）
    messages_User_EntryHead = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    messages_User_EntryUserName = (By.ID, 'com.hkfuliao.chamet:id/userNameTv')
    messages_User_TitleName = (By.ID, 'com.hkfuliao.chamet:id/tv_name')
    messages_User_GobackBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_back')
    messages_User_MoreBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_more')
    # Mary33470557…啊bbb哦哦哦
    # messages_User_33470557Strange = (By.XPATH,"//*[@text='Mary33470557…啊bbb哦哦哦']")
    messages_User_StrangeTopName = (By.ID,'com.hkfuliao.chamet:id/tv_name')
    messages_User_ListCountryIcon = (By.ID,'com.hkfuliao.chamet:id/countryIv')
    messages_User_ListLevelIcon = (By.ID ,'com.hkfuliao.chamet:id/iv_vip_level')
    messages_User_userContentText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]')
    messages_User_userContentUnreadDot = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[2]')


















    # 等级
    my_vipLevel_entryAll = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout')
    my_vipLevel_entryText= (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView[1]')
    my_vipLevel_entryRightClick = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView[2]')
    my_vipLevel_UpLevelImgManAll = (By.ID,'com.hkfuliao.chamet:id/LevelNumTv')
    my_vipLevel_UpLevelImgManLevel=(By.ID,'com.hkfuliao.chamet:id/level')
    my_vipLevel_UpLevelImgManNextLevel = (By.ID, 'com.hkfuliao.chamet:id/nextVlevel')
    my_vipLevel_NowLevelImgZeroAndWoman = (By.ID, 'com.hkfuliao.chamet:id/level')
    level_title = (By.ID, 'leveltitle')
    level_titleXpath = (By.XPATH,"//*[@text='等级']")
    level_titleTextXpath = (By.XPATH, '//*[@id="leveltitle"]')
    level_goback = (By.CLASS_NAME, 'go_back')
    level_gobackCss = (By.XPATH, '/html/body/div[1]/div[1]/img')
    level_specificNumber = (By.CLASS_NAME, 'vLevelFake')
    level_specificNumberCss = (By.XPATH, '/html/body/div/div[2]/div[1]/span')
    level_specificNumberAll = (By.CLASS_NAME,'hd-level')
    level_specificNumberAllCss = (By.CSS_SELECTOR, '[class="hd-level"]')
    level_specificNumberleftAll = (By.CLASS_NAME, 'hd-progress-tip')
    level_specificNumberleftAllCss = (By.CSS_SELECTOR, '[class="hd-progress-tip"]')
    level_specificNumberleft = (By.CLASS_NAME, 'vlevel')
    level_specificNumberleftCss = (By.XPATH,'/html/body/div/div[2]/div[2]/div[1]/span')
    level_tabSelectedMan = (By.CLASS_NAME, 'lev_tab_item lev_tab_item_select')
    level_tabSelectedManCss = (By.CSS_SELECTOR, '[class="lev_tab_item lev_tab_item_select"]')
    level_tabSelectedManClass = (By.XPATH,'//*[@id="lev_tab_item lev_tab_item_select"]/li')
    level_tabSelectedWoman = (By.CLASS_NAME, 'lev_tab_item lev_tab_item_select_female')
    level_tabSelectedWomanCss = (By.CSS_SELECTOR, '[class="lev_tab_item lev_tab_item_select_female"]')
    # level_tabItem = (By.CLASS_NAME, 'lev_tab_item')
    level_tabItem = (By.XPATH, '//*[@id="lev_tab_menu"]/li')
    # =(,'//*[@id="lev_tab_menu"]/li[1]')
    level_tabItemCss = (By.CSS_SELECTOR, '[class="lev_tab_item"]')
    level_privilege_DetailList = (By.XPATH,'//*[@id="lev_detail_menu"]/div')
    level_privilege_DetailAll = (By.CLASS_NAME, 'lev_detail_item')
    level_privilege_DetailAllCss = (By.CSS_SELECTOR, '[class="lev_detail_item"]')
    level_detail_itemCheckRightClick = (By.CLASS_NAME, 'lev_detail_ft')
    level_detail_itemCheckRightClickCss = (By.CSS_SELECTOR, '[class="lev_detail_ft"]')
    level_privilege_detailPopover = (By.CLASS_NAME, 'swiper-container swiper-container-initialized swiper-container-horizontal swiper-container-android')
    level_privilege_detailPopoverHeadFrame=(By.CLASS_NAME,'entry_car_title')
    level_privilege_detailPopoverHeadFrameCss = (By.CSS_SELECTOR, '[class="entry_car_title"]')
    level_rank_ruleText = (By.CLASS_NAME, 'bd-item bd-head')
    level_TopUp_btn = (By.XPATH, '//*[@id="leveltopbtn"]')
    level_rules_text = (By.XPATH,'//*[@id="leveltopamount"]')
    level_rules_text_woman = (By.XPATH, '/html/body/div/div[5]/ul/li[2]/div[3]')

    # 我的收入
    MyBalance_entry_man = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[8]')
    MyBalance_entry_woman = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]')
    MyBalance_entry_manText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[8]/android.widget.LinearLayout/android.widget.TextView')
    MyBalance_entry_womanText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.TextView')
    MyBalance_earnText = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div[1]/div')
    # MyBalance_earnText = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[1]/div/div[1]/div/text()')
    MyBalance_earnTitleText =(AppiumBy.XPATH,"//*[@text='我的赚取']")
    MyBalance_title = (By.XPATH, '//*[@id="app"]/div/div/div[1]/span')
    MyBalance_goback = (By.XPATH, '//*[@id="app"]/div/div/div[1]/svg/path')




    # 设置
    settings_entry = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[9]/android.widget.TextView[1]')
    settings_entry_RightClick = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[9]/android.widget.TextView[2]')
    settings_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    settings_goback = (By.ID, 'com.hkfuliao.chamet:id/back')

    # 设置——app language
    settings_AppLanguage_All = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.ViewGroup')
    settings_AppLanguage_selectedText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    settings_AppLanguageTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    settings_AppLanguageGoback = (By.ID, 'com.hkfuliao.chamet:id/back')
    settings_AppLanguage_selectedLanguage = (By.ID, 'com.hkfuliao.chamet:id/tv_language_title')
    settings_AppLanguage_selectFlagID = (By.ID, 'com.hkfuliao.chamet:id/iv_select_flag')
    settings_AppLanguage_selectFlagXPATH = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
    settings_AppLanguage_saveBtn = (By.ID, 'com.hkfuliao.chamet:id/right')
    settings_AppLanguage_Automatic = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
    settings_AppLanguage_AutomaticText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    settings_AppLanguage_English = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    settings_AppLanguage_EnglishText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')

    # 设置——黑名单
    settings_blocklist = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup')
    settings_blocklist_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    settings_blocklist_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    settings_blocklist_UserAll = (By.ID,'com.hkfuliao.chamet:id/recyclerView')
    settings_blocklist_oneUserClick = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout')
    settings_blocklist_oneUserName = (By.ID,'com.hkfuliao.chamet:id/tv_country_name')
    settings_blocklist_firstUserName = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
    settings_blocklist_firstUserClick = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]')
    settings_blocklist_UserNameList = (By.ID,'com.hkfuliao.chamet:id/tv_user_name')
    settings_blocklist_UserClickList = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')

    settings_blocklist_noUserText = (By.ID,'com.hkfuliao.chamet:id/tv_empty_content')
    # 设置——隐私政策
    # global PrivacyPolicyIntroCon
    # PrivacyPolicyIntroCon = (
    #     'This is the Privacy Policy of FULIAO HONGKONG LIMITED and CHAMET and its various & next versions including CHAMET web version (hereinafter collectively referred to as "CHAMET", "us", "we", or "our") and is incorporated into and is subject to our Terms of Use.In this Privacy Policy, we refer to our products and services as the "Service". Please read on to learn more about our data handling practices. Your use of the Service signifies that you agree with the terms of this Privacy Policy. If you do not agree with the terms of this Privacy Policy, please do not use the Service.')

    settings_PrivacyPolicy = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[3]/android.view.ViewGroup')
    settings_PrivacyPolicy_goback = (By.CLASS_NAME, 'go_back')
    settings_PrivacyPolicy_title = (By.ID, 'pricetlt')
    settings_PrivacyPolicy_titleXpath = (By.XPATH,'//*[@id="pricetlt"]')
    settings_PrivacyPolicy_Headline = (By.XPATH,"//*[@text='Introduction']")
    settings_PrivacyPolicy_HeadlineXpath = (By.XPATH,'//*[@id="protocol"]/div[1]')
    # settings_PrivacyPolicy_introConXpath = (By.XPATH, "//*[@text='This is the Privacy Policy of FULIAO HONGKONG LIMITED and CHAMET and its various & next versions including CHAMET web version (hereinafter collectively referred to as "CHAMET", "us", "we", or "our") and is incorporated into and is subject to our Terms of Use.In this Privacy Policy, we refer to our products and services as the "Service". Please read on to learn more about our data handling practices. Your use of the Service signifies that you agree with the terms of this Privacy Policy. If you do not agree with the terms of this Privacy Policy, please do not use the Service.'")
    settings_PrivacyPolicy_policyTitle = (By.CLASS_NAME, 'bt')


    # 设置——用户协议
    settings_UserAgreement = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.view.ViewGroup')
    settings_UserAgreement_goback = (By.CLASS_NAME, 'go_back')
    settings_UserAgreement_titleXpath = (By.XPATH, '//*[@id="pricetlt"]')
    settings_UserAgreement_titleTextXpath = (By.XPATH, '//*[@text="User Agreement"')
    settings_UserAgreement_titleAndGoback = (By.XPATH, '//*[@id="nav_box"]/img')
    settings_UserAgreement_Welcome = (By.XPATH, "//*[@id='protocol']/div[1]")
    # settings_UserAgreement_Contents = (By.XPATH, "//*[@text='We've drafted these Terms of Service (which we simply call the "Terms") so that you'll know the rules that govern our relationship with you. Although we have tried our best to strip the legalese from the Terms, there are places where these Terms may still read like a traditional contract. There's a good reason for that: These Terms do indeed form a legally binding contract between you and FULIAO HONG KONG LIMITED. So please read them carefully.']")

    # 设置——关于我们
    settings_AboutUs = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[5]/android.view.ViewGroup')
    settings_AboutUs_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    settings_AboutUs_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    settings_AboutUs_accountDeleteBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_delete_account')
    settings_AboutUs_deleteDeleteBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_delete_btn')
    settings_AboutUs_deleteUserName = (By.ID, 'com.hkfuliao.chamet:id/tv_user_name')
    settings_AboutUs_deleteEditReason = (By.ID, 'com.hkfuliao.chamet:id/edit_reason')
    settings_AboutUs_deletePopoverConfirm = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    settings_AboutUs_deletePopoverContentText = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    settings_AboutUs_deletePopoverCancel = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')
    settings_AboutUs_deleteGoback = (By.CLASS_NAME, 'go_back')
    settings_AboutUs_deleteLoginPopover = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
    settings_AboutUs_deleteLoginPopoverTitle = (By.ID, 'com.hkfuliao.chamet:id/tv_title')
    settings_AboutUs_deleteLoginPopoverConfirm = (By.ID,'com.hkfuliao.chamet:id/tv_confirm')
    settings_AboutUs_deleteLoginPopoverCancel = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')

    # 设置——chamet评分
    settings_RateChamet = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[6]/android.view.ViewGroup')
    settings_RateChametText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[6]/android.view.ViewGroup/android.widget.TextView[1]')
    # 设置——清除缓存
    settings_ClearCache = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[7]/android.view.ViewGroup')
    settings_ClearCache_cache = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[7]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')

    # 设置——版本
    settings_versions = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[8]/android.view.ViewGroup')
    settings_versions_versionText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[8]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')

    # 设置——登出
    settings_logout = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[9]/android.view.ViewGroup')
    settings_logout_logoutText = (By.ID, 'com.hkfuliao.chamet:id/tv_center_name')
    settings_logout_popover = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
    settings_logout_popoverTitle = (By.ID, 'com.hkfuliao.chamet:id/tv_title')
    settings_logout_popoverConfirm = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    settings_logout_popoverCancel = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')


    # 我的邀请
    MyInvite_entry_All = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[6]')
    MyInvite_entry_nameText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[6]/android.widget.TextView[1]')
    MyInvite_inviteRewardsText = (By.ID,'invitation_rewards')
    MyInvite_inviteRewardsTextName =(By.XPATH, "//*[@text='邀请奖励']")
    # MyInvite_inviteRewardsTextXpath = (By.XPATH,'//*[@id="invitation_rewards"]')
    MyInvite_inviteRewardsTextXpath = (MobileBy.XPATH,'//*[@id="invitation_rewards"]')
    MyInvite_entry_FreeCardsText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[6]/android.widget.LinearLayout/android.widget.TextView')
    MyInvite_instructionsBtn = (AppiumBy.XPATH, '/html/body/div/div[1]/div[1]/img[2]')
    # MyInvite_instructionsBtn = (By.XPATH, '/html/body/div/div[1]/div[1]/img[2]')
    MyInvite_instructionsPopover = (By.CLASS_NAME, 'close_pop_up rule_pop')
    MyInvite_instructionsPopover_rule1= (AppiumBy.XPATH,'//*[@id="rule1"]')
    # 聊天卡免费用于视频聊天1分钟，每张卡有效期为5天
    # 只有新的Chamet用户才能获得奖励
    MyInvite_instructionsPopover_rule2 = (AppiumBy.XPATH, '//*[@id="rule2"]')



    MyInvite_goback = (By.XPATH, '/html/body/div/div[1]/div[1]/img[1]')
    MyInvite_inviteFriendsBtn = (By.CLASS_NAME, 'i18n invite_friends')
    MyInvite_inviteFriendsBtnID = (By.XPATH, '//*[@id="invite_friends"]')
    MyInvite_inviteFriendsPopover = (By.ID, 'com.hkfuliao.chamet:id/cardView3')
    MyInvite_inviteFriendsPopover_whats = (By.ID, 'com.hkfuliao.chamet:id/but_jump_whatsapp')
    MyInvite_inviteFriendsPopover_mess = (By.ID, 'com.hkfuliao.chamet:id/but_jump_messenger')
    MyInvite_myInvitees = (By.XPATH, '//*[@id="my_invitees"]')
    MyInvite_my_TotalRewardsBtn = (By.CLASS_NAME, 'total_rewards')
    MyInvite_my_inviteesListAll = (By.CLASS_NAME,'list_box invite_box')
    MyInvite_my_inviteesList = (By.CLASS_NAME, 'flex jc-sb list_item link_personal')
    MyInvite_my_inviteesListPic = (By.CLASS_NAME, 'flex')
    MyInvite_my_inviteesListCardNum = (By.CLASS_NAME, 'flex card_count')
    MyInvite_my_inviteesListFirstName = (By.CLASS_NAME, 'user_name')
    MyInvite_my_inviteesListNameXpath = (By.XPATH,'/html/body/div/div[2]/div[3]/div')
    MyInvite_my_inviteesListName4 = (By.XPATH, '//android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[7]/android.widget.TextView')
    MyInvite_my_inviteesListNoUser = (By.ID, 'norecord')
    MyInvite_weeklyRank = (By.XPATH, '//*[@id="weekly_rank"]')
    MyInvite_weekly_noUser = (By.XPATH,'//*[@id="norecord"]')
    MyInvite_my_firstUser = (317, 1343)
    MyInvite_weekly_firstUser = (445, 1349)

    # 我的背包
    myBackpack_entryAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[5]')
    myBackpack_entryText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.LinearLayout/android.widget.TextView')
    myBackpack_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    myBackpack_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myBackpack_Frame_Num = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')
    myBackpack_EntranceEffect_Num = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView')
    myBackpack_Frame_inUse_NameText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    myBackpack_Frame_inUse_Head = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    myBackpack_Frame_inUse_NoneImage = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
    myBackpack_Frame_inUse_PopTag= (By.ID,'com.hkfuliao.chamet:id/tv_in_user_tag')
    myBackpack_Frame_inUse_PopFrame1= (By.ID,'com.hkfuliao.chamet:id/iv_user_head_level_frame')
    myBackpack_Frame_inUse_PopFrame2= (By.ID,'com.hkfuliao.chamet:id/svga_user_head_level_frame')
    # myBackpack_Frame_inUse_PopFrame3 = (By.ID, 'com.hkfuliao.chamet:id/svga_user_head_level_frame')
    myBackpack_Frame_inUse_PopSourceLink= (By.ID,'com.hkfuliao.chamet:id/tv_source_link')
    myBackpack_Entrance_inUse_NameText= (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')
    myBackpack_Entrance_inUse_Image= (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView')
    myBackpack_Entrance_inUse_NoneImage= (By.ID,'com.hkfuliao.chamet:id/svag_effect')
    myBackpack_Entrance_inUse_PopTag= (By.ID,'com.hkfuliao.chamet:id/tv_in_user_tag')
    myBackpack_Entrance_inUse_PopPreviewImg= (By.ID,'com.hkfuliao.chamet:id/svga_preview')
    myBackpack_Entrance_inUse_PopSourceLink= (By.ID,'com.hkfuliao.chamet:id/tv_source_link')
    myBackpack_Entrance_inUse_PopPreviewBtn= (By.ID,'com.hkfuliao.chamet:id/btn_single')
    myBackpack_Entrance_inUse_PreviewUser= (By.ID,'com.hkfuliao.chamet:id/tv_user_name')
    myBackpack_Entrance_inUse_PreviewEffect= (By.ID,'com.hkfuliao.chamet:id/special_effects_enter')





    myBackpack_expiredEntry = (By.ID, 'com.hkfuliao.chamet:id/right')
    myBackpack_expiredTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    myBackpack_expiredGoback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myBackpack_expired_noIcon = (By.ID, 'com.hkfuliao.chamet:id/iv_empty')
    myBackpack_expired_noText = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')
    myBackpack_expiredList_First = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
    myBackpack_expiredList_FirstIcon = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[2]')
    myBackpack_expiredList_FirstName = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]')
    myBackpack_expiredList_FirstTime = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[2]')
    # all
    myBackpack_all_emptyIcon = (By.ID, 'com.hkfuliao.chamet:id/iv_empty')
    myBackpack_all_emptyText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView')
    myBackpack_all_headFrameList = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')
    myBackpack_all_headFrameClItem = (By.ID,'com.hkfuliao.chamet:id/cl_item')
    myBackpack_now_frameID = (By.ID, 'com.hkfuliao.chamet:id/iv_tool_image')
    myBackpack_now_frameSvgID = (By.ID, 'com.hkfuliao.chamet:id/svag_tool_image')
    myBackpack_all_frameList = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')
    myBackpack_all_entranceList = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')




    # 我的任务
    # 男生
    MyTasks_entry = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.TextView[1]')
    MyTasks_entry_RightClick = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.TextView[2]')
    MyTasks_entry_points = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView')
    MyTasks_entry_rewards = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.LinearLayout')
    MyTasks_entry_rewardsRedDot = (By.ID, 'com.hkfuliao.chamet:id/reddot')
    MyTasks_task_completedPopover = (By.ID, 'com.hkfuliao.chamet:id/ll_content')
    MyTasks_task_completedPopoverOkBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_ok')
    MyTasks_tab_tasks = (By.ID, 'com.hkfuliao.chamet:id/tv_tab_tasks')
    MyTasks_tab_pointsNumber = (By.ID, 'com.hkfuliao.chamet:id/tv_points_number')
    MyTasks_tab_pointsSwitchBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_get_reward')
    MyTasks_tab_pointsMonthlyHistory = (By.ID, 'com.hkfuliao.chamet:id/ll_monthly_history')
    MyTasks_tab_pointsMonthlyHistoryPopoverUserID = (By.ID, 'com.hkfuliao.chamet:id/tv_user_id')
    MyTasks_tab_pointsMonthlyHistoryPopoverUsername = (By.ID, 'com.hkfuliao.chamet:id/tv_user_name')
    MyTasks_tasks_signinEntry = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.ViewGroup')
    MyTasks_tasks_signinSuccessXPATH = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView[1]')
    MyTasks_tasks_signinSuccessID = (By.ID, 'com.hkfuliao.chamet:id/iv_sign_success')
    MyTasks_tasks_signinTEXT = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]')
    MyTasks_tasks_signinPoints = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]')
    MyTasks_tasks_inviteEntry = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup')
    MyTasks_tasks_inviteEntryText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView[1]')
    MyTasks_tasks_inviteEntryTextXpath = (By.XPATH,"//*[@text='邀请']")
    MyTasks_tasks_invitePopoverAll = (By.ID,'com.hkfuliao.chamet:id/cardView3')
    MyTasks_tasks_TopOffersEntry = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[3]/android.view.ViewGroup')
    MyTasks_tasks_TopOffersEntryText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView[1]')
    MyTasks_tasks_TopOffersEntryTextXPATH = (By.XPATH,"//*[@text='Top Offers']")
    MyTasks_tasks_TopOffersTitle = (By.ID, 'com.hkfuliao.chamet:id/tv_base_title')
    MyTasks_tasks_TopOffersGoback = (By.ID, 'com.hkfuliao.chamet:id/iv_base_back')
    MyTasks_tasks_DailyTasksName = (By.ID, 'com.hkfuliao.chamet:id/tvTaskName')
    MyTasks_tasks_DailyTasksAll = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')
    MyTasks_tasks_DailyTasksList = (By.XPATH,'//android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')
    MyTasks_tasks_MonthlyTasksName = (By.ID, 'com.hkfuliao.chamet:id/tvTaskName')
    MyTasks_tasks_MonthlyTasksAll = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    MyTasks_tasks_MonthlyTasksList = (By.XPATH,'//android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')
    # 奖励
    MyTasks_tab_rewards = (By.ID, 'com.hkfuliao.chamet:id/tv_tab_rewards')
    MyTasks_rewards_RedTagNew = (By.ID, 'com.hkfuliao.chamet:id/tv_reward_red_tag')
    MyTasks_rewards_TopUpMonthCard = (By.ID, 'com.hkfuliao.chamet:id/svga_top_up_month_card')
    MyTasks_rewards_TopUpMonthCardPopoverAll = (By.ID, 'com.hkfuliao.chamet:id/rootView')
    MyTasks_rewards_TopUpMonthCardPopoverBuyBtn = (By.ID, 'com.hkfuliao.chamet:id/ll_buy_btn')
    MyTasks_rewards_TopUpMonthCardPopoverCard = (By.ID, 'com.hkfuliao.chamet:id/cl_card')
    MyTasks_rewards_TopUpMonthCardPopoverCardText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]')
    MyTasks_rewards_TopUpMonthCard0Points = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout')
    MyTasks_rewards_LeftReward = (By.ID, 'com.hkfuliao.chamet:id/fl_left_reward')
    MyTasks_rewards_RewardClaimedIcon = (By.ID, 'com.hkfuliao.chamet:id/iv_receive_status')
    MyTasks_rewards_RewardDetailsPopoverOkBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_ok_btn')
    MyTasks_rewards_CongratsPopover = (By.ID, 'com.hkfuliao.chamet:id/flPopup')
    MyTasks_rewards_CongratsPopoverAwesomeBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_awesome')
    MyTasks_rewards_CongratsPopoverGiftTag = (By.ID, 'com.hkfuliao.chamet:id/tv_gift_tag')
    MyTasks_rewards_RightReward = (By.ID, 'com.hkfuliao.chamet:id/fl_right_reward')
    MyTasks_rewards_RightRewardContent = (By.ID, 'com.hkfuliao.chamet:id/right_ll_reward_content')
    MyTasks_rewards_TaskCompletePopover=(By.ID,'com.hkfuliao.chamet:id/tv_task_complete')
    MyTasks_rewards_TaskCompletePopoverOkBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_ok')
    MyTasks_rewards_DoTasksNowBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_do_task_now')
    MyTasks_rewards_first100Claimed = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout')
    MyTasks_rewards_manFirst100Claimed_Status = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView[2]')
    MyTasks_rewards_manLast6500NoClaim = (By.ID, 'com.hkfuliao.chamet:id/iv_gift_pic')
    MyTasks_rewards_manLast6500NoClaimXpath = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView')
    MyTasks_rewards_LeftClickGuideID = (By.ID, 'com.hkfuliao.chamet:id/svga_left_click_guide')
    MyTasks_rewards_RightClickGuideID= (By.ID,'com.hkfuliao.chamet:id/svga_right_click_guide')



    # 女生
    MyTasks_womanTasks_LoginAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView')
    MyTasks_womanTasks_LoginDayNum = (By.ID,'com.hkfuliao.chamet:id/tv_day_num')
    MyTasks_womanTasks_LoginRewardNum = (By.ID, 'com.hkfuliao.chamet:id/tv_reward_num')
    MyTasks_womanTasks_alreadyLoginAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
    MyTasks_womanTasks_alreadyLoginCompletedText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]')
    MyTasks_womanTasks_LoginTomorrowAll = (By.ID, 'com.hkfuliao.chamet:id/ll_sign_tomorrow_day')
    MyTasks_womanTasks_LoginTomorrowText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]')
    MyTasks_womanTasks_dailyTasks = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')

    MyTasks_womanRewards_RewardsText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView')
    MyTasks_womanRewards_RewardsAll = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout')
    # 你获得了
    MyTasks_womanRewards_RewardsPopoverText = (By.ID, 'com.hkfuliao.chamet:id/tv_you_got')
    MyTasks_womanRewards_RewardsPointsText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView')
    MyTasks_womanRewards_RewardsStatusClaimed = (By.ID, 'com.hkfuliao.chamet:id/tv_receive_state_claimed')
    MyTasks_womanRewards_RewardsStatusClaim = (By.ID, 'com.hkfuliao.chamet:id/tv_receive_state_claim')
    MyTasks_womanRewards_RewardsStatusLocked = (By.ID, 'com.hkfuliao.chamet:id/tv_receive_state_locked')




    # 我的打招呼
    MyGreetingWords_entryText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[7]/android.widget.TextView[1]')
    MyGreetingWords_entry = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[7]')
    MyGrWords_Title = (By.ID, 'com.hkfuliao.chamet:id/title')
    MyGrWords_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    MyGrWords_faceVerification_popoverAll = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup')
    MyGrWords_faceVerification_popoverText = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    MyGrWords_faceVerification_popoverConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_single_btn')
    # 真人检测
    # 这仅用于检测真人，不用于任何其他目的。
    MyGrWords_faceVerification_cameraTitle = (By.ID, 'com.hkfuliao.chamet:id/tv_title')
    MyGrWords_faceVerification_cameraTips = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[5]')
    MyGrWords_faceVerification_cameraTipsXpath = (By.XPATH,"//*[@text='这仅用于检测真人，不用于任何其他目的。']")
    MyGrWords_faceVerification_cameraCloseBtn = (By.ID, 'com.hkfuliao.chamet:id/closeTv')
    # 未检测到该动作，请重试。
    MyGrWords_faceVerification_cameraTryPopContent = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    MyGrWords_faceVerification_cameraTryPopConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    MyGrWords_faceVerification_cameraTryPopCancelBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')


    # 之前没有打招呼记录
    MyGrWords_edit_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    MyGrWords_edit_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    MyGrWords_edit_contentText = (By.ID, 'com.hkfuliao.chamet:id/et_message_content')
    MyGrWords_edit_camera = (By.ID, 'com.hkfuliao.chamet:id/iv_send_camera')
    # tap(533,1892)拍照按钮
    MyGrWords_edit_cameraRecordBtn = (By.ID,'com.hkfuliao.chamet:id/record_btn')
    MyGrWords_edit_cameraConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/img_record_success_and_send')
    MyGrWords_edit_albumPhoto = (By.ID, 'com.hkfuliao.chamet:id/iv_send_album_photo')
    # tap(522,427)系统第二张图片
    MyGrWords_edit_errorTip = (By.ID, 'com.hkfuliao.chamet:id/tv_error_tip')
    MyGrWords_edit_saveBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_save')
    # 有打招呼记录list
    MyGrWords_wordListAll = (By.ID, 'com.hkfuliao.chamet:id/rv_greeting_words_list')
    MyGrWords_wordListNum = (By.ID,'com.hkfuliao.chamet:id/v_select_message')
    MyGrWords_wordListID = (By.ID,'com.hkfuliao.chamet:id/rootView')
    MyGrWords_wordListFirst = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.View[1]')
    MyGrWords_wordListNumTotal = (By.CLASS_NAME, 'android.widget.ImageView')
    MyGrWords_wordList_StatusFailedAndIng = (By.ID, 'com.hkfuliao.chamet:id/tv_audit_status')
    MyGrWords_wordList_StatusFailedText = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.TextView')
    MyGrWords_wordList_StatusFailedList = (By.CLASS_NAME,'android.widget.LinearLayout')
    MyGrWords_wordList_editBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_edit')
    MyGrWords_TipsWords = (By.ID, 'com.hkfuliao.chamet:id/tv_msg')
    MyGrWords_MyWords_AddBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_add')
    MyGrWords_sendAllBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_send_mass_message')
    MyGrWords_MyWordsText = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView')
    MyGrWords_MyWordsEditor = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
    # 暂时不能群发消息，因为你的等级低于Lv3。
    # 我的等级
    # 取消
    MyGrWords_sendAllBtn_3levelPopCon = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    MyGrWords_sendAllBtn_3levelPopConfirm = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    MyGrWords_sendAllBtn_3levelPopCancel = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')



    # 我的简介
    myProfile_entry_man = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[7]/android.widget.TextView[1]')
    myProfile_entry_woman = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[6]/android.widget.TextView[1]')
    myProfile_entry_manRightClick = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[7]/android.widget.TextView[2]')
    myProfile_entry_womanRightClick = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[6]/android.widget.TextView[2]')
    myProfile_Title=(By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_Goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_MyAvatar_img = (By.ID, 'com.hkfuliao.chamet:id/civ_default_image')
    myProfile_MyAvatar_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_MyAvatar_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_MyAvatar_poster = (By.ID, 'com.hkfuliao.chamet:id/iv_poster_pic')
    myProfile_MyAvatar_posterTipContents = (By.ID, 'com.hkfuliao.chamet:id/tv_poster_default_tip')
    myProfile_MyAvatar_posterScoreTitle = (By.ID,'com.hkfuliao.chamet:id/tv_poster_score_title')
    myProfile_MyAvatar_posterScoreNum = (By.ID, 'com.hkfuliao.chamet:id/tv_poster_score')
    myProfile_MyAvatar_posterScoreTips = (By.ID, 'com.hkfuliao.chamet:id/tv_score_tip')
    myProfile_MyAvatar_ChangePosterBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_change_poster')
    myProfile_MyAvatar_ChangePosterPopoverAll = (By.ID,'com.hkfuliao.chamet:id/recyclerView')
    myProfile_MyAvatar_ChangePosterPopPictureBtn = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')
    myProfile_MyAvatar_ChangePosterUpdateConfirm = (By.ID,'com.hkfuliao.chamet:id/iv_cover_update')
    myProfile_MyAvatar_PosterState = (By.ID, 'com.hkfuliao.chamet:id/ll_upload_poster_state')
    myProfile_MyAvatar_PosterStateText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
    myProfile_MyAvatar_ChangePosterFailedBtn = (By.ID,'com.hkfuliao.chamet:id/single_btn')
    myProfile_MyAvatar_PosterHistoryBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_poster_history')
    myProfile_MyAvatar_PosterHistoryTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_MyAvatar_PosterScore = (By.ID, 'com.hkfuliao.chamet:id/tv_poster_score')
    myProfile_MyAvatar_PosterHistoryScore = (By.ID, 'com.hkfuliao.chamet:id/tv_poster_score')
    myProfile_MyAvatar_PosterHistoryGoback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_MyAvatar_PosterHistorySaveBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_save_poster')
    myProfile_MyAvatar_PosterHistoryThirdPoints = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.FrameLayout/android.widget.TextView')

    myProfile_ID_Number = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[1]')
    myProfile_ID_CopyBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_copy_btn')

    myProfile_NickName_Text = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_NickName_RightClick = (By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView[2]')
    myProfile_NickName_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_NickName_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_NickName_EditorCommit = (By.ID, 'com.hkfuliao.chamet:id/iv_commit')
    myProfile_NickName_EditorContent = (By.ID, 'com.hkfuliao.chamet:id/et_content')

    myProfile_Gender = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_GenderAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.view.ViewGroup')
    myProfile_GenderTextGender = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.TextView')
    myProfile_GenderTextMan = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_GenderTextWoman = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')

    myProfile_Age_Text = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[5]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_Age_All = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[5]/android.view.ViewGroup')
    myProfile_Age_popoverDateYear = (By.ID, 'android:id/date_picker_header_year')
    myProfile_Age_popoverDateYearSecond = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.ListView/android.widget.TextView[2]')
    myProfile_Age_popoverDateCancelBtn = (By.ID, 'android:id/button2')
    myProfile_Age_popoverDateConfirmBtn = (By.ID, 'android:id/button1')

    myProfile_Region_Text = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[6]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_Region_Image=(By.ID,'com.hkfuliao.chamet:id/civ_country_image')

    myProfile_Location_Text = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[7]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_Location_All = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[7]/android.view.ViewGroup')
    myProfile_Location_PopoverAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout')
    myProfile_Location_Popover1stIcon = (By.ID, 'com.hkfuliao.chamet:id/firstPosIcon')
    myProfile_Location_Popover1stIcon_Text = (By.ID, 'com.hkfuliao.chamet:id/firstPostText')
    myProfile_Location_Popover2edIcon = (By.ID, 'com.hkfuliao.chamet:id/secondPosIcon')
    myProfile_Location_Popover2edIcon_Text = (By.ID, 'com.hkfuliao.chamet:id/secondPostText')
    myProfile_Location_PopoverConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    myProfile_Location_PopoverCancelBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')

    myProfile_Language_Text = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[8]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_Language_All = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[8]/android.view.ViewGroup')
    myProfile_Language_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_Language_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_Language_ChooseLanguage = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
    myProfile_Language_ChooseLanguageText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    myProfile_Language_SelectFlag = (By.ID, 'com.hkfuliao.chamet:id/iv_select_flag')
    myProfile_Language_LanguageEnglish = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    myProfile_Language_LanguageEnglishText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')
    myProfile_Language_PopoverContent = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    myProfile_Language_PopoverConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    myProfile_Language_PopoverCancelBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')

    myProfile_SecondLanguage_Text = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[9]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[9]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView
    # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[9]/android.view.ViewGroup/android.widget.TextView[1]
    myProfile_SecondLanguage_All = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[9]/android.view.ViewGroup')
    myProfile_SecondLanguage_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_SecondLanguage_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_SecondLanguage_ChooseLanguageAll = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
    myProfile_SecondLanguage_ChooseLanguageText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    myProfile_SecondLanguage_SelectFlag = (By.ID, 'com.hkfuliao.chamet:id/iv_select_flag')
    myProfile_SecondLanguage_LanguageMalayu = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[10]')
    myProfile_SecondLanguage_LanguageMalayuText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[10]/android.widget.TextView')
    myProfile_SecondLanguage_LanguageIndonesia = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[9]')
    myProfile_SecondLanguage_LanguageIndonesiaText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[9]/android.widget.TextView')
    myProfile_SecondLanguage_PopoverContent = (By.ID, 'com.hkfuliao.chamet:id/tv_content')
    myProfile_SecondLanguage_PopoverConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')
    myProfile_SecondLanguage_PopoverCancelBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_cancel')

    myProfile_SelfIntroduction_All = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[11]/android.view.ViewGroup')
    myProfile_SelfIntroduction_title = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_SelfIntroduction_goback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_SelfIntroduction_content = (By.ID, 'com.hkfuliao.chamet:id/et_content')
    myProfile_SelfIntroduction_CommitBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_commit')

    myProfile_Google_All = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[12]/android.view.ViewGroup')
    myProfile_Google_Popover = (By.ID, 'com.google.android.gms:id/account_picker_container')
    myProfile_Google_PopoverFirstAccountAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout')
    myProfile_Google_PopoverFirstAccountText = (By.ID, 'com.google.android.gms:id/account_display_name')
    myProfile_Google_PopoverAccountAddText = (By.ID,'com.google.android.gms:id/add_account_chip_title')
    myProfile_Google_PopoverAccountAddAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]')

    myProfile_Phone_entryText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[13]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_Phone_entryAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[13]/android.view.ViewGroup')
    myProfile_Phone_ChangeNumAll = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
    myProfile_Phone_ChangeNumText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    myProfile_Phone_ChangeCancelAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    myProfile_Phone_ChangeTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_Phone_ChangeGoback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_Phone_ChangeAreaCode = (By.ID, 'com.hkfuliao.chamet:id/tv_area_code')
    myProfile_Phone_ChangePhoneNum = (By.ID, 'com.hkfuliao.chamet:id/edit_phone_number')
    myProfile_Phone_ChangeVerCode = (By.ID, 'com.hkfuliao.chamet:id/edit_code')
    myProfile_Phone_ChangeSendBtn = (By.ID, 'com.hkfuliao.chamet:id/send')
    myProfile_Phone_ChangeNextBtn = (By.ID, 'com.hkfuliao.chamet:id/next')
    myProfile_Phone_ChangeBindBtn = (By.ID, 'com.hkfuliao.chamet:id/bind_phone')

    myProfile_Gmail_entry = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[14]/android.view.ViewGroup')
    myProfile_Gmail_BindTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_Gmail_entryText = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[14]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    # 换绑
    myProfile_Gmail_BindChangePopConf = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    myProfile_Gmail_BindChangePopCan = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')
    #绑定Gmail邮箱
    #输入你的Gmail邮箱
    #@gmail.com
    myProfile_Gmail_BindMail = (By.ID, 'com.hkfuliao.chamet:id/edit_phone_number')
    myProfile_Gmail_BindMailTips = (By.ID, 'com.hkfuliao.chamet:id/tv_gmail_tip')
    myProfile_Gmail_BindCode = (By.ID, 'com.hkfuliao.chamet:id/edit_code')
    myProfile_Gmail_BindCodeSend = (By.ID, 'com.hkfuliao.chamet:id/send')
    myProfile_Gmail_BindConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/bind_phone')
    myProfile_Gmail_BindGoback = (By.ID, 'com.hkfuliao.chamet:id/back')




    myProfile_Password_entryAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[15]/android.view.ViewGroup')
    myProfile_Password_entryText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[15]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView')
    myProfile_Password_entryRedDotXpath = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[15]/android.view.ViewGroup/android.widget.LinearLayout/android.view.View')
    myProfile_Password_entryRedDot = (By.ID,'com.hkfuliao.chamet:id/iv_red_dot')
    myProfile_Password_popoverResetText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    myProfile_Password_popoverResetAll=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
    myProfile_Password_popoverResetCancel = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    myProfile_Password_ResetTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_Password_ResetGoback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_Password_ResetEditCode = (By.ID, 'com.hkfuliao.chamet:id/edit_code')
    myProfile_Password_ResetSendBtn = (By.ID, 'com.hkfuliao.chamet:id/send')
    myProfile_Password_ResetNextBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_next')
    myProfile_Password_ChangeTitle = (By.ID, 'com.hkfuliao.chamet:id/title')
    myProfile_Password_ChangeGoback = (By.ID, 'com.hkfuliao.chamet:id/back')
    myProfile_Password_ChangeNumber = (By.ID, 'com.hkfuliao.chamet:id/tv_reset_password_tips')
    myProfile_Password_ChangeTipsText = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]')
    myProfile_Password_ChangeEnterPw = (By.ID, 'com.hkfuliao.chamet:id/edit_enter_password')
    myProfile_Password_ChangeReEnterPw = (By.ID, 'com.hkfuliao.chamet:id/edit_reenter_password')
    myProfile_Password_ChangeConfirmBtn = (By.ID, 'com.hkfuliao.chamet:id/tv_confirm')

    # 我的余额
    myBalance_entryManAll=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]')
    myBalance_entryWomanAll = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[8]')
    myBalance_entryDiscountIcon = (By.ID, 'com.hkfuliao.chamet:id/img_discount_coupon')
    myBalance_entryDiamondManNum = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.TextView')
    myBalance_entryDiamondWomanNum = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[8]/android.widget.LinearLayout/android.widget.TextView')
    myBalance_entry_goback = (By.ID, 'com.hkfuliao.chamet:id/fv_back')
    myBalance_myDiamondText = (By.ID, 'com.hkfuliao.chamet:id/tv_my_diamonds')
    myBalance_entry3rdID = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div[1]/div/div[2]/span')
    myBalance_entry3rdDetail = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[1]/img[4]')
    myBalance_entry3rdDetailCLASS= (By.XPATH,'//*[@id="type-txt"]')
    myBalance_entry3rdAmount = (By.CLASS_NAME,'balance_amount')
    myBalance_entry3rdAmountTEXT = (By.CLASS_NAME, "//*[@text='余额']")
    myBalance_entry3rdAmountXPATH = (By.XPATH,'/html/body/div/div/div/div[1]/div[3]/div[1]/div/div')
    myBalance_myDiamondCountText = (By.ID, 'com.hkfuliao.chamet:id/tv_my_diamonds_count')
    myBalance_topOffers_Entry = (By.ID, 'com.hkfuliao.chamet:id/iv_free_advertising')
    myBalance_topOffers_Title = (By.ID, 'com.hkfuliao.chamet:id/tv_base_title')
    myBalance_topOffers_Goback = (By.ID, 'com.hkfuliao.chamet:id/iv_base_back')
    myBalance_topOffers_AllOffers = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.TextView')
    myBalance_DiamondDetailEntry = (By.ID, 'com.hkfuliao.chamet:id/fv_recharge_detail')
    myBalance_DiamondDetail_TitleID = (By.ID, 'transactions')
    myBalance_DiamondDetail_TitleClass = (By.CLASS_NAME, 'title i18n')
    myBalance_DiamondDetail_TitleXpath = (By.XPATH,"//*[@text='交易记录']")
    myBalance_DiamondDetail_Goback = (By.CLASS_NAME, 'go_back')
    myBalance_DiamondDetail_selectTab = (By.CLASS_NAME, 'hdtab hdtab_other')
    myBalance_DiamondDetail_ContentBox = (By.CLASS_NAME, 'withdraw-box')
    myBalance_ServiceEntry = (By.ID, 'com.hkfuliao.chamet:id/fv_service')
    myBalance_Service_title = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView')
    myBalance_Service_goback = (By.ID, 'com.hkfuliao.chamet:id/aihelp_iv_back')
    myBalance_Service_helpInput = (By.ID, 'com.hkfuliao.chamet:id/aihelp_et_input')
    myBalance_FirstRecharge = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup')
    myBalance_FirstRechargeText = (By.ID, 'com.hkfuliao.chamet:id/tv_first_recharge_title')
    myBalance_TopUpList = (By.ID, 'com.hkfuliao.chamet:id/recycler_top_up_list')
    myBalance_TopUpList5Id = (By.ID, 'com.hkfuliao.chamet:id/root_view')
    myBalance_TopUpTabTitle = (By.ID,'com.hkfuliao.chamet:id/tv_recharge_tab_title')
    myBalance_TopUpRecChangeBtn = (By.ID,'com.hkfuliao.chamet:id/btn_change')
    myBalance_TopUpRecChangePopSelected = (By.ID,'com.hkfuliao.chamet:id/iv_select_type')
    myBalance_TopUpListNextCard= (By.ID,'com.hkfuliao.chamet:id/webview')
    myBalance_TopUp_googleTestCard = (By.XPATH, '//android.widget.LinearLayout[@content-desc="测试卡，一律批准. 更改付款方式"]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')
    myBalance_TopUp_googleTestCardXpath = (By.XPATH, "//*[@text='测试卡，一律批准']")
    myBalance_TopUp_googleBuyBtn = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button')
    myBalance_TopUp_googleBuyBtnXpath = (By.XPATH,"//*[@text='一键购买']")
    myBalance_TopUp_successText = (By.ID, 'com.hkfuliao.chamet:id/dialog_msg')
    # 恭喜！你得到4,500[diamond]
    # 知道了
    myBalance_TopUp_successKnowBtn = (By.ID, 'com.hkfuliao.chamet:id/single_btn')
    myBalance_TopUpList_firstEle = (By.ID, 'com.hkfuliao.chamet:id/view9')
    myBalance_TopUpListmoreBtn = (By.ID,'com.hkfuliao.chamet:id/iv_more_pic')
    myBalance_TopUpListmoreTitle = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.Image[2]')
    myBalance_agreeBtn = (By.ID, 'com.hkfuliao.chamet:id/iv_agree')
    myBalance_agreeContent = (By.ID, 'com.hkfuliao.chamet:id/tv_agree_content')
    more_btn = (By.ID, 'com.hkfuliao.chamet:id/tv_more')



    '''===================【顶部个人主页内容】==================='''
    # '登录的前置函数'
    def login_step(self,phone,password):
        self.phone = phone
        self.password=password
        l=LoginView(self.driver)
        l.more_Btn()
        l.phonenumber_Btn()
        time.sleep(2)
        l.login_input_phonenumber(phone)
        l.login_input_password_or_code(password)

    def login_direct_phone(self,phone,password):
        try:
            self.phone = phone
            self.password = password
            l = LoginView(self.driver)
            l.more_Btn()
            self.driver.find_element(*LoginView.phonenumber_btn).click()
            self.driver.find_element(*LoginView.input_phonenumber).set_value(self.phone)
            self.driver.find_element(*LoginView.next_btn).click()
            l.login_input_phone_password(self.password)
        except NoSuchElementException:
            logging.info('no ele')
        else:
            l.tap(930, 2123)

    '''点击我的图标'''
    def tab_Mine_Btn(self):
        try:
            Common.tap(self, 960, 2262)
            tab_mine = self.driver.find_element(*self.tab_mine_btn)
        except NoSuchElementException:
            logging.info('no tab_mine_btn')
        else:
            tab_mine.click()

    '''点击我的图标'''
    def tab_Mine_Btn_126(self):
        try:
            tab_mine = self.driver.find_element(*self.tab_mine_btn)
        except NoSuchElementException:
            logging.info('no tab_mine_btn')
        else:
            tab_mine.click()

    '''点击我的图标85手机'''
    def tab_Mine_Btn_85(self):
        try:
            Common.tap(self, 956, 2124)
            tab_mine = self.driver.find_element(*self.tab_mine_btn)
        except NoSuchElementException:
            logging.info('no tab_mine_btn')
        else:
            tab_mine.click()





    '''点击我的页面个人头像'''
    def tab_Mine_Head(self):
        try:
            tab_mine_head=self.driver.find_element(*self.tab_mine_head)
        except NoSuchElementException:
            logging.info('no tab_mine_head')
        else:
            tab_mine_head.click()

    '''获取我的页面个人头像框'''
    def tab_Mine_Head_level_frame(self):
        try:
            self.driver.find_element(*self.user_head_levelFrameAll)
        except NoSuchElementException:
            logging.info('no user_head_levelFrame')
            return False
        else:
            return True


    '''获取我的页面个人昵称'''
    def tab_Mine_user_name(self):
        try:
            user_name = self.driver.find_element(*self.user_name)
        except NoSuchElementException:
            logging.info('no user_name')
            return False
        else:
            return True

    '''获取我的页面等级图标'''
    def tab_Mine_user_vip_level(self):
        try:
            user_vipLevel = self.driver.find_element(*self.user_vipLevel)
        except NoSuchElementException:
            logging.info('no user_vipLevel')
            return False
        else:
            return user_vipLevel

    '''我的等级页校验'''
    def tab_Mine_user_vipLevel_LelEle(self):
        lel_ele = self.tab_Mine_user_vip_level()
        if lel_ele != False:
            return lel_ele
        else:
            logging.info('no user_vipLevel')
            return False

    '''获取我的页面国家图标'''
    def tab_Mine_user_nation(self):
        try:
            user_nationText = self.driver.find_element(*self.user_nationText)
        except NoSuchElementException:
            logging.info('no user_nationText')
            return False
        else:
            return user_nationText.text

    '''获取我的页面语言图标'''
    def tab_Mine_user_language(self):
        try:
            user_language_Text = self.driver.find_element(*self.user_language_Text)
        except NoSuchElementException:
            logging.info('no user_language_Text')
            return False
        else:
            return user_language_Text.text

    '''我的页面语言跳转校验'''
    def tab_Mine_user_language_LanEle(self):
        lan_ele = self.tab_Mine_user_language()
        lan_point=chr(183)
        if lan_ele !=False:
            if lan_point in lan_ele:
                return 2
            else:
                return 1
        else:
            logging.info('no user_language')
            return 0

    '''获取我的页面朋友图标'''
    def tab_Mine_user_friend(self):
        try:
            user_friendNumText = self.driver.find_element(*self.user_friendNumText)
        except NoSuchElementException:
            logging.info('no user_friendNumText')
            return False
        else:
            return user_friendNumText.text

        # 获取聊天区文本消息
    def get_usermessage_textcontent(self, num):
        # usermessage_region_textele = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView")
        usermessage_region_textele = (MobileBy.XPATH,
                                      "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView")
        usermessage_region_text = self.driver.find_elements(*usermessage_region_textele)
        return usermessage_region_text[num].text


    '''我的页面朋友跳转校验'''
    def tab_Mine_user_friend_FriendsEle(self):
        friend_ele = self.tab_Mine_user_friend()
        if friend_ele != False:
            if friend_ele != '0':
                return 1
            else:
                return 0
        else:
            logging.info('no user_friendNumText')
            return False

    '''获取我的页面关注图标'''
    def tab_Mine_user_following(self):
        try:
            user_followingNumText = self.driver.find_element(*self.user_followingNumText)
        except NoSuchElementException:
            logging.info('no user_followingNumText')
            return False
        else:
            return user_followingNumText.text

    '''我的页面关注跳转校验'''
    def tab_Mine_user_following_FollowingEle(self):
        following_ele = self.tab_Mine_user_following()
        if following_ele != False:
            if following_ele != '0':
                return 1
            else:
                return 0
        else:
            logging.info('no user_followingNumText')
            return False

    '''获取我的页面粉丝图标'''
    def tab_Mine_user_followers(self):
        try:
            user_followers_NumText = self.driver.find_element(*self.user_followers_NumText)
        except NoSuchElementException:
            logging.info('no user_followers_NumText')
            return False
        else:
            return user_followers_NumText.text

    '''我的页面粉丝跳转校验'''
    def tab_Mine_user_followers_FollowersEle(self):
        followers_ele = self.tab_Mine_user_followers()
        if followers_ele != False:
            if followers_ele!='0':
                return 1
            else:
                return 0
        else:
            logging.info('no user_followers_NumText')
            return False

        # if followers_ele != False and followers_ele != 0:
        #     # return 1
        #     print('1')
        #
        # elif followers_ele != False and followers_ele == 0:
        #     # return 0
        #     print('0')
        # else:
        #     logging.info('no user_followers_NumText')
        #     # return False
        #     print('False')

    # 男生签到后点击好的弹窗消失，女生签到后点击兑换奖励跳转到我的任务-奖励页面（任务完成弹窗或者奖励的selected=true页面）
    '''获取我的页面签到图标'''
    def tab_Mine_user_signInfoTop(self):
        try:
            user_sign_infoTop = self.driver.find_element(*self.user_sign_infoTop)
        except NoSuchElementException:
            logging.info('no user_sign_infoTop')
            return False
        else:
            return user_sign_infoTop

    # '''校验我的页面签到图标再点击'''
    # def tab_Mine_user_signInfoTopEle(self):
    #     signInfoTopEle = self.tab_Mine_user_signInfoTop()
    #     if signInfoTopEle!=False:
    #         # signInfoTopEle.click()
    #         return True
    #     else:
    #         logging.info('no signInfoTopEle')
    #         return False

    '''校验我的页面签到图标跳转任务页的有无任务完成弹窗'''
    def tab_Mine_user_signInfoTopEleTASK(self):
        try:
            MyTasks_rewards_TaskCompletePopoverOkBtn = self.driver.find_element(*self.MyTasks_rewards_TaskCompletePopoverOkBtn)
        except NoSuchElementException:
            logging.info('no MyTasks_rewards_TaskCompletePopoverOkBtn')
            return False
        else:
            return MyTasks_rewards_TaskCompletePopoverOkBtn



    # ======个人主页================================
    '''进入个人主页，查找个人信息元素'''
    def tab_mine_personal_information_test(self):
        try:
            user_own_pagePersonalInformationText = self.driver.find_element(*self.user_own_pagePersonalInformationText)
        except NoSuchElementException:
            logging.info('no user_own_pagePersonalInformationText')
            return False
        else:
            return True

    '''获取个人主页昵称'''
    def tab_mine_user_own_pagePersonalName(self):
        try:
            user_own_pagePersonalName = self.driver.find_element(*self.user_own_pagePersonalName)
        except NoSuchElementException:
            logging.info('no user_own_pagePersonalName')
            return False
        else:
            return True

    '''获取个人主页自我介绍'''
    def user_ownPage_selfIntroductionEle(self):
        try:
            user_ownPage_selfIntroduction = self.driver.find_element(*self.user_ownPage_selfIntroduction)
        except NoSuchElementException:
            logging.info('no user_ownPage_selfIntroduction')
            return False
        else:
            return user_ownPage_selfIntroduction.text

    '''点击个人主页返回键'''
    def tab_mine_personal_goback_btn(self):
        try:
            user_own_pageGobackBtn = self.driver.find_element(*self.user_own_pageGobackBtn)
        except NoSuchElementException:
            logging.info('no user_own_pageGobackBtn')
            return False
        else:
            user_own_pageGobackBtn.click()
            return True


    '''半屏个人主页浮层姓名将"..."拆出去'''
    def messages_Group_userHalfPagePopoverNameText(self):
        try:
            messages_Group_userHalfPagePopoverName = self.driver.find_element(*self.messages_Group_userHalfPagePopoverName).text
        except NoSuchElementException:
            logging.info('no messages_Group_userHalfPagePopoverName')
            return False
        else:
            if "..." in messages_Group_userHalfPagePopoverName:
                return messages_Group_userHalfPagePopoverName.split('...')
            else:
                return messages_Group_userHalfPagePopoverName



    '''速配弹窗'''
    def randomCall_popoverEle(self):
        logging.info('查找速配弹窗有无')
        try:
            Permission_85Phone_PopoverTitle = self.driver.find_element(*self.randomCall_popover)
        except NoSuchElementException:
            return False
        else:
            logging.info('有速配弹窗')
            return True

    # '''速配弹窗检查'''
    # def Check_RandomCall_PopoverEle(self):
    #     if self.Permission_popoverTitleEle() != False:
    #         logging.info('速配弹窗检查')
    #         self.tap(930,2123)


    '''“Chamet”请求权限弹窗？'''
    # “Chamet”请求使用摄像头权限，是否允许？
    # “Chamet”请求存储权限，是否允许？
    # “Chamet”请求录音权限，是否允许？
    # def Permission_popoverTitleEle(self):
    #     logging.info('权限弹窗，是否允许？')
    #     try:
    #         Permission_popoverTitle = self.driver.find_element(*self.Permission_popoverTitle)
    #     except NoSuchElementException:
    #         return False
    #     else:
    #         print(Permission_popoverTitle.text)
    #         return Permission_popoverTitle.text
    #
    # '''85手机-请求权限弹窗？'''
    # def Permission_85Phone_PopoverTitleEle(self):
    #     logging.info('权限弹窗，是否允许？')
    #     try:
    #         Permission_85Phone_PopoverTitle = self.driver.find_element(*self.Permission_85Phone_PopoverTitle)
    #     except NoSuchElementException:
    #         return False
    #     else:
    #         print(Permission_85Phone_PopoverTitle.text)
    #         return Permission_85Phone_PopoverTitle.text



    def get_permission_checkPopover(self):
        logging.info('权限弹窗，是否允许？')
        try:
            Permission_popoverConfirmBtn = self.driver.find_element(*self.Permission_popoverConfirmBtn)
        except NoSuchElementException:
            return False
        else:
            print(Permission_popoverConfirmBtn)
            Permission_popoverConfirmBtn.click()
            return True

    '''85手机-请求权限弹窗？'''
    def Phone85_getPermission_checkPopover(self):
        logging.info('85权限弹窗，是否允许？')
        try:
            Permission_85Phone_PopoverConfirmBtn = self.driver.find_element(*self.Permission_85Phone_PopoverConfirmBtn)
        except NoSuchElementException:
            return False
        else:
            print(Permission_85Phone_PopoverConfirmBtn)
            Permission_85Phone_PopoverConfirmBtn.click()
            return True

    '''114手机-请求权限弹窗？'''
    def Phone114_getPermission_checkPopover(self):
        logging.info('114权限弹窗，是否允许？')
        try:
            Permission_114Phone_PopoverConfirmBtn1 = self.driver.find_element(*self.Permission_114Phone_PopoverConfirmOnlyBtn)
        except NoSuchElementException:
            return False
        else:
            print(Permission_114Phone_PopoverConfirmBtn1)
            Permission_114Phone_PopoverConfirmBtn1.click()
            return True


    '''114手机-请求权限弹窗？'''
    def Permission_114Phone_MediaPopoverConfirmBtnEle(self):
        logging.info('114权限弹窗，是否允许？')
        try:
            Permission_114Phone_MediaPopoverConfirmBtn1 = self.driver.find_element(*self.Permission_114Phone_MediaPopoverConfirmBtn)
        except NoSuchElementException:
            return False
        else:
            print(Permission_114Phone_MediaPopoverConfirmBtn1)
            Permission_114Phone_MediaPopoverConfirmBtn1.click()
            return True


    # def get_permission_checkPopover(self):
    #     if self.Permission_popoverTitleEle() != False:
    #         self.driver.find_element(*MultiMan.Permission_popoverConfirmBtn).click()


    # def system_getPermission_checkPopover(self):
    #     if self.Permission_85Phone_PopoverTitleEle() != False:
    #         self.driver.find_element(*MultiMan.Permission_85Phone_PopoverConfirmBtn).click()





    # '''===================开始【一级页面】内容==================='''

    # '''========留言============'''
    '''留言-留言入口-未读数元素有无'''
    def messages_entry_UnReadNumIDEle(self):
        logging.info('===未读数元素有无===')
        try:
            messages_entry_UnReadNumID111 = self.driver.find_element(*self.messages_entry_UnReadNumXpath)
        except NoSuchElementException:
            logging.info('no messages_entry_UnReadNumXpath')
            return False
        else:
            print(messages_entry_UnReadNumID111)
            print(type(messages_entry_UnReadNumID111))
            # print(messages_entry_UnReadNumID[0].text)
            # print(messages_entry_UnReadNumID[1].text)
            return messages_entry_UnReadNumID111.text

    '''留言-留言入口-chamet团队未读数元素有无'''
    def messages_system_UnReadNumXpathEle(self):
        logging.info('===chamet团队未读数元素有无===')
        try:
            messages_system_UnReadNumXpath = self.driver.find_elements(*self.messages_system_UnReadNumXpath)
        except NoSuchElementException:
            logging.info('no messages_system_UnReadNumXpath')
            return False
        else:
            print(messages_system_UnReadNumXpath)
            return messages_system_UnReadNumXpath


    '''留言-留言一级页面-未读数总和'''
    def messages_UnReadNum_lists(self):
        logging.info('===留言一级页面-未读数总和===')
        try:
            messages_UnReadNum3 = self.driver.find_elements(*self.messages_UnReadNumID)
            messages_system_UnReadNum2 = self.driver.find_elements(*self.messages_system_UnReadNumID)
        except NoSuchElementException:
            logging.info('no messages_UnReadNum')
            return False
        else:
            Num = 0
            for i, y in enumerate(messages_UnReadNum3):
                print(y.text)
                print(type(y))
                # text = self.driver.find_elements(y).text
                text = y.text
                Num = int(text) + Num
                # Num = int(y.text) + Num
                print(Num)
                print(type(Num))
            if len(messages_system_UnReadNum2)!=0:
                messages_system_UnReadNum22 = messages_system_UnReadNum2[0].text
                print(type(messages_system_UnReadNum22))
                return Num+int(messages_system_UnReadNum22)
            return Num

                # print(messages_system_UnReadNum1)
                # print(type(messages_system_UnReadNum1))
                #
                # print(messages_system_UnReadNum11)
                # print(type(messages_system_UnReadNum11))
                # print(messages_UnReadNum1)
                #
                # +messages_system_UnReadNum11





    # 通过更多-id查找用户
    def find_search_id(self):
        logging.info('===开始查找用户id===')
        try:
            self.driver.find_element(*self.tab_discoverEle).click()
            self.driver.find_element(*self.tab_discoverEle_selectedEntry).click()
            self.swipe(904,996,904,695,1000)
            self.driver.find_element(*self.tab_discoverEle_moreEntry).click()
            self.driver.find_element(*self.tab_discoverEle_searchInput).send_keys('33364388')
            self.driver.find_element(*self.tab_discoverEle_searchBtn).click()
            time.sleep(1)
            self.driver.find_element(*self.otherPage_messageBtn).click()
            time.sleep(1)
            self.driver.find_element(*self.message_editEle).send_keys('hhhhh')
            self.driver.find_element(*self.message_editEle).click()
            self.driver.find_element(*self.message_sendBtn).click()
        except NoSuchElementException:
            logging.info('查找陌生人未成功')
            return False
        else:
            logging.info('查找陌生人33364388已成功')


    '''留言列表-unread—元素有无'''
    def messages_Stranger_entryUnread_Ele(self):
        logging.info('===留言列表-unread—元素有无===')
        try:
            messages_Stranger_entryUnread_ele = self.driver.find_elements(*self.messages_Stranger_entryUnread)
        except NoSuchElementException:
            logging.info('no messages_Group_entryGroupName')
            return False
        else:
            return True


    '''留言用户-unread—元素有无'''
    def messages_Stranger_userListUnread_Ele(self):
        logging.info('===留言用户-unread—元素有无===')
        try:
            messages_Stranger_userListUnread1 = self.driver.find_element(*self.messages_Stranger_userListUnread)
        except NoSuchElementException:
            logging.info('no messages_Stranger_userListUnread')
            return False
        else:
            return messages_Stranger_userListUnread1




    # 观众端打开私聊送礼页面
    def usermessage_open_giftpage(self):
        try:
            logging.info('===打开私聊送礼页面===')
            open_giftbut = self.driver.find_element(MobileBy.ID, 'com.hkfuliao.chamet:id/ll_send_gift')
            open_giftbut.click()
        except:
            logging.info('===无礼物按钮===')

        # # 礼物浮层页面左滑右滑
        # def usermessage_scroll_gift(self):
        #     logging.info('送礼浮层左右滑动')
        #     gift_list_text = self.driver.find_elements(*self.messages_Stranger_GiftFirstTabFirst)
        #     gift_list_text[1].click()
        #     self.swipe(1000, 1750, 100, 1750, 500)
        #     nowgift_list_text = self.driver.find_elements(*self.messages_Stranger_GiftFirstTabFirst)
        #     self.swipe(100, 1750, 1000, 1750, 500)
        #     newgift_list_text = self.driver.find_elements(*self.messages_Stranger_GiftFirstTabFirst)
        #     return nowgift_list_text, newgift_list_text


        # 观众端私聊礼物页面左滑右滑
    def usermessage_scroll_gift(self):
        # self.usermessage_open_giftpage()
        logging.info('送礼浮层左右滑动')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("热门")').click()
        gift_list_text = self.driver.find_elements(MobileBy.XPATH,
                                                   "//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
        gift_list_text[1].click()
        self.swipe(1000, 1750, 100, 1750, 500)
        nowgift_list_text = self.driver.find_elements(MobileBy.XPATH,
                                                      "//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")[0].text
        self.swipe(100, 1750, 1000, 1750, 500)
        newgift_list_text = self.driver.find_elements(MobileBy.XPATH,
                                                      "//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")[0].text
        return nowgift_list_text, newgift_list_text




    '''留言-翻译内容元素有无'''
    def messages_Stranger_translateContentEle(self):
        logging.info('===chamet团队未读数元素有无===')
        try:
            messages_Stranger_translateContent1 = self.driver.find_element(*self.messages_Stranger_translateContent).text
        except NoSuchElementException:
            logging.info('no messages_Stranger_translateContent')
            return False
        else:
            return messages_Stranger_translateContent1



    # 观众端私聊页面发送表情
    def audience_usermessage_sendexpression(self,index):
        logging.info('===准备发送表情===')
        usermessage_expression_but = (MobileBy.ID,"com.hkfuliao.chamet:id/iv_face_gif")
        self.driver.find_element(*usermessage_expression_but).click()
        time.sleep(2)
        usermessage_expression = (MobileBy.XPATH,
                                  "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
        if index == 0:
            logging.info('===发送google表情===')
            self.driver.find_elements(*usermessage_expression)[index].click()
            google_expression_searchframe = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/et_search_id")
            google_expression_searchframe.send_keys("hah")
            google_expression_searchbut = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_search")
            google_expression_searchbut.click()
            time.sleep(0.5)
            google_expression_list = self.driver.find_elements(MobileBy.XPATH, "//android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
            time.sleep(1)
            google_expression_list[0].click()
        else:
            logging.info('===发送Chamet表情===')
            self.driver.find_elements(*usermessage_expression)[index].click()
            self.tap(350, 800)
        logging.info('===发送成功===')

        # 查看私聊界面自己发送表情(谷歌表情)
    def watch_selfsendgooglexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        try:
            head_frame = self.driver.find_element(MobileBy.XPATH, "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" % message_num)
        except NoSuchElementException as e:
            logging.info('===断言成功，为自己发的消息===')
            assert True
        else:
            logging.info('===断言失败，自己未发消息===')
            assert False
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.view.ViewGroup/android.widget.ImageView[1]" % message_num)
        return expression

        # 查看私聊界面对方发送表情(谷歌表情)
    def watch_othersendgoogleexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,
                                                 "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        head_frame = self.driver.find_element(MobileBy.XPATH,
                                              "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" % message_num)
        expression = self.driver.find_element(MobileBy.XPATH,
                                              "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.view.ViewGroup/android.widget.ImageView[1]" % message_num)
        return head_frame, expression


    # 查看私聊界面对方发送表情(Chamet表情)
    def watch_othersendexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" %message_num)
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.view.ViewGroup/android.widget.ImageView" %message_num)
        return head_frame,expression

    # 查看私聊界面自己发送表情(Chamet表情)
    def watch_selfsendexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        try:
            head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" %message_num)
        except NoSuchElementException as e:
            logging.info('===断言成功，为自己发的消息===')
            assert True
        else:
            logging.info('===断言失败，自己未发消息===')
            assert False
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.view.ViewGroup/android.widget.ImageView" %message_num)
        return expression









    '''留言-群聊-群聊消息元素有无'''
    def messages_Group_entryGroupNameEle(self):
        logging.info('===chamet团队未读数元素有无===')
        try:
            messages_Group_entryGroupName = self.driver.find_elements(*self.messages_Group_entryGroupName)
        except NoSuchElementException:
            logging.info('no messages_Group_entryGroupName')
            return False
        else:
            return messages_Group_entryGroupName


    '''留言-群聊-群聊更多按钮元素有无'''
    def messages_Group_detailMoreBtnEle(self):
        logging.info('===群聊更多按钮元素有无===')
        try:
            messages_Group_detailMoreBtn = self.driver.find_element(*self.messages_Group_detailMoreBtn)
        except NoSuchElementException:
            logging.info('no messages_Group_detailMoreBtn')
            return False
        else:
            return True

    def groupCount_number(self,time):
        time_filter = filter(str.isdigit, time)
        print(time_filter)  # <filter object at 0x0000019358731BE0>
        print(type(time_filter))  # <class 'filter'>
        time_list = list(time_filter)  # ['2', '0', '1', '9', '0', '9', '0', '4', '1', '1', '0', '0']
        time_str = "".join(time_list)  # 转为str    201909041100
        time_int = int(time_str)  # 转为int    201909041100
        return time_int

    '''留言-群聊-群聊上麦人头像元素有无'''
    def messages_Group_upMicUserHeadListEle(self):
        logging.info('===群聊上麦人头像元素有无===')
        try:
            messages_Group_upMicUserHeadList = self.driver.find_elements(*self.messages_Group_upMicUserHeadList)
        except NoSuchElementException:
            logging.info('no messages_Group_upMicUserHeadList')
            return False
        else:
            print(messages_Group_upMicUserHeadList)
            return messages_Group_upMicUserHeadList



    '''点击头像出现半屏浮层的送礼按钮有无'''
    def userHalfPagePopoverGiftSendBtnEle(self):
        logging.info('===群聊上麦人头像元素有无===')
        try:
            messages_Group_upMicUserHeadList = self.driver.find_elements(*self.messages_Group_userHalfPagePopoverGiftSendBtn)
        except NoSuchElementException:
            logging.info('no messages_Group_upMicUserHeadList')
            return False
        else:
            print(messages_Group_upMicUserHeadList)
            return messages_Group_upMicUserHeadList


    '''点击头像出现半屏浮层的昵称个人还是他人'''
    def userHalfPagePopoverNameOrOneselfEle(self):
        try:
            sendBtnEle=self.userHalfPagePopoverGiftSendBtnEle()
            if sendBtnEle!=False and len(sendBtnEle)!=0:
                userHalfPagePopoverName_username = self.driver.find_element(*self.messages_Group_userHalfPagePopoverName)
                return userHalfPagePopoverName_username.text
            else:
                OneSelfHalfPagePopoverName_username = self.driver.find_element(*self.messages_Group_OneSelfHalfPagePopoverName)
                return OneSelfHalfPagePopoverName_username.text

        except NoSuchElementException:
            logging.info('no myProfile_entry')
            return False




    '''留言-群聊-群聊个人半屏主页表情'''
    def messages_Group_userHalfPagePopoverImgListEle(self):
        logging.info('===群聊个人半屏主页表情元素有无===')
        try:
            self.driver.find_elements(*self.messages_Group_userHalfPagePopoverImgList)
        except NoSuchElementException:
            logging.info('no messages_Group_userHalfPagePopoverImgList')
            return False
        else:
            return True

    # 观众端群聊页面发送表情
    def audience_groupmessage_sendexpression(self, index):
        logging.info('===准备发送表情===')
        usermessage_expression_but = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_face_gif")
        usermessage_expression = (MobileBy.XPATH,
                                  "//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
        self.driver.find_element(*usermessage_expression_but).click()
        time.sleep(3)
        if index == 0:
            logging.info('===发送google表情===')
            self.driver.find_elements(*usermessage_expression)[index].click()
            google_expression_searchframe = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/et_search_id")
            google_expression_searchframe.send_keys("hah")
            google_expression_searchbut = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_search")
            google_expression_searchbut.click()
            time.sleep(0.5)
            google_expression_list = self.driver.find_elements(MobileBy.XPATH,
                                                               "//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")
            time.sleep(1)
            google_expression_list[0].click()
            # self.tap(350, 900)
            # self.tap(882,170)
            time.sleep(2)
            self.tap(137,1329)
        else:
            logging.info('===发送Chamet表情===')
            self.driver.find_elements(*usermessage_expression)[index].click()
            # self.tap(350, 900)
            # self.tap(882,170)
            time.sleep(2)
            self.tap(390,1329)
        logging.info('===发送成功===')

    # 查看群聊界面对方发送表情(Chamet表情)
    def watchgroup_othersendexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,
                                                 "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        head_frame = self.driver.find_element(MobileBy.XPATH,
                                              "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout" % message_num)
        expression = self.driver.find_element(MobileBy.XPATH,
                                              "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.ImageView[2]" % message_num)
        return head_frame, expression



    # 群聊界面发送表情
    def groupmessage_send_expression(self,index):
        logging.info('===准备发送表情===')
        groupmessage_expression_but = (By.ID, 'com.hkfuliao.chamet:id/iv_face_gif')
        groupmessage_expression = (MobileBy.XPATH,"//android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView")
        # self.driver.find_element(*groupmessage_expression_but).click()
        self.driver.find_element(By.ID, 'com.hkfuliao.chamet:id/iv_face_gif').click()
        time.sleep(3)
        if index == 0:
            logging.info('===发送google表情===')
            self.driver.find_elements(*groupmessage_expression)[index].click()
            google_expression_searchframe = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/et_search_id")
            google_expression_searchframe.send_keys("wow")
            google_expression_searchbut = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_search")
            google_expression_searchbut.click()
            time.sleep(1)
            # google_expression_list = self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")
            # time.sleep(0.5)
            # google_expression_list[0].click()
            self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")[0].click()
            time.sleep(1)
            # self.tap(330, 1100)
            self.tap(882,170)
        else:
            logging.info('===发送Chamet表情===')
            self.driver.find_elements(*groupmessage_expression)[index].click()
            time.sleep(1)
            self.tap(882,170)
            # self.tap(330, 1100)
        logging.info('===发送成功===')



    # 查看群聊界面自己发送表情(谷歌表情)
    def watchgroup_selfsendgooglexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        try:
            head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout" % message_num)
        except NoSuchElementException as e:
            logging.info('===断言成功，为自己发的消息===')
            assert True
        else:
            logging.info('===断言失败，自己未发消息===')
            assert False
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.ImageView[3]" % message_num)
        return expression

    # 查看群聊界面对方发送表情(谷歌表情)
    def watchgroup_othersendgoogleexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,
                                                 "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        user_name = self.driver.find_element(MobileBy.XPATH,
                                             "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout" % message_num)
        expression = self.driver.find_element(MobileBy.XPATH,
                                              "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.ImageView[3]" % message_num)
        return user_name, expression

    # 查看私聊界面自己发送表情(Chamet表情)
    def watchgroup_selfsendexpression(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        try:
            user_name = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout" %message_num)
        except NoSuchElementException as e:
            logging.info('===断言成功，为自己发的消息===')
            assert True
        else:
            logging.info('===断言失败，自己未发消息===')
            assert False
        expression = self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.ImageView[2]" %message_num )
        return expression


    # 群聊中发送相册图片
    def groupmessage_send_photo(self,num):
        logging.info('===发送照片===')
        photo_camera_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/iv_more_pic")
        photo_camera_but.click()
        photo_choicebut = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("从相册挑选")')
        photo_choicebut.click()
        logging.info('===发送相册照片===')
        try:
            # self.driver.find_elements(MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView")[num].click()
            # self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[%d]/android.widget.ImageView[2]" %num ).click()
            self.driver.find_elements(By.ID, 'com.hkfuliao.chamet:id/iv_select')[num].click()
            time.sleep(1)
            self.driver.find_element(By.ID, 'com.hkfuliao.chamet:id/btn_confirm').click()
            time.sleep(1)
            logging.info('===发送成功===')
            return True
        except:
            logging.info('===发送失败===')
            return False




    # 观众端群聊页面发送钻石包
    def audience_send_diamondenvelope(self, envelope_num, diamond_num):
        logging.info('===发送钻石包===')
        diamond_envelope_but = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_packet")
        diamond_envelope_but.click()
        member = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/tv_label_members").text
        packet_count = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/ed_packet_count")
        packet_total_energy = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/ed_packet_total_energy")
        send_but = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/btn_send_packet")
        packet_count.send_keys(envelope_num)
        packet_total_energy.send_keys(diamond_num)
        send_but.click()
        time.sleep(1)
        enrich_window = self.audience_enrich_window()
        if enrich_window:
            logging.info("===有优惠券===")
            self.system_goback_key()
        else:
            logging.info("===无优惠券===")

    # 观众端充值优惠卷
    def audience_enrich_window(self):
        logging.info("===判断有无充值优惠券===")
        try:
            enrich_window = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("去使用")')
            return True
        except:
            return False

    # 钻石红包获取
    def messageregion_getenvelope(self):
        time.sleep(1)
        envelope = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, 'text("幸运红包")')
        return envelope

    # 观众端群聊页面领取钻石包
    def audience_get_diamondenvelope(self):
        logging.info('===领取钻石包===')
        messageregion_getenvelope = self.messageregion_getenvelope()
        messageregion_getenvelope[-1].click()
        open_envelope = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_open_diamond_packet")
        open_envelope.click()

    # 领红包标识（用户头像）
    def getenvelope_userhead(self):
        user_head = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/civ_user_head")
        return user_head

    # 群聊页面领取钻石包
    def get_diamond_envelope(self):
        logging.info('===领取钻石包===')
        envelope = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, 'text("幸运红包")')
        envelope[-1].click()
        open_envelope = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/iv_open_diamond_packet")
        open_envelope.click()


    # 获取群聊文本消息
    def groupmessage_text(self,num):
        grouptext_message = self.driver.find_elements(MobileBy.ID,"com.hkfuliao.chamet:id/tv_content")
        return grouptext_message[num].text.encode("utf-8")

    # 观众端群聊页面打开送礼窗口
    def group_opengiftwin(self):
        logging.info('===打开礼物页面===')
        gift_but = self.driver.find_element(MobileBy.XPATH,
                                            "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[4]")
        gift_but.click()


    # 观众端群聊页面送礼
    def audience_groupmessage_sendgift(self, gift_tab, gift_name):
        logging.info('===送礼===')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("{}")'.format(gift_tab)).click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("么么哒")').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("{}")'.format(gift_name)).click()
        self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/item_group_count_text")[0].click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("1")').click()
        audience_sendgift_but = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/sendTv")
        audience_sendgift_but.click()
        if self.rechargewindow_bysendgift() and self.rechargewindow_able():
            if self.rechargewindow_recharge():
                self.driver.find_elements(MobileBy.XPATH,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")[1].click()
                self.audience_sendgift_bymessage("热门", "幸运之吻")
            else:
                logging.info('===设备无法充值，跳过下方送礼断言用例。===')
                return 0
        elif self.rechargewindow_bysendgift() and self.rechargewindow_able() == False:
            self.system_goback_key()
            logging.info('===余额不足，设备无法充值，跳过下方送礼断言用例。===')
            return 0
        else:
            # 是否夺宝弹窗
            lucky_window = self.audience_lucky_window()
            if lucky_window:
                finish = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("真棒！")')
                finish.click()
                self.system_goback_key()
            else:
                self.system_goback_key()
            return 1



    # 观众端送礼
    def audience_sendgift(self,gift_tab,gift_name):
        logging.info('===送礼===')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("{}")'.format(gift_tab)).click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("幸运锁")').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("{}")'.format(gift_name)).click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("1")').click()
        audience_sendgift_but = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/sendTv")
        audience_sendgift_but.click()
        if self.rechargewindow_bysendgift() and self.rechargewindow_able():
            self.rechargewindow_recharge()
            # self.audience_sendgift("简体中文chinese simplified","Moon sighting")
            self.audience_sendgift("热门", "幸运之吻")
        elif self.rechargewindow_bysendgift() and self.rechargewindow_able() == False:
            self.system_goback_key()
            logging.info('===余额不足，设备无法充值，跳过下方送礼断言用例。===')
            return 0
        else:
            lucky_window = self.audience_lucky_window()
            if lucky_window:
                finish = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("真棒！")')
                finish.click()
                self.system_goback_key()
            else:
                self.system_goback_key()
            return 1



    # 查看群聊界面自己发送礼物
    def watchgroup_selfsendgift(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        try:
            user_name = self.driver.find_element(MobileBy.XPATH,
                                                 "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout[1]/android.widget.TextView" % message_num)
        except NoSuchElementException as e:
            logging.info('===断言成功，为自己发的消息===')
            assert True
        else:
            logging.info('===断言失败，自己未发消息===')
            assert False
        gift_text = self.driver.find_element(MobileBy.XPATH,
                                             "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]" % message_num)
        return gift_text.text

    # 查看群聊界面对方发送礼物
    def watchgroup_othersendgift(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,
                                                 "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        user_name = self.driver.find_element(MobileBy.XPATH,
                                             "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout[1]/android.widget.TextView" % message_num)
        gift_text = self.driver.find_element(MobileBy.XPATH,
                                             "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.TextView[1]" % message_num)
        return user_name, gift_text.text




    # 留言-群聊信息-头像状态
    def messages_Group_MoreGroupHeadPic_picStatusEle(self):
        logging.info('===群聊信息-头像状态===')
        try:
            messages_Group_MoreGroupHeadPic_picStatusele = self.driver.find_element(*self.messages_Group_MoreGroupHeadPic_picStatus)
        except NoSuchElementException:
            logging.info('no messages_Group_MoreGroupHeadPic_picStatus')
            return False
        else:
            return True


    '''留言-群聊信息-头像点击-从相册选择ele'''
    def messages_Group_MoreGroupHeadPic_ChangeEle(self):
        logging.info('===群聊信息-头像点击-从相册选择ele===')
        try:
            messages_Group_MoreGroupHeadPic_Changeele = self.driver.find_element(*self.messages_Group_MoreGroupHeadPic_Change)
        except NoSuchElementException:
            logging.info('no messages_Group_MoreGroupHeadPic_Change')
            return False
        else:
            return True



    '''留言-群聊-群聊上麦点击知直到自己'''
    def userHalfPagePopoverImgListEle_onebyone(self):
        len_num = len(self.driver.find_elements(*MultiMan.messages_Group_upMicUserHeadList))
        for i in range(len_num):
            self.driver.find_elements(*MultiMan.messages_Group_upMicUserHeadList)[i].click()
            while self.messages_Group_userHalfPagePopoverImgListEle() == False:
                self.tap(946, 647)
            else:
                break

    '''留言-群聊-群聊发送钻石包'''
    def messages_Group_diamondsPacketSendAction(self,count,num):
        logging.info('===群聊上麦人头像元素有无===')
        try:
            messages_Group_diamondsPacketPopTitle = self.driver.find_elements(*self.messages_Group_diamondsPacketPopTitle)
        except NoSuchElementException:
            logging.info('no messages_Group_diamondsPacketPopTitle')
            return False
        else:
            self.driver.find_element(*self.messages_Group_diamondsPacketPopCount).send_keys(count)
            self.driver.find_element(*self.messages_Group_diamondsPacketPopTotalNum).send_keys(num)
            self.driver.find_element(*self.messages_Group_diamondsPacketPopSendBtn).click()
            return True

    '''留言-群聊-群聊钻石包状态-待打开'''
    def messages_Group_diamondsPacketStatusOpenEle(self):
        logging.info('===留言-群聊-群聊钻石包状态-待打开===')
        try:
            self.driver.find_elements(*self.messages_Group_diamondsPacketStatusOpen)
        except NoSuchElementException:
            logging.info('no messages_Group_diamondsPacketStatusOpen')
            return False
        else:
            return True

    '''留言-群聊-群聊钻石包状态-已开启'''
    def messages_Group_diamondsPacketStatusReceivedEle(self):
        logging.info('===留言-群聊-群聊钻石包状态-已开启===')
        try:
            self.driver.find_elements(*self.messages_Group_diamondsPacketStatusReceived)
        except NoSuchElementException:
            logging.info('no messages_Group_diamondsPacketStatusReceived')
            return False
        else:
            return True

    '''留言-群聊-群聊钻石包状态-已过期'''
    def messages_Group_diamondsPacketStatusExpiredEle(self):
        logging.info('===留言-群聊-群聊钻石包状态-已过期或被抢光===')
        try:
            self.driver.find_elements(*self.messages_Group_diamondsPacketStatusExpired)
        except NoSuchElementException:
            logging.info('no messages_Group_diamondsPacketStatusExpired')
            return False
        else:
            return True



    '''留言-群聊-礼物橱窗-tab礼物下列表礼物元素'''
    def messages_Group_GiftLayerTypeListEle(self):
        logging.info('===tab礼物下-具体礼物元素===')
        try:
            self.driver.find_elements(*self.messages_Group_GiftLayerTypeList)
        except NoSuchElementException:
            logging.info('no messages_Group_GiftLayerTypeList')
            return False
        else:
            return True


    '''留言-群聊-礼物橱窗-礼物组刷元素'''
    def messages_Group_GiftLayerGroupNumEle(self):
        logging.info('===tab礼物下-具体礼物元素===')
        try:
            GiftLayerGroupNum=self.driver.find_elements(*self.messages_Group_GiftLayerGroupNum)
        except NoSuchElementException:
            logging.info('no messages_Group_GiftLayerGroupNum')
            return False
        else:
            return GiftLayerGroupNum


    '''留言-群聊-礼物橱窗-礼物组刷元素第一个'''
    def messages_Group_GiftLayerGroupNumFirstEle(self):
        logging.info('===tab礼物下-具体礼物元素===')
        try:
            messages_Group_GiftLayerGroupNumFirst=self.driver.find_elements(*self.messages_Group_GiftLayerGroupNumFirst)
        except NoSuchElementException:
            logging.info('no messages_Group_GiftLayerGroupNumFirst')
            return False
        else:
            return messages_Group_GiftLayerGroupNumFirst




    '''留言-群聊-礼物橱窗-礼物夺宝弹窗'''
    def messages_Group_GiftTreasuresAwesomeBtnEle(self):
        logging.info('===tab礼物下-具体礼物元素===')
        try:
            messages_Group_GiftTreasuresAwesomeBtn=self.driver.find_element(*self.messages_Group_GiftTreasuresAwesomeBtn)
        except NoSuchElementException:
            logging.info('no messages_Group_GiftTreasuresAwesomeBtn')
            return False
        else:
            messages_Group_GiftTreasuresAwesomeBtn.click()
            return True


    '''留言-群聊-更多-动态整个元素'''
    def messages_Group_MoreMomentAllEle(self):
        logging.info('===动态整个元素===')
        try:
            messages_Group_MoreMomentAllELE=self.driver.find_elements(*self.messages_Group_MoreMomentAll)
        except NoSuchElementException:
            logging.info('no messages_Group_MoreMomentAll')
            return False
        else:
            return messages_Group_MoreMomentAllELE

    '''留言-群聊-更多-除最后一个元素'''
    def messages_Group_MoreMomentPicFrontEle(self):
        logging.info('===动态整个元素===')
        try:
            MoreMomentPicFront=self.driver.find_elements(*self.messages_Group_MoreMomentPicFront)
        except NoSuchElementException:
            logging.info('no messages_Group_MoreMomentPicFront')
            return False
        else:
            return MoreMomentPicFront


    # 留言_群聊_管理群组
    def messages_Group_MoreGroupManaEle(self):
        logging.info('===动态整个元素===')
        try:
            messages_Group_MoreGroupMana_ele = self.driver.find_element(*self.messages_Group_MoreGroupMana)
        except NoSuchElementException:
            logging.info('no messages_Group_MoreGroupMana_ele')
            return False
        else:
            return messages_Group_MoreGroupMana_ele



    # 留言_群聊_他人-个人半屏动态元素有无
    def messages_Group_userHalfPagePopoverMomentListEle(self):
        logging.info('===动态整个元素===')
        try:
            messages_Group_userHalfPagePopoverMomentList_ele = self.driver.find_element(*self.messages_Group_userHalfPagePopoverMomentList)
        except NoSuchElementException:
            logging.info('没有动态元素')
            return False
        else:
            logging.info('有动态元素')
            return True


    # 留言_群聊_他人-个人半屏动态元素有无
    def messages_Group_CallMoneyNotEnoughEle(self):
        logging.info('===动态整个元素===')
        try:
            self.driver.find_element(*self.messages_Group_CallMoneyNotEnough)
        except NoSuchElementException:
            logging.info('余额充足')
            return False
        else:
            logging.info('余额不足')
            return True


    '''留言-陌生人消息-入口图标元素有无'''
    def messages_Stranger_entryHeadPicEle(self):
        logging.info('===陌生人消息-入口图标元素===')
        try:
            Stranger_entryHeadPic1=self.driver.find_elements(*self.messages_Stranger_entryHeadPic)
        except NoSuchElementException:
            logging.info('no messages_Stranger_entryHeadPic')
            return False
        else:
            print(Stranger_entryHeadPic1)
            return Stranger_entryHeadPic1


    '''留言-陌生人消息-一对一更多元素有无'''
    def messages_Stranger_userMoreBtnEle(self):
        logging.info('===陌生人消息-一对一更多元素有无===')
        try:
            Stranger_userMoreBtn1=self.driver.find_elements(*self.messages_Stranger_userMoreBtn)
        except NoSuchElementException:
            logging.info('no messages_Stranger_userMoreBtn')
            return False
        else:
            print(Stranger_userMoreBtn1)
            return Stranger_userMoreBtn1


    '''留言-陌生人消息-一对一视频聊通话按钮元素有无'''
    def messages_Stranger_videoCallEnableEle(self):
        logging.info('===陌生人消息-一对一视频聊通话按钮元素有无===')
        try:
            self.driver.find_element(*self.messages_Stranger_videoCallEnable)
        except NoSuchElementException:
            logging.info('no messages_Stranger_videoCallEnable')
            return False
        else:
            return True

    '''留言-陌生人消息-一对一视频聊不可拨打提示弹窗元素有无'''
    def messages_Stranger_videoCallUnablePopAllEle(self):
        logging.info('===陌生人消息-一对一视频聊不可拨打提示弹窗元素有无===')
        try:
            self.driver.find_element(*self.messages_Stranger_videoCallUnablePopAll)
        except NoSuchElementException:
            logging.info('no messages_Stranger_videoCallUnablePopAll')
            return False
        else:
            return True


    # 用户无法接通
    def not_available_ele(self):
        try:
            not_availableele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("用户此时无法连接。请稍后拨打。")')
            logging.info('===用户不在线===')
            return True
        except:
            logging.info('===用户在线===')
            return False


        # 私聊页面拨打语音聊天
    def usermessage_Voice_chat(self):
        logging.info('===拨打视频聊天===')
        usermessage_drop_down_list = (MobileBy.XPATH,
                                      "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout")
        self.driver.find_elements(*usermessage_drop_down_list)[3].click()


        # 观众端私聊页面拨打语音聊天
    def usermessage_video_but(self):
        video_butele = (MobileBy.ANDROID_UIAUTOMATOR, 'text("语音聊天")')
        video_but = self.driver.find_element(*video_butele)
        logging.info('===拨打语言聊天===')
        video_but.click()
        self.not_available_win()

    # 拨打语音电话
    def not_available_win(self):
        not_available_ele = self.not_available_ele()
        if not_available_ele:
            single_btn = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/single_btn")
            single_btntext = single_btn.text
            assert single_btntext == "确认"
            logging.info('===断言成功，用户无法接通===')
            single_btn.click()
            time.sleep(1)
        else:
            time.sleep(6)
            get_usermessage_voicecontent1 = self.get_usermessage_voicecontent(-1)
            assert "用户没有回答" in get_usermessage_voicecontent1
            logging.info('===断言成功，成功拨打电话===')


    # 获取聊天区未接电话文本消息
    def get_usermessage_voicecontent(self,num):
        usermessage_region_voiceele = (MobileBy.XPATH,
                                   "//android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]")
        usermessage_region_voice = self.driver.find_elements(*usermessage_region_voiceele)
        return usermessage_region_voice[num].text

    '''留言-一对一列表-用户头像元素有无'''
    def messages_User_EntryHeadEle(self):
        logging.info('===一对一列表-用户头像元素有无===')
        try:
            OneUserEntryHead= self.driver.find_elements(*self.messages_User_EntryHead)
        except NoSuchElementException:
            logging.info('no messages_User_EntryHead')
            return False
        else:
            return OneUserEntryHead


    # 观众端送礼(私聊)
    def audience_sendgift_bymessage(self, gift_tab, gift_name):
        logging.info('===送礼===')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("{}")'.format(gift_tab)).click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("{}")'.format(gift_name)).click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("1")').click()
        self.driver.find_elements(MobileBy.ID,'com.hkfuliao.chamet:id/item_group_count_text')[0].click()
        audience_sendgift_but = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/sendTv")
        audience_sendgift_but.click()
        if self.rechargewindow_bysendgift() and self.rechargewindow_able():
            if self.rechargewindow_recharge():
                self.driver.find_elements(MobileBy.XPATH, "//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")[1].click()
                self.audience_sendgift_bymessage("热门", "棒棒糖")
            else:
                logging.info('===设备无法充值，跳过下方送礼断言用例。===')
                return 0
        elif self.rechargewindow_bysendgift() and self.rechargewindow_able() == False:
            self.system_goback_key()
            logging.info('===余额不足，设备无法充值，跳过下方送礼断言用例。===')
            return 0
        else:
            # 是否夺宝弹窗
            lucky_window = self.audience_lucky_window()
            if lucky_window:
                finish = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("真棒！")')
                finish.click()
                self.system_goback_key()
            else:
                self.system_goback_key()
            return 1

        # 查看私聊界面对方发送礼物
    def watch_othersendgift(self):
        message_list = self.driver.find_elements(MobileBy.XPATH,
                                                 "//android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        # message_list = self.driver.find_elements(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
        message_num = len(message_list)
        # head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout" %message_num)
        # head_frame = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout/android.view.ViewGroup" %message_num)
        head_frame = self.driver.find_element(MobileBy.XPATH,
                                              "//android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]" % message_num)
        # gift_content = self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout[1]/android.widget.TextView" %message_num).text
        gift_content = self.driver.find_element(MobileBy.XPATH,
                                                "//android.widget.RelativeLayout/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.LinearLayout[1]/android.widget.TextView" % message_num).text
        return head_frame, gift_content



    # 观众端夺宝礼物弹窗
    def audience_lucky_window(self):
        logging.info('===判断有无夺宝弹窗===')
        try:
            lucky_window = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/ll_lucky_content")
            logging.info('===获得夺宝弹窗===')
            return True
        except:
            logging.info('===无夺宝弹窗===')
            return False


    # 观众端设备进行充值
    def rechargewindow_recharge(self):
        logging.info('===充值===')
        try:
            logging.info('===进行充值===')
            recharge_level = self.driver.find_elements(MobileBy.ID,"com.hkfuliao.chamet:id/root_view")
            recharge_level[0].click()
            time.sleep(2)
            buy_but = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("一键购买")')
            buy_but.click()
            # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("不用了")').click()
            time.sleep(3)
            buy_success_page = self.audience_buysuccess_page()
            assert len(buy_success_page)!=0
            logging.info('===充值成功===')
            self.system_goback_key()
            self.system_goback_key()
            return True
        except:
            logging.info('===充值失败===')
            self.system_goback_key()
            # self.system_goback_key()
            return False

    # 获取钻石弹窗
    def audience_buysuccess_page(self):
        # buy_success_page = (MobileBy.ID, "com.hkfuliao.chamet:id/dialog_msg")
        buy_success_page = (MobileBy.ID, "com.hkfuliao.chamet:id/iv_card_icon")
        return self.driver.find_elements(*buy_success_page)




        # 观众端判断设备是否可进行google充值
    def rechargewindow_able(self):
        logging.info('===判断设备是否可进行google充值===')
        try:
            self.driver.find_elements(MobileBy.ID, "com.hkfuliao.chamet:id/tv_recharge_tab_title")[0]
            rechargewindow = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/root_view")
            # rechargewindow = self.driver.find_element(MobileBy.ID, "com.hkfuliao.chamet:id/recycler_top_up_list")
            logging.info('===设备可进行google充值===')
            return True
        except:
            logging.info('===设备不可进行google充值===')
            return False

    # 观众端判断送礼时是否余额不足
    def rechargewindow_bysendgift(self):
        logging.info('===判断是否余额不足，有无充值弹窗===')
        try:
            rechargewindow = self.driver.find_element(MobileBy.ID,"com.hkfuliao.chamet:id/tv_my_diamonds")
            logging.info('===送礼失败，余额不足，有充值弹窗。===')
            return True
        except:
            logging.info('===送礼成功，无充值弹窗。===')
            return False



    '''留言-一对一列表-用户昵称元素有无'''
    def messages_User_EntryUserNameEle(self):
        logging.info('===一对一列表-用户昵称元素有无===')
        try:
            OneUserEntryUserName= self.driver.find_elements(*self.messages_User_EntryUserName)
        except NoSuchElementException:
            logging.info('no messages_User_EntryUserName')
            return False
        else:
            messages_Stranger_entryHeadPicEle11=self.messages_Stranger_entryHeadPicEle()
            if messages_Stranger_entryHeadPicEle11!=False and len(messages_Stranger_entryHeadPicEle11)!=0:
                logging.info('有陌生人')
                for i, y in enumerate(OneUserEntryUserName):
                    if y.text=='陌生人留言':
                        pass
                    else:
                        print(y)
                        return y
                return y[0]

                # if len(OneUserEntryUserName)==2:
                #     for i,y in enumerate(OneUserEntryUserName):
                #         if y.text=='陌生人留言':
                #             pass
                #         else:
                #             print(y)
                #             return y
                # elif len(OneUserEntryUserName)>2:
                    # for i,y in enumerate(OneUserEntryUserName):
                    #     while y.text!='陌生人留言':
                    #         print(y)
                    #         return y
            elif messages_Stranger_entryHeadPicEle11==False or len(messages_Stranger_entryHeadPicEle11)==0:
                logging.info('没有陌生人')
                return OneUserEntryUserName[0]
                # if len(OneUserEntryUserName)==1:
                #     for i,y in enumerate(OneUserEntryUserName):
                #         print(y)
                #         return y
                # elif len(OneUserEntryUserName)>1:
                #     print(OneUserEntryUserName[0])
                #     return OneUserEntryUserName[0]



    '''留言-一对一-更多按钮元素有无'''
    def messages_User_MoreBtnEle(self):
        logging.info('===一对一列表-更多按钮元素有无===')
        try:
            self.driver.find_element(*self.messages_User_MoreBtn)
        except NoSuchElementException:
            logging.info('no messages_User_MoreBtn')
            return False
        else:
            return True



    '''留言-一对一-第三排未读数元素元素有无'''
    def messages_User_userContentUnreadDotEle(self):
        logging.info('===一对一列表-第三排未读数元素元素有无===')
        try:
            self.driver.find_element(*self.messages_User_userContentUnreadDot)
        except NoSuchElementException:
            logging.info('no messages_User_userContentUnreadDot')
            return False
        else:
            return True


    # '''留言-群聊-群聊发送语音消息'''
    # def message_group_sendVoice(self):
    #     logging.info('===准备发送语音===')
    #     message_group_sendVoiceBtn = self.driver.find_element(*self.messages_Group_voiceBtn)
    #     message_group_sendVoiceBtn.click()
    #     message_group_sendVoicePress = self.driver.find_element(*self.messages_Group_voiceAddBtn)
    #     # 长按录入语音
    #     self.click_hold(message_group_sendVoicePress)

    # '''留言-群聊-群聊更多按钮元素有无'''
    # def message_group_sendPhoto(self, num):
    #     logging.info('===发送照片===')
    #     photo_camera_but = self.driver.find_element(*self.)
    #     photo_camera_but.click()
    #     photo_choicebut = self.driver.find_element(*self.)
    #     photo_choicebut.click()
    #     logging.info('===发送相册照片===')
    #     try:
    #         self.driver.find_elements(*self.)[num].click()
    #         time.sleep(1)
    #         return True
    #     except:
    #         return False





    # '''========我的等级====='''

    '''点击我的页面—我的等级'''
    def vip_Level_right_click(self):
        logging.info('===开始点击我的等级===')
        try:
            my_vipLevel_entryRightClick22 = self.driver.find_element(*self.my_vipLevel_entryRightClick)
        except NoSuchElementException:
            logging.info('no my_vipLevel_entryRightClick')
        else:
            my_vipLevel_entryRightClick22.click()
            logging.info('已经点击')
            # print(self.driver.contexts)
            # context = self.driver.contexts
            # self.driver.switch_to.context(context[-1])
            #进入h5界面后，获取上下文，并切换至h5
            # Common.native_to_h5(self)
            time.sleep(3)
            logging.info('已经进入')


    '''查找等级外部显示男用户lvx-lvx+1'''
    def my_vipLevel_UpLevelImgManAllEle(self):
        logging.info('===查找等级外部显示lvx===')
        try:
            my_vipLevel_UpLevelImgManAll = self.driver.find_element(*self.my_vipLevel_UpLevelImgManAll)
        except NoSuchElementException:
            logging.info('no my_vipLevel_UpLevelImgManAll')
            return False
        else:
            return True

    # 我的余额中提取钻石数值
    # 28,216[diamond]提取成28216
    def string_find_num(self,string1):
        result = re.findall("\d+", string1)
        print(result)
        num = ''.join(result)
        print(num)
        return num



    '''先判断男女，再看男女的等级外部显示具体等级'''
    def myVipLevel_level_value(self):
        logging.info('===开始查看用户我的等级值===')
        ImgManAllEle=self.my_vipLevel_UpLevelImgManAllEle()
        if self.myProfile_Gender_ManorW()==1:
            logging.info('===该用户为男生===')
            if ImgManAllEle==False:
                logging.info('===等级为lv0===')
                try:
                    my_vipLevel_NowLevelImgZeroAndWoman = self.driver.find_element(*self.my_vipLevel_NowLevelImgZeroAndWoman)
                except NoSuchElementException:
                    logging.info('no my_vipLevel_NowLevelImgZeroAndWoman')
                    return False
                else:
                    print(my_vipLevel_NowLevelImgZeroAndWoman.text)
                    return my_vipLevel_NowLevelImgZeroAndWoman.text
            else:
                logging.info('===等级不是lv0===')
                try:
                    my_vipLevel_UpLevelImgManLevel = self.driver.find_element(*self.my_vipLevel_UpLevelImgManLevel)
                except NoSuchElementException:
                    logging.info('no my_vipLevel_UpLevelImgManLevel')
                    return False
                else:
                    print(my_vipLevel_UpLevelImgManLevel.text)
                    return my_vipLevel_UpLevelImgManLevel.text

        elif self.myProfile_Gender_ManorW()==2:
            logging.info('===该用户为女生===')
            try:
                my_vipLevel_NowLevelImgZeroAndWoman = self.driver.find_element(*self.my_vipLevel_NowLevelImgZeroAndWoman)
            except NoSuchElementException:
                logging.info('no my_vipLevel_NowLevelImgZeroAndWoman')
                return False
            else:
                print(my_vipLevel_NowLevelImgZeroAndWoman.text)
                return my_vipLevel_NowLevelImgZeroAndWoman.text

        else:
            logging.error('该用户性别未知，或者外部内部元素没获取到')
            print(None)
            return None

    '''我的等级内部顶部值需要拼接Lv'''
    def vipLevel_level_value(self):
        logging.info('开始拼接')
        try:
            ll = self.driver.find_element(*self.level_specificNumberCss).text
        except NoSuchElementException:
            logging.info('no level_title')
            return False
        else:
            print(ll)
            level='Lv''{}'.format(ll)
            print(level)
            return level

    '''我的等级内部下面左边等级值需要拼接Lv'''
    def vipLevel_levelLeft_value(self):
        try:
            ll = self.driver.find_element(*self.level_specificNumberleftCss).text
        except NoSuchElementException:
            logging.info('no level_specificNumberleft')
            return False
        else:
            level='Lv''{}'.format(ll)
            return level

    '''我的等级内部立即充值按钮'''
    def vipLevel_level_topUpBtn(self):
        try:
            level_TopUp_Btn = self.driver.find_elements(*self.level_TopUp_btn)

        except NoSuchElementException:
            logging.info('no level_TopUp_btn')
            return False
        else:
            return level_TopUp_Btn

    '''我的等级页面点击返回键——切换回我的页面'''
    def vip_Level_mylevel_goback(self):
        try:
            ll = self.driver.find_elements(*self.level_gobackCss)
        except NoSuchElementException:
            logging.info('no level_title')
        else:
            # print(ll)
            ll[0].click()
            # 返回至原生界面后，切换至原生界面
            Common.h5_to_native(self)
            logging.info('click vip_level_level_goback already')



    # '''========我的任务====='''
    # '''我的页面-我的任务积分显示具体积分值'''
    # def my_Tasks_entryText(self):
    #     try:
    #         MyTasks_entry_points = self.driver.find_element(*self.MyTasks_entry_points)
    #
    #     except NoSuchElementException:
    #         logging.info('no MyTasks_entry_points')
    #         print(False)
    #         return False
    #     else:
    #         print(MyTasks_entry_points.text)
    #         logging.info('没有新奖励、显示积分')
    #         return MyTasks_entry_points.text
    #
    # '''我的页面-我的任务文字显示'''
    # def my_Tasks_entryTwoText(self):
    #     my_Tasks_entryPoint = self.my_Tasks_entryText()
    #     if my_Tasks_entryPoint != False:
    #         return my_Tasks_entryPoint
    #     else:
    #         try:
    #             MyTasks_entry_rewards = self.driver.find_element(*self.MyTasks_entry_rewards)
    #         except NoSuchElementException:
    #             logging.info('no MyTasks_entry_rewards')
    #             print(False)
    #             return False
    #         else:
    #             print(MyTasks_entry_rewards.text)
    #             return MyTasks_entry_rewards.text

    '''我的页面-我的任务文字显示'''
    def my_Tasks_entryTwoText(self):
        try:
            MyTasks_entry_points = self.driver.find_element(*self.MyTasks_entry_points)
        except NoSuchElementException:
            logging.info('没有显示积分，显示新奖励')
            MyTasks_entry_rewards = self.driver.find_element(*self.MyTasks_entry_rewards)
            return MyTasks_entry_rewards.text
        else:
            logging.info('显示积分')
            return MyTasks_entry_points.text





    '''我的页面-我的任务男用户-通行证历史'''
    def my_Tasks_pointsMonthlyHistory(self):
        try:
            MyTasks_tab_pointsMonthlyHistory = self.driver.find_element(*self.MyTasks_tab_pointsMonthlyHistory)

        except NoSuchElementException:
            logging.info('no MyTasks_tab_pointsMonthlyHistory')
            return False
        else:
            return MyTasks_tab_pointsMonthlyHistory

    '''我的页面-我的任务男用户-任务完成领取弹窗按钮元素'''
    def MyTasks_task_completedPopoverOkBtnEle(self):
        try:
            MyTasks_task_completedPopoverOkBtn = self.driver.find_element(*self.MyTasks_task_completedPopoverOkBtn)

        except NoSuchElementException:
            logging.info('no MyTasks_task_completedPopoverOkBtn')
            return False
        else:
            return MyTasks_task_completedPopoverOkBtn




    '''我的页面-我的任务男用户-签到入口'''
    def my_Tasks_ManSignInSuccess(self):
        try:
            MyTasks_tasks_signinSuccessID = self.driver.find_element(*self.MyTasks_tasks_signinSuccessID)

        except NoSuchElementException:
            logging.info('no MyTasks_tasks_signinSuccessID')
            return False
        else:
            return True

    '''我的页面-我的任务男用户-邀请入口文字元素'''
    def MyTasks_tasks_inviteEntryTextEle(self):
        try:
            MyTasks_tasks_inviteEntryText = self.driver.find_element(*self.MyTasks_tasks_inviteEntryText)

        except NoSuchElementException:
            logging.info('no MyTasks_tasks_inviteEntryText')
            return False
        else:
            return True

    '''我的页面-我的任务男用户-免费top offers口文字元素'''
    def MyTasks_tasks_TopOffersEntryTextEle(self):
        try:
            MyTasks_tasks_TopOffersEntryText = self.driver.find_element(*self.MyTasks_tasks_TopOffersEntryText)

        except NoSuchElementException:
            logging.info('no MyTasks_tasks_TopOffersEntryText')
            return False
        else:
            return True


    '''我的页面-我的任务男用户-每日任务'''
    def my_Tasks_ManDailyTasksAll(self):
        try:
            MyTasks_tasks_DailyTasksAll = self.driver.find_element(*self.MyTasks_tasks_DailyTasksAll)

        except NoSuchElementException:
            logging.info('no MyTasks_tasks_DailyTasksAll')
            return False
        else:
            return True

    '''我的页面-我的任务男用户-每月任务'''
    def my_Tasks_ManMonthlyTasksAll(self):
        try:
            MyTasks_tasks_MonthlyTasksAll = self.driver.find_element(*self.MyTasks_tasks_MonthlyTasksAll)

        except NoSuchElementException:
            logging.info('no MyTasks_tasks_MonthlyTasksAll')
            return False
        else:
            return True

    '''我的页面-我的任务男用户-奖励页充值月卡'''
    def myTasks_rewards_TopUpMonthCard(self):
        try:
            MyTasks_rewards_TopUpMonthCard = self.driver.find_element(*self.MyTasks_rewards_TopUpMonthCard)

        except NoSuchElementException:
            logging.info('no MyTasks_rewards_TopUpMonthCard')
            return False
        else:
            return True

    '''我的页面-我的任务男用户-奖励真棒弹窗按钮元素'''
    def MyTasks_rewards_CongratsPopoverAwesomeBtnEle(self):
        try:
            MyTasks_rewards_CongratsPopoverAwesomeBtn1 = self.driver.find_element(*self.MyTasks_rewards_CongratsPopoverAwesomeBtn)

        except NoSuchElementException:
            logging.info('no MyTasks_rewards_CongratsPopoverAwesomeBtn')
            return False
        else:
            return MyTasks_rewards_CongratsPopoverAwesomeBtn1.click()

    '''我的页面-我的任务男用户-奖励细节弹窗按钮元素-完成任务获得更多奖励'''
    def MyTasks_rewards_RewardDetailsPopoverOkBtnEle(self):
        try:
            MyTasks_rewards_RewardDetailsPopoverOkBtn1 = self.driver.find_element(*self.MyTasks_rewards_RewardDetailsPopoverOkBtn)

        except NoSuchElementException:
            logging.info('no MyTasks_rewards_RewardDetailsPopoverOkBtn')
            return False
        else:
            return MyTasks_rewards_RewardDetailsPopoverOkBtn1


    '''我的页面-我的任务男用户-已完成已领取奖励'''
    def MyTasks_rewards_RewardClaimedIconEle(self):
        try:
            MyTasks_rewards_RewardClaimedIcon = self.driver.find_elements(*self.MyTasks_rewards_RewardClaimedIcon)

        except NoSuchElementException:
            logging.info('no MyTasks_rewards_RewardClaimedIcon')
            return False
        else:
            print(MyTasks_rewards_RewardClaimedIcon)
            return MyTasks_rewards_RewardClaimedIcon

    '''点击我的页面—我的任务-引导手势元素有无'''
    def MyTasks_rewards_LeftClickGuideIDEle(self):
        logging.info('===左侧引导手势元素有无===')
        try:
            MyTasks_rewards_LeftClickGuideID = self.driver.find_elements(*self.MyTasks_rewards_LeftClickGuideID)
        except NoSuchElementException:
            logging.info('no MyTasks_rewards_LeftClickGuideID')
            return False
        else:
            return MyTasks_rewards_LeftClickGuideID

    '''点击我的页面—我的任务-引导手势元素有无'''
    def MyTasks_rewards_RightClickGuideIDEle(self):
        logging.info('===右侧引导手势元素有无===')
        try:
            MyTasks_rewards_RightClickGuideID = self.driver.find_elements(*self.MyTasks_rewards_RightClickGuideID)
        except NoSuchElementException:
            logging.info('no MyTasks_rewards_RightClickGuideID')
            return False
        else:
            return MyTasks_rewards_RightClickGuideID


    '''点击我的页面—我的任务-积分元素有无'''
    def MyTasks_tab_pointsNumberEle(self):
        logging.info('===积分元素有无===')
        self.l.swipe(40, 387, 40, 1473, 100)
        try:
            MyTasks_tab_pointsNumber = self.driver.find_elements(*self.MyTasks_tab_pointsNumber)
        except NoSuchElementException:
            logging.info('no MyTasks_tab_pointsNumberEle')
            return False
        else:
            return MyTasks_tab_pointsNumber.text


    '''点击我的页面—我的任务-引导第一个100积分的已领取元素有无'''
    def MyTasks_rewards_first100Claimed_StatusEle(self):
        logging.info('===引导第一个100积分的已领取元素有无===')
        self.swipe(40, 387, 40, 1473, 100)
        try:
            MyTasks_rewards_first100Claimed_Status = self.driver.find_elements(*self.MyTasks_rewards_manFirst100Claimed_Status)
        except NoSuchElementException:
            logging.info('no MyTasks_rewards_first100Claimed_Status')
            return False
        else:
            return MyTasks_rewards_first100Claimed_Status


    '''点击我的页面—我的任务-女生签到第二天元素有无'''
    def MyTasks_womanTasks_LoginTomorrowAllEle(self):
        logging.info('===女生签到第二天元素===')
        try:
            MyTasks_womanTasks_LoginTomorrowAll = self.driver.find_elements(*self.MyTasks_womanTasks_LoginTomorrowAll)
        except NoSuchElementException:
            logging.info('no MyTasks_womanTasks_LoginTomorrowAll')
            return False
        else:
            return True

    '''点击我的页面—我的任务-女生待领取奖励元素有无'''
    def MyTasks_womanRewards_RewardsStatusClaimEle(self):
        logging.info('===女生待领取奖励元素有无===')
        try:
            MyTasks_womanRewards_RewardsStatusClaim = self.driver.find_elements(*self.MyTasks_womanRewards_RewardsStatusClaim)
        except NoSuchElementException:
            logging.info('no MyTasks_womanRewards_RewardsStatusClaim')
            return False
        else:
            return MyTasks_womanRewards_RewardsStatusClaim

    '''点击我的页面—我的任务-女生已领取奖励元素有无'''
    def MyTasks_womanRewards_RewardsStatusClaimedEle(self):
        logging.info('===女生已领取奖励元素有无===')
        try:
            MyTasks_womanRewards_RewardsStatusClaimed = self.driver.find_elements(*self.MyTasks_womanRewards_RewardsStatusClaimed)
        except NoSuchElementException:
            logging.info('no MyTasks_womanRewards_RewardsStatusClaimed')
            return False
        else:
            return MyTasks_womanRewards_RewardsStatusClaimed

    '''点击我的页面—我的任务-女生待解锁奖励元素有无'''
    def MyTasks_womanRewards_RewardsStatusLockedEle(self):
        logging.info('===女生待解锁奖励元素有无===')
        try:
            MyTasks_womanRewards_RewardsStatusLocked = self.driver.find_elements(*self.MyTasks_womanRewards_RewardsStatusLocked)
        except NoSuchElementException:
            logging.info('no MyTasks_womanRewards_RewardsStatusLocked')
            return False
        else:
            return True






    # '''========我的背包====='''

    '''点击我的页面—我的背包显示数量'''
    def myBackpack_all_ClItemNum(self):
        logging.info('===开始点击我的背包入口===')
        try:
            myBackpack_all_headFrameClItem = self.driver.find_elements(*self.myBackpack_all_headFrameClItem)
        except NoSuchElementException:
            logging.info('no myBackpack_all_headFrameClItem')
            return False
        else:
            return len(myBackpack_all_headFrameClItem)

    '''点击我的页面—我的背包-frame的元素有无'''
    def myBackpack_now_frameIDEle(self):
        logging.info('===frame的元素有无===')
        try:
            myBackpack_now_frameID = self.driver.find_elements(*self.myBackpack_now_frameID)
        except NoSuchElementException:
            logging.info('no myBackpack_now_frameID')
            return False
        else:
            return True

    '''点击我的页面—我的背包-frameSvg的元素有无'''
    def myBackpack_now_frameSvgIDEle(self):
        logging.info('===frameSvg的元素有无===')
        try:
            myBackpack_now_frameSvgID = self.driver.find_elements(*self.myBackpack_now_frameSvgID)
        except NoSuchElementException:
            logging.info('no myBackpack_now_frameSvgID')
            return False
        else:
            return True














    # '''========我的邀请====='''

    '''点击我的页面—我的邀请入口'''
    def MyInvite_entry_AllEle(self):
        logging.info('===开始点击我的邀请入口===')
        try:
            MyInvite_entry_All = self.driver.find_element(*self.MyInvite_entry_All)
        except NoSuchElementException:
            logging.info('no MyInvite_entry_All')
        else:
            MyInvite_entry_All.click()
            # time.sleep(2)
            #进入h5界面后，获取上下文，并切换至h5
            # Common.native_to_h5(self)



    '''我的页面-我的邀请总奖励图标'''
    def MyInvite_my_TotalRewardsBtnEle(self):
        logging.info('===我的邀请总奖励图标有无===')
        try:
            MyInvite_my_TotalRewardsBtn1 = self.driver.find_element(*self.MyInvite_my_TotalRewardsBtn)

        except NoSuchElementException:
            logging.info('no MyInvite_my_TotalRewardsBtn1')
            return False
        else:
            print(MyInvite_my_TotalRewardsBtn1)
            print(MyInvite_my_TotalRewardsBtn1.text)
            return MyInvite_my_TotalRewardsBtn1.text

    '''我的页面-我的邀请无记录图标'''
    def MyInvite_my_inviteesListNoUserEle(self):
        logging.info('===我的邀请无记录图标有无===')
        try:
            MyInvite_my_inviteesListNoUser1 = self.driver.find_elements(*self.MyInvite_my_inviteesListNoUser)

        except NoSuchElementException:
            logging.info('no MyInvite_my_inviteesListNoUser')
            return False
        else:
            print(MyInvite_my_inviteesListNoUser1)
            return MyInvite_my_inviteesListNoUser1

    '''我的页面-周排行无记录图标'''
    def MyInvite_weekly_noUserEle(self):
        logging.info('===周排行无记录图标有无===')
        try:
            MyInvite_weekly_noUser = self.driver.find_element(*self.MyInvite_weekly_noUser)

        except NoSuchElementException:
            logging.info('no MyInvite_weekly_noUser')
            return False
        else:
            return True


    '''我的邀请页面点击返回键——切换回我的页面'''
    def MyInvite_gobackEle(self):
        try:
            ll = self.driver.find_elements(*self.MyInvite_goback)
        except NoSuchElementException:
            logging.info('no MyInvite_goback')
        else:
            ll[0].click()
            # 返回至原生界面后，切换至原生界面
            Common.h5_to_native(self)


    # '''========我的背包====='''

    '''点击我的页面—我的背包-过期道具'''
    def myBackpack_expired_noTextEle(self):
        logging.info('===开始点击我的邀请入口===')
        try:
            myBackpack_expired_noText = self.driver.find_element(*self.myBackpack_expired_noText)
        except NoSuchElementException:
            logging.info('no myBackpack_expired_noText')
            return False
        else:
            return True






    # '''========我的简介====='''
    '''我的页面-我的简介点击右键进入'''
    def my_Profile_entry(self):
        try:
            myProfile_entry_man = self.driver.find_element(*self.myProfile_entry_man)
            myProfile_entry_woman = self.driver.find_element(*self.myProfile_entry_woman)
            if myProfile_entry_man.text=='我的简介':
                myProfile_entry_man.click()
                return True
            elif myProfile_entry_woman.text=='我的简介':
                myProfile_entry_woman.click()
                return True

        except NoSuchElementException:
            logging.info('no myProfile_entry')
            return False



    '''我的页面-我的简介点击右键进入'''

    def myProfile_MyAvatar_PosterHistoryBtn_Ele(self):
        try:
            logging.info('开始查找历史图集入口')
            myProfile_MyAvatar_PosterHistoryBtn_ele11 = self.driver.find_element(*self.myProfile_MyAvatar_PosterHistoryBtn)
        except NoSuchElementException:
            logging.info('no myProfile_MyAvatar_PosterHistoryBtn_ele')
            return False
        else:
            return myProfile_MyAvatar_PosterHistoryBtn_ele11


    '''我的页面-我的简介——性别分男女'''
    def myProfile_Gender_ManorW(self):
        if self.my_Profile_entry():
            try:
                myProfile_Gender_sex = self.driver.find_element(*self.myProfile_GenderTextWoman)

            except NoSuchElementException:
                logging.info('no myProfile_Gender')
                self.system_goback_key()
                return False
            else:
                print(myProfile_Gender_sex.text)
                if myProfile_Gender_sex.text=='男':
                    self.system_goback_key()
                    return 1
                elif myProfile_Gender_sex.text == '性别':
                    # 女实际代码中打印出来是性别
                    self.system_goback_key()
                    return 2
                elif myProfile_Gender_sex.text == '女':
                    # 女实际代码中打印出来是性别
                    self.system_goback_key()
                    return 2
                else:
                    self.system_goback_key()
                    return False
        else:
            logging.info('no myProfile ')
            return False


    '''我的页面-我的简介-头像历史按钮元素'''
    def myProfile_MyAvatar_PosterHistoryBtnEle(self):
        logging.info('头像历史按钮元素查找')
        try:
           self.driver.find_element(*self.myProfile_MyAvatar_PosterHistoryBtn)

        except NoSuchElementException:
            logging.info('no myProfile_MyAvatar_PosterHistoryBtn')
            return False
        else:
            return True

    '''我的页面-我的简介-昵称确认按钮元素'''
    def myProfile_NickName_EditorCommitBtnEle(self):
        logging.info('昵称确认按钮元素')
        try:
           myProfile_NickName_EditorCommit1=self.driver.find_element(*self.myProfile_NickName_EditorCommit)

        except NoSuchElementException:
            logging.info('no myProfile_MyAvatar_PosterHistoryBtn')
            return False
        else:
            myProfile_NickName_EditorCommit1.click()
            logging.info('昵称确认按钮元素已点击')




    '''我的页面-我的简介定位内容上是否有内容'''
    def myProfile_Location_TextContents(self):
        try:
            myProfile_Location_Text3 = self.driver.find_element(*self.myProfile_Location_Text)

        except NoSuchElementException:
            logging.info('no myProfile_Location_Text3')
            return False
        else:
            print(myProfile_Location_Text3.text)
            return myProfile_Location_Text3


    '''我的页面-我的简介——第二语言显示text有无'''
    def myProfile_SecondLanguage_textContents(self):
        try:
            myProfile_SecondLanguage_Text1 = self.driver.find_element(*self.myProfile_SecondLanguage_Text)

        except NoSuchElementException:
            logging.info('no myProfile_SecondLanguage_Text')
            return False
        else:
            print(myProfile_SecondLanguage_Text1)
            return myProfile_SecondLanguage_Text1




    '''我的简介——女用户头像更改审核弹窗'''
    def myProfile_MyAvatar_ChangePosterFailed_Btn(self):
        try:
            myProfile_MyAvatar_ChangePosterFailedBtn11 = self.driver.find_element(*self.myProfile_MyAvatar_PosterStateText)
            # myProfile_MyAvatar_ChangePosterFailedBtn11 = self.driver.find_element(*self.myProfile_MyAvatar_ChangePosterFailedBtn)

        except NoSuchElementException:
            logging.info('没有——我的简介——女用户头像更改审核弹窗')
            self.driver.find_element(*self.myProfile_MyAvatar_ChangePosterFailedBtn).click()
            self.tap(952, 2200)
            return False
        else:
            logging.info('我的简介——女用户头像更改审核弹窗已点击')
            return True


    '''我的简介——女用户头像更改审核弹窗'''
    def myProfile_MyAvatar_ChangePosterFailed_Pop(self):
        try:
            myProfile_MyAvatar_ChangePosterFailedBtn11 = self.driver.find_element(*self.myProfile_MyAvatar_ChangePosterFailedBtn)

        except NoSuchElementException:
            logging.info('没有——我的简介——女用户头像更改审核弹窗')
            return False
        else:
            myProfile_MyAvatar_ChangePosterFailedBtn11.click()
            self.tap(545, 120)
            logging.info('我的简介——女用户头像更改审核弹窗已点击')
            return True




    '''我的页面-我的简介——重置密码重置字样显示'''
    def myProfile_Password_entryTextEle(self):
        try:
            myProfile_Password_entryText = self.driver.find_element(*self.myProfile_Password_entryText)

        except NoSuchElementException:
            logging.info('no myProfile_Password_entryText')
            return False
        else:
            return True



    # '''========我的打招呼====='''
    '''我的页面-我的打招呼-真人检测元素'''
    def MyGrWords_faceVerification_popoverAllEle(self):
        try:
            MyGrWords_faceVerification_popoverAll = self.driver.find_element(*self.MyGrWords_faceVerification_popoverAll)

        except NoSuchElementException:
            logging.info('no MyGrWords_faceVerification_popoverAll')
            return False
        else:
            return True

    '''我的页面-我的打招呼-编辑你的打招呼消息页面元素'''
    def MyGrWords_edit_saveBtnEle(self):
        try:
            MyGrWords_edit_saveBtn = self.driver.find_element(*self.MyGrWords_edit_saveBtn)

        except NoSuchElementException:
            logging.info('no MyGrWords_edit_saveBtn')
            return False
        else:
            return True

    '''我的页面-我的打招呼-打招呼消息列表页面元素'''
    def MyGrWords_sendAllBtnEle(self):
        try:
            MyGrWords_sendAllBtn = self.driver.find_element(*self.MyGrWords_sendAllBtn)
        except NoSuchElementException:
            logging.info('no MyGrWords_sendAllBtn')
            return False
        else:
            return True


    '''我的页面-我的打招呼-打招呼消息列表页面元素'''
    def MyGrWords_sendAllBtn_3levelPopConEle(self):
        try:
            MyGrWords_sendAllBtn_3levelPopConEle = self.driver.find_element(*self.MyGrWords_sendAllBtn_3levelPopCon)
        except NoSuchElementException:
            logging.info('no MyGrWords_sendAllBtn_3levelPopCon')
            return False
        else:
            assert MyGrWords_sendAllBtn_3levelPopConEle.text=='暂时不能群发消息，因为你的等级低于Lv3。'
            self.driver.find_element(*self.MyGrWords_sendAllBtn_3levelPopCancel).click()
            logging.info('有3级等级限制，已点击取消按钮')
            return True

    '''我的页面-我的打招呼-打招呼消息列表页面元素'''
    def MyGrWords_MyWords_AddBtnEle(self):
        try:
            MyGrWords_MyWords_AddBtn = self.driver.find_element(*self.MyGrWords_MyWords_AddBtn)
        except NoSuchElementException:
            logging.info('no MyGrWords_sendAllBtn')
            return False
        else:
            return True





    # '''摄像头权限弹窗'''
    # def cameraPermission_popoverConfirmBtnEle(self):
    #     try:
    #         cameraPermission_popoverConfirmBtn = self.driver.find_element(*self.cameraPermission_popoverConfirmBtn)
    #
    #     except NoSuchElementException:
    #         logging.info('no cameraPermission_popoverConfirmBtn')
    #         return False
    #     else:
    #         cameraPermission_popoverConfirmBtn.click()
    #
    # '''储存权限弹窗'''
    # def StorePermission_popoverConfirmBtnEle(self):
    #     try:
    #         StorePermission_popoverConfirmBtn = self.driver.find_element(*self.StorePermission_popoverConfirmBtn)
    #
    #     except NoSuchElementException:
    #         logging.info('no cameraPermission_popoverConfirmBtn')
    #         return False
    #     else:
    #         StorePermission_popoverConfirmBtn.click()














    # '''========我的设置====='''
    '''我的页面-设置-黑名单无用户的元素'''
    def settings_blockList_NoUserTextEle(self):
        try:
            settings_blocklist_noUser = self.driver.find_element(*self.settings_blocklist_noUserText)

        except NoSuchElementException:
            logging.info('no settings_blocklist_noUserText')
            return False
        else:
            return settings_blocklist_noUser.text

    '''我的页面-设置-黑名单一个用户的元素'''
    def settings_blocklist_oneUserClickEle(self):
        try:
            settings_blocklist_oneUserClick = self.driver.find_element(*self.settings_blocklist_oneUserClick)

        except NoSuchElementException:
            logging.info('no settings_blocklist_oneUserClick')
            return False
        else:
            return True



if __name__ == '__main__':
    driver = appium_desired()
    l = MultiMan(driver)
    l.login_step(4087010,111111)
    l.tab_Mine_Btn()

    l.my_Tasks_entryTwoText()

    # 50[points]
    # l.vipLevel_level_topUpBtn()
    # l.vip_Level_mylevel_goback()
    # driver = appium_desired()
    # l = MultiMan(driver)
    # l.login_step(4086333,111111)
    # l.tab_Mine_Btn()
    # l.tab_Mine_Head()
    # time.sleep(3)
    # l.tab_mine_personal_information_test()
    # time.sleep(2)
    # l.tab_mine_personal_goback_btn()
    # driver.quit()

