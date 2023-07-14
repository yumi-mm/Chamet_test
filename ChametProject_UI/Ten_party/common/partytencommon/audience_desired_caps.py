from appium import webdriver
import yaml
import logging
import logging.config
import os

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../config/partytenconfig/log_conf.py')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()

def audience_appium_desired():
    # with open('C:\Users\pgk bqt\PycharmProjects\github_Chamet\ChametProject_UI\config\partytenconfig\mult_config_audience.py', 'r', encoding='utf-8') as file:
    # with open('C:\\Users\pgk bqt\PycharmProjects\github_Chamet\ChametProject_UI\Ten_party\config\partytenconfig\mult_config_audience.py', 'r', encoding='utf-8') as file:
    audienceconfig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../config/partytenconfig/mult_config_audience.py')
    with open(audienceconfig_path, 'r', encoding='utf-8') as file:
        data=yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    desired_caps2 = {}
    desired_caps2['platformName'] = data['audience_platformName']
    # desired_caps['platformVersion'] = data['audience_platformVersion']
    desired_caps2['deviceName'] = data['audience_deviceName']
    desired_caps2['udid'] = data['audience_udid']
    # 可用于调用apk包的路径
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, 'app', data['audience_appPackage'])

    desired_caps2['appPackage'] = data['audience_appPackage']
    desired_caps2['appActivity'] = data['audience_appActivity']
    desired_caps2['automationName'] = data['audience_automationName']
    desired_caps2['noReset'] = data['audience_noReset']
    desired_caps2['unicodeKeyboard'] = data['audience_unicodeKeyboard']
    desired_caps2['resetKeyboard'] = data['audience_resetKeyboard']
    desired_caps2['newCommandTimeout'] = data['audience_newCommandTimeout']

    logging.info('start app......')
    driver = webdriver.Remote('http://localhost' + ":" + str(data['audience_port']) + '/wd/hub', desired_caps2)
    driver.implicitly_wait(8)
    return driver

if __name__== '__main__':
    audience_appium_desired()
#     验证
#     with open('../config/caps_85phone.yaml.py', 'r', encoding='utf-8') as file:
#         data = yaml.load(file, Loader=yaml.FullLoader)
#     base_dir = os.path.dirname(os.path.dirname(__file__))
#     print(os.path.dirname(__file__))
#     print(base_dir)
#     app_path = os.path.join(base_dir,'app',data['appPackage'])
#     print(app_path)

