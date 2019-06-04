import socket

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:
    pckt = s.recvfrom(65565)
    print(pckt)


