# -*- coding: utf-8 -*-

from appium import webdriver
import yaml
import logging
import logging.config
import os

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../config/log_conf.py')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()

def woman_appium_desired():
    # with open('C:\\Users\pgk bqt\PycharmProjects\github_Chamet\ChametProject_UI\config\partytenconfig\mult_config_anchor.py', 'r', encoding='utf-8') as file:
    # with open('C:\\Users\pgk bqt\PycharmProjects\github_Chamet\ChametProject_UI\Ten_party\config\partytenconfig\mult_config_anchor.py', 'r', encoding='utf-8') as file:
    anchorconfig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../config/multi_mapage_config/multi_mypage_woman85.py')
    with open(anchorconfig_path, 'r', encoding='utf-8') as file:
        data=yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    desired_caps2= {}
    desired_caps2['platformName'] = data['woman_platformName']
    desired_caps2['platformVersion'] = data['woman_platformVersion']
    desired_caps2['deviceName'] = data['woman_deviceName']
    desired_caps2['udid'] = data['woman_udid']
    # 可用于调用apk包的路径
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, 'app', data['anchor_appPackage'])

    desired_caps2['appPackage'] = data['woman_appPackage']
    desired_caps2['appActivity'] = data['woman_appActivity']
    desired_caps2['automationName'] = data['woman_automationName']
    desired_caps2['noReset'] = data['woman_noReset']
    desired_caps2['unicodeKeyboard'] = data['woman_unicodeKeyboard']
    desired_caps2['resetKeyboard'] = data['woman_resetKeyboard']
    desired_caps2['newCommandTimeout'] = data['woman_newCommandTimeout']

    logging.info('start app......')
    driver = webdriver.Remote('http://localhost' + ":" + str(data['woman_port']) + '/wd/hub', desired_caps2)
    driver.implicitly_wait(8)
    return driver

if __name__== '__main__':
    woman_appium_desired()
#     验证
#     with open('../config/caps_85phone.yaml.py', 'r', encoding='utf-8') as file:
#         data = yaml.load(file, Loader=yaml.FullLoader)
#     base_dir = os.path.dirname(os.path.dirname(__file__))
#     print(os.path.dirname(__file__))
#     print(base_dir)
#     app_path = os.path.join(base_dir,'app',data['appPackage'])
#     print(app_path)