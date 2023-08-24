from common.login_unittest import StartEnd
from businessView.login_phoneView import LoginView
import unittest
import logging



class TestLogin(StartEnd):
    csv_file='../data/account.csv'

    @unittest.skip('skip test_login_error_password_less_6bite')
    def test_login_error_password_less_6bite(self):
        logging.info("===test_login_error_password_less_6bite===")
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.more_Btn()
        l.phonenumber_Btn()
        l.login_input_phonenumber(data[0])
        self.assertIs(l.login_input_password_or_code(data[1]),True,msg='LOGIN failed........')

    # @unittest.skip('skip test_login_correct_password_4087014')
    def test_login_correct_password_4087014(self):
        logging.info("===test_login_correct_password_4087014===")
        l= LoginView(self.driver)
        data=l.get_csv_data(self.csv_file,2)
        l.more_Btn()
        l.phonenumber_Btn()
        l.login_input_phonenumber(data[0])
        self.assertIs(l.login_input_password_or_code(data[1]),True,msg='LOGIN failed........')

    @unittest.skip('skip test_login_wrong_password_4087014')
    def test_login_wrong_password_4087014(self):
        logging.info("===test_login_wrong_password_4087014===")
        l= LoginView(self.driver)
        data=l.get_csv_data(self.csv_file,3)
        l.more_Btn()
        l.phonenumber_Btn()
        l.login_input_phonenumber(data[0])
        self.assertIs(l.login_input_password_or_code(data[1]),True,msg='LOGIN failed........')

    @unittest.skip('skip test_login_correct_code_8087050')
    def test_login_correct_code_8087050(self):
        logging.info("===test_login_correct_code_8087050===")
        l= LoginView(self.driver)
        data=l.get_csv_data(self.csv_file,4)
        l.more_Btn()
        l.phonenumber_Btn()
        l.login_input_phonenumber(data[0])
        self.assertIs(l.login_input_password_or_code(data[1]),True,msg='LOGIN failed........')


if __name__ == '__main__':
    unittest.main()



