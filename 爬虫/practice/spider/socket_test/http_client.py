import socket

client=socket.socket()
client.connect(("wwww.baidu.com",80))
client.send('GET / HTTP/1.1\r\n\r\nConnection:close\r\n\r\n'.encode("utf8"))

data=''
while True:
    data_byte=client.recv(1024)
    if data_byte:
        data+=data_byte.decode("utf8")
    else:
        break
print(data)
