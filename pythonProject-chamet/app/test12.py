import socket

# 创建对象
socket_server=socket.socket()
# 绑定对象到指定ip和地址
socket_server.bind(("localhost",8888))
# 服务端开始监听端口
socket_server.listen(1)
# 接收客户端连接，获得连接对象；coon是客户和服务的链接对象 address是客户端的地址信息
conn,address=socket_server.accept()
print(f"接收到了客户端的链接，客户端的信息是，{address}")
# 客户端连接后，通过recv方法，接收客户端发送的消息
data:str =conn.recv(1024).decode("utf-8")
print(f"客户端发来的消息是：{data}")
# 通过coon（客户端当次连接对象），调用send方法可以回复消息
msg=input("请输入你要跟客户端回复的消息：").encode("utf-8")
conn.send(msg)
# coon（客户端当次连接对象）和socket.socket对象调用close方法，关闭连接
conn.close()
socket_server.close()