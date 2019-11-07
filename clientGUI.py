import tkinter as tk
import tkinter.messagebox
import sys
import random
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024
mySocket = socket( AF_INET, SOCK_DGRAM )

class IntroWindow:
    def __init__(self, intro):
        self.intro = intro
        intro.geometry("1920x720")
        self.frame = tk.Frame(intro)
        self.frame.pack()


        greeting = "         Hi, there!I am the client.\nHow's it going?\n      Let's Chat!\n"


        photo = tk.PhotoImage(file="rsz_test.gif")

        #self.config = tk.Label(intro, compound=tk.CENTER,
                               #text=greeting, font=("Arial", 23), image=photo)
        self.config = tk.Label(intro, compound=tk.CENTER, image=photo)                       
        self.config.image = photo
        self.config.place(x=570, y=200)

        self.greet = tk.Label(intro, compound=tk.CENTER, text=greeting, font=("Arial",30))
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
        chat.geometry("700x400")

        self.frame = tk.Frame(chat)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.msg_list = tk.Listbox(self.frame, height=20, width=60, yscrollcommand=self.scrollbar.set)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.user = tk.Listbox(self.frame, height=20, width=20)
        self.user.pack(side=tk.RIGHT)

        self.frame.pack()

        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("Type your messages here.")

        self.entry_win = tk.Entry(chat, textvariable=self.my_msg, width=70)
        self.entry_win.bind("<Return>", self.send)
        self.entry_win.place(x=18, y=350)

        self.send_btn = tk.Button(chat, text="Send", command=self.send)
        self.send_btn.place(x=620, y=350)

    def send(self):
        msg = self.my_msg.get()
        self.my_msg.set("")
        self.msg_list.insert(tk.END, "ME:  "+msg)
        mySocket.sendto(str(msg).encode('utf-8'),(SERVER_IP,PORT_NUMBER))
        i = 0
        x=[]
        if msg == "send data" :
            while i < 500:
                x.append(random.uniform(0,1))
    # mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
                mySocket.sendto(str(sum(x)).encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    # mySocket.sendto(str(i).encode('utf-8'),(SERVER_IP,PORT_NUMBER))
                self.msg_list.insert(tk.END, "Velocity:"+str(sum(x))+"   Time:"+str(i))
                i = i + 1
            while 500<=i<=1000:
                x.append(random.uniform(0,10))
                mySocket.sendto(str(sum(x)).encode('utf-8'),(SERVER_IP,PORT_NUMBER))
                self.msg_list.insert(tk.END, "Velocity:"+str(sum(x))+"   Time:"+str(i))
                i = i+1


intro = tk.Tk()
intro.title("GUI")

introWindow = IntroWindow(intro)

intro.mainloop()
