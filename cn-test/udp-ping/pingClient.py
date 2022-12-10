"""
    UDP Ping 客户端

"""
import time
from socket import *

server_name = '127.0.0.1'
server_port = 8899

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)


for i in range(0, 10):
    old_time = time.time()
    send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(old_time))
    message = ('package %d, client_local_time:%s' % (i+1, send_time)).encode()
    try:
        client_socket.sendto(message, (server_name, server_port))
        modifiedMessage, serverAddress = client_socket.recvfrom(1024)

        rtt = time.time() - old_time
        modifiedMessage = modifiedMessage.decode("utf-8")
        print('报文 %d 收到来自 %s 的应答: %s, 往返时延(RTT) = %fs' %(i+1, server_name, modifiedMessage, rtt))
    except Exception as e:
        print("报文 %d: 请求超时" % (i + 1))