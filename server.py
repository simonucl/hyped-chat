import matplotlib.pyplot as plt 
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( '127.0.0.1' )

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
        while i<100:
            (data,addr) = mySocket.recvfrom(SIZE)
            x= data.decode('utf-8')
            string.append(float(x))
            i=i+1
            y.append(i)
        print(string)
        print(y)
        plt.plot(string,y)
        plt.show()
        break
    else:
        print(x)