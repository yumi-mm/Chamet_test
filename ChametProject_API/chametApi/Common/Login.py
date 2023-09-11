# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 14:00
# @Author  : whf
# @email: 272445948@qq.com
# @File    : Login.py
import json
import os
import requests
from chametApi.Common.ChametDESCrypt import ChametDESCrypt
from chametApi.Common.OperateYaml import readYaml



def login(url, userid, mobile, identification, password):
    passwordLoginUrl = url + '/pub/passwordLogin'
    tokenLoginUrl = url + '/pub/login/tokenLogin'
    # 登录参数
    data = {'userid': userid,
            'mobile': mobile,
            'identification': identification,
            'password': password}
    # 密码登录请求
    res = requests.post(url=passwordLoginUrl, json=data)
    ciphertext = res.text
    des = ChametDESCrypt('')
    text = des.decrypt(ciphertext)
    js = json.loads(text)
    if res.status_code != 200 or js['msg'] != 'success':
        assert False, '密码登录失败，请检查！'
    info = js['info']
    loginToken = info['loginToken']
    uId = info['userid']
    data = {'userid': uId,
            'loginToken': loginToken,
            'identification': identification
            }
    res = requests.post(url=tokenLoginUrl, json=data)
    if res.status_code != 200:
        assert False, '统一登录失败，请检查！'
    # 统一登录接口返回的密文
    ciphertext = res.text
    # print(ciphertext)
    des = ChametDESCrypt('')
    text = des.decrypt(ciphertext)
    js = json.loads(text)
    if js['msg'] != 'success':
        assert False, '统一登录失败，请检查！'
    info = js['info']
    sk = info['sessionKey']
    sessionKey = {'userid': userid,
                  'appsign': sk
                  }
    # sessionKey = {'userid': userid}
    return sessionKey

def allLogin(user_type):
    num_1 = ''
    num_2 = ''
    if user_type == 'anchor':
        num_1,num_2 = 0,1
    else:
        num_1,num_2 = 1,2
    fileName = os.path.dirname(__file__)[:-7] + '/ConfigData' + '/User.yaml'
    users_info = readYaml(fileName)
    users = dict(list(users_info.items())[num_1:num_2])
    fileName = os.path.dirname(__file__)[:-7] + '/ConfigData' + '/Request.yaml'
    requestData = readYaml(fileName)
    loginUrl = requestData['baseUrl']
    global sessionDict
    sessionDict = {}
    for user in users.keys():
        userData = users[user]
        userid = userData['userid']
        mobile = userData['mobile']
        identification = userData['identification']
        password = userData['password']
        session = login(loginUrl, userid, mobile, identification, password)
        # Constans.addSessionDict(user, session)
        sessionDict[user] = session

def getSessionDict():
    return sessionDict

# def getSessionDict():
#     return Constans.sessionDict
