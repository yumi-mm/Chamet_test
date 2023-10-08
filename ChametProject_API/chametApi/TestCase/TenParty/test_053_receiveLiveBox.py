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

@allure.story('直播间宝箱领取接口')
class Test_ReceiveLiveBox(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'anchor')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_ReceiveLiveBox(self, caseData):
        time.sleep(1)
        user_type = 'anchor'
        allLogin(user_type)
        # 从文件中读取bizCode值
        with open('bizCode.pkl', 'rb') as f:
            bizCode = pickle.load(f)
            print('\nbizCode:{}'.format(bizCode))
        # 从文件中读取packetId值
        with open('packetId.pkl', 'rb') as f:
            packetId = pickle.load(f)
            print('\npacketId:{}'.format(packetId))
        # 使用bizCode进行后续操作
        caseData['data']['bizCode'] = bizCode
        # 使用packetId进行后续操作
        caseData['data']['packetId'] = packetId
        returnValue = request(caseData)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_053_receiveLiveBox.py'])
