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

@allure.story('检测用户是否可视频聊（交友房房主不允许拨打视频聊）')
class Test_CheckIsVideoChat(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'anchor')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_CheckIsVideoChat(self, caseData):
        time.sleep(1)
        user_type = 'anchor'
        allLogin(user_type)
        returnValue = requestnoresult(caseData)

        # 断言交友房房主不允许拨打视频聊
        assert returnValue['msg'] == "Party host are not allowed to make video chat"

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_069_checkIsVideoChat.py'])
