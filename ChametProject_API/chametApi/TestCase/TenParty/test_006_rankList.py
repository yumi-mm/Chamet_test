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



@allure.story('观众列表')
class Test_RoomPositionInfo(object):
    datas = readYaml(os.path.realpath(__file__)[:-3] + '.yaml')
    cases = createCaseData(datas,user_type_1 = 'anchor')
    caseDataList = cases['caseDataList']
    caseNameList = cases['caseNameList']

    @pytest.mark.parametrize('caseData', caseDataList, ids=caseNameList)
    def test_RankList(self, caseData):
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

        # 获取touserid值
        touserid = returnValue['info']['rankUserResultList'][0]['userId']
        print('touserid:{}'.format(touserid))
        # 将touserid保存到文件中
        with open('touserid.pkl', 'wb') as f:
            pickle.dump(touserid, f)
        # 断言交友房人数是否为2
        assert returnValue['info']['total'] == 2

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_006_rankList.py'])


