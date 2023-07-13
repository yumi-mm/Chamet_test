from common.partytencommon.desired_caps import appium_desired
from common.partytencommon.party_ten_audience import PartyTenaudience
import logging


class partyaudiencecontinuous_Start_End:
    def setup_class(self):
        logging.info('===setUp===')
        self.driver=appium_desired()
        self.driver.implicitly_wait(5)
        self.partyten = PartyTenaudience(self.driver)
        self.partyten.audience_login_account()
        self.partyten.audience_sign_in()
        # self.partytencommon.auself.partyten.audience_sign_in()dience_party_tab_Btn()

    def teardown_class(self):
        logging.info('===tearDown===')
        print("end")
        self.driver.quit()
    #     sleep(5)
    #     n = PartyTen(self.driver)
    #     n.quit_account()

    # def setup_method(self):
    #     logging.info('===启动app===')
    #     self.driver=appium_desired()
    #     self.driver.implicitly_wait(10)
    #     self.partytencommon = PartyTenaudience(self.driver)
    #
    #
    # def teardown_method(self):
    #     self.driver.quit()


