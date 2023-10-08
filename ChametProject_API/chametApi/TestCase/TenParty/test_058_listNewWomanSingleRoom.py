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

@allure.story('单人直播间新女榜列表')
class Test_ListNewWomanSingleRoom(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'anchor')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_ListNewWomanSingleRoom(self, caseData):
        time.sleep(1)
        user_type = 'anchor'
        allLogin(user_type)
        returnValue = request(caseData)

        # 断言是否推荐榜
        assert returnValue['info']['isRecommendRank'] == 1


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_058_listNewWomanSingleRoom.py'])
