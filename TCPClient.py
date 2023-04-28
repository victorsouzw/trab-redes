from socket import *
serverAddressPort = ("127.0.0.1", 12000)

#Read server address and port
inputServerAddressPort = tuple(input("Host/IP Port [Default: localhost 20001]: ").split())
if inputServerAddressPort:
    print("teste")
    serverAddressPort = inputServerAddressPort
i = 0
while 1:
    # Create a TCP socket at client side
    clientSocket = socket(AF_INET, SOCK_STREAM)

    #Connect to TCPServer
    clientSocket.connect(serverAddressPort)

    #Read the message
    msgFromClient = input("Message to send: ")

    #Send the message
    clientSocket.send(msgFromClient.encode())

    #Receive message from server
    modifiedSentence = clientSocket.recv(1024)
    print("From Server #{}: {}".format(i, modifiedSentence.decode()))

    #close the connection
    clientSocket.close()
    i = i + 1