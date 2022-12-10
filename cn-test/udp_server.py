

from socket import *

server_port = 12000

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('', server_port))

print("server is ready to receive")

while True:
    message, clientAddress = server_socket.recvfrom(2048)
    input_message = message.decode()
    print("received message is:", input_message)
    modifiedMessage = input_message.upper()
    server_socket.sendto(modifiedMessage.encode(), clientAddress)