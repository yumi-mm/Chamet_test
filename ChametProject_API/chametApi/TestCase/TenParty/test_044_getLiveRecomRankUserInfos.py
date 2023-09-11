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

@allure.story('获取指定房间的单人直播间卡片页信息')
class Test_GetLiveRecomRankUserInfos(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'audience')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_GetLiveRecomRankUserInfos(self, caseData):
        time.sleep(1)
        user_type = 'audience'
        allLogin(user_type)
        # 从文件中读取bizCode值
        with open('roomId.pkl', 'rb') as f:
            roomId = pickle.load(f)
            print('\nroomId:{}'.format(roomId))
        # 使用bizCode进行后续操作
        caseData['data']['roomIdList'] = roomId
        returnValue = request(caseData)

        # 断言卡片页主播是否正确
        assert returnValue['info'][0]['ownerId'] == 2000004

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_044_getLiveRecomRankUserInfos.py'])
