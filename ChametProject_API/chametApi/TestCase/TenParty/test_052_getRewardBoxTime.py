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

@allure.story('获取奖励宝箱时间(新版宝箱)')
class Test_GetRewardBoxTime(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'anchor')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_GetRewardBoxTime(self, caseData):
        time.sleep(1)
        user_type = 'anchor'
        allLogin(user_type)
        # 从文件中读取bizCode值
        with open('bizCode.pkl', 'rb') as f:
            bizCode = pickle.load(f)
            print('\nbizCode:{}'.format(bizCode))
        # 使用bizCode进行后续操作
        caseData['data']['bizCode'] = bizCode
        returnValue = request(caseData)
        packetId = returnValue['info']['packetId']
        print(packetId)
        # 将packetId保存到文件中
        with open('packetId.pkl', 'wb') as f:
            pickle.dump(packetId, f)



if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_052_getRewardBoxTime.py'])
