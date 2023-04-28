import socket

serverPort = 12000
localIP = "127.0.0.1"

serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
serverSocket.bind((localIP, serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    clientIP = addr[0]
    clientPort = addr[1]


    message = connectionSocket.recv(1024)
    print("Received message from {}:{}".format(clientIP, clientPort))
    capitalizedSentence = message.decode().upper()
    connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()
