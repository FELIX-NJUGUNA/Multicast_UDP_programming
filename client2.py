import socket
import struct

cast_grp = socket.gethostbyname('224.1.1.1')
cast_port = 15000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the multicast group and port
sock.bind(('', cast_port))

# Joins the multicast group
mreq = struct.pack("4sl", socket.inet_aton(cast_grp), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Make the socket non-blocking
sock.setblocking(True)

# Disable loopback for the multicast group
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 0)

while True:
    # creates a datagram packet and sends over the socket
    try:
        data, addr = sock.recvfrom(1024)
    except socket.error:
        # No data available to receive
        continue

    # Decode the received data
    msg = data.decode()

    # Print the received message
    print(f"{addr}:{msg}")
    break

# Close the socket
sock.close()
