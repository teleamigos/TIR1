import socket
from TDM import*
import time


"""-----------------------------------------------------------------------"""

tdm=TDM()

n=int(input("Ingrese el numero de entradas : "))
tdm.add_sources(n)
for i in range(n):#Ingresa mensajes para N canales
    message=input("Ingrese un mensaje : ")
    tdm.add_msj(message)

#Ingresar sincronizacion
#Ingresar unidad

to_send=tdm.mux()

print(to_send)

"""socket"""

IP='127.0.0.1'
PORT=3000
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Descriptor
sock.connect((IP,PORT))
print("connecting to %s with %s",IP,PORT)
i=0
print(len(to_send))
for bit in to_send:
    #print("...")
    #print(i)
    sock.sendall(bit.to_bytes(1,byteorder="little"))
    time.sleep(0.1)
sock.close()
