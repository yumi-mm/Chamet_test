from common.partytencommon.anchor_desired_caps import anchor_appium_desired
from common.partytencommon.audience_desired_caps import audience_appium_desired
from common.partytencommon.multparty_ten_anchor import Multanchor
from common.partytencommon.multparty_ten_audience import Multaudience
import logging
from time import sleep

class anchorparty_Start_End:
    def setup_class(self):
        logging.info('===主播端启动app===')
        self.anchordriver=anchor_appium_desired()
        self.anchordriver.implicitly_wait(10)
        self.multanchor = Multanchor(self.anchordriver)
        self.multanchor.anchor_sign_in()
        sleep(5)
        logging.info('===观众端启动app===')
        self.audiencedriver=audience_appium_desired()
        self.audiencedriver.implicitly_wait(10)
        self.multaudience = Multaudience(self.audiencedriver)
        self.multaudience.audience_sign_in()

# class anchorparty_Start_End:
    # def setup_class(self):
    #     logging.info('===setUp===')
    #     self.anchordriver=anchor_appium_desired()
    #     self.anchordriver.implicitly_wait(5)
    #     self.multanchor = Multanchor(self.anchordriver)
    #     self.multanchor.login_account('1839174','1839174')
    #     self.multanchor.sign_in()
    #
    # def teardown_class(self):
    #     logging.info('===tearDown===')
    #     print("end")
    #     self.anchordriver.quit()

    # def setup_method(self):
    #     logging.info('===启动app===')
    #     self.anchordriver=anchor_appium_desired()
    #     self.anchordriver.implicitly_wait(10)
    #     self.multanchor = Multanchor(self.anchordriver)
    #     self.multanchor.party_tab_Btn()

    # def teardown_method(self):
    #     self.anchordriver.quit()

    # def setup_class(self):
    #     logging.info('===主播端启动app===')
    #     self.anchordriver=anchor_appium_desired()
    #     self.anchordriver.implicitly_wait(10)
    #     self.multanchor = Multanchor(self.anchordriver)
    #     self.multanchor.party_tab_Btn()


# class audienceeparty_Start_End:
    # def setup_class(self):
    #     logging.info('===setUp===')
    #     self.audiencedriver=audience_appium_desired()
    #     self.audiencedriver.implicitly_wait(5)
    #     self.multaudience = Multaudience(self.audiencedriver)
    #     self.multaudience.login_account('1839172','1839172')
    #     self.multaudience.sign_in()
    #
    # def teardown_class(self):
    #     logging.info('===tearDown===')
    #     print("end")
    #     self.audiencedriver.quit()

    # def setup_method(self):
    #     logging.info('===启动app===')
    #     self.audiencedriver=audience_appium_desired()
    #     self.audiencedriver.implicitly_wait(10)
    #     self.multaudience = Multaudience(self.audiencedriver)
    #     self.multaudience.party_tab_Btn()

    # def teardown_method(self):
    #     self.audiencedriver.quit()

    # def setup_class(self):
    #     logging.info('===启动app===')
    #     self.audiencedriver=audience_appium_desired()
    #     self.audiencedriver.implicitly_wait(10)
    #     self.multaudience = Multaudience(self.audiencedriver)
    #     self.multaudience.party_tab_Btn()