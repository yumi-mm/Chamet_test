# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 15:45
# @Author  : whf
# @email: 272445948@qq.com
# @File    : test_100_closeLiveRoom.py
import time

import allure
import os
import pytest
from chametApi.Common.Function import createCaseData
from chametApi.Common.OperateYaml import readYaml
from chametApi.Common.Request import request
import yaml
import pickle
from chametApi.Common.Login import allLogin



@allure.story('关闭直播间（主动关闭）')
class Test_CloseLiveRoom(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'anchor')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_CloseLiveRoom(self, caseData):
        time.sleep(1)
        user_type = 'anchor'
        allLogin(user_type)
        # 从文件中读取bizCode值
        with open('bizCode.pkl', 'rb') as f:
            bizCode = pickle.load(f)
            print('\nbizCode:{}'.format(bizCode))
        # 使用bizCode进行后续操作
        caseData['data']['bizCode'] = bizCode
        bizCode, returnValue = request(caseData)

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_100_closeLiveRoom.py'])


