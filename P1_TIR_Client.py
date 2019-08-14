import socket

"""TXTable"""

def TXTable(Frame):
    file_out=open("frame_sent.txt",'a')
    print(Frame)
    for slot in Frame:
        file_out.write(slot)
    file_out.close()

"""Main"""
to_send=[]
frame=[]
n=int(input("Ingrese el numero de entradas : "))
len_max=1
for i in range(n):#Ingresa mensajes para N canales
    message=input("Ingrese un mensaje : ")
    to_send.append(message)
    if len(message)>len_max:
        len_max=len(message)#longitud del mensaje mas largo

for i in range(len_max):
    """Parte el mensaje"""
    for message in to_send:
        if i >= len(message):
            #Agrega espacio
            frame.append(" ")
        else:
            frame.append(message[i])

    frame.append("--sync--")
    """Genera archivo TXT"""
    TXTable(frame)

    """Borra el frame actual"""
    for j in range(n+1):
        frame.pop()

"""Envia archivo a treves del socket"""

"""socket"""

IP='127.0.0.1'
PORT=3000
file_to_send=open("frame_sent.txt",'r')#open file
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Descriptor
sock.connect((IP,PORT))
print("connecting to %s with %s",IP,PORT)
