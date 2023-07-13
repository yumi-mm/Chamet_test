# from Six_party.common.myunittest import StartEnd
# from Six_party.businessView.login_phoneView import LoginView
# import unittest
# import logging
#
#
#
# class TestLogin(StartEnd):
#     csv_file='../data/account.csv'
#
#     # @unittest.skip('skip test_login_One_click_login')
#     def test_login_One_click_login(self):
#         logging.info("===test_login_One_click_login===")
#         l = LoginView(self.driver)
#         l.check_perBtn()
#         l.One_click_login()
#         self.assertIs(l.check_loginStatus(), True)
#
#
#     @unittest.skip('skip test_Guge_login')
#     def test_Guge_login(self):
#         logging.info('===test_Guge_login===')
#         l = LoginView(self.driver)
#         l.check_perBtn()
#         l.more_Btn()
#         l.Guge_Button()
#         l.Goolgle_ID()
#         self.assertIs(l.check_loginStatus(), True)
#
#     # @unittest.skip('skip test_login_error_password_less_6bite')
#     def test_login_error_password_less_123406121212121111(self):
#         logging.info("===test_login_error_password_less_6bite===")
#         l = LoginView(self.driver)
#         data = l.get_csv_data(self.csv_file, 1)
#         l.more_Btn()
#         l.phonenumber_Btn()
#         l.login_input_phonenumber(data[0])
#         self.assertIs(l.login_input_password_or_code(data[1]),False,msg='LOGIN failed........')
#
#     # @unittest.skip('skip test_login_correct_password_4087014')
#     def test_login_correct_password_123407(self):
#         logging.info("===test_login_correct_password_4087014===")
#         l= LoginView(self.driver)
#         data=l.get_csv_data(self.csv_file,2)
#         l.more_Btn()
#         l.phonenumber_Btn()
#         l.login_input_phonenumber(data[0])
#         self.assertIs(l.login_input_password_or_code(data[0]),True,msg='LOGIN failed........')
#
#     # @unittest.skip('skip test_login_wrong_password_4087014')
#     def test_login_wrong_password_123406(self):
#         logging.info("===test_login_wrong_password_4087014===")
#         l= LoginView(self.driver)
#         data=l.get_csv_data(self.csv_file,3)
#         l.more_Btn()
#         l.phonenumber_Btn()
#         l.login_input_phonenumber(data[0])
#         self.assertIs(l.login_input_password_or_code(data[0]),False,msg='LOGIN failed........')
#
#     # @unittest.skip('skip test_login_correct_code_8087050')
#     def test_login_correct_code_1234067979(self):
#         logging.info("===test_login_correct_code_8087050===")
#         l= LoginView(self.driver)
#         data=l.get_csv_data(self.csv_file,4)
#         l.more_Btn()
#         l.phonenumber_Btn()
#         l.login_input_phonenumber(data[0])
#         self.assertIs(l.login_input_password_or_code(data[0]),True,msg='LOGIN failed........')
#
#     def test_login_wrong_code_8087050(self):
#         logging.info("===test_login_correct_code_8087050===")
#         l= LoginView(self.driver)
#         data=l.get_csv_data(self.csv_file,5)
#         l.more_Btn()
#         l.phonenumber_Btn()
#         l.login_input_phonenumber(data[0])
#         self.assertIs(l.login_input_password_or_wrong_code(data[0]),False,msg='LOGIN failed........')
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
#
