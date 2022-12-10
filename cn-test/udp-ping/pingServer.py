"""
    UDP Ping 服务端

"""

import random
from socket import *

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('127.0.0.1', 8899))

while True:
    rand = random.randint(0, 10)
    message, address = server_socket.recvfrom(1024)
    print("接收到报文:", (address, message))

    print("生成随机数:", rand)
    if rand < 3:
        continue
    message = message.upper()
    server_socket.sendto(message, address)


