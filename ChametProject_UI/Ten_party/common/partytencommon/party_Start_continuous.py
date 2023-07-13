from common.partytencommon.desired_caps import appium_desired
from common.partytencommon.party_ten import PartyTen
import logging


class party_Start_End_continuous:
    def setup_class(self):
        logging.info('===setUp===')
        self.driver=appium_desired()
        self.driver.implicitly_wait(5)
        self.partyten = PartyTen(self.driver)
        self.partyten.login_account()
        self.partyten.sign_in()
        self.partyten.party_tab_Btn()

    def teardown_class(self):
        logging.info('===tearDown===')
        print("end")
        self.driver.quit()
        # sleep(5)
        # n = PartyTen(self.driver)
        # n.quit_account()

    # def setup_method(self):
    #     logging.info('===启动app===')
    #     self.driver=appium_desired()
    #     self.driver.implicitly_wait(10)
    #     self.partytencommon = PartyTen(self.driver)
    #     self.partytencommon.party_tab_Btn()


    # def teardown_method(self):
    #     self.driver.quit()


