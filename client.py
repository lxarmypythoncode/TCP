from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
n = int(input('Jumlah anggota kelompok:'));
for i in range(n):
	message = input('Masukkan pesan <Nama dan NIM>:')
	clientSocket.sendto(message.encode(),(serverName,serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print(modifiedMessage.decode())
	
clientSocket.close()