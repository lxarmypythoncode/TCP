from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("[START]Server is starting...")
print("The server is ready to receive")
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode()
	serverSocket.sendto(('[SERVER]: Pesan diterima, '+ modifiedMessage +'\n').encode(), clientAddress)
	print("message received:")
	print(modifiedMessage)