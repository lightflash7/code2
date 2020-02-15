# socket服务端
import socket
import threading

server = socket.socket()  # 如果是tcp协议则参数默认，如果是udp协议type=SOCK_DGRAM
server.bind(('0.0.0.0', 16000))  # 绑定到本地0.0.0.0:16000端口
server.listen()


def hand1_sock(sock, addr):  # 打包函数实现多线程的调用
    print('连接成功')
    data = ''
    while True:
        # recv是阻塞的，如果没有收到东西会一直等待，除非没有客户端退出连接了
        data_byte = sock.recv(1024)
        if data_byte:
            data = data + data_byte.decode("utf8")
        else:
            break        #记得break，一定要跳出while循环使得进程结束，不然进程还调用刚刚的sock就报错了
        if data.endswith("#"):  # 如果收到的data以#结尾则打印data并清空
            print(data[:-1])
            data = ''
    print('客户端连接断开')


print('等待连接...')
while True:
    sock, addr = server.accept()  # 等待连接(阻塞状态，停在这一行直到有客户端连接)
    sock.send('您与服务器连接成功'.encode("utf8"))
    client_thread = threading.Thread(target=hand1_sock, args=(sock, addr))
    client_thread.start()

server.close()  # 关闭服务端
