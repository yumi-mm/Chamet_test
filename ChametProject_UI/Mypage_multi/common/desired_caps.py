# coding=utf-8
from appium import webdriver
import yaml
import logging
import logging.config
import os
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), '../config/log_conf.py')
logging.config.fileConfig(log_file_path)
#logging.config.fileConfig('resources/logging.conf')
logging = logging.getLogger()


# CON_LOG='../config/log_conf.py'
# logging.config.fileConfig(CON_LOG)
# logging = logging.getLogger()

'''打开软件并且返回appium的控制对象driver,  encoding='utf-8'在r的后面跟上'''
def appium_desired():
    # with open('../config/caps_85phone.yaml.py','r',encoding='utf-8') as file:
    #     data=yaml.load(file, Loader=yaml.FullLoader)
    with open('D:/chamet_testProject1/config/caps_85phone.yaml.py','r',encoding='utf-8') as file:
        data=yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
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

    # 最新加入的h5页面报错定位器错误或者差找不到元素的修改
    desired_caps["chromeOptions"] = data['chromeOptions']
    desired_caps["showChromedriverLog"] = data['showChromedriverLog']

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