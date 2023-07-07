from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import requests
from Six_party.baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    per_btn = (By.ID,'com.lbe.security.miui:id/permission_allow_foreground_only_button')
    # start_btn=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView')




    def check_perBtn(self):
        logging.info('================check_perB=====================')
        try:
            per_btn=self.driver.find_element(*self.per_btn)

        except NoSuchElementException:
            logging.info('no perbtn')
        else:
            per_btn.click()
            logging.info('click already')

    def get_size(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y

    def swipeLeft(self):
        logging.info('================swipeLeft================')
        l=self.get_size()
        x1=int(l[0]*0.9)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.1)
        self.swipe(x1,y1,x2,y1,1000)

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)


    def get_csv_data(self,csv_file,line):
        logging.info('===get_csv_data===')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

    def get_toast_data(self,message):  # 查找toast值
        '''
        method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
        parameter explain：【text】查找的toast值
        Usage:
            device.get_Toast('再按一次退出iBer')
        '''
        # self.message=message
        # logging.info("开始查找toast值---'%s'" % (message))
        try:
            message = '//*[@text=\'{}\']'.format(message)
            ele = WebDriverWait(self.driver, 2, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, message)))
            return ele.get_attribute("text")
            logging.info("成功查找到toast----%s" % message)
        except:
            logging.error("未查找到toast----%s" % message)
            return False

    def request_get_correct_code(self, area, message):
        url='https://api.ichamet.net/test/getSmsCode'
        para={"mobile": str(area)+str(message)}
        print(para)
        resp=requests.get(url, json=para)
        code=resp.text
        return code,resp,para
        # page = Response.encode("utf-8")
        # page_dict = json.loads(page)
        # url_l=url+query
        # page = request.urlopen(url_l).read()  # 结果为byte
        # page = page.decode("utf8")  # byte转str
        # page_dict = json.loads(page)  # str转dict
        # return page_dict
    '''进入h5界面后，获取上下文，并切换至h5'''
    def native_to_h5(self):
        '''Common.native_to_h5(self) 可以直接调用'''
        context = self.driver.contexts
        self.driver.switch_to.context(context[-1])

    '''返回至原生界面后，切换至原生界面'''
    def h5_to_native(self):
        '''Common.h5_to_native(self)  可以直接调用'''
        self.driver.switch_to.context('NATIVE_APP')

if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_perBtn()
    com.getScreenShot('startAPP')


