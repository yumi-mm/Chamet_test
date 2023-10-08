# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 17:45
# @Author  : whf
# @email: 272445948@qq.com
# @File    : Constans.py
sessionDict = {}

def getSessionDict():
    return sessionDict

def addSessionDict(key, value):
    sessionDict[key] = value