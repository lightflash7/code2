# socket客户端
import socket

client = socket.socket()
client.connect(('192.168.0.126', 16000))

# 接收服务器连接成功的消息
data_get = client.recv(1024)
print(data_get.decode("utf8"))

# 发送信息
while True:
    data_tosent = input('请输入要发送的内容(输入#结尾表示一句话发送完，输入exit退出):')
    if data_tosent == 'exit':
        break
    client.send(data_tosent.encode("utf8"))

client.close()
