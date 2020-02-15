# socket服务端
import socket
import threading


server = socket.socket()  # 如果是tcp协议则参数默认，如果是udp协议type=SOCK_DGRAM
server.bind(('0.0.0.0', 16000))  # 绑定到本地0.0.0.0:16000端口
server.listen()


def hand1_sock(sock, addr):  # 打包函数实现多线程的调用
    while True:
        # recv是阻塞的，如果没有收到东西会一直等待，除非没有客户端退出连接了
        data_byte = sock.recv(1024)
        print(data_byte.decode("utf8"))
        http_template = '''HTTP/1. 1 200 OK

<html>
 <head>
  <title>Build A Web Server</title>
 </head>
 <body>
  Hello World
 </body>
</html>

'''
        sock.send(http_template.encode("utf8"))
        break


print('工作中...')
while True:
    sock, addr = server.accept()  # 等待连接(阻塞状态，停在这一行直到有客户端连接)
    client_thread = threading.Thread(target=hand1_sock, args=(sock, addr))
    client_thread.start()

server.close()  # 关闭服务端
