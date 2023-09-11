# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 10:37
# @Author  : whf
# @email: 272445948@qq.com
# @File    : Function.py
import json
import os
from chametApi.Common.Login import getSessionDict
from chametApi.Common.OperateYaml import readYaml


# 封装用例
def createCaseData(datas,user_type_1):
    try:
        num_1 = ''
        num_2 = ''
        if user_type_1 == 'anchor':
            num_1 = 0
            num_2 = 1
        else:
            num_1 = 1
            num_2 = 2
        # 抛出第一行
        apiData = datas.pop(0)
        caseDataList = []
        caseNameList = []
        cases = {}
        fileName = os.path.dirname(__file__)[:-7] + '/ConfigData' + '/GlobalVariable.yaml'
        users_info = readYaml(fileName)
        users = dict(list(users_info.items())[num_1:num_2])
        for user in users.keys():
            print(user)
            userData = users[user]
            for data in datas:
                caseData = {}
                for key in data.keys():
                    caseData[key] = data[key]
                caseData['api'] = apiData['api']
                caseData['apiName'] = apiData['apiName']
                caseData['method'] = apiData['method']
                caseData['url'] = apiData['url']
                caseData['headers'] = apiData['headers']
                caseData['userid'] = userData['userid']
                caseData['user'] = user
                caseName = user + '：' + caseData['caseName']
                caseDataList.append(caseData)
                caseNameList.append(caseName)
        cases['caseDataList'] = caseDataList
        cases['caseNameList'] = caseNameList
    except Exception as Error:
        assert False, '封装用例数据失败，请检查！错误信息：%s' % Error
    else:
        return cases


def setJsonParam(caseData):
    data = caseData['data']
    sessionDict = getSessionDict()
    sessionKey = sessionDict[caseData['user']]
    for key in sessionKey.keys():
        data[key] = sessionKey[key]
    caseData['data'] = data



