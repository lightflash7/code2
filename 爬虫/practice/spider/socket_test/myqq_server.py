import socket
from collections import defaultdict
import threading
import json

# 维护用户连接
online_users = defaultdict(dict)
# 维护用户历史信息
user_message = defaultdict(list)
# 开启sock
server = socket.socket()
server.bind(('0.0.0.0', 16000))
server.listen()


def handle_sock(sock, addr):
    while True:
        data_recv = sock.recv(1024)
        json_like_data = json.loads(data_recv.decode("utf8"))
        action = json_like_data.get('action', '')
        if action == 'login':
            online_users[json_like_data['user']] = sock
            sock.send("登录成功!".encode("utf8"))
        elif action == "list_user":  # 获取当前在线用户
            all_users = [user for user, sock in online_users.items()]
            sock.send(json.dumps(all_users).encode("utf8"))
        elif action == 'history_msg':  # 发送用户历史信息
            user_want_msg = user_message.get(json_like_data["user"], "")
            sock.send(json.dumps(user_want_msg).encode("utf8"))
        elif action == "send_msg":  # 发送数据到对应的用户
            to_whom = json_like_data["to"]
            if to_whom in online_users:
                online_users[to_whom].send(data_recv)
            user_message[to_whom].append(json_like_data)
        elif action == "exit":
            del online_users[json_like_data['user']]
            break         #记得break，一定要跳出while循环使得进程结束，不然进程还调用刚刚的sock就报错了
            # sock.send("您已退出！".encode("utf8"))


while True:
    sock, addr = server.accept()
    server_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    server_thread.start()
