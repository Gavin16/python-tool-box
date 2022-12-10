
from socket import *

server_port = 13000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))

server_socket.listen(1)
print('server is ready to connect')

while True:
    connection_socket, address = server_socket.accept()
    sentence = connection_socket.recv(1024).decode()
    print('client ', address , ' sent sentence : ', sentence)
    upper_sentence = sentence.upper()
    connection_socket.send(upper_sentence.encode())
    connection_socket.close()