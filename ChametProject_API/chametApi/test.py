# import requests
# url = 'https://api.ichamet.net/videoChat/checkIsVideoChat'
# # data = {'bizCode': '20230803090352077LV1cd305088224', 'userid': '20113007'}
# data ={"userid":2000004,"touserid":20113007,"type":1,"callType":14,"isUseChatCard":0,"videoType":2}
# response = requests.post(url=url, json=data)
# print(response)
# print(response.text)

path = 'Allure'
for i in range(3):
    for j in [1,2,3]:
        path += str(j)
    print(path)