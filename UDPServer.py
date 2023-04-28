import socket

localIP = "127.0.0.1"
localPort = 20001

# Create a datagram socket
print("<<Socket created>>")
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ipp
print("<<Socket bind complete>>")
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
# Listen for incoming datagrams
i = 0
while (True):
    i = i + 1
    #receive from client
    bytesAddressPair = UDPServerSocket.recvfrom(1024)

    #unpack the receive to message and address
    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1]

    response = "Message {}: {} #{}".format(address, message, i)
    print(response)

    # Sending a reply to client
    UDPServerSocket.sendto(("your message uppercased: " + message.upper()).encode(), address)

