from tkinter import *
from tqdm import tqdm
from time import sleep
import colorama
from colorama import Fore, Style
import socket
import subprocess
import time
from tkinter import messagebox
import sys
import os

def scanner1():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = entry444.get()
    startport = int(startport1.get())
    endport = int(endport1.get())

    def scan(port):
        try:
            server.connect((host , port))
            time.sleep(0.3)
            return True
        except:
            return False

    for x in range(startport , endport):
        if scan(x):
            print('port ' , x ,' is open')
        else:
            print('port ' , x ,' is closed')
    close()


def scanner():

    global winscreen6
    global endport1
    global startport1
    global entry444
    winscreen6 = Toplevel(win)
    winscreen6.geometry('400x200')
    winscreen6.title('0rbit sc4nn3r')

    lable333 = Label(winscreen6 , text='Host :')
    lable333.place(x = 80 , y = 60)
    entry444 = Entry(winscreen6)
    entry444.place(x = 120 , y = 60)

    lable313 = Label(winscreen6 , text='S-port:')
    lable313.place(x = 75 , y = 80)
    startport1 = Entry(winscreen6)
    startport1.place(x = 120 , y = 80)

    lable323 = Label(winscreen6 , text='E-port:')
    lable323.place(x = 75 , y = 100)
    endport1 = Entry(winscreen6)
    endport1.place(x = 120 , y = 100)
    buto = Button(winscreen6 , text = 'scan ports' , command = scanner1)
    buto.place(x = 150 , y = 120)

def session():

    global client

    host = str(entry11.get())
    port = int(entry22.get())
    socket1 = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    socket1.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
    socket1.bind((host , port))
    socket1.listen(5)

    while True:
        client , address = socket1.accept()
        print(Fore.RED + 'connected to ' + str(address[0]) + ' at port : ' + str(address[1]) + Fore.BLUE)
        while True:
            s = str(input(' >'))
            client.send(s.encode())
            clrecv = client.recv(1024).decode()
            time.sleep(0.5)
            print(clrecv)

    session()

def generator():
    global winscreen1
    global entry6
    global entry4
    winscreen1 = Toplevel(win)
    winscreen1.geometry('400x200')
    winscreen1.title('0rbit s3rv3r')
    lable2 = Label(winscreen1 , text='TH3 ORB1T')
    lable2.place(x = 120 , y = 30)
    lable3 = Label(winscreen1 , text='Host :')
    lable3.place(x = 80 , y = 60)
    entry4 = Entry(winscreen1)
    entry4.place(x = 120 , y = 60)
    lable5 = Label(winscreen1 , text='Port :')
    lable5.place(x = 82 , y = 90)
    entry6 = Entry(winscreen1)
    entry6.place(x = 120 , y = 90)
    button4 = Button(winscreen1 , text = 'Generat' , command = generator1)
    button4.place(x = 80 , y = 160)
    button5 = Button(winscreen1 , text = 'Close' , command = close )
    button5.place(x = 250 , y = 160)

def generator1():
    result = messagebox.askokcancel('' ,'We are sorry this is not avilable for now')
    print(result)
    #file = open('p4y104d.py' , 'a')
    #file.write('host = ' + str(entry4.get()) + '\nport = '+ str(entry6.get()))
    #file.close()

def close():
    print(Fore.BLUE + 'We hope you had a great time ligally ;)')
    sys.exit(Tk)

def server():
    global entry11
    global entry22
    global winscreen
    winscreen = Toplevel(win)
    winscreen.geometry('380x180')
    winscreen.title('0rbit s3rv3r')
    lable22 = Label(winscreen , text='TH3 ORB1T')
    lable22.place(x = 120 , y = 30)
    lable00 = Label(winscreen , text='host :')
    lable00.place(x = 80 , y = 60)
    entry11 = Entry(winscreen)
    entry11.place(x = 120 , y = 60)
    lable11 = Label(winscreen , text='port :')
    lable11.place(x = 80 , y = 90)
    entry22 = Entry(winscreen)
    entry22.place(x = 120 , y = 90)
    button7 = Button(winscreen , text = 'Listen' , command = session )
    button7.place(x = 80 , y = 130)
    button17 = Button(winscreen , text = 'Close' , command = close )
    button17.place(x = 250 , y = 130)


clear = 'clear'
subprocess.call( clear , shell=True )

for i in tqdm(range(10)):
    sleep(0.1)

print(Fore.BLUE + 'Welcome')
win = Tk()
win.geometry('380x200')
win.title('0rbit s3rv3r')

lable1 = Label(win , text='TH3 ORB1T')
lable1.place(x = 120 , y = 30)
button1 = Button(win , text= 'Rootkit generator' , command = generator)
button1.place(x = 120 , y = 60)
button2 = Button(win , text= 'Server' , command = server)
button2.place(x = 120 , y = 90)
button8 = Button(win , text= 'Scanner' , command = scanner)
button8.place(x = 120 , y = 120)
button3 = Button(win , text= 'Exit' , command = close)
button3.place(x = 120 , y = 150)
win.mainloop()
