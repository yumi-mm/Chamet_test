# import pytest
# from chametApi.TestCase.TenPartyAllowawaylucky28.AutomatedTask import run_scheduled_task
# from chametApi.Common.Login import allLogin
# import allure
# import os
# import pytest
# import schedule
# import time
# from functools import partial
# from chametApi.Common.Function import createCaseData
# from chametApi.Common.Request import request
# import pickle
# from chametApi.Common.OperateYaml import readYaml
# from chametApi.Common.Login import allLogin

# class AutomatedTask:
#     @staticmethod
#     def AnchorimHeartbeat(self, caseData):
#         time.sleep(1)
#         user_type = 'anchor'
#         allLogin(user_type)
#         # 从文件中读取bizCode值
#         with open('bizCode.pkl', 'rb') as f:
#             bizCode = pickle.load(f)
#             print('\nbizCode:{}'.format(bizCode))
#         # 使用bizCode进行后续操作
#         caseData['data']['body'] = caseData['data']['body'].replace("'bizCode':null", f"'bizCode':'{bizCode}'")
#         print('\ncaseData:{}'.format(caseData))
#         returnValue = request(caseData)
#         print("Running scheduled API task anchor")
#
#     @staticmethod
#     def AudienceimHeartbeat(self, caseData):
#         time.sleep(1)
#         user_type = 'audience'
#         allLogin(user_type)
#         # 从文件中读取bizCode值
#         with open('bizCode.pkl', 'rb') as f:
#             bizCode = pickle.load(f)
#             print('\nbizCode:{}'.format(bizCode))
#         # 使用bizCode进行后续操作
#         caseData['data']['body'] = caseData['data']['body'].replace("'bizCode':null", f"'bizCode':'{bizCode}'")
#         print('\ncaseData:{}'.format(caseData))
#         returnValue = request(caseData)
#         print("Running scheduled API task audience")
#
#     datas_1 = readYaml(
#         r'C:\Users\pgk bqt\PycharmProjects\chametApi\chametApi\TestCase\TenPartyAllowawaylucky28\AutomatedTaskAnchor.yaml')
#     cases_1 = createCaseData(datas_1, user_type_1='anchor')
#     caseDataList_1 = cases_1['caseDataList']
#     caseNameList_1 = cases_1['caseNameList']
#
#     def run_anchor_task(self):
#         for caseData in self.caseDataList_1:
#             self.AnchorimHeartbeat(self, caseData)
#             time.sleep(3)
#
#     datas_2 = readYaml(
#         r'C:\Users\pgk bqt\PycharmProjects\chametApi\chametApi\TestCase\TenPartyAllowawaylucky28\AutomatedTaskAudience.yaml')
#     cases_2 = createCaseData(datas_2, user_type_1='audience')
#     caseDataList_2 = cases_2['caseDataList']
#     caseNameList_2 = cases_2['caseNameList']
#
#     def run_audience_task(self):
#         for caseData in self.caseDataList_2:
#             self.AudienceimHeartbeat(self, caseData)
#             time.sleep(3)
#
# # 创建一个pytest的fixture，在测试前运行定时任务
# @pytest.fixture(autouse=True)
# def run_scheduled_task_before_test():
#     automatedtask = AutomatedTask()
#
#     # 每3秒执行一次定时任务，调用静态方法
#     for caseData in automatedtask.caseDataList_1:
#         func = partial(automatedtask.AnchorimHeartbeat, automatedtask, caseData)
#         schedule.every(3).seconds.do(func)
#     for caseData in automatedtask.caseDataList_2:
#         func = partial(automatedtask.AudienceimHeartbeat, automatedtask, caseData)
#         schedule.every(3).seconds.do(func)
#
#     # 执行定时任务
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# @pytest.fixture(scope='session', autouse=True)
# def start(user_type):
#     allLogin(user_type)
# # 创建一个pytest的fixture，在测试前运行定时任务
# @pytest.fixture(autouse=True)
# def run_scheduled_task_before_test():
#     # 启动定时任务
#     run_scheduled_task()


import pytest
from chametApi.Common.Login import allLogin
import pickle
import chametApi.Common.Request

@pytest.fixture(scope='session', autouse=True)
def start(request):
    # 通过request获取--openCase的值
    openCase = request.config.getoption("--openCase")
    allLogin('anchor')
    caseData = eval(openCase)
    returnValue = chametApi.Common.Request.request(caseData)
    bizCode = returnValue['info']['bizCode']
    roomId = returnValue['info']['roomId']
    print(roomId)
    # 将bizCode保存到文件中
    with open('bizCode.pkl', 'wb') as f:
        pickle.dump(bizCode, f)
    # 将roomId保存到文件中
    with open('roomId.pkl', 'wb') as f:
        pickle.dump(roomId, f)

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')

'''
1.注册pytest命令项--openCase
2.注册完后使用命令执行用例pytest --openCase=xxx就能被pytest给识别到。
'''
def pytest_addoption(parser):
    parser.addoption("--openCase",action="store",default="{'caseName': '开启10人交友房,语音房&普通房&允许被带走', 'data': {'isAllowBeTaken': 1, 'beTakenLimitLevel': 1, 'avType': 2, 'gameType': 0}, 'api': 'POST /openLiveRoom', 'apiName': '开启10人交友房', 'method': 'post', 'url': '/live/openLiveRoom', 'headers': 0, 'userid': '2000004', 'user': 'A_primary'}",help="开启直播间用例信息")
