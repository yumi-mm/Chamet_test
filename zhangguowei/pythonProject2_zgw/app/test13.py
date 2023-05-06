# import socket
#
# # 创建对象
# socket_client=socket.socket()
# # 连接到服务端
# socket_client.connect(("localhost",8888))
# # 发送消息
# while True:
#     send_msg=input("请输入要发送的消息")
#     if send_msg=='exit':
#         break
#     socket_client.send(send_msg.encode('utf-8'))
# while True:
#     send_msg=input("请输入要发送的消息".encode('utf-8'))
#     socket_client.send(send_msg)
#     recv_data=socket_client.recv(1024)
#     print("服务端消息为：",recv_data.decode("utf-8"))
#
# #  socket_client对象调用close方法，关闭连接
# socket_client.close()
import json

# import requests
# # -*- coding:utf-8 -*-
# class Socket_q:
#     def request_get_correct_code(self, area, message):
#         self.area = area
#         self.message = message
#         url = 'https://api.ichamet.net/test/getSmsCode'
#         para = {"mobile": "2000004"}
#         response = requests.get(url, params=para)
#         # re=response.json
#
#         print(response,response.text,type(response))
#         # print(json.dumps(response))
#
# if __name__ == '__main__':
#     com=Socket_q()

import requests
class Socket_q:
    def request_get_correct_code(self, area, message):
        self.area = area
        self.message = message
        s=requests.Session
        url = 'https://api.ichamet.net/test/getSmsCode'
        para = {"mobile": "2000004"}
        response = requests.get(url, params=para)
        # re=response.json

        print(response,response.text,type(response))
        # print(json.dumps(response))

if __name__ == '__main__':
    com=Socket_q()
    com.request_get_correct_code(86,1886810)