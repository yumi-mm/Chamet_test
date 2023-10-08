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

@allure.story('拨打视频聊（观众给房主）')
class Test_StartVideoChat(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'audience')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_StartVideoChat(self, caseData):
        time.sleep(5)
        user_type = 'audience'
        allLogin(user_type)
        returnValue = request(caseData)
        sid = returnValue['info']['sid']
        print(sid)
        # 将sid保存到文件中
        with open('sid.pkl', 'wb') as f:
            pickle.dump(sid, f)

        # 断言被拨打用户是否为2000004
        assert returnValue['info']['userid'] == 2000004

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_082_startVideoChat.py'])
