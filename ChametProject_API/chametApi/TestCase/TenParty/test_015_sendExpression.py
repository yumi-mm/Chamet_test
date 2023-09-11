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

@allure.story('发送交友房-麦位表情（主播端）')
class Test_SendExpression(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'audience')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_SendExpression(self, caseData):
        time.sleep(1)
        user_type = 'audience'
        allLogin(user_type)
        # 从文件中读取bizCode值
        with open('bizCode.pkl', 'rb') as f:
            bizCode = pickle.load(f)
            print('\nbizCode:{}'.format(bizCode))
        # 使用bizCode进行后续操作
        caseData['data']['bizCode'] = bizCode
        returnValue = request(caseData)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_015_sendExpression.py'])