import os.path
from socket import *

import sys

# 校验代理服务器传参是否指定
if len(sys.argv) <= 1:
    print('Usage: "Python ProxyServer.py server_ip"\n : It is the Ip Address of Proxy Server')
    sys.exit(2)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.listen(10)

while True:
    print("ready to serve...")
    tcp_client_socket, address = tcp_socket.accept()
    print("receive a connection from :", address)
    message = tcp_client_socket.recv(2048).decode()
    print("message:", message)
    if message == '':
        continue

    # 从消息体中提取文件名
    file_name = message.split()[1]
    print('file name is :', file_name)
    file_name = file_name.partition("/")[2]

    file_exist = False
    file_path = "/" + file_name
    try:
        f = open(file_path[1:], "rb")
        output_data = f.readlines()
        file_exist = True
        tcp_client_socket.send("HTTP/1.0 200 OK\r\n")
        tcp_client_socket.send("Content-Type: text/html\r\n")
        tcp_client_socket.send(output_data)
    except IOError:
        # 若文件不存在,则从原服务器获取,并缓存下来
        if not file_exist:
            c = socket(AF_INET, SOCK_STREAM)
            host_name = file_name.replace("www","", 1)
            server_port = 80
            print("hostname is:", host_name)
            try:
                c.connect((host_name, server_port))
                ask_file = ''.join(file_name.partition("/")[1:])
                print("ask_file: ", ask_file)
                file_obj = c.makefile('rwb', 0)
                file_obj.write("GET " + "HTTP://" + file_name + "HTTP/1.0\n\n")

                server_response = file_obj.read()
                file_name = "WEB/" + file_name
                file_split = file_name.split('/')
                for k in range(0, len(file_split) - 1):
                    if not os.path.exists("/".join(file_split[0: k+1])):
                        os.makedirs("/".join(file_split[0:k+1]))
                tmp_file = open(file_name, 'wb')
                print(server_response)
                server_response = server_response.split(b'\r\n\r\n')[1]
                print(server_response)
                tmp_file.close()
                tcp_client_socket.send("HTTP/1.1 200 OK\r\n".encode())
                tcp_client_socket.send("Content-Type:text/html\r\n\r\n".encode())
                tcp_client_socket.send(server_response)
            except:
                print("Illegal Request")
            c.close()
        else:
            print("NET ERROR")
    tcp_client_socket.close()

tcp_socket.close()
