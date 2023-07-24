# -*- coding: utf-8 -*-
import logging
from ChametProject_UI.Live_broadcast.common.common_fun import Common, NoSuchElementException
from ChametProject_UI.Six_party.common.desired_caps import anchor_appium_desired
from selenium.webdriver.common.by import By


class Live_anchor(Common):
    tab_discover = (By.ID, 'com.hkfuliao.chamet:id/rl_tab_discover')
    tab_live_list = (By.ID, 'com.hkfuliao.chamet:id/rl_tab_live_list')
    tab_party = (By.ID, 'com.hkfuliao.chamet:id/rl_tab_party')
    tab_group = (By.ID, 'com.hkfuliao.chamet:id/rl_tab_group')
    tab_group_group = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
    tab_mine = (By.ID, 'com.hkfuliao.chamet:id/rl_tab_mine')
    setup_party = (By.ID, 'com.hkfuliao.chamet:id/btn')
    setup_six_party = (By.ID, 'com.hkfuliao.chamet:id/ll_live_room_six')
    setup_six_Preview = (By.ID, 'com.hkfuliao.chamet:id/live_item0_texture')
    setup_beauty = (By.ID, 'com.hkfuliao.chamet:id/btn_beauty')
    setup_sticker = (By.ID, 'com.hkfuliao.chamet:id/btn_sticker')
    six_party_audience_information = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView')
    test_expect44 = (By.ID, 'com.hkfuliao.chamet:id/applicantsCount')
    test_expect45 = (By.ID, 'com.hkfuliao.chamet:id/lrv_host_1')
    sticker_download = (By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.ImageView[1]')
    sticker_downloading = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.ImageView')
    tow_Setup = (By.ID, 'com.hkfuliao.chamet:id/btn_live')
    more_Setting = (By.ID, 'com.hkfuliao.chamet:id/vc_setting')
    more_message = (By.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android'
                    '.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                    '/android.view.ViewGroup[2]/android.widget.FrameLayout')
    stranger_message = (By.ID, 'com.hkfuliao.chamet:id/headIv')
    stranger_message_people = (By.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget'
                               '.RelativeLayout['
                               '2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android'
                               '.widget.LinearLayout/android.widget.LinearLayout')
    private_letter_more = (By.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view'
                           '.ViewGroup/android.widget.RelativeLayout[1]/android.widget.TextView[2]')
    private_letter_more_follow = (By.XPATH,
                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view'
                                  '.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
    test_expect41 = (By.XPATH,
                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
    more_message_people = (By.ID,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget'
                           '.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    more_message_people_gift = (By.ID, 'com.hkfuliao.chamet:id/iv_chat_gift')
    more_message_people_sendgift = (By.ID, 'com.hkfuliao.chamet:id/sendTv')
    room_message_button = (By.XPATH,
                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout['
                           '3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
    room_message_button_input = (By.ID, 'com.hkfuliao.chamet:id/editEt')
    room_message_button_send = (By.ID, 'com.hkfuliao.chamet:id/btn_send')
    room_Homeowner_place_emo = (By.XPATH,
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout['
                                '2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget'
                                '.FrameLayout[3]/android.widget.ImageView')
    room_Homeowner_place = (By.ID, 'com.hkfuliao.chamet:id/groups_icon')
    room_banner = (By.ID, 'com.hkfuliao.chamet:id/recyclerView')
    more_Setting_background = (By.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx'
                               '.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                               '1]/android.widget.FrameLayout/android.widget.ImageView')
    more_Setting_background_Lv20 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout')
    more_top_up = (By.XPATH,  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.FrameLayout/android.widget.ImageView')
    more_top_up_4500 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    more_top_up_confirm = (By.ID, 'com.hkfuliao.chamet:id/single_btn')
    more_top_up_pay = (By.ID, 'com.android.vending:id/button_group')
    more_Setting_setting = (By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                            '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                            '.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx'
                            '.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]')
    more_setting_sticker = (By.ID, 'com.hkfuliao.chamet:id/sticker')
    more_setting_sticker_1 = (By.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                              '3]/android.widget.ImageView[1]')
    more_setting_sticker_1download = (By.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                      '.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout'
                                      '/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android'
                                      '.view.ViewGroup[3]/android.widget.ImageView')
    more_setting_beauty = (By.ID, 'com.hkfuliao.chamet:id/beauty')
    more_setting_beauty_reset = (By.ID, 'com.hkfuliao.chamet:id/tv_reset')
    more_setting_beauty_confirmreset = (By.ID, 'com.hkfuliao.chamet:id/positive_btn')
    more_setting_mirror_mode = (By.ID, 'com.hkfuliao.chamet:id/mirror_mode')
    more_setting_turn_off_camera = (By.ID, 'com.hkfuliao.chamet:id/turn_off_camera')
    more_setting_switch_camera = (By.ID, 'com.hkfuliao.chamet:id/switch_camera')
    more_setting_switch_microphone = (By.ID, 'com.hkfuliao.chamet:id/switch_microphone')
    close_six_party = (By.ID, 'com.hkfuliao.chamet:id/vc_close')
    close_six_party_tow_confirm = (By.ID, 'com.hkfuliao.chamet:id/positive_btn')
    close_six_party_two_cancle = (By.ID, 'com.hkfuliao.chamet:id/negative_btn')
    six_party_endpage_profile = (By.ID, 'com.hkfuliao.chamet:id/profile_head')
    six_party_endpage_running_account = (By.ID, 'com.hkfuliao.chamet:id/live_earn')
    partytab_one_partyroom = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView[1]')
    six_party_anchor_head = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View')
    six_party_follow_anchor = (By.ID, 'com.hkfuliao.chamet:id/iv_follow')
    six_party_report_anchor = (By.ID, 'com.hkfuliao.chamet:id/tv_report')
    six_party_gift = (By.ID, 'com.hkfuliao.chamet:id/vc_gift')
    six_party_send_gift = (By.ID, 'com.hkfuliao.chamet:id/sendTv')
    six_party_one_gift = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                    '.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view'
                                    '.ViewGroup/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager'
                                    '/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx'
                                    '.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
    six_party_two_gift = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                    '.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view'
                                    '.ViewGroup/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager'
                                    '/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx'
                                    '.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    six_party_call_anchor = (By.ID, 'com.hkfuliao.chamet:id/ll_enable')
    six_party_at_anchor = (By.ID, 'com.hkfuliao.chamet:id/tv_atHer')
    six_party_room_message_button = (By.ID, 'com.hkfuliao.chamet:id/vc_edt')
    six_party_room_message = (By.ID, 'com.hkfuliao.chamet:id/editEt')
    six_party_room_message_send = (By.ID, 'com.hkfuliao.chamet:id/btn_send')
    six_party_supernatant_anchor_head = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    six_party_supernatant_follow = (By.ID, 'com.hkfuliao.chamet:id/iv_follow')
    six_party_supernatant_gift = (By.ID, 'com.hkfuliao.chamet:id/profile_gift')
    six_party_more_people = (By.ID, 'com.hkfuliao.chamet:id/iv_more_people')
    six_party_more_people_list_one = (By.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]')
    six_party_more_people_list_two = (By.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]')
    six_party_supernatant_dynamic = (By.XPATH,
                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView')
    six_party_person_homepage_mine = (By.ID, 'com.hkfuliao.chamet:id/cl_fusion_about_me')
    six_party_tow_location = (By.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[3]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout')
    six_party_twice_apply = (By.ID, 'com.hkfuliao.chamet:id/apply')
    six_party_guest_enter = (By.ID, 'com.hkfuliao.chamet:id/special_effects_enter')
    six_party_off_mic = (By.ID, 'com.hkfuliao.chamet:id/leaveZone')
    six_party_anchor = (By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View')
    six_party_invite = (By.ID, 'com.hkfuliao.chamet:id/fl_invite')
    six_party_invite_list_one = (By.ID, 'com.hkfuliao.chamet:id/live_queue_invite')
    six_party_agree_list_one = (By.ID, 'com.hkfuliao.chamet:id/agree')
    six_party_invite_list_one_refuse = (By.ID, 'com.hkfuliao.chamet:id/refuse')
    six_party_agree_invite = (By.ID, 'com.hkfuliao.chamet:id/positive_btn')
    six_party_down_invite = (By.ID, 'com.hkfuliao.chamet:id/negative_btn')
    anchor_accept_phone = (By.ID, 'com.hkfuliao.chamet:id/vc_iv_accept')
    anchor_die_phone = (By.ID, 'com.hkfuliao.chamet:id/vc_iv_reject')
    homepage_back = (By.ID, 'com.hkfuliao.chamet:id/img_go_back_btn')
    six_party_gift_single = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]')
    confirmation_winning = (By.ID, 'com.hkfuliao.chamet:id/finish')
    gift_window_Activity = (
    By.XPATH, '//android.widget.LinearLayout[@content-desc="简体中文chinese simplified"]/android.widget.TextView')
    supernatant_message = (By.ID, 'com.hkfuliao.chamet:id/rl_send_message')
    supernatant_message_back = (By.ID, 'com.hkfuliao.chamet:id/iv_back')
    supernatant_message_setting = (By.ID, 'com.hkfuliao.chamet:id/iv_more_bottom')
    supernatant_message_setting_translate = (By.ID, 'com.hkfuliao.chamet:id/translateView')
    supernatant_message_setting_photo = (By.ID, 'com.hkfuliao.chamet:id/ll_photoView')
    supernatant_message_setting_camera = (By.ID, 'com.hkfuliao.chamet:id/tv_take_camera')
    supernatant_message_setting_video = (By.ID, 'com.hkfuliao.chamet:id/videoView')
    myphoto_one = (By.XPATH,
                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    myphoto_confirm = (By.ID, 'com.hkfuliao.chamet:id/menu_id_confirm')
    myphoto_message_one = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[2]')
    supernatant_message_setting_photo_confirm = (By.ID, 'com.sec.android.app.camera:id/normal_center_button')
    supernatant_message_setting_photo_twoconfirm = (By.ID, 'com.sec.android.app.camera:id/okay')
    supernatant_message_face_gif = (By.ID, 'com.hkfuliao.chamet:id/iv_face_gif')
    supernatant_message_face_gif_one = (By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.ImageView')
    supernatant_message_group = (By.XPATH, '//android.widget.TextView[contains(@text, "创建群里咳咳")]')
    supernatant_message_group_pic = (By.ID, 'com.hkfuliao.chamet:id/iv_more_pic')
    supernatant_message_group_pic_photo = (By.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView')
    supernatant_message_group_pic_camera = (By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')
    supernatant_message_group_chat = (By.ID, 'com.hkfuliao.chamet:id/et_edit_chat_info')
    supernatant_message_group_chat_send = (By.ID, 'com.hkfuliao.chamet:id/iv_send_message')
    supernatant_message_group_gif_one = (By.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.ImageView')
    supernatant_message_group_voice = (By.ID, 'com.hkfuliao.chamet:id/iv_voice')
    supernatant_message_group_upmic = (By.ID, 'com.hkfuliao.chamet:id/iv_bottom_up_mic')
    supernatant_message_group_addvoice = (By.ID, 'com.hkfuliao.chamet:id/tv_add_voice')
    supernatant_message_group_packet = (By.ID, 'com.hkfuliao.chamet:id/iv_packet')
    supernatant_message_group_packet_number = (By.ID, 'com.hkfuliao.chamet:id/ed_packet_count')
    supernatant_message_group_packet_diamond = (By.ID, 'com.hkfuliao.chamet:id/ed_packet_total_energy')
    supernatant_message_group_packet_send = (By.ID, 'com.hkfuliao.chamet:id/btn_send_packet')
    supernatant_message_group_packet_get = (By.ID, 'com.hkfuliao.chamet:id/ll_diamond_packet_content')
    supernatant_message_group_packet_open = (By.ID, 'com.hkfuliao.chamet:id/iv_open_diamond_packet')
    supernatant_message_group_gift = (By.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[4]')
    supernatant_message_group_more = (By.ID, 'com.hkfuliao.chamet:id/mic_play')
    supernatant_message_group_more_banner = (By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.ImageView[3]')
    supernatant_mute = (By.ID, 'com.hkfuliao.chamet:id/tv_mute')
    supernatant_unmute = (By.XPATH, '//android.widget.TextView[contains(@text, "禁言")]')
    supernatant_remove = (By.ID, 'com.hkfuliao.chamet:id/tv_remove')
    test_xx = (By.XPATH, '//android.widget.TextView[contains(@text, "交友房")]')
    homepage_video = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup')
    six_message_user = (By.XPATH,
                        '//android.widget.TextView[contains(@text, "[level]  goodbay1 送出1 Lucky Kiss给lisa1111 [gift] ")]')
    six_message_inuser = (By.XPATH, '//android.widget.TextView[contains(@text, "[level]  goodbay1 加入了房间")]')
    close_end_page = (By.ID, 'com.hkfuliao.chamet:id/closeTv')
    six_party_send_all_gift = (By.ID, 'com.hkfuliao.chamet:id/switchBtn')
    more_join = (By.XPATH,
                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout')
    end_party_two = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView')
    six_party_one_position = (By.ID, 'com.hkfuliao.chamet:id/lrv_host')
    six_party_two_position = (By.ID, 'com.hkfuliao.chamet:id/live_item1')
    six_party_anchor_floating_emo = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.ImageView')
    test_expect001 = (By.ID, 'com.hkfuliao.chamet:id/closeTv')
    test_expect002 = (By.ID, 'com.hkfuliao.chamet:id/live_item0_texture')
    test_expect003 = (By.ID, 'com.hkfuliao.chamet:id/tv_reset')
    test_expect004 = (By.ID, 'com.hkfuliao.chamet:id/progress')
    test_expect005 = (By.ID, 'com.hkfuliao.chamet:id/bg_user_level')
    test_expect006 = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    test_expect007 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
    test_expect009 = (By.ID, 'com.hkfuliao.chamet:id/iv_follow')
    test_expect010 = (By.ID, 'com.hkfuliao.chamet:id/tv_report_title')
    test_expect011 = (By.ID, 'com.hkfuliao.chamet:id/img_love')
    test_expect012 = (By.ID, 'com.hkfuliao.chamet:id/iv_follow')
    test_expect013 = (By.ID, 'com.hkfuliao.chamet:id/sendTv')
    test_expect014 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    test_expect015 = (By.ID, 'com.hkfuliao.chamet:id/iv_more')
    test_expect016 = (By.ID, 'com.hkfuliao.chamet:id/rl_system_content')
    test_expect017 = (By.ID, 'com.hkfuliao.chamet:id/iv_user_head')
    test_expect025 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup')
    test_expect027 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView')
    test_expect029 = (By.ID, 'com.hkfuliao.chamet:id/ll_content')
    test_expect030 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView')
    test_expect031 = (By.ID, 'com.hkfuliao.chamet:id/iv_error')
    test_expect032 = (By.ID, 'com.hkfuliao.chamet:id/iv_pic')
    test_expect033 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.ImageView[2]')
    test_expect034 = (By.ID, 'com.hkfuliao.chamet:id/ll_content')
    test_expect035 = (By.ID, 'com.hkfuliao.chamet:id/iv_pic')
    test_expect036 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.RelativeLayout')
    test_expect039 = (By.ID, 'com.hkfuliao.chamet:id/tv_sender_nick_name')
    test_expect040 = (By.ID, 'com.hkfuliao.chamet:id/rl_gift_info')
    test_expect041 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View')
    test_expect042 = (By.XPATH,
                      '//android.widget.TextView[contains(@text, "[level] goodbay1 加入了房间")]')
    test_expect044 = (By.XPATH, '//android.widget.TextView[contains(@text, "[level] lisa1111 : @goodbay1 ")]')

    test_expect059 = (By.XPATH,
                      '//android.widget.TextView[contains(@text, "欢迎来到Chamet 直播间！警告：直播期间严禁出现色情、粗俗、暴力、未成年人等相关情况。人工智能系统每天24 小时对其进行审查。一旦违反规定，将受到严惩！")]')
    test_expect060 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')
    test_expect066 = (By.ID, 'com.hkfuliao.chamet:id/special_effects_enter')
    test_expect068 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView')
    test_expect070 = (By.ID, 'com.hkfuliao.chamet:id/recycler_group')
    test_expect071 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.LinearLayout/android.view.View[1]')
    test_expect072 = (By.ID, 'com.hkfuliao.chamet:id/webview')
    test_expect074 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.ImageView[2]')
    test_expect083 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[3]')
    test_expect085 = (By.ID, 'com.hkfuliao.chamet:id/title')
    test_expect086 = (By.ID, 'com.hkfuliao.chamet:id/tv_fusion_about_me_title')
    test_expect090 = (By.ID, 'com.hkfuliao.chamet:id/headInfo')
    test_expect091 = (By.ID, 'com.hkfuliao.chamet:id/tv_atHer')
    test_expect093 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    test_expect094 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    test_expect096 = (By.XPATH, '//android.widget.TextView[contains(@text, "[level] goodbay1 : @lisa1111 ")]')
    test_expect097 = (By.ID, 'com.hkfuliao.chamet:id/vc_box')
    test_expect102 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    test_expect103 = (By.ID, 'com.hkfuliao.chamet:id/img_love')
    test_expect116 = (By.XPATH,
                      '//android.widget.TextView[contains(@text, "欢迎来到Chamet 直播间！警告：直播期间严禁出现色情、粗俗、暴力、未成年人等相关情况。人工智能系统每天24 小时对其进行审查。一旦违反规定，将受到严惩！")]')
    test_expect117 = (By.XPATH, '//android.widget.TextView[contains(@text, "[level]  Hello123456 : 1234")]')

    test_expect120 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')
    test_expect122 = (By.ID, 'com.hkfuliao.chamet:id/special_effects_enter')
    test_expect_94 = (By.XPATH,
                      '//android.widget.TextView[contains(@text, "[level]  Hello123456 送出1 Halloween给User20111243 [gift] ")]')
    test_expect106 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')
    test_expect107 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout')
    test_expect133 = (By.XPATH, '//android.widget.TextView[contains(@text, "0")]')
    test_expect155 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup')
    test_expect157 = (By.ID, 'com.hkfuliao.chamet:id/positive_btn')
    test_expect165 = (By.ID, 'com.hkfuliao.chamet:id/title')
    test_expect166 = (By.ID, 'com.hkfuliao.chamet:id/live_duration')
    test_expect140 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView[2]')
    test_expect018 = (By.XPATH, '//android.widget.TextView[contains(@text, "[level] goodbay1 送出1 幸运之吻给lisa1111 [gift] ")]')
    test_expect31 = (By.ID, '//android.widget.TextView[contains(@text, "[level] lisa1111 送出1 幸运之吻给goodbay1 [gift] ")]')
    per_btn = (By.ID, 'com.lbe.security.miui:id/permission_allow_foreground_only_button')
    test_expect105 = (By.XPATH, '//android.widget.TextView[contains(@text, "[level] goodbay1 已被主播移出房间")]')
    test_expect_106 = (By.XPATH, '//android.widget.TextView[contains(@text, "[level] goodbay1 被主播禁言")]')
    test_expect109 = (By.XPATH, '//android.widget.TextView[contains(@text, "[level] lisa1111 : 1234")]')
    test_expect16 = (By.XPATH, '//android.widget.TextView[contains(@text, "[level] goodbay1 送出1 Lucky Kiss给lisa1111 [gift] ")]')
    test_expect6 = (By.XPATH, '//android.widget.TextView[contains(@text, "直播期间，你可以获得更多的曝光和高收益拨打")]')


    def check_perBtn(self):
        logging.info('=进行授权=')
        try:
            per_btn=self.driver.find_element(*self.per_btn)

        except NoSuchElementException:
            logging.info('未授权成功')
        else:
            per_btn.click()
            logging.info('已授权')

    def Tab_discover(self):
        logging.info('=视频聊Tab页点击=')
        try:
            tab_discover = self.driver.find_element(*self.tab_discover)
        except NoSuchElementException:
            logging.info('=未找到视频聊Tab页=')
        else:
            tab_discover.click()

    def Tab_live_list(self):
        logging.info('=直播间Tab页点击=')
        try:
            tab_live_list = self.driver.find_element(*self.tab_live_list)
        except NoSuchElementException:
            logging.info('=未找到直播间Tab页=')
        else:
            tab_live_list.click()

    def Tab_party(self):
        logging.info('=交友房Tab页点击=')
        try:
            tab_party = self.driver.find_element(*self.tab_party)
        except NoSuchElementException:
            logging.info('=未找到交友房Tab页=')
        else:
            tab_party.click()

    def Tab_group(self):
        logging.info('=群聊动态Tab页点击=')
        try:
            tab_group = self.driver.find_element(*self.tab_group)
        except NoSuchElementException:
            logging.info('=未找到群聊动态Tab页=')
        else:
            tab_group.click()

    def Tab_group_group(self):
        logging.info('=群聊动态Tab页群组栏目点击=')
        try:
            tab_group_group = self.driver.find_element(*self.tab_group_group)
        except NoSuchElementException:
            logging.info('=未找到群聊动态Tab页群组栏目=')
        else:
            tab_group_group.click()

    def Tab_mine(self):
        logging.info('=群聊动态Tab页点击=')
        try:
            tab_mine = self.driver.find_element(*self.tab_mine)
        except NoSuchElementException:
            logging.info('=未找到群聊动态Tab页=')
        else:
            tab_mine.click()

        # 创建交友房按钮

    def Setup_party(self):
        logging.info('=开始创建交友房=')
        try:
            setup_party = self.driver.find_element(*self.setup_party)
        except NoSuchElementException:
            logging.info('=未找到创建交友房按钮=')
        else:
            setup_party.click()

    def Setup_live(self):
        logging.info('=开始创建直播间=')
        try:
            setup_live = self.driver.find_element(*self.setup_party)
        except NoSuchElementException:
            logging.info('=未找到创建直播间按钮=')
        else:
            setup_live.click()

        # 选择6人房

    def Setup_six_party(self):
        logging.info('=选择6人交友房=')
        try:
            setup_six_party = self.find_element(*self.setup_six_party)
        except NoSuchElementException:
            logging.info('=未找到6人交友房按钮=')
        else:
            setup_six_party.click()

    def Setup_beauty(self):
        logging.info('=找美颜按钮=')
        try:
            setup_beauty = self.find_element(*self.setup_beauty)
        except NoSuchElementException:
            logging.info('=未找到美颜按钮=')
        else:
            setup_beauty.click()

    def Setup_sticker(self):
        logging.info('=找贴纸按钮=')
        try:
            setup_sticker = self.find_element(*self.setup_sticker)
        except NoSuchElementException:
            logging.info('=未找到贴纸按钮=')
        else:
            setup_sticker.click()

    def Six_party_audience_information(self):
        logging.info('=房主点击信息列表的观众=')
        try:
            six_party_audience_information = self.find_element(*self.six_party_audience_information)
        except NoSuchElementException:
            logging.info('=未找到信息列表的观众=')
        else:
            six_party_audience_information.click()
    def Sticker_download(self):
        logging.info('=点击下载贴纸=')
        try:
            sticker_download = self.find_element(*self.sticker_download)
        except NoSuchElementException:
            logging.info('=未找到下载贴纸按钮=')
        else:
            sticker_download.click()

    def Sticker_downloading(self):
        logging.info('=判断有无下载贴纸=')
        try:
            self.driver.find_element(*self.sticker_downloading)
        except NoSuchElementException:
            logging.info('=未找到下载的贴纸=')
            return False
        else:
            logging.info('=以下载贴纸=')
            return True

    def Two_Setup(self):
        logging.info('=点击确认创建按钮=')
        try:
            tow_Setup = self.find_element(*self.tow_Setup)
        except NoSuchElementException:
            logging.info('=未找到确认创建按钮=')
        else:
            tow_Setup.click()

    def More_Setting(self):
        logging.info('=点击更多设置按钮=')
        try:
            more_Setting = self.find_element(*self.more_Setting)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮=')
        else:
            more_Setting.click()

    def More_Message(self):
        logging.info('=点击更多设置-消息按钮=')
        try:
            more_message = self.find_element(*self.more_message)
        except NoSuchElementException:
            logging.info('=未找到更多设置-消息按钮=')
        else:
            more_message.click()

    def More_join(self):
        logging.info('=点击申请上麦按钮')
        try:
            more_join = self.find_element(*self.more_join)
        except NoSuchElementException:
            logging.info('=未找到申请上麦按钮')
        else:
            more_join.click()

    def Stranger_message(self):
        logging.info('=点击私信浮层-陌生人按钮=')
        try:
            stranger_message = self.find_element(*self.stranger_message)
        except NoSuchElementException:
            logging.info('=未找到私信浮层-陌生人按钮=')
        else:
            stranger_message.click()

    def Stranger_message_people(self):
        logging.info('=点击私信浮层-陌生人列表用户=')
        try:
            stranger_message_people = self.find_element(*self.stranger_message_people)
        except NoSuchElementException:
            logging.info('=未找到私信浮层-陌生人列表用户=')
        else:
            stranger_message_people.click()

    def Private_letter_more(self):
        logging.info('=点击私信-更多按钮=')
        try:
            private_letter_more = self.find_element(*self.private_letter_more)
        except NoSuchElementException:
            logging.info('=未找到私信-更多按钮=')
        else:
            private_letter_more.click()

    def Private_letter_more_follow(self):
        logging.info('=点击私信-更多信息浮层-关注=')
        try:
            private_letter_more_follow = self.find_element(*self.private_letter_more_follow)
        except NoSuchElementException:
            logging.info('=未找到私信-更多信息浮层-关注=')
        else:
            private_letter_more_follow.click()

    def Homepage_back(self):
        logging.info('=点击个人主页返回按钮=')
        try:
            homepage_back = self.find_element(*self.homepage_back)
        except NoSuchElementException:
            logging.info('=未找个人主页返回按钮=')
        else:
            homepage_back.click()

    def Six_party_anchor(self):
        logging.info('=点击交友房房主流=')
        try:
            six_party_anchor = self.find_element(*self.six_party_anchor)
        except NoSuchElementException:
            logging.info('=未找到交友房房主流=')
        else:
            six_party_anchor.click()

    def Six_party_invite(self):
        logging.info('=房主点击邀请按钮=')
        try:
            six_party_invite = self.find_element(*self.six_party_invite)
        except NoSuchElementException:
            logging.info('=房主未找到邀请按钮=')
        else:
            six_party_invite.click()

    def Six_party_invite_list_one(self):
        logging.info('=房主邀请第一个观众=')
        try:
            six_party_invite_list_one = self.find_element(*self.six_party_invite_list_one)
        except NoSuchElementException:
            logging.info('=房主未找到邀请按钮=')
        else:
            six_party_invite_list_one.click()

    def Six_party_agree_list_one(self):
        logging.info('=房主同意列表中第一个观众的申请=')
        try:
            six_party_agree_list_one = self.find_element(*self.six_party_agree_list_one)
        except NoSuchElementException:
            logging.info('=房主未找到同意申请按钮=')
        else:
            six_party_agree_list_one.click()

    def Six_party_gift_single(self):
        logging.info('=点击礼物组刷数为一个=')
        try:
            six_party_gift_single = self.find_element(*self.six_party_gift_single)
        except NoSuchElementException:
            logging.info('=未找到礼物礼物组刷数为一个按钮=')
        else:
            six_party_gift_single.click()

    def Confirmation_winning(self):
        logging.info('=判读有无中奖弹窗=')
        try:
            confirmation_winning = self.find_element(*self.confirmation_winning)
        except NoSuchElementException:
            logging.info('=无中奖弹窗=')
        else:
            confirmation_winning.click()

    def Six_party_invite_list_one_refuse(self):
        logging.info('=房主删除列表中第一个观众的申请=')
        try:
            six_party_invite_list_one_refuse = self.find_element(*self.six_party_invite_list_one_refuse)
        except NoSuchElementException:
            logging.info('=房主未找到删除申请按钮=')
        else:
            six_party_invite_list_one_refuse.click()


    def Six_party_agree_invite(self):
        logging.info('=观众点击同意邀请=')
        try:
            six_party_agree_invite = self.find_element(*self.six_party_agree_invite)
        except NoSuchElementException:
            logging.info('=观众未找到同意按钮=')
        else:
            six_party_agree_invite.click()

    def Six_party_down_invite(self):
        logging.info('=观众点击拒绝邀请=')
        try:
            six_party_down_invite = self.find_element(*self.six_party_down_invite)
        except NoSuchElementException:
            logging.info('=观众未找到拒绝按钮=')
        else:
            six_party_down_invite.click()

    def Six_party_one_position(self):
        logging.info('=房主点击麦位上的自己的流=')
        try:
            six_party_one_position = self.find_element(*self.six_party_one_position)
        except NoSuchElementException:
            logging.info('=房主未找到麦位上自己的流=')
        else:
            six_party_one_position.click()

    def Six_party_anchor_floating_emo(self):
        logging.info('=房主点击自己信息浮层的表情=')
        try:
            six_party_anchor_floating_emo = self.find_element(*self.six_party_anchor_floating_emo)
        except NoSuchElementException:
            logging.info('=房主未找到自己信息浮层的表情=')
        else:
            six_party_anchor_floating_emo.click()

    def Six_party_two_position(self):
        logging.info('=房主点击房间第二麦位的流=')
        try:
            six_party_two_position = self.find_element(*self.six_party_two_position)
        except NoSuchElementException:
            logging.info('=房主未找到房间第二麦位的流=')
        else:
            six_party_two_position.click()

    def More_message_people(self):
        logging.info('=点击私信-用户=')
        try:
            more_message_people = self.find_element(*self.more_message_people)
        except NoSuchElementException:
            logging.info('=未找到私信-用户=')
        else:
            more_message_people.click()

    def More_message_people_gift(self):
        logging.info('=点击私信-礼物按钮=')
        try:
            more_message_people_gift = self.find_element(*self.more_message_people_gift)
        except NoSuchElementException:
            logging.info('=未找到私信-礼物按钮=')
        else:
            more_message_people_gift.click()

    def More_message_people_sendgift(self):
        logging.info('=点击私信-送礼按钮=')
        try:
            more_message_people_sendgift = self.find_element(*self.more_message_people_sendgift)
        except NoSuchElementException:
            logging.info('=未找到私信-送礼按钮=')
        else:
            more_message_people_sendgift.click()

    def Room_message_button(self):
        logging.info('=点击交友房-发消息按钮=')
        try:
            room_message_button = self.find_element(*self.room_message_button)
        except NoSuchElementException:
            logging.info('=未找到交友房-发消息按钮=')
        else:
            room_message_button.click()

    def Room_message_button_click(self):
        logging.info('=点击输入框输入文本=')
        try:
            room_message_button_input = self.find_element(*self.room_message_button_input)
        except NoSuchElementException:
            logging.info('=未找到输入框=')
        else:
            room_message_button_input.send_keys('1234')

    def Room_message_button_input(self):
        logging.info('=点击输入框输入文本=')
        try:
            room_message_button_input = self.find_element(*self.room_message_button_input)
        except NoSuchElementException:
            logging.info('=未找到输入框=')
        else:
            room_message_button_input.send_keys('1234')

    def Room_message_button_send(self):
        logging.info('=点击发送=')
        try:
            room_message_button_send = self.find_element(*self.room_message_button_send)
        except NoSuchElementException:
            logging.info('=未找到发送按钮=')
        else:
            room_message_button_send.click()

    def Room_Homeowner_place(self):
        logging.info('=点击房主麦位-点击表情=')
        try:
            room_Homeowner_place = self.find_element(*self.room_Homeowner_place)
        except NoSuchElementException:
            logging.info('=未找到麦位-表情按钮=')
        else:
            room_Homeowner_place.click()

    def Room_Homeowner_place_emo(self):
        logging.info('=点击房主麦位-点击表情=')
        try:
            room_Homeowner_place_emo = self.find_element(*self.room_Homeowner_place_emo)
        except NoSuchElementException:
            logging.info('=未找到麦位-表情按钮=')
        else:
            room_Homeowner_place_emo.click()

    def Room_banner(self):
        logging.info('=点击房主麦位-点击表情=')
        try:
            room_banner = self.find_element(*self.room_banner)
        except NoSuchElementException:
            logging.info('=未找到麦位-表情按钮=')
        else:
            room_banner.click()

    def More_Setting_background(self):
        logging.info('=点击更多设置中的交友房背景=')
        try:
            more_Setting_background = self.find_element(*self.more_Setting_background)
        except NoSuchElementException:
            logging.info('=未找到交友房背景=')
        else:
            more_Setting_background.click()

    def More_Setting_background_Lv20(self):
        logging.info('=点击更多设置-交友房背景=')
        try:
            more_Setting_background_Lv20 = self.find_element(*self.more_Setting_background_Lv20)
        except NoSuchElementException:
            logging.info('=未找到更多设置-交友房背景=')
        else:
            more_Setting_background_Lv20.click()

    def More_top_up(self):
        logging.info('=点击更多设置-充值按钮=')
        try:
            more_top_up = self.find_element(*self.more_top_up)
        except NoSuchElementException:
            logging.info('=未找到更多设置-充值按钮=')
        else:
            more_top_up.click()

    def More_top_up_4500(self):
        logging.info('=点击更多设置-充值按钮-充值第一档=')
        try:
            more_top_up_4500 = self.find_element(*self.more_top_up_4500)
        except NoSuchElementException:
            logging.info('=未找到更多设置-充值按钮-充值第一档=')
        else:
            more_top_up_4500.click()

    def More_top_up_pay(self):
        logging.info('=点击一键支付=')
        try:
            more_top_up_pay = self.find_element(*self.more_top_up_pay)
        except NoSuchElementException:
            logging.info('=未找到一键支付=')
        else:
            more_top_up_pay.click()

    def More_top_up_confirm(self):
        logging.info('=点击充值完成后确认按钮')
        try:
            more_top_up_confirm = self.find_element(*self.more_top_up_confirm)
        except NoSuchElementException:
            logging.info('=未找到充值完成后确认按钮=')
        else:
            more_top_up_confirm.click()

    def More_Setting_setting(self):
        logging.info('=更多设置按钮')
        try:
            more_setting = self.find_element(*self.more_Setting_setting)
        except NoSuchElementException:
            logging.info('=未找到更多按钮=')
        else:
            more_setting.click()

    def More_setting_sticker(self):
        logging.info('=更多设置按钮-贴纸')
        try:
            more_setting_sticker = self.find_element(*self.more_setting_sticker)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-贴纸=')
        else:
            more_setting_sticker.click()

    def More_setting_sticker_1(self):
        logging.info('=更多设置按钮-贴纸-下载第一个贴纸')
        try:
            more_setting_sticker_1 = self.find_element(*self.more_setting_sticker_1)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-贴纸-下载按钮=')
        else:
            more_setting_sticker_1.click()

    def More_setting_beauty(self):
        logging.info('=更多设置按钮-美颜')
        try:
            more_setting_beauty = self.find_element(*self.more_setting_beauty)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-美颜=')
        else:
            more_setting_beauty.click()

    def More_setting_beauty_reset(self):
        logging.info('=更多设置按钮-清除美颜')
        try:
            more_setting_beauty_reset = self.find_element(*self.more_setting_beauty_reset)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-清除美颜=')
        else:
            more_setting_beauty_reset.click()

    def More_setting_beauty_confirmreset(self):
        logging.info('=更多设置按钮-二次确认清除美颜')
        try:
            more_setting_beauty_confirmreset = self.find_element(*self.more_setting_beauty_confirmreset)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-二次确认清除美颜美颜=')
        else:
            more_setting_beauty_confirmreset.click()

    def More_setting_mirror_mode(self):
        logging.info('=点击更多设置按钮-镜像')
        try:
            more_setting_mirror_mode = self.find_element(*self.more_setting_mirror_mode)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-镜像=')
        else:
            more_setting_mirror_mode.click()

    def More_setting_turn_off_camera(self):
        logging.info('=点击更多设置按钮-开关摄像头')
        try:
            more_setting_turn_off_camera = self.find_element(*self.more_setting_turn_off_camera)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-开关摄像头=')
        else:
            more_setting_turn_off_camera.click()

    def More_setting_switch_camera(self):
        logging.info('=点击更多设置按钮-切换摄像头')
        try:
            more_setting_switch_camera = self.find_element(*self.more_setting_switch_camera)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-切换摄像头=')
        else:
            more_setting_switch_camera.click()

    def More_setting_switch_microphone(self):
        logging.info('=点击更多设置按钮-开关麦克风')
        try:
            more_setting_switch_microphone = self.find_element(*self.more_setting_switch_microphone)
        except NoSuchElementException:
            logging.info('=未找到更多设置按钮-开关麦克风=')
        else:
            more_setting_switch_microphone.click()

    def Close_six_party(self):
        logging.info('=点击关闭交友房=')
        try:
            close_six_party = self.find_element(*self.close_six_party)
        except NoSuchElementException:
            logging.info('=未找到关闭交友房按钮=')
        else:
            close_six_party.click()

    def Close_six_party_two_confirm(self):
        logging.info('=点击关闭交友房二次确认弹窗-确认=')
        try:
            close_six_party_tow_confirm = self.find_element(*self.close_six_party_tow_confirm)
        except NoSuchElementException:
            logging.info('=未找到关闭交友房二次确认弹窗-确认=')
        else:
            close_six_party_tow_confirm.click()

    def Close_six_party_two_cancle(self):
        logging.info('=点击关闭交友房二次确认弹窗-取消=')
        try:
            close_six_party_two_cancle = self.find_element(*self.close_six_party_two_cancle)
        except NoSuchElementException:
            logging.info('=未找到关闭交友房二次确认弹窗-取消=')
        else:
            close_six_party_two_cancle.click()

    def Six_party_endpage_profile(self):
        logging.info('=点击交友房结束界面的主播头像=')
        try:
            six_party_endpage_profile = self.find_element(*self.six_party_endpage_profile)
        except NoSuchElementException:
            logging.info('=未找到交友房结束界面的主播头像=')
        else:
            six_party_endpage_profile.click()

    def Six_party_endpage_running_account(self):
        logging.info('=点击交友房结束界面的流水=')
        try:
            six_party_endpage_running_account = self.find_element(*self.six_party_endpage_running_account)
        except NoSuchElementException:
            logging.info('=未找到交友房结束界面的流水=')
        else:
            six_party_endpage_running_account.click()

    def Partytab_one_partyroom(self):
        logging.info('=点击进去交友房Tab的第一个交友房=')
        try:
            partytab_one_partyroom = self.find_element(*self.partytab_one_partyroom)
        except NoSuchElementException:
            logging.info('=未找到交友房Tab的第一个交友房=')
        else:
            partytab_one_partyroom.click()

    def Six_party_anchor_head(self):
        logging.info('=点击交友房主播头像=')
        try:
            six_party_anchor_head = self.find_element(*self.six_party_anchor_head)
        except NoSuchElementException:
            logging.info('=未找到交友房主播头像=')
        else:
            six_party_anchor_head.click()

    def Six_party_follow_anchor(self):
        logging.info('=关注房主=')
        try:
            six_party_follow_anchor = self.find_element(*self.six_party_follow_anchor)
        except NoSuchElementException:
            logging.info('=未找到关注房主按钮=')
        else:
            six_party_follow_anchor.click()

    def Six_party_report_anchor(self):
        logging.info('=举报房主=')
        try:
            six_party_report_anchor = self.find_element(*self.six_party_report_anchor)
        except NoSuchElementException:
            logging.info('=未找到举报房主按钮=')
        else:
            six_party_report_anchor.click()

    def Six_party_gift(self):
        logging.info('=点击礼物按钮=')
        try:
            six_party_gift = self.find_element(*self.six_party_gift)
        except NoSuchElementException:
            logging.info('=未找到礼物按钮=')
        else:
            six_party_gift.click()

    def Six_party_one_gift(self):
        logging.info('=点击礼物橱窗的第一个礼物=')
        try:
            six_party_one_gift = self.find_element(*self.six_party_one_gift)
        except NoSuchElementException:
            logging.info('=未找到礼物橱窗的第一个礼物=')
        else:
            six_party_one_gift.click()

    def Six_party_two_gift(self):
        logging.info('=点击礼物橱窗的第二个礼物=')
        try:
            six_party_two_gift = self.find_element(*self.six_party_two_gift)
        except NoSuchElementException:
            logging.info('=未找到礼物橱窗的第二个礼物=')
        else:
            six_party_two_gift.click()

    def Six_party_send_gift(self):
        logging.info('=点击送出礼物=')
        try:
            six_party_send_gift = self.find_element(*self.six_party_send_gift)
        except NoSuchElementException:
            logging.info('=未找到送出礼物按钮=')
        else:
            six_party_send_gift.click()

    def Six_party_call_anchor(self):
        logging.info('=点击信息橱窗中的拨打按钮=')
        try:
            six_party_call_anchor = self.find_element(*self.six_party_call_anchor)
        except NoSuchElementException:
            logging.info('=未找到信息橱窗中的拨打按钮=')
        else:
            six_party_call_anchor.click()

    def Six_party_at_anchor(self):
        logging.info('=点击信息橱窗中的@=')
        try:
            six_party_at_anchor = self.find_element(*self.six_party_at_anchor)
        except NoSuchElementException:
            logging.info('=未找到信息橱窗中的@=')
        else:
            six_party_at_anchor.click()

    def Six_party_room_message_button(self):
        logging.info('=点击房间中的输入框按钮=')
        try:
            six_party_room_message_button = self.find_element(*self.six_party_room_message_button)
        except NoSuchElementException:
            logging.info('=未找到房间中的输入框按钮=')
        else:
            six_party_room_message_button.click()

    def Six_party_room_message(self):
        logging.info('=点击房间中的输入框=')
        try:
            six_party_room_message = self.find_element(*self.six_party_room_message)
        except NoSuchElementException:
            logging.info('=未找到房间中的输入框=')
        else:
            six_party_room_message.send_keys('1234')

    def Six_party_room_message_send(self):
        logging.info('=点击房间中的输入框发送=')
        try:
            six_party_room_message_send = self.find_element(*self.six_party_room_message_send)
        except NoSuchElementException:
            logging.info('=未找到房间中的输入框发送=')
        else:
            six_party_room_message_send.click()

    def Six_party_supernatant_anchor_head(self):
        logging.info('=点击信息浮层中的头像=')
        try:
            six_party_supernatant_anchor_head = self.find_element(*self.six_party_supernatant_anchor_head)
        except NoSuchElementException:
            logging.info('=未找到信息浮层中的头像=')
        else:
            six_party_supernatant_anchor_head.click()

    def Six_party_supernatant_follow(self):
        logging.info('=点击信息浮层中的关注=')
        try:
            six_party_supernatant_follow = self.find_element(*self.six_party_supernatant_follow)
        except NoSuchElementException:
            logging.info('=未找到信息浮层中的关注=')
        else:
            six_party_supernatant_follow.click()

    def Six_party_supernatant_gift(self):
        logging.info('=点击信息浮层中的送礼=')
        try:
            six_party_supernatant_gift = self.find_element(*self.six_party_supernatant_gift)
        except NoSuchElementException:
            logging.info('=未找到信息浮层中的送礼=')
        else:
            six_party_supernatant_gift.click()

    def Six_party_more_people(self):
        logging.info('=点击房间内观众按钮=')
        try:
            six_party_more_people = self.find_element(*self.six_party_more_people)
        except NoSuchElementException:
            logging.info('=未找到房间内观众按钮=')
        else:
            six_party_more_people.click()

    def Six_party_more_people_list_one(self):
        logging.info('=点击房间观众列表第一个观众=')
        try:
            six_party_more_people_list_one = self.find_element(*self.six_party_more_people_list_one)
        except NoSuchElementException:
            logging.info('=未找到房间观众列表第一个观众=')
        else:
            six_party_more_people_list_one.click()

    def Six_party_more_people_list_two(self):
        logging.info('=点击房间观众列表第二个观众=')
        try:
            six_party_more_people_list_two = self.find_element(*self.six_party_more_people_list_two)
        except NoSuchElementException:
            logging.info('=未找到房间观众列表第二个观众=')
        else:
            six_party_more_people_list_two.click()

    def Six_party_tow_location(self):
        logging.info('=点击房间第二个麦位=')
        try:
            six_party_tow_location = self.find_element(*self.six_party_tow_location)
        except NoSuchElementException:
            logging.info('=未找到房间第二个麦位=')
        else:
            six_party_tow_location.click()

    def Six_party_twice_apply(self):
        logging.info('=确认申请连麦=')
        try:
            six_party_twice_apply = self.find_element(*self.six_party_twice_apply)
        except NoSuchElementException:
            logging.info('=确认申请连麦=')
        else:
            six_party_twice_apply.click()

    def Six_party_off_mic(self):
        logging.info('=点击离开嘉宾位=')
        try:
            six_party_off_mic = self.find_element(*self.six_party_off_mic)
        except NoSuchElementException:
            logging.info('=未找到离开嘉宾位按钮=')
        else:
            six_party_off_mic.click()

    def Six_party_off_mic_confirm(self):
        logging.info('=二次确认离开嘉宾位=')
        try:
            six_party_off_mic_confirm = self.find_element(*self.close_six_party_tow_confirm)
        except NoSuchElementException:
            logging.info('=未找到离开嘉宾位按钮=')
        else:
            six_party_off_mic_confirm.click()

    def Gift_window_Activity(self):
        logging.info('=点击礼物橱窗-Activity栏目=')
        try:
            gift_window_Activity = self.find_element(*self.gift_window_Activity)
        except NoSuchElementException:
            logging.info('=未找到礼物橱窗-Activity栏目=')
        else:
            gift_window_Activity.click()

    def Supernatant_message(self):
        logging.info('=信息浮窗-私信按钮=')
        try:
            supernatant_message = self.find_element(*self.supernatant_message)
        except NoSuchElementException:
            logging.info('=未找到信息浮窗-私信按钮=')
        else:
            supernatant_message.click()

    def Supernatant_message_back(self):
        logging.info('=点击私信浮层-返回按钮=')
        try:
            supernatant_message_back = self.find_element(*self.supernatant_message_back)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗-返回按钮=')
        else:
            supernatant_message_back.click()

    def Supernatant_message_more(self):
        logging.info('=点击私信浮层-更多按钮=')
        try:
            supernatant_message_more = self.find_element(*self.test_expect015)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗-更多按钮=')
        else:
            supernatant_message_more.click()

    def Supernatant_message_setiing(self):
        logging.info('=私信浮层展开折叠区域=')
        try:
            supernatant_message_setting = self.find_element(*self.supernatant_message_setting)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗-展开折叠区域按钮=')
        else:
            supernatant_message_setting.click()

    def Supernatant_message_setiing_translate(self):
        logging.info('=私信浮层折叠区域-翻译按钮=')
        try:
            supernatant_message_setting_translate = self.find_element(*self.supernatant_message_setting_translate)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗折叠区域-翻译按钮=')
        else:
            supernatant_message_setting_translate.click()

    def Supernatant_message_setiing_photo(self):
        logging.info('=私信浮层折叠区域-拍照按钮=')
        try:
            supernatant_message_setting_photo = self.find_element(*self.supernatant_message_setting_photo)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗折叠区域-拍照按钮=')
        else:
            supernatant_message_setting_photo.click()

    def Supernatant_message_setiing_photo_confirm(self):
        logging.info('=私信浮层折叠区域-拍照按钮-拍照-=')
        try:
            supernatant_message_setting_photo_confirm = self.find_element(
                *self.supernatant_message_setting_photo_confirm)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗折叠区域-拍照按钮-拍照=')
        else:
            supernatant_message_setting_photo_confirm.click()

    def Supernatant_message_setiing_photo_twoconfirm(self):
        logging.info('=私信浮层折叠区域-拍照按钮-拍照发送=')
        try:
            supernatant_message_setting_photo_twoconfirm = self.find_element(
                *self.supernatant_message_setting_photo_twoconfirm)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗折叠区域-拍照发送=')
        else:
            supernatant_message_setting_photo_twoconfirm.click()

    def Supernatant_message_setiing_camera(self):
        logging.info('=私信浮层折叠区域-相册按钮=')
        try:
            supernatant_message_setting_camera = self.find_element(*self.supernatant_message_setting_camera)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗折叠区域-相册按钮=')
        else:
            supernatant_message_setting_camera.click()

    def Supernatant_message_setiing_video(self):
        logging.info('=私信浮层折叠区域-视频聊按钮=')
        try:
            supernatant_message_setting_video = self.find_element(*self.supernatant_message_setting_video)
        except NoSuchElementException:
            logging.info('=未找到私信浮窗折叠区域-视频聊按钮=')
        else:
            supernatant_message_setting_video.click()

    def Myphoto_one(self):
        logging.info('=点击我的相册-选择第一张照片=')
        try:
            myphoto_one = self.find_element(*self.myphoto_one)
        except NoSuchElementException:
            logging.info('=未找到我的相册-选择第一张照片=')
        else:
            myphoto_one.click()

    def Myphoto_message_one(self):
        logging.info('=私信中点击我的相册-选择第一张照片=')
        try:
            myphoto_message_one = self.find_element(*self.myphoto_message_one)
        except NoSuchElementException:
            logging.info('=未找到我的相册-选择第一张照片=')
        else:
            myphoto_message_one.click()

    def Myphoto_comfirm(self):
        logging.info('=我的相册-确认发送=')
        try:
            myphoto_confirm = self.find_element(*self.myphoto_confirm)
        except NoSuchElementException:
            logging.info('=未找到我的相册-确认发送按钮=')
        else:
            myphoto_confirm.click()

    def Supernatant_message_face_gif(self):
        logging.info('=点击私信浮层-表情按钮=')
        try:
            supernatant_message_face_gif = self.find_element(*self.supernatant_message_face_gif)
        except NoSuchElementException:
            logging.info('=未找到私信浮层-表情按钮=')
        else:
            supernatant_message_face_gif.click()

    def Supernatant_message_face_gif_one(self):
        logging.info('=点击私信浮层-表情按钮-第一个表情=')
        try:
            supernatant_message_face_gif_one = self.find_element(*self.supernatant_message_face_gif_one)
        except NoSuchElementException:
            logging.info('=未找到私信浮层-表情按钮-第一个表情=')
        else:
            supernatant_message_face_gif_one.click()

    def Supernatant_message_group(self):
        logging.info('=点击私信浮层-群聊=')
        try:
            supernatant_message_group = self.find_element(*self.supernatant_message_group)
        except NoSuchElementException:
            logging.info('=未找到私信浮层-群聊=')
        else:
            supernatant_message_group.click()

    def Supernatant_message_group_pic(self):
        logging.info('=点击私信浮层中群聊-发图片=')
        try:
            supernatant_message_group_pic = self.find_element(*self.supernatant_message_group_pic)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-发图片按钮=')
        else:
            supernatant_message_group_pic.click()

    def Supernatant_message_group_pic_photo(self):
        logging.info('=点击私信浮层中群聊-发图片-拍照=')
        try:
            supernatant_message_group_pic_photo = self.find_element(*self.supernatant_message_group_pic_photo)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-发图片拍照按钮=')
        else:
            supernatant_message_group_pic_photo.click()

    def Supernatant_message_group_pic_camera(self):
        logging.info('=点击私信浮层中群聊-发图片-相册=')
        try:
            supernatant_message_group_pic_camera = self.find_element(*self.supernatant_message_group_pic_camera)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-发相册图片按钮=')
        else:
            supernatant_message_group_pic_camera.click()

    def Supernatant_message_group_chat(self):
        logging.info('=点击私信浮层中群聊-输入消息=')
        try:
            supernatant_message_group_chat = self.find_element(*self.supernatant_message_group_chat)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-输入发消息=')
        else:
            supernatant_message_group_chat.send_keys('1234')

    def Supernatant_message_group_chat_send(self):
        logging.info('=点击私信浮层中群聊-发消息=')
        try:
            supernatant_message_group_chat_send = self.find_element(*self.supernatant_message_group_chat_send)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-发消息=')
        else:
            supernatant_message_group_chat_send.click()

    def Supernatant_message_group_gif_one(self):
        logging.info('=点击私信浮层中群聊-第一个表情=')
        try:
            supernatant_message_group_gif_one = self.find_element(*self.supernatant_message_group_gif_one)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-第一个表情=')
        else:
            supernatant_message_group_gif_one.click()

    def Supernatant_message_group_voice(self):
        logging.info('=点击私信浮层中群聊-语音按钮=')
        try:
            supernatant_message_group_voice = self.find_element(*self.supernatant_message_group_voice)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-语音按钮=')
        else:
            supernatant_message_group_voice.click()

    def Supernatant_message_group_addvoice(self):
        logging.info('=点击私信浮层中群聊-录制语音=')
        try:
            supernatant_message_group_addvoice = self.find_element(*self.supernatant_message_group_addvoice)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-录制按钮=')
        else:
            supernatant_message_group_addvoice.click()

    def Supernatant_message_group_upmic(self):
        logging.info('=点击私信浮层中群聊-上麦=')
        try:
            supernatant_message_group_upmic = self.find_element(*self.supernatant_message_group_upmic)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-上麦=')
        else:
            supernatant_message_group_upmic.click()

    def Supernatant_message_group_packet(self):
        logging.info('=点击私信浮层中群聊-红包=')
        try:
            supernatant_message_group_packet = self.find_element(*self.supernatant_message_group_packet)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-红包=')
        else:
            supernatant_message_group_packet.click()

    def Supernatant_message_group_packet_number(self):
        logging.info('=点击私信浮层中群聊-红包-个数=')
        try:
            supernatant_message_group_packet_number = self.find_element(*self.supernatant_message_group_packet_number)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-红包-个数=')
        else:
            supernatant_message_group_packet_number.send_keys('2')

    def Supernatant_message_group_packet_diamond(self):
        logging.info('=点击私信浮层中群聊-红包-钻石数=')
        try:
            supernatant_message_group_packet_diamond = self.find_element(*self.supernatant_message_group_packet_diamond)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-红包=钻石数=')
        else:
            supernatant_message_group_packet_diamond.send_keys('200')

    def Supernatant_message_group_packet_send(self):
        logging.info('=点击私信浮层中群聊-红包-发送=')
        try:
            supernatant_message_group_packet_send = self.find_element(*self.supernatant_message_group_packet_send)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-红包-发送=')
        else:
            supernatant_message_group_packet_send.click()

    def Supernatant_message_group_packet_get(self):
        logging.info('=点击私信浮层中群聊-红包-领取=')
        try:
            supernatant_message_group_packet_get = self.find_element(*self.supernatant_message_group_packet_get)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-红包-领取=')
        else:
            supernatant_message_group_packet_get.click()

    def Supernatant_message_group_packet_open(self):
        logging.info('=点击私信浮层中群聊-红包-二次确认领取=')
        try:
            supernatant_message_group_packet_open = self.find_element(*self.supernatant_message_group_packet_open)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-红包-二次确认领取=')
        else:
            supernatant_message_group_packet_open.click()

    def Supernatant_message_group_gift(self):
        logging.info('=点击私信浮层中群聊-送礼按钮=')
        try:
            supernatant_message_group_gift = self.find_element(*self.supernatant_message_group_gift)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-送礼按钮=')
        else:
            supernatant_message_group_gift.click()

    def Supernatant_message_group_more(self):
        logging.info('=点击私信浮层中群聊-更多按钮=')
        try:
            supernatant_message_group_more = self.find_element(*self.supernatant_message_group_more)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-更多按钮=')
        else:
            supernatant_message_group_more.click()

    def Supernatant_message_group_more_banner(self):
        logging.info('=点击私信浮层中群聊-更多_banner=')
        try:
            supernatant_message_group_more_banner = self.find_element(*self.supernatant_message_group_more_banner)
        except NoSuchElementException:
            logging.info('=未找到私信浮层中群聊-更多banner=')
        else:
            supernatant_message_group_more_banner.click()

    def Supernatant_mute(self):
        logging.info('=点击信息浮层中-禁言=')
        try:
            supernatant_mute = self.find_element(*self.supernatant_mute)
        except NoSuchElementException:
            logging.info('=未找到信息浮层中-禁言=')
        else:
            supernatant_mute.click()

    def Supernatant_remove(self):
        logging.info('=点击信息浮层中-禁言=')
        try:
            supernatant_remove = self.find_element(*self.supernatant_remove)
        except NoSuchElementException:
            logging.info('=未找到信息浮层中-禁言=')
        else:
            supernatant_remove.click()

    def Six_message_user(self):
        logging.info('=点击公聊信息-用户名=')
        try:
            supernatant_mute = self.find_element(*self.six_message_user)
        except NoSuchElementException:
            logging.info('=未找到公聊信息-用户名=')
        else:
            supernatant_mute.click()

    def Six_message_inuser(self):
        logging.info('=点击公聊信息-进场观众用户名=')
        try:
            six_message_inuser = self.find_element(*self.six_message_inuser)
        except NoSuchElementException:
            logging.info('=未找到公聊信息-进场观众用户名=')
        else:
            six_message_inuser.click()

    def Close_end_page(self):
        logging.info('=交友房关闭结束页=')
        try:
            close_end_page = self.find_element(*self.close_end_page)
        except NoSuchElementException:
            logging.info('=未找到关闭交友房结束页按钮=')
        else:
            close_end_page.click()


    def Six_party_send_all_gift(self):
        logging.info('=选中所有人送礼=')
        try:
            six_party_send_all_gift = self.find_element(*self.six_party_send_all_gift)
        except NoSuchElementException:
            logging.info('=未找到选中所有人按钮=')
        else:
            six_party_send_all_gift.click()


    def Homepage_video(self):
        logging.info('=个人主页视频流=')
        try:
            homepage_video = self.find_element(*self.homepage_video)
        except NoSuchElementException:
            logging.info('=未找到个人主页视频流=')
        else:
            homepage_video.click()

    def Anchor_accept_phone(self):
        logging.info('=主播接听电话=')
        try:
            anchor_accept_phone = self.find_element(*self.anchor_accept_phone)
        except NoSuchElementException:
            logging.info('=主播未找到接听电话按钮=')
        else:
            anchor_accept_phone.click()

    def Anchor_die_phone(self):
        logging.info('=主播拒绝电话=')
        try:
            anchor_die_phone = self.find_element(*self.anchor_die_phone)
        except NoSuchElementException:
            logging.info('=主播未找到拒绝电话按钮=')
        else:
            anchor_die_phone.click()

    def End_party_two(self):
        logging.info('=点击交友房结束页的推荐房间=')
        try:
            end_party_two = self.find_element(*self.end_party_two)
        except NoSuchElementException:
            logging.info('=未找到交友房结束页的推荐房间=')
        else:
            end_party_two.click()


###############################################################################################################################################################################################################################################################################################################
    # 点击创建交友房时判断右上角出现 × 按钮

    def Test_XX(self):
        logging.info('=测试判断=')
        try:
            self.driver.find_element(*self.test_xx)
        except NoSuchElementException:
            logging.info('=未找到=')
            return False
        else:
            logging.info('=找到了=')
            return True

    def Test_X001(self):
        logging.info('=判断有无× 按钮=')
        try:
            self.driver.find_element(*self.test_expect001)
        except NoSuchElementException:
            logging.info('=未找到× 按钮=')
            return False
        else:
            logging.info('=找到× 按钮=')
            return True

    # 开启6人交友房时判断是否有预览画面
    def Test_X002(self):
        logging.info('=判断有无预览画面=')
        try:
            self.driver.find_element(*self.test_expect002)
        except NoSuchElementException:
            logging.info('=未找到预览画面=')
            return False
        else:
            logging.info('=找到预览画面=')
            return True

    # 点击美颜按钮判断是否弹出美颜按钮
    def Test_X003(self):
        logging.info('=判断有无美颜按钮=')
        try:
            self.driver.find_element(*self.test_expect003)
        except NoSuchElementException:
            logging.info('=未找到美颜按钮=')
            return False
        else:
            logging.info('=找到美颜按钮=')
            return True

    def Test_X005(self):
        logging.info('=判断是否创建成功=')
        try:
            self.driver.find_element(*self.test_expect005)
        except NoSuchElementException:
            logging.info('=未创建成功=')
            return False
        else:
            logging.info('=创建成功=')
            return True

    def Test_X006(self):
        logging.info('=判断是否有观众列表=')
        try:
            self.driver.find_element(*self.test_expect006)
        except NoSuchElementException:
            logging.info('=没有观众列表=')
            return False
        else:
            logging.info('=有观众列表=')
            return True

    def Test_X007(self):
        logging.info('=判断观众列表能否正常滑动=')
        try:
            self.driver.find_element(*self.test_expect007)
        except NoSuchElementException:
            logging.info('=不能正常滑动=')
            return False
        else:
            logging.info('=能正常滑动=')
            return True

    def Test_X009(self):
        logging.info('=判断能否打开观众浮层=')
        try:
            self.driver.find_element(*self.test_expect009)
        except NoSuchElementException:
            logging.info('=不能打开观众信息浮层=')
            return False
        else:
            logging.info('=能打开观众信息浮层=')
            return True

    def Test_X010(self):
        logging.info('=判断能否打开举报浮层=')
        try:
            self.driver.find_element(*self.test_expect010)
        except NoSuchElementException:
            logging.info('=不能打开举报浮层=')
            return False
        else:
            logging.info('=能打开举报浮层=')
            return True

    def Test_X011(self):
        logging.info('=判断能否进入观众个人主页=')
        try:
            self.driver.find_element(*self.test_expect011)
        except NoSuchElementException:
            logging.info('=不能进入观众个人主页=')
            return False
        else:
            logging.info('=能进入观众个人主页=')
            return True

    def Test_X012(self):
        logging.info('=判断能否有无关注按钮=')
        try:
            self.driver.find_element(*self.test_expect012)
        except NoSuchElementException:
            logging.info('=没有关注按钮=')
            return True
        else:
            logging.info('=有关注按钮=')
            return False

    def Test_X013(self):
        logging.info('=判断是否打开了礼物橱窗=')
        try:
            self.driver.find_element(*self.six_party_one_gift)
        except NoSuchElementException:
            logging.info('=没有打开礼物橱窗=')
            return False
        else:
            logging.info('=打开了礼物橱窗=')
            return True

    def Test_X014(self):
        logging.info('=判断是否成功送礼=')
        try:
            self.driver.find_element(*self.test_expect014)
        except NoSuchElementException:
            logging.info('=没有成功送礼=')
            return False
        else:
            logging.info('=成功送礼=')
            return True

    def Test_X015(self):
        logging.info('=判断是否进入私信小窗=')
        try:
            self.driver.find_element(*self.test_expect015)
        except NoSuchElementException:
            logging.info('=没有进入私信小窗=')
            return False
        else:
            logging.info('=成功进入私信小窗=')
            return True

    def Test_X016(self):
        logging.info('=判断是否返回私信列表=')
        try:
            self.driver.find_element(*self.test_expect016)
        except NoSuchElementException:
            logging.info('=没有返回私信列表=')
            return False
        else:
            logging.info('=成功返回私信列表=')
            return True

    def Test_X017(self):
        logging.info('=判断是否打开个人主页浮层=')
        try:
            self.driver.find_element(*self.test_expect017)
        except NoSuchElementException:
            logging.info('=未打开个人主页浮层=')
            return False
        else:
            logging.info('=成功打开个人主页浮层=')
            return True

    def Test_X018(self):
        logging.info('=判断是否成功关注=')
        try:
            self.driver.find_element(*self.private_letter_more_follow)
        except NoSuchElementException:
            logging.info('=成功关注=')
            return True
        else:
            logging.info('=未成功关注=')
            return False

    def Test_X019(self):
        logging.info('=判断是否成功送礼=')
        try:
            self.driver.find_element(*self.more_message_people_sendgift)
        except NoSuchElementException:
            logging.info('=未成功送礼=')
            return False
        else:
            logging.info('=成功送礼=')
            return True

    def Test_X021(self):
        logging.info('=判断是否展开了折叠区域=')
        try:
            self.driver.find_element(*self.supernatant_message_setting_photo)
        except NoSuchElementException:
            logging.info('=未展开了折叠区域=')
            return False
        else:
            logging.info('=展开了折叠区域=')
            return True

    def Test_X022(self):
        logging.info('=判断是否点击翻译按钮=')
        try:
            self.driver.find_element(*self.supernatant_message_setting_translate)
        except NoSuchElementException:
            logging.info('=未点击了翻译按钮=')
            return False
        else:
            logging.info('=点击翻译按钮=')
            return True

    def Test_X024(self):
        logging.info('=判断是否打开了我的相册=')
        try:
            self.driver.find_element(*self.myphoto_confirm)
        except NoSuchElementException:
            logging.info('=未打开了我的相册=')
            return False
        else:
            logging.info('=打开我的相册=')
            return True

    def Test_X025(self):
        logging.info('=判断是否发送了照片=')
        try:
            self.driver.find_element(*self.test_expect025)
        except NoSuchElementException:
            logging.info('未发送照片=')
            return False
        else:
            logging.info('=发送照片=')
            return True

    def Test_X026(self):
        logging.info('=判断进入了拍照界面=')
        try:
            self.driver.find_element(*self.supernatant_message_setting_photo_confirm)
        except NoSuchElementException:
            logging.info('=未进入了拍照界面=')
            return False
        else:
            logging.info('=进入拍照界面=')
            return True

    def Test_X027(self):
        logging.info('=判断是否发送了拍照照片=')
        try:
            self.driver.find_element(*self.test_expect027)
        except NoSuchElementException:
            logging.info('=未发送了拍照照片=')
            return False
        else:
            logging.info('=发送拍照照片=')
            return True

    def Test_X029(self):
        logging.info('=判断是否发送了文字消息=')
        try:
            self.driver.find_element(*self.test_expect029)
        except NoSuchElementException:
            logging.info('=未发送了文字消息=')
            return False
        else:
            logging.info('=发送文字消息=')
            return True

    def Test_X030(self):
        logging.info('=判断是否发送表情=')
        try:
            self.driver.find_element(*self.test_expect030)
        except NoSuchElementException:
            logging.info('=未发送了表情=')
            return False
        else:
            logging.info('=发送表情=')
            return True

    def Test_X031(self):
        logging.info('=判断是否发出礼物=')
        try:
            self.driver.find_element(*self.test_expect031)
        except NoSuchElementException:
            logging.info('=发出了礼物=')
            return False
        else:
            logging.info('=未发出礼物=')
            return True

    def Test_X032(self):
        logging.info('=判断是否发出图片=')
        try:
            self.driver.find_element(*self.test_expect032)
        except NoSuchElementException:
            logging.info('=未出了图片=')
            return False
        else:
            logging.info('=发出了图片=')
            return True

    def Test_X033(self):
        logging.info('=判断是否发出图片=')
        try:
            self.driver.find_element(*self.test_expect033)
        except NoSuchElementException:
            logging.info('=未发出了图片=')
            return False
        else:
            logging.info('=发出了图片=')
            return True

    def Test_X034(self):
        logging.info('=判断是否发出消息=')
        try:
            self.driver.find_element(*self.test_expect034)
        except NoSuchElementException:
            logging.info('=未发出了消息=')
            return False
        else:
            logging.info('=发出消息=')
            return True

    def Test_X035(self):
        logging.info('=判断是否发出表情=')
        try:
            self.driver.find_element(*self.test_expect035)
        except NoSuchElementException:
            logging.info('=未发出了表情=')
            return False
        else:
            logging.info('=发出表情=')
            return True

    def Test_X036(self):
        logging.info('=判断是否发出语音=')
        try:
            self.driver.find_element(*self.test_expect036)
        except NoSuchElementException:
            logging.info('=未发出了语音=')
            return False
        else:
            logging.info('=发出语音=')
            return True

    def Test_X037(self):
        logging.info('=判断是否不会上麦=')
        try:
            self.driver.find_element(*self.test_expect41)
        except NoSuchElementException:
            logging.info('=没有上麦=')
            return False
        else:
            logging.info('=未判断出是否上麦=')
            return True

    def Test_X038(self):
        logging.info('=判断红包是否发送成功=')
        try:
            self.driver.find_element(*self.supernatant_message_group_packet_get)
        except NoSuchElementException:
            logging.info('=没有发送成功=')
            return False
        else:
            logging.info('=发送成功=')
            return True

    def Test_X039(self):
        logging.info('=判断红包是否领取成功=')
        try:
            self.driver.find_element(*self.test_expect039)
        except NoSuchElementException:
            logging.info('=没有领取成功=')
            return False
        else:
            logging.info('=领取成功=')
            return True

    def Test_X040(self):
        logging.info('=判断是否送礼成功=')
        try:
            self.driver.find_element(*self.test_expect040)
        except NoSuchElementException:
            logging.info('=没有送礼成功=')
            return False
        else:
            logging.info('=送礼成功=')
            return True

    def Test_X041(self):
        logging.info('=判断是否打开了banner=')
        try:
            self.driver.find_element(*self.test_expect041)
        except NoSuchElementException:
            logging.info('=没有打开banner=')
            return False
        else:
            logging.info('=打开了banner=')
            return True

    def Test_X042(self):
        logging.info('=判断是否禁言=')
        try:
            self.driver.find_element(*self.test_expect042)
        except NoSuchElementException:
            logging.info('=没有禁言=')
            return False
        else:
            logging.info('=已禁言=')
            return True

    def Test_X043(self):
        logging.info('=判断是否解禁=')
        try:
            self.driver.find_element(*self.supernatant_unmute)
        except NoSuchElementException:
            logging.info('=没有解禁=')
            return False
        else:
            logging.info('=已解禁=')
            return True

    def Test_X044(self):
        logging.info('=判断是否有@消息=')
        try:
            self.driver.find_element(*self.test_expect044)
        except NoSuchElementException:
            logging.info('=没有@消息=')
            return False
        else:
            logging.info('=有@消息=')
            return True

    def Test_X058(self):
        logging.info('=判断表情是否发送成功=')
        try:
            self.driver.find_element(*self.room_Homeowner_place_emo)
        except NoSuchElementException:
            logging.info('=成功发送表情=')
            return True
        else:
            logging.info('=未成功发送表情=')
            return False

    def Test_X059(self):
        logging.info('=判断是否有开播警示文案=')
        try:
            self.driver.find_element(*self.test_expect059)
        except NoSuchElementException:
            logging.info('=没开播警示文案=')
            return False
        else:
            logging.info('=有开播警示文案=')
            return True

    def Test_006(self):
        logging.info('=判断是否有高收益提示=')
        try:
            self.driver.find_element(*self.test_expect6)
        except NoSuchElementException:
            logging.info('=没高收益提示=')
            return False
        else:
            logging.info('=有高收益提示=')
            return True

    def Test_X060(self):
        logging.info('=判断是否成功发言=')
        try:
            self.driver.find_element(*self.test_expect060)
        except NoSuchElementException:
            logging.info('=未成功发言=')
            return False
        else:
            logging.info('=成功发言=')
            return True

    def Test_109(self):
        logging.info('=判断是否成功发言=')
        try:
            self.driver.find_element(*self.test_expect109)
        except NoSuchElementException:
            logging.info('=未成功发言=')
            return False
        else:
            logging.info('=成功发言=')
            return True

    def Test_X062(self):
        logging.info('=判断是否向上滚动=')
        try:
            self.driver.find_element(*self.test_expect059)
        except NoSuchElementException:
            logging.info('=未向上滚动=')
            return False
        else:
            logging.info('=向上滚动=')
            return True

    def Test_X063(self):
        logging.info('=判断是否向下滚动=')
        try:
            self.driver.find_element(*self.test_expect059)
        except NoSuchElementException:
            logging.info('=向下滚动=')
            return True
        else:
            logging.info('=未向下滚动=')
            return False

    def Test_X066(self):
        logging.info('=判断有无进场特效动=')
        try:
            self.driver.find_element(*self.test_expect066)
        except NoSuchElementException:
            logging.info('=没有进场特效=')
            return False
        else:
            logging.info('=有进场特效=')
            return True

    def Test_X067(self):
        logging.info('=判断有无进场条=')
        try:
            self.driver.find_element(*self.test_expect042)
        except NoSuchElementException:
            logging.info('=没有进场条=')
            return False
        else:
            logging.info('=有进场条=')
            return True

    def Test_X068(self):
        logging.info('=判断是否打开了信息浮层=')
        try:
            self.driver.find_element(*self.test_expect017)
        except NoSuchElementException:
            logging.info('=没有信息浮层=')
            return False
        else:
            logging.info('=有信息浮层=')
            return True


    def Test_X070(self):
        logging.info('=判断是否能给自己送礼=')
        try:
            self.driver.find_element(*self.test_expect070)
        except NoSuchElementException:
            logging.info('=不能给自己送礼=')
            return True
        else:
            logging.info('=能给自己送礼=')
            return False

    def Test_X071(self):
        logging.info('=判断是否成功滑动banner=')
        try:
            self.driver.find_element(*self.test_expect071)
        except NoSuchElementException:
            logging.info('=未成功滑动=')
            return False
        else:
            logging.info('=成功滑动=')
            return True

    def Test_X072(self):
        logging.info('=判断是否打开了banner=')
        try:
            self.driver.find_element(*self.test_expect072)
        except NoSuchElementException:
            logging.info('=未成功打开banner=')
            return False
        else:
            logging.info('=成功打开banner=')
            return True

    def Test_X073(self):
        logging.info('=判断是否滑动了交友房背景列表=')
        try:
            self.driver.find_element(*self.more_Setting_background_Lv20)
        except NoSuchElementException:
            logging.info('=未成功滑动了交友房背景列表=')
            return False
        else:
            logging.info('=成功滑动了交友房背景列表=')
            return True

    def Test_X074(self):
        logging.info('=判断是否更换了交友房封面=')
        try:
            self.driver.find_element(*self.test_expect074)
        except NoSuchElementException:
            logging.info('=未成功更换交友房封面=')
            return True
        else:
            logging.info('=成功更换交友房封面=')
            return False

    def Test_X075(self):
        logging.info('=判断是否打开信息列表=')
        try:
            self.driver.find_element(*self.test_expect016)
        except NoSuchElementException:
            logging.info('=未打开信息列表=')
            return False
        else:
            logging.info('=打开信息列表=')
            return True

    def Test_X078(self):
        logging.info('=判断是否充值成功=')
        try:
            self.driver.find_element(*self.more_top_up_confirm)
        except NoSuchElementException:
            logging.info('=未充值成功=')
            return False
        else:
            logging.info('=充值成功=')
            return True

    def Test_X079(self):
        logging.info('=判断是否开关麦克风=')
        try:
            self.driver.find_element(*self.more_setting_switch_microphone)
        except NoSuchElementException:
            logging.info('=未开关麦克风=')
            return False
        else:
            logging.info('=开关麦克风成功=')
            return True

    def Test_X080(self):
        logging.info('=判断是否下载贴纸=')
        try:
            self.driver.find_element(*self.more_setting_sticker_1download)
        except NoSuchElementException:
            logging.info('=未下载贴纸=')
            return False
        else:
            logging.info('=成功下载贴纸=')
            return True

    def Test_X081(self):
        logging.info('=判断是否清除成功=')
        try:
            self.driver.find_element(*self.more_setting_beauty_reset)
        except NoSuchElementException:
            logging.info('=未清除成功=')
            return False
        else:
            logging.info('=清除成功=')
            return True

    def Test_X082(self):
        logging.info('=判断是否开关镜像=')
        try:
            self.driver.find_element(*self.more_setting_mirror_mode)
        except NoSuchElementException:
            logging.info('=未开关镜像=')
            return False
        else:
            logging.info('=开关镜像成功=')
            return True

    def Test_X083(self):
        logging.info('=判断是否关闭了摄像头=')
        try:
            self.driver.find_element(*self.test_expect083)
        except NoSuchElementException:
            logging.info('=未关闭摄像头=')
            return False
        else:
            logging.info('=关闭了摄像头=')
            return True

    def Test_X084(self):
        logging.info('=判断是否关闭了摄像头=')
        try:
            self.driver.find_element(*self.more_setting_switch_camera)
        except NoSuchElementException:
            logging.info('=未关闭摄像头=')
            return False
        else:
            logging.info('=关闭了摄像头=')
            return True

    def Test_X085(self):
        logging.info('=判断是否关闭了交友房=')
        try:
            self.driver.find_element(*self.test_expect085)
        except NoSuchElementException:
            logging.info('=未关闭交友房=')
            return False
        else:
            logging.info('=关闭了交友房=')
            return True

    def Test_X086(self):
        logging.info('=判断是否进入主播个人主页=')
        try:
            self.driver.find_element(*self.more_setting_switch_camera)
        except NoSuchElementException:
            logging.info('=未进入主播个人主页=')
            return False
        else:
            logging.info('=进入了主播个人主页=')
            return True

    def Test_X087(self):
        logging.info('=判断是否有直播流水=')
        try:
            self.driver.find_element(*self.six_party_endpage_running_account)
        except NoSuchElementException:
            logging.info('=没有直播流水=')
            return False
        else:
            logging.info('=有直播流水=')
            return True

    def Test_X088(self):
        logging.info('=判断交友房Tab是否可以正常上下滑动=')
        try:
            self.driver.find_element(*self.setup_six_party)
        except NoSuchElementException:
            logging.info('=交友房Tab不可以正常上下滑动=')
            return False
        else:
            logging.info('=交友房Tab可以正常上下滑动=')
            return True

    def Test_X089(self):
        logging.info('=判断交友房Tab中房间是否正常显示=')
        try:
            self.driver.find_element(*self.partytab_one_partyroom)
        except NoSuchElementException:
            logging.info('=交友房Tab房间不可正常显示=')
            return False
        else:
            logging.info('=交友房Tab房间可正常显示=')
            return True

    def Test_X090(self):
        logging.info('=判断是否进入交友房=')
        try:
            self.driver.find_element(*self.test_expect090)
        except NoSuchElementException:
            logging.info('=没有进去交友房=')
            return False
        else:
            logging.info('=成功进入交友房=')
            return True

    def Test_X091(self):
        logging.info('=判断是否打开主播信息浮层=')
        try:
            self.driver.find_element(*self.test_expect091)
        except NoSuchElementException:
            logging.info('=没有打开主播信息浮层=')
            return False
        else:
            logging.info('=成功打开主播信息浮层=')
            return True

    def Test_X092(self):
        logging.info('=判断是否关注房主=')
        try:
            self.driver.find_element(*self.six_party_follow_anchor)
        except NoSuchElementException:
            logging.info('=成功关注房主=')
            return True
        else:
            logging.info('=未成功关注房主=')
            return False

    def Test_X093(self):
        logging.info('=判断是否打开举报浮层=')
        try:
            self.driver.find_element(*self.test_expect093)
        except NoSuchElementException:
            logging.info('=没有打开举报浮层=')
            return False
        else:
            logging.info('=成功打开举报浮层=')
            return True

    def Test_X094(self):
        logging.info('=判断是否送礼成功=')
        try:
            self.driver.find_element(*self.test_expect_94)
        except NoSuchElementException:
            logging.info('=没有送礼成功=')
            return False
        else:
            logging.info('=送礼成功=')
            return True

    def Test_X16(self):
        logging.info('=主播端判断是否送礼成功=')
        try:
            self.driver.find_element(*self.test_expect16)
        except NoSuchElementException:
            logging.info('=主播端判断没有送礼成功=')
            return False
        else:
            logging.info('=主播端判断送礼成功=')
            return True

    def Test_X17(self):
        logging.info('=判断是否弹出送礼弹窗=')
        try:
            self.driver.find_element(*self.six_party_send_gift)
        except NoSuchElementException:
            logging.info('=未弹出送礼弹窗=')
            return False
        else:
            logging.info('=弹出送礼弹窗=')
            return True

    def Test_X13(self):
        logging.info('=主播端判断是否送礼成功=')
        try:
            self.driver.find_element(*self.six_message_user)
        except NoSuchElementException:
            logging.info('=主播端判断没有送礼成功=')
            return True
        else:
            logging.info('=主播端判断送礼成功=')
            return False

    def Test_18(self):
        logging.info('=判断是否送礼成功=')
        try:
            self.driver.find_element(*self.test_expect018)
        except NoSuchElementException:
            logging.info('=没有送礼成功=')
            return False
        else:
            logging.info('=送礼成功=')
            return True

    def Test_31(self):
        logging.info('=主播端判断是否送礼成功=')
        try:
            self.driver.find_element(*self.test_expect31)
        except NoSuchElementException:
            logging.info('=没有送礼成功=')
            return True
        else:
            logging.info('=送礼成功=')
            return False

    def Test_X095(self):
        logging.info('=判断是否拨打成功=')
        try:
            self.driver.find_element(*self.anchor_accept_phone)
        except NoSuchElementException:
            logging.info('=没有拨打成功=')
            return False
        else:
            logging.info('=拨打成功=')
            return True

    def Test_X096(self):
        logging.info('=判断是否发送成功=')
        try:
            self.driver.find_element(*self.test_expect096)
        except NoSuchElementException:
            logging.info('=没有发送成功=')
            return False
        else:
            logging.info('=发送成功=')
            return True

    def Test_X097(self):
        logging.info('=判断是否成功跳回交友房=')
        try:
            self.driver.find_element(*self.test_expect097)
        except NoSuchElementException:
            logging.info('=没有成功跳回交友房=')
            return False
        else:
            logging.info('=成功跳回交友房=')
            return True

    def Test_X098(self):
        logging.info('=判断是否打开观众浮层=')
        try:
            self.driver.find_element(*self.six_party_more_people_list_one)
        except NoSuchElementException:
            logging.info('=没有成功打开观众浮层=')
            return False
        else:
            logging.info('=成功打开观众浮层=')
            return True

    def Test_X101(self):
        logging.info('=判断是否打开观众信息浮层=')
        try:
            self.driver.find_element(*self.six_party_supernatant_dynamic)
        except NoSuchElementException:
            logging.info('=没有成功打开观众信息浮层=')
            return False
        else:
            logging.info('=成功打开观众信息浮层=')
            return True

    def Test_X103(self):
        logging.info('=判断是否打开观众个人主页=')
        try:
            self.driver.find_element(*self.test_expect103)
        except NoSuchElementException:
            logging.info('=没有成功打开观众个人主页=')
            return False
        else:
            logging.info('=成功打开观众个人主页=')
            return True

    def Test_X104(self):
        logging.info('=判断信息浮层内有无关注按钮=')
        try:
            self.driver.find_element(*self.six_party_person_homepage_mine)
        except NoSuchElementException:
            logging.info('=成功关注=')
            return True
        else:
            logging.info('=未成功关注=')
            return False

    def Test_X105(self):
        logging.info('=判断有无打开礼物橱窗=')
        try:
            self.driver.find_element(*self.six_party_one_gift)
        except NoSuchElementException:
            logging.info('=未成功打开礼物橱窗=')
            return False
        else:
            logging.info('=成功打开礼物橱窗=')
            return True

    def Test_X106(self):
        logging.info('=判断是否送礼成功=')
        try:
            self.driver.find_element(*self.test_expect106)
        except NoSuchElementException:
            logging.info('=未送礼成功=')
            return False
        else:
            logging.info('=送礼成功=')
            return True

    def Test_X107(self):
        logging.info('=判断@成功=')
        try:
            self.driver.find_element(*self.test_expect107)
        except NoSuchElementException:
            logging.info('=未成功@=')
            return False
        else:
            logging.info('=成功@=')
            return True

    def Test_X116(self):
        logging.info('=判断是否有警告消息成功=')
        try:
            self.driver.find_element(*self.test_expect116)
        except NoSuchElementException:
            logging.info('=没有警告消息=')
            return False
        else:
            logging.info('=有警告消息=')
            return True

    def Test_X117(self):
        logging.info('=判断是否发消息成功=')
        try:
            self.driver.find_element(*self.test_expect117)
        except NoSuchElementException:
            logging.info('=发消息失败=')
            return False
        else:
            logging.info('=发消息成功=')
            return True

    def Test_X118(self):
        logging.info('=判断消息是否在公屏滚动=')
        try:
            self.driver.find_element(*self.test_expect116)
        except NoSuchElementException:
            logging.info('=消息在公屏滚动=')
            return True
        else:
            logging.info('=消息没有在公屏滚动=')
            return False

    def Test_X119(self):
        logging.info('=判断消息是否正常滑动公屏=')
        try:
            self.driver.find_element(*self.test_expect116)
        except NoSuchElementException:
            logging.info('=没有滑动公屏=')
            return False
        else:
            logging.info('=正常滑动公屏=')
            return True

    def Test_X121(self):
        logging.info('=判断消息是否有进场消息=')
        try:
            self.driver.find_element(*self.test_expect094)
        except NoSuchElementException:
            logging.info('=没有进场消息=')
            return False
        else:
            logging.info('=有进场消息=')
            return True

    def Test_X122(self):
        logging.info('=判断消息是否有进场特效=')
        try:
            self.driver.find_element(*self.test_expect122)
        except NoSuchElementException:
            logging.info('=没有进场特效=')
            return False
        else:
            logging.info('=有进场特效=')
            return True

    def Test_X124(self):
        logging.info('=判断是否打开礼物橱窗=')
        try:
            self.driver.find_element(*self.more_message_people_sendgift)
        except NoSuchElementException:
            logging.info('=没有打开礼物橱窗=')
            return False
        else:
            logging.info('=打开礼物橱窗=')
            return True

    def Test_X127(self):
        logging.info('=判断是否送礼成功=')
        try:
            self.driver.find_element(*self.more_message_people_sendgift)
        except NoSuchElementException:
            logging.info('=没有送礼成功=')
            return True
        else:
            logging.info('=送礼成功了=')
            return False

    def Test_X128(self):
        logging.info('=判断是否打开送礼浮层=')
        try:
            self.driver.find_element(*self.six_party_send_gift)
        except NoSuchElementException:
            logging.info('=没有打开送礼浮层=')
            return False
        else:
            logging.info('=送礼成功了打开送礼浮层=')
            return True
    def Test_X133(self):
        logging.info('=判断收礼榜是否为0=')
        try:
            self.driver.find_element(*self.test_expect133)
        except NoSuchElementException:
            logging.info('=收礼榜不为0=')
            return False
        else:
            logging.info('=收礼榜为0=')
            return True

    def Test_X134(self):
        logging.info('=判断收礼榜是否为0=')
        try:
            self.driver.find_element(*self.test_expect133)
        except NoSuchElementException:
            logging.info('=收礼榜不为0=')
            return False
        else:
            logging.info('=收礼榜为0=')
            return True

    def Test_X137(self):
        logging.info('=判断是否打开信息列表=')
        try:
            self.driver.find_element(*self.test_expect016)
        except NoSuchElementException:
            logging.info('=未打开信息列表=')
            return False
        else:
            logging.info('=打开信息列表=')
            return True

    def Test_X138(self):
        logging.info('=判断是否打开了申请弹窗=')
        try:
            self.driver.find_element(*self.six_party_twice_apply)
        except NoSuchElementException:
            logging.info('=未打开申请弹窗=')
            return False
        else:
            logging.info('=打开了申请弹窗=')
            return True

    def Test_X139(self):
        logging.info('=判断是否成为嘉宾=')
        try:
            self.driver.find_element(*self.six_party_guest_enter)
        except NoSuchElementException:
            logging.info('=未成为嘉宾=')
            return False
        else:
            logging.info('=成为了嘉宾=')
            return True
    def Test_44(self):
        logging.info('=房主判断是否申请成功=')
        try:
            self.driver.find_element(*self.test_expect44)
        except NoSuchElementException:
            logging.info('=未申请成功=')
            return True
        else:
            logging.info('=申请成功=')
            return False

    def Test_45(self):
        logging.info('=判断观众是否进入交友房麦位=')
        try:
            self.driver.find_element(*self.test_expect45)
        except NoSuchElementException:
            logging.info('=未进入交友房麦位=')
            return False
        else:
            logging.info('=进入了交友房麦位=')
            return True

    def Test_99(self):
        logging.info('=判断观众是否离开交友房麦位=')
        try:
            self.driver.find_element(*self.test_expect45)
        except NoSuchElementException:
            logging.info('=离开了交友房麦位=')
            return True
        else:
            logging.info('=未离开交友房麦位=')
            return False

    def Test_X140(self):
        logging.info('=判断群聊界面发相册图片=')
        try:
            self.driver.find_element(*self.test_expect140)
        except NoSuchElementException:
            logging.info('=未在群聊界面发相册图片=')
            return False
        else:
            logging.info('=在群聊界面发相册图片=')
            return True

    def Test_X155(self):
        logging.info('=判断是关闭摄像头=')
        try:
            self.driver.find_element(*self.test_expect155)
        except NoSuchElementException:
            logging.info('=未关闭摄像头=')
            return False
        else:
            logging.info('=关闭摄像头=')
            return True

    def Test_X157(self):
        logging.info('=判断有无离开嘉宾位二次确认弹窗=')
        try:
            self.driver.find_element(*self.test_expect157)
        except NoSuchElementException:
            logging.info('=没有二次确认弹窗=')
            return False
        else:
            logging.info('=有二次确认弹窗=')
            return True

    def Test_X158(self):
        logging.info('=判断二次确认弹窗是否消掉=')
        try:
            self.driver.find_element(*self.close_six_party_two_cancle)
        except NoSuchElementException:
            logging.info('=二次确认弹窗消掉=')
            return True
        else:
            logging.info('=二次确认弹窗未消掉=')
            return False

    def Test_X159(self):
        logging.info('=判断是否离开嘉宾位=')
        try:
            self.driver.find_element(*self.test_expect155)
        except NoSuchElementException:
            logging.info('=离开了嘉宾位=')
            return True
        else:
            logging.info('=未离开嘉宾位=')
            return False

    def Test_X162(self):
        logging.info('=判断是否离开交友房=')
        try:
            self.driver.find_element(*self.tab_party)
        except NoSuchElementException:
            logging.info('=未离开交友房=')
            return False
        else:
            logging.info('=离开了交友房=')
            return True
    def Test_X163(self):
        logging.info('=判断进入结束页=')
        try:
            self.driver.find_element(*self.close_end_page)
        except NoSuchElementException:
            logging.info('=未进入结束页=')
            return False
        else:
            logging.info('=进入结束页=')
            return True

    def Test_X165(self):
        logging.info('=判断结束页是否有标题=')
        try:
            self.driver.find_element(*self.close_end_page)
        except NoSuchElementException:
            logging.info('=没有标题=')
            return False
        else:
            logging.info('=有标题=')
            return True

    def Test_X166(self):
        logging.info('=判断结束页是否有派对时长/观众=')
        try:
            self.driver.find_element(*self.close_end_page)
        except NoSuchElementException:
            logging.info('=没有派对时长/观众=')
            return False
        else:
            logging.info('=有派对时长/观众=')
            return True

    def Test_X102(self):
        logging.info('=判断有无交友房消息区提示=')
        try:
            self.driver.find_element(*self.test_expect102)
        except NoSuchElementException:
            logging.info('=没有交友房消息区提示=')
            return False
        else:
            logging.info('=有交友房消息区提示=')
            return True

    def Test_X95(self):
        logging.info('=判断申请列表有无数据=')
        try:
            self.driver.find_element(*self.six_party_agree_list_one)
        except NoSuchElementException:
            logging.info('=申请列表无数据=')
            return False
        else:
            logging.info('=申请列表有数据=')
            return True

    def Test_X96(self):
        logging.info('=判断申请列表有无数据=')
        try:
            self.driver.find_element(*self.six_party_agree_list_one)
        except NoSuchElementException:
            logging.info('=申请列表无数据=')
            return True
        else:
            logging.info('=申请列表有数据=')
            return False

    def Test_103(self):
        logging.info('=判断房主是否发送表情=')
        try:
            self.driver.find_element(*self.six_party_anchor_floating_emo)
        except NoSuchElementException:
            logging.info('=发送表情=')
            return True
        else:
            logging.info('=没有发送表情=')
            return False

    def Test_105(self):
        logging.info('=判断房主是否移除嘉宾=')
        try:
            self.driver.find_element(*self.test_expect105)
        except NoSuchElementException:
            logging.info('=未移除嘉宾=')
            return False
        else:
            logging.info('=已移除嘉宾=')
            return True

    def Test_106(self):
        logging.info('=判断房主是否禁言嘉宾=')
        try:
            self.driver.find_element(*self.test_expect_106)
        except NoSuchElementException:
            logging.info('=未禁言嘉宾=')
            return False
        else:
            logging.info('=已禁言嘉宾=')
            return True

    def Test_107(self):
        logging.info('=判断嘉宾是否被移除麦位=')
        try:
            self.driver.find_element(*self.supernatant_mute)
        except NoSuchElementException:
            logging.info('=嘉宾未被移除麦位=')
            return True
        else:
            logging.info('=嘉宾被移除麦位=')
            return False

    def Test_129(self):
        logging.info('=判断是否进入了交友房=')
        try:
            self.driver.find_element(*self.close_six_party)
        except NoSuchElementException:
            logging.info('=未进入交友房=')
            return False
        else:
            logging.info('=进入了交友房=')
            return True



if __name__ == '__main__':
    driver = anchor_appium_desired()
    S = Live_anchor(driver)
    S.Tab_party()
    S.Setup_party()
    S.Setup_six_party()
    S.Two_Setup()
    S.Room_message_button()
