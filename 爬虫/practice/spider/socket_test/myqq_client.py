import socket
import json
import threading

exit = False

client = socket.socket()
client.connect(("127.0.0.1", 16000))

# 1登录
user = "bobby1"

login_template = {
    "action": "login",
    "user": user
}

client.send(json.dumps(login_template).encode("utf8"))
res = client.recv(1024)
print(res.decode("utf8"))

# 2获取在线用户
get_user_template = {
    "action": "list_user"
}
client.send(json.dumps(get_user_template).encode("utf8"))
res = client.recv(1024)
print("在线用户有:{}".format(res.decode("utf8")))

# 3获取历史消息
offline_msg_template = {
    "action": "history_msg",
    "user": user
}
client.send(json.dumps(offline_msg_template).encode("utf8"))
res = client.recv(1024)
print("历史消息:{}".format(res.decode("utf8")))


# 交互
def jiaohu():
    while True:
        op_type = input("请输入你要进行的操作:1.发送消息，2.退出，3.获取在线用户")
        if op_type not in ["1", "2", "3"]:
            print("不支持这种操作！")
        elif op_type == "1":
            user_sent_to = input("要发给谁")
            msg = input("输入您要发送的消息:")
            send_message_template = {
                "action": "send_msg",
                "to": user_sent_to,
                "from": user,
                "data": msg
            }
            client.send(json.dumps(send_message_template).encode("utf8"))
        elif op_type == "2":
            exit_template = {
                "action": "exit",
                "user": user
            }
            client.send(json.dumps(exit_template).encode("utf8"))
            exit = True
            client.close()
            break
        elif op_type == "3":
            get_user_template = {
                "action": "list_user"
            }
            client.send(json.dumps(get_user_template).encode("utf8"))
            # res = client.recv(1024)
            # print("在线用户有:{}".format(res.decode("utf8")))


# 接收函数
def receive():
    while True:
        if exit:
            break
        else:
            try:
                data = client.recv(1024).decode("utf8")
            except:
                break
            try:
                data_json = json.loads(data)
                user_from = data_json["from"]
                msg = data_json["data"]
                print('')
                print("收到来自{}的一条消息：{}".format(user_from, msg))
            except:
                print('')
                print(data)


if __name__ == '__main__':
    send_thread = threading.Thread(target=jiaohu)
    receive_thread = threading.Thread(target=receive)
    send_thread.start()
    receive_thread.start()
