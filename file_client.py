import sys
import socket
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
	serverName = sys.argv[1]
	fileName = sys.argv[2]

	print(serverName)
	print(fileName)

	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect((serverName, PORT))
	
	Lib.writeTextTCP(str(fileName), clientSocket)

	fileSize = Lib.getFileSizeTCP(clientSocket)
	if fileSize == 0:
		print('File does not exist')
		clientSocket.close()
	else:
		receiveFile(fileName, clientSocket, fileSize)
		clientSocket.close()

def receiveFile(fileName,  conn, fileSize):
	file = open(Lib.extractFilename(fileName), "w+")

	bytesReceived = 0
	while bytesReceived < fileSize:
		print(bytesReceived)
		received = conn.recv(min(fileSize - bytesReceived,BUFSIZE))
		file.write(received)
		bytesReceived += len(received)
	file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
