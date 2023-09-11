import os
import pytest
from chametApi.Common.OperateYaml import readYaml
from Common.Function import createCaseData
import json
import subprocess

# 整个流程
# 1.拿到所有开启直播间的用例
# 2.遍历开启直播间用例 在循环里面执行main方法 将开启直播间用例当作自定义参数传入main方法
# 3.进入main方法 会先执行前置方法 在前置方法里面拿到main方法传入的自定义参数 开启直播间 （Tips:前置方法在每个main方法运行时 只会执行一次 所以每次循环只会开启一次直播间）
# 4.前置方法执行完后 执行所有用例
# 5. 所有用例执行完后 退出main方法 异步打开allure报告 进入下一次循环 拿到下一个开启直播间的用例 从第三步继续走
# 6.所有循环执行完成 控制台输入close关闭allure报告的java进程 不关闭的话 好像java进程一直在 最好关一下
if __name__ == '__main__':

    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)
    # 获取当前文件所在的目录路径
    current_directory = os.path.dirname(current_file_path)
    # 构建 YAML 文件路径
    yaml_file_path = os.path.join(current_directory, 'openLiveRoom.yaml')
    # 读取开启直播间时需要的参数
    datas = readYaml(yaml_file_path)
    cases = createCaseData(datas, user_type_1='anchor')
    # 所有开启直播间时的用例
    caseDataList = cases['caseDataList']
    # 遍历所有用例
    processes = list()
    i = 0
    try:
        for caseData in caseDataList:
            i += 1
            allurePath = os.path.realpath(os.path.dirname(__file__)) + '/Result/Allure' + str(i)
            pytest.main(
                ['-vs', '--alluredir=%s' % allurePath, '--clean-alluredir', '--openCase=%s' % json.dumps(caseData)])
            # 异步打开报告 不然会阻塞
            process = subprocess.Popen(['allure', 'serve', allurePath])
            processes.append(process)
    finally:
        user_input = input("输入 'close' 关闭allure报告的java进程：")
        i = 0  # 输入错误超过三次 也直接关闭
        while user_input != "close" and i < 3:
            i += 1
            user_input = input("输入 'close' 关闭allure报告的java进程：")
        for process in processes:
            # 将allure报告的java进程关闭 不然会一致占用内存
            process.terminate()
