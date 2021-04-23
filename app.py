#!/usr/bin/python3

import socket
import threading 
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 30000

my_ip = input("Enter your IP address")
s.bind( (my_ip,port) )
dest_ip_name = []
fip= input("\n\tEnter your Friends IP address : ")
dest_ip_name.append(fip)
fname= input("\n\tEnter Friends Name: ")
dest_ip_name.append(fname)


os.system("clear")


print(f"\n\t\t\tConnected to {dest_ip_name[1]}")


def send():
    while True:
        msg=input("\n\t\t\t\t >>>")

        if msg !=  "" :
            fmsg=msg.encode()
            s.sendto(fmsg,(dest_ip_name[0],port))
            if fmsg.decode() == "exit":
                s.sendto("The user is offline...type exit to end the chat or wait till they appear".encode(),(dest_ip_name[0],port))
                os._exit(1)

        else:
             pass

def recv():
    while True:
    
        msg = s.recvfrom(1024)
        recip=msg[1][0]
        if recip == dest_ip_name[0]:
            fname=dest_ip_name[1] 
        if msg[0].decode() == "exit":
            os._exit(1)
        
        print('\n'+ fname +" : " + msg[0].decode() + "\n\t\t\t\t\t\t\t" )


t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()
