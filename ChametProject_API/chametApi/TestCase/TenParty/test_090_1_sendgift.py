import time
import allure
import os
import pytest
from chametApi.Common.Function import createCaseData
from chametApi.Common.OperateYaml import readYaml
from chametApi.Common.Request_noresult import requestnoresult
import yaml
import pickle
from chametApi.Common.Login import allLogin

@allure.story('送礼接口（观众送房主，余额不足）')
class Test_Sendgift(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'audience')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_Sendgift(self, caseData):
        time.sleep(1)
        user_type = 'audience'
        allLogin(user_type)
        # 从文件中读取bizCode值
        with open('bizCode.pkl', 'rb') as f:
            bizCode = pickle.load(f)
            print('\nbizCode:{}'.format(bizCode))
        # 使用bizCode进行后续操作
        caseData['data']['bizCode'] = bizCode
        returnValue = requestnoresult(caseData)

        # 断言余额不足请先充值
        assert returnValue['msg'] == "Insufficient balance, please top up first."

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_090_1_sendgift.py'])
