# -*- coding: utf-8 -*-
from common.mypage_multi.desired_caps_man import man_appium_desired
from common.mypage_multi.desired_caps_woman import woman_appium_desired
from common.mypage_multi.multiMypage_man import MultiMan
from common.mypage_multi.multiMypage_woman import MultiWoman
from common.mypage_multi import mypage_common_fun
import logging
from time import sleep

class mypage_multi_Start_End:
    def setup_class(self):
        logging.info('===男用户端启动app===')
        self.mandriver=man_appium_desired()
        self.mandriver.implicitly_wait(8)
        self.multiman = MultiMan(self.mandriver)
        # self.multanchor.anchor_sign_in()
        # sleep(2)

        logging.info('===女用户端启动app===')
        self.womandriver = woman_appium_desired()
        self.womandriver.implicitly_wait(8)
        self.multiwoman = MultiWoman(self.womandriver)
        # self.multaudience.audience_sign_in()
