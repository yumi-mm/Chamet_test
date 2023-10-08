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

@allure.story('取消拨打')
class Test_CancelVideoChat(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'audience')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_CancelVideoChat(self, caseData):
        time.sleep(1)
        user_type = 'audience'
        allLogin(user_type)
        # 从文件中读取sid值
        with open('sid.pkl', 'rb') as f:
            sid = pickle.load(f)
            print('\nsid:{}'.format(sid))
        # 使用sid进行后续操作
        caseData['data']['sid'] = sid
        returnValue = request(caseData)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_073_cancelVideoChat.py'])
