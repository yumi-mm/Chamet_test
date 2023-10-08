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

@allure.story('检测用户是否可以免费视频聊（约聊）')
class Test_CheckFreeVChat(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'audience')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_CheckFreeVChat(self, caseData):
        time.sleep(1)
        user_type = 'audience'
        allLogin(user_type)
        returnValue = request(caseData)

        # 断言被拨打用户是否为2000004
        assert returnValue['info'][0]['touserid'] == 2000004

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_072_1_checkFreeVChat.py'])
