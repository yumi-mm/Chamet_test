from appium import webdriver
import yaml
import logging
import logging.config
import os


log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../config/partytenconfig/log_conf.py')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()

def appium_desired():
    with open('../../config/partytenconfig/caps_85phone.yaml.py', 'r', encoding='utf-8') as file:
        data=yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    # desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    # 可用于调用apk包的路径
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, 'app', data['appPackage'])

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['automationName'] = data['automationName']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['newCommandTimeout'] = data['newCommandTimeout']

    logging.info('start app......')
    driver = webdriver.Remote('http://localhost' + ":" + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__== '__main__':
    appium_desired()
#     验证
#     with open('../config/caps_85phone.yaml.py', 'r', encoding='utf-8') as file:
#         data = yaml.load(file, Loader=yaml.FullLoader)
#     base_dir = os.path.dirname(os.path.dirname(__file__))
#     print(os.path.dirname(__file__))
#     print(base_dir)
#     app_path = os.path.join(base_dir,'app',data['appPackage'])
#     print(app_path)