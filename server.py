import socket

group = '224.1.1.1'
port = 15000


# for all packets sent, after two hops on the network the packet will not be re-sent/broadcast
ttl = 2

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Make the socket non-blocking
sock.setblocking(True)

# Set the multicast TTL
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Get input from the user
input_msg = input("Enter your message: ")

# Sends the packet/message
sock.sendto(input_msg.encode(), (group, port))

sock.close()

