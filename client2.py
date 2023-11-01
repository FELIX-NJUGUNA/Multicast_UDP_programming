import socket
import struct

cast_grp = '224.1.1.1'
cast_port = 15000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


sock.bind(('', cast_port))
mreq = struct.pack("4sl", socket.inet_aton(cast_grp), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print(sock.recv(1024))

