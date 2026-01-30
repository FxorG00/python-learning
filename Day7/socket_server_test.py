# 1. 创建 socket 对象（准备开餐厅店）
import socket
socket_server=socket.socket()
# 2. 绑定 address & port （确定店址）
socket_server.bind(("localhost",8888))
# 3. 开始监听（开门迎客）
# 有一个等候区，客人都在那里排队，等待专属服务员
socket_server.listen()
# 4. 接受客户端连接（派一个服务员去接待客人）
conn,address=socket_server.accept()
print(f"接收到了客户端连接，信息{address}")
# accept 是阻塞，如果没有客人，会停在这里
# 5. 接收客户端消息（听客人点单）
# 通过专属对象/服务员 conn 来听这个客人点单
# 数据在 socket 上传输都是使用 Bytes（字节数组）
while True :
    data=conn.recv(1024).decode('UTF-8')
    # recv 也是阻塞方法
    print(f"接收到客户端消息：{data}")
    msg=input('请输入发送给客户端的信息')
    if msg=='退出' :
        break
    # encode：把 str->bytes
    # 6. 向客户端发送回复（通过专属服务员给客人回话）
    conn.send(msg.encode('UTF-8'))
# 7. 关闭连接（送客打烊）
conn.close()
socket_server.close()


