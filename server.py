import matplotlib.pyplot as plt
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
PORT_NUMBER = 5000
SIZE = 1024



hostName = gethostbyname( '0.0.0.0' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
    (data,addr) = mySocket.recvfrom(SIZE)
    x= data.decode('utf-8')
    if x == "send data":
        i=0
        string=[]
        y=[]
        while i<=10000:
            (data,addr) = mySocket.recvfrom(SIZE)
            x= data.decode('utf-8')
            string.append(float(x)/1000)
            i=i+1
            y.append(i)
            print(x)
        plt.plot(y,string)
        plt.xlabel('Time(ms)')
        plt.ylabel('Velocity(km/ms)')
        plt.suptitle('Velocity/Time graph')
        plt.show()
        break
    else:
        print(x)