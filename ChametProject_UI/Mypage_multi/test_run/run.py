import sys

path = 'D:\\chamet_testProject1\\'

sys.path.append(path)
import unittest
from BSTestRunner import BSTestRunner
import time, logging

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + ' test_report.html'
report_name = report_name.encode()

with open(report_name, 'w', encoding='utf-8') as f:
    runner = BSTestRunner(stream=f, title='Chamet Test Report', description='Chamet Android app Test Report')
    logging.info('start run testcase.....')
    runner.run(discover)
