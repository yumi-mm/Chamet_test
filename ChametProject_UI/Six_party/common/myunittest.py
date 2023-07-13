import unittest
from ChametProject_UI.Six_party.businessView.six_party_anchor import Six_partyView_anchor
from ChametProject_UI.Six_party.businessView.six_party_spectator import Six_partyView_spectator
from ChametProject_UI.Six_party.common.desired_caps_anchor import anchor_appium_desired
from ChametProject_UI.Six_party.common.desired_caps_spectatpr import spectator_appium_desired
import logging
from ChametProject_UI.Six_party.common.common_fun import Common

class StartEnd(Common,unittest.TestCase):
    def setup_class(self):
        logging.info('===主播端启动app===')
        self.anchordriver = anchor_appium_desired()
        self.multanchor = Six_partyView_anchor(self.anchordriver)
        logging.info('===观众端启动app===')
        self.audiencedriver = spectator_appium_desired()
        self.multspectator = Six_partyView_spectator(self.audiencedriver)

# from common.desired_caps import appium_desired
# from businessView.six_party import Six_partyView
# import logging
# import pytest
# from time import sleep
#
# class StartEnd(unittest.TestCase):
#     def setup_class(self):
#         logging.info('===setUp===')
#         self.driver=appium_desired()
#
#     def teardown_class(self):
#         logging.info('===tearDown===')
#         print("end")
#         self.driver.quit()