# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 20:12
# @Author  : whf
# @email: 272445948@qq.com
# @File    : yaml.py
import yaml


# 读取yaml数据
def readYaml(fileName):
    with open(fileName, 'r', encoding='utf8') as file:
        data = yaml.load(stream=file, Loader=yaml.FullLoader)
        return data


# 写入yaml数据
def writeYaml(fileName, data):
    with open(fileName, 'a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)


# 清空yaml数据
def clearYaml(fileName):
    with open(fileName, 'r+') as f:
        f.truncate()
