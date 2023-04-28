import socket

serverAddressPort = ("127.0.0.1", 20001)

#Read server address and port
inputServerAddressPort = tuple(input("Host/IP Port [Default: localhost 20001]: ").split())
if inputServerAddressPort:
    print("teste")
    serverAddressPort = inputServerAddressPort
while 1:
    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    #Read the message
    msgFromClient = input("Digite uma mensagem: ")

    #Encode the message
    bytesToSend = str.encode(msgFromClient)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    #Receive message from server
    msgFromServer = UDPClientSocket.recvfrom(1024)

    #Decode and format the response message
    msg = "Message from Server: {}".format(msgFromServer[0].decode())

    print(msg)

    #close the connection
    UDPClientSocket.close()

