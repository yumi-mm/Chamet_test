# -*- coding: utf-8 -*-

from appium import webdriver
import yaml
import logging
import logging.config
import os

# log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../config/log_conf.py')
# logging.config.fileConfig(log_file_path)
logging = logging.getLogger()

def man_appium_desired():
    # with open('C:\\Users\pgk bqt\PycharmProjects\github_Chamet\ChametProject_UI\config\partytenconfig\mult_config_anchor.py', 'r', encoding='utf-8') as file:
    # with open('C:\\Users\pgk bqt\PycharmProjects\github_Chamet\ChametProject_UI\Ten_party\config\partytenconfig\mult_config_anchor.py', 'r', encoding='utf-8') as file:
    anchorconfig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../config/multi_mapage_config/multi_mypage_man114.py')
    with open(anchorconfig_path, 'r', encoding='utf-8') as file:
        data=yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    desired_caps1 = {}
    desired_caps1['platformName'] = data['man_platformName']
    desired_caps1['platformVersion'] = data['man_platformVersion']
    desired_caps1['deviceName'] = data['man_deviceName']
    desired_caps1['udid'] = data['man_udid']
    # 可用于调用apk包的路径
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, 'app', data['anchor_appPackage'])

    desired_caps1['appPackage'] = data['man_appPackage']
    desired_caps1['appActivity'] = data['man_appActivity']
    desired_caps1['automationName'] = data['man_automationName']
    desired_caps1['noReset'] = data['man_noReset']
    desired_caps1['unicodeKeyboard'] = data['man_unicodeKeyboard']
    desired_caps1['resetKeyboard'] = data['man_resetKeyboard']
    desired_caps1['newCommandTimeout'] = data['man_newCommandTimeout']

    logging.info('start app......')
    driver = webdriver.Remote('http://localhost' + ":" + str(data['man_port']) + '/wd/hub', desired_caps1)
    driver.implicitly_wait(8)
    return driver

if __name__== '__main__':
    man_appium_desired()
#     验证
#     with open('../config/caps_85phone.yaml.py', 'r', encoding='utf-8') as file:
#         data = yaml.load(file, Loader=yaml.FullLoader)
#     base_dir = os.path.dirname(os.path.dirname(__file__))
#     print(os.path.dirname(__file__))
#     print(base_dir)
#     app_path = os.path.join(base_dir,'app',data['appPackage'])
#     print(app_path)