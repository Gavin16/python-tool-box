from socket import *



'''
    UDP 客户端程序
'''
if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    message = input('Input lower case sentence:')

    clientSocket.sendto(message.encode(), (serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    clientSocket.close()
