import tkinter as tk
import tkinter.messagebox
import matplotlib.pyplot as plt
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
PORT_NUMBER = 5000
SIZE = 1024



hostName = gethostbyname( '0.0.0.0' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

win = tk.Tk()
win.title = "Server"

class Server:
    def __init__(self, win):
        self.win = win
        win.geometry("1920x1080")
        self.frame = tk.Frame(win)
        self.scrollbar = tk.Scrollbar(self.frame)
        self.msg_list = tk.Listbox(self.frame, height=50, width=150, yscrollcommand=self.scrollbar.set)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.frame.pack()


server = Server(win)
server.msg_list.insert(tk.END, "Test server listening on port {0}\n".format(PORT_NUMBER))
win.update()

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
            server.msg_list.insert(tk.END, "Velocity:" + str(x) + " m/ms   Time:" + str(i)+" ms")
        
        win.update()
        plt.plot(y,string)
        plt.xlabel('Time(ms)')
        plt.ylabel('Velocity(km/ms)')
        plt.suptitle('Velocity/Time graph')
        plt.show()
        break
    else:
        server.msg_list.insert(tk.END, x)
        win.update()
