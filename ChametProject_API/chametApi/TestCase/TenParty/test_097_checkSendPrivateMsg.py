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

@allure.story('校验是否可以发送私聊消息')
class Test_CheckSendPrivateMsg(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'audience')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_CheckSendPrivateMsg(self, caseData):
        time.sleep(1)
        user_type = 'audience'
        allLogin(user_type)
        returnValue = request(caseData)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_097_checkSendPrivateMsg.py'])
