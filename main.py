#
# import utime
# import network
# try:
#     import usocket as socket
# except:
#     import socket
def claPI():
    N = 1000000
    sum = 0.00000
    getInitTimes = utime.ticks_ms()
    for i in range(N+1):
        if(i%2==0):
            # print("i是偶数")
            sum = sum + 1/(2*i+1)
        elif(i%2==1):
            # print("i是奇数")
            sum = sum - 1/(2*i+1)
        # print(i)
    print("waste:"+str(-getInitTimes + utime.ticks_ms())+"ms")
    print(sum*4)
#
# def fact(N):
#     if(N==0):
#         return 1
#     elif(N!=0):
#         return N*fact(N-1)
#
#
# def socketConnet(use_stream=False):
#     s = socket.socket()
#
#     ai = socket.getaddrinfo("www.baidu.com", 80)
#     print("Address infos:", ai)
#     addr = ai[0][-1]
#     print("Connect address:", addr)
#     s.connect(addr)
#
#     if use_stream:
#         # MicroPython socket objects support stream (aka file) interface
#         # directly, but the line below is needed for CPython.
#         s = s.makefile("rwb", 0)
#         s.write(b"GET / HTTP/1.0\r\n\r\n")
#         print(s.read())
#     else:
#         s.send(b"GET / HTTP/1.0\r\n\r\n")
#         print(s.recv(4096))
#
#     s.close()
# if __name__ == '__main__':
#     sta_if = network.WLAN(network.STA_IF)
#     sta_if.active(True)
#     sta_if.connect("M", "12345678")
#     socketConnet(True)

import network
import socket
import time
port=10086
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("M", "12345678")
while(wlan.isconnected() == False):
    time.sleep(1)
ip = wlan.ifconfig()[0]
print(ip)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip,port))
print('waiting....')
while True:
    data,addr=s.recvfrom(1024)
    s.sendto(data,addr)
    print('received:',data,'from',addr)
