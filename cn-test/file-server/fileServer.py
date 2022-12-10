"""
    文件服务器:
    使用传输层 TCP 协议接收数据,将接收到的数据解析成为HTTP请求体

"""
from socket import *

host_address = 'localhost'
listen_port = 8888

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', listen_port))
server_socket.listen(10)

if __name__ == '__main__':
    print("ready to serve...")
    while True:
        try:
            connection_socket, address = server_socket.accept()
            data = connection_socket.recv(4096)
            if not data:
                continue
            file_name = data.split()[1]
            fid = open(file_name[1:], encoding="utf-8")
            output_data = fid.read()

            header = 'HTTP/1.1 200 OK \r\n\r\n'

            connection_socket.send(header.encode())
            for i in range(0, len(output_data.encode())):
                connection_socket.send(output_data[i].encode())
            connection_socket.close()
        except IOError:
            header = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
            connection_socket.send(header.encode())
            connection_socket.close()
