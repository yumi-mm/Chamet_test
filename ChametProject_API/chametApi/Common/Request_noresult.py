# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 10:32
# @Author  : whf
# @email: 272445948@qq.com
# @File    : Request.py

import allure
import json
import os
import requests
from chametApi.Common.ChametDESCrypt import ChametDESCrypt
from chametApi.Common.Function import setJsonParam
from chametApi.Common.OperateYaml import readYaml

def requestnoresult(caseData):
    try:
        # 获取请求配置
        fileName = os.path.dirname(__file__)[:-7] + '/ConfigData' + '/Request.yaml'
        requestData = readYaml(fileName)
        # 请求url
        if 'baseUrl' in caseData:
            url = caseData['baseUrl'] + caseData['url']
        else:
            url = requestData['baseUrl'] + caseData['url']
        # 请求方式
        method = caseData['method']
        api = caseData['api']
        apiName = caseData['apiName']
        with allure.step('请求接口'):
            allure.attach(api, '接口')
            allure.attach(apiName, '接口名称')
            allure.attach(url, '请求地址')
            if method == 'get' or method == 'delete':
                # TODO 这里毛凯璐说项目里面全是post请求方式 故这里参数没做处理
                allure.attach(str(caseData['data']), '请求数据')
                if caseData['data'] == None:
                    response = requests.get(url=url)
                else:
                    response = requests.get(url=url + caseData['data'])
            # post请求
            elif method == 'post' or method == 'patch':
                setJsonParam(caseData)
                data = json.dumps(caseData['data'])
                allure.attach(str(json.dumps(caseData['data'], ensure_ascii=False)), '请求数据')
                if data == None:
                    response = requests.post(url=url)
                else:
                    print("url:{}".format(url))
                    print("data:{}".format(caseData['data']))
                    response = requests.post(url=url, json=caseData['data'])
    except Exception as Error:
        with allure.step('请求接口失败，请检查！'):
            allure.attach(str(Error), '错误信息')
        assert False, '请求接口失败，请检查！'
    else:
        # returnValue_str = response.text
        # returnValue = json.loads(returnValue_str)
        # print(returnValue)
        ciphertext = response.text
        des = ChametDESCrypt('')
        text = des.decrypt(ciphertext)
        returnValue = json.loads(text)
        print('returnValue:{}'.format(returnValue))
        with allure.step('接口返回数据'):
            allure.attach(str(returnValue), '返回数据')
        status_code = response.status_code
        if status_code != 200:
            with allure.step('接口响应码错误，请检查！'):
                allure.attach(str(status_code), '接口响应码')
                assert False, '接口响应码错误，请检查！'
    return returnValue
