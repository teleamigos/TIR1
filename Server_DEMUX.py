import socket

"""socket"""
IP='127.0.0.1'
PORT=3000

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Descriptor
sock.bind((IP,PORT))
sock.listen(1)


rec=[]
"""Recibe informacion"""
while True:
    print("waiting...")
    connection,client_address=sock.accept()

    while True:
        print("Connecting...")
        data=connection.recv(1024)
        rec.append(int.from_bytes(data,byteorder='little'))
        if not data:
            break
    print(rec)
    print(len(rec))
