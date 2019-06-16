#!/usr/bin/python
import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((socket.gethostname(),1233))
mssg = s.recv(1024)
print(mssg.decode("utf-8"))
