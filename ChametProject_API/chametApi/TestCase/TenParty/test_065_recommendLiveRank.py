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

@allure.story('直播间推荐榜单')
class Test_RecommendLiveRank(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'anchor')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_RecommendLiveRank(self, caseData):
        time.sleep(1)
        user_type = 'anchor'
        allLogin(user_type)
        returnValue = request(caseData)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_065_recommendLiveRank.py'])
