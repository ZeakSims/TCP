#!/bin/usr/python
import sys
import socket
import pickle
a={1:6,2:4}
b=a
sys.argv[1]=b
file=open("l.pickle","wb")
pickle.dump(l,file)
file=open("l.pickle","rb")
data=pickle.load(file)
x=data[1]+data[2]
y=str(x)
soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((socket.gethostname(),1233))
soc.listen(5)
while True:
	clientsocket, address=soc.accept()
	print("Connected "+str(address))
	clientsocket.send(bytes(N))
	clientsocket.close()
