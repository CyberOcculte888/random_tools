#!/usr/bin/python
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.settimeout(1)

param = sys.argv
ip = param[1]
print("Target => ",ip)

def grab(conn):
    banner=''
    try:
        conn.send("\x01".encode())
        conn.settimeout(1)
        banner = conn.recv(1024)
        print("[+] Banner: ",banner)
        return banner
    except Exception as e:
        strerror = e.args
        print("Cannot grab banner")
def write(file,data):
    fh = open (file, 'a')
    fh.write(data)

for port in range(1,1000):
    try :
        #print ("[+] Attempting to connect to 127.0.0.1:"+str(port))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("[+] Port "+str(port)+" open on host "+ip)
        ban = grab(s)
        write("scanlog","TARGET:"+ip+"\tPORT:"+str(port))
        if ban : write("scanlog","\tBANNER:"+str(ban))
        write("scanlog","\n")
        s.close()
    except socket.error as e: 
        strerror = e.args
        #print("Error({0}): ".format(strerror))

