import socket
socket_client=socket.socket()
socket_client.connect(('localhost',8888))
while True :
    msg=input('请输入你给服务端发送的内容：\n')
    if msg=='exit' :
        break
    socket_client.send(msg.encode('UTF-8'))
    data=socket_client.recv(1024).decode('UTF-8')
    print(f"收到服务端消息：{data}")
socket_client.close()