import tkinter as tk
import tkinter.messagebox
import sys
import random
from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime
from datetime import timedelta

SERVER_IP = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024
mySocket = socket(AF_INET, SOCK_DGRAM)


class IntroWindow:
    def __init__(self, intro):
        self.intro = intro
        intro.geometry("1920x1080")
        self.frame = tk.Frame(intro)
        self.frame.pack()

        greeting = "    Start the journey of your data."

        photo = tk.PhotoImage(file="rsz_test.gif")

        # self.config = tk.Label(intro, compound=tk.CENTER,
        # text=greeting, font=("Arial", 23), image=photo)
        self.config = tk.Label(intro, compound=tk.CENTER, image=photo)
        self.config.image = photo
        self.config.place(x=370, y=200)

        self.greet = tk.Label(intro, compound=tk.CENTER, text=greeting, font=("Arial", 30))
        self.greet.place(x=500, y=400)

        self.text_btn = tk.Button(intro, text="Get Connected", command=self.connect)
        self.text_btn.place(x=670, y=600)

        self.close_btn = tk.Button(intro, text="Quit", command=intro.quit)
        self.close_btn.place(x=705, y=630)

    def connect(self):
        self.intro.destroy()
        chatting = tk.Tk()
        chatting.title("ChatRoom")
        Chat(chatting)


class Chat:

    def __init__(self, chat):
        self.chat = chat
        chat.geometry("1920x1080")

        self.frame = tk.Frame(chat)

        self.scrollbar1 = tk.Scrollbar(self.frame)
        self.msg_list = tk.Listbox(self.frame, height=40, width=110, yscrollcommand=self.scrollbar1.set)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar1.pack(side=tk.LEFT, fill=tk.Y)

        self.scrollbar2 = tk.Scrollbar(self.frame)
        self.user = tk.Listbox(self.frame, height=40, width=80, yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.pack(side=tk.RIGHT,fill=tk.Y)
        self.user.pack(side=tk.RIGHT)

        self.frame.pack()

        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("Type your messages here.")

        self.entry_win = tk.Entry(chat, textvariable=self.my_msg, width=70)
        self.entry_win.bind("<Return>", self.send)
        self.entry_win.place(x=100, y=700)

        self.send_btn = tk.Button(chat, text="Send", command=self.send)
        self.send_btn.place(x=800, y=700)

        self.msg_list.insert(tk.END, "Successfully connected to server!")
        x = datetime.now()
        self.user.insert(tk.END, x.strftime("%X") + " : Connected to:" + SERVER_IP)

    def send(self):
        msg = self.my_msg.get()
        self.my_msg.set("")

        mySocket.sendto(str(msg).encode('utf-8'), (SERVER_IP, PORT_NUMBER))
        i = 0
        x = []
        if msg == "send data":
            while i < 2500:
                x.append(random.uniform(0, (10000/(i+1))))
                # mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
                mySocket.sendto(str(sum(x)).encode('utf-8'), (SERVER_IP, PORT_NUMBER))
                # mySocket.sendto(str(i).encode('utf-8'),(SERVER_IP,PORT_NUMBER))
                self.msg_list.insert(tk.END, "Velocity:" + str(sum(x)) +" m/ms   Time:" + str(i)+" ms")
                i = i + 1
            
            while 2500 <= i <= 5000:
                x.append(random.uniform(0, (10000/(i+1))))
                # mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
                mySocket.sendto(str(sum(x)).encode('utf-8'), (SERVER_IP, PORT_NUMBER))
                # mySocket.sendto(str(i).encode('utf-8'),(SERVER_IP,PORT_NUMBER))
                self.msg_list.insert(tk.END, "Velocity:" + str(sum(x)) + " m/ms   Time:" + str(i)+" ms")
                i = i + 1
        
            while 5000 <= i <= 10000:
                x.append(random.uniform(0,(10000/(i+1))))
                mySocket.sendto(str(sum(x)).encode('utf-8'), (SERVER_IP, PORT_NUMBER))
                self.msg_list.insert(tk.END, "Velocity:" + str(sum(x)) + " m/ms   Time:" + str(i)+" ms")
                i = i + 1
            while i == 10001:
                x = datetime.now()
                self.user.insert(tk.END,
                                 x.strftime("%X") + " : [1..10000] data have been sent successfully to " + SERVER_IP)
                i = i + 1
        else:
            self.msg_list.insert(tk.END, "ME:  " + msg)
            time = datetime.now()
            self.user.insert(tk.END, time.strftime("%X") + " : Data has been sent successfully to " + SERVER_IP)


intro = tk.Tk()
intro.title("GUI")

introWindow = IntroWindow(intro)

intro.mainloop()