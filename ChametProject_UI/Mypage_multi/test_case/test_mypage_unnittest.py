from common.my_page_startend import StartEnd
from businessView.my_page import MyPage
import unittest
import logging


class TestMyPage(StartEnd):
    csv_file='../data/account.csv'

    # @unittest.skip('skip test_login_error_password_less_6bite')
    def test_login_error_password_less_6bite(self):
        try:
                logging.info("===test_login_error_password_less_6bite===")
                l = MyPage(self.driver)
                l.tab_Mine_Btn()
                l.vip_Level_right_click()
                assert MyPage.vip_level_level_goback
                logging.info("===yes===")
        except:
                logging.info("===no===")




if __name__ == '__main__':
    unittest.main()



