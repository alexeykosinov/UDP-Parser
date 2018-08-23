"""
initial library
"""
import select
import socket 

Client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Client.bind((' ', 50116))
Client.setblocking(0)

while True:
    Result = select.select([Client],[],[])
    ReceivedMessages = Result[0][0].recv(1024) 
    print ("Угол поворота:", ReceivedMessages.decode())
    