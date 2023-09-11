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

@allure.story('拨打被叫方收到消息回复（接听）')
class Test_CancelVideoChat(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'anchor')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_CancelVideoChat(self, caseData):
        time.sleep(1)
        user_type = 'anchor'
        allLogin(user_type)
        # 从文件中读取sid值
        with open('sid.pkl', 'rb') as f:
            sid = pickle.load(f)
            print('\nsid:{}'.format(sid))
        # 使用sid进行后续操作
        caseData['data']['sid'] = sid
        returnValue = requestnoresult(caseData)

        # 断言用户已取消
        assert returnValue['msg'] == "The user cancelled"


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_074_reqVideoGetReceivedOver.py'])
