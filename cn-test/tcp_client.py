from socket import *

server_name = 'localhost'
server_port = 13000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

sentence = input('input lowercase sentence: ')
client_socket.send(sentence.encode())

upper_case_sentence = client_socket.recv(1024)
print(upper_case_sentence)

client_socket.close()