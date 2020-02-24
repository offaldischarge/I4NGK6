import sys
import socket
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind((HOST, PORT))
	serverSocket.listen(1)
	print('The server is ready to receive')
	
	while (True):
		(clientSocket, addr) = serverSocket.accept()
		filenameRequest = Lib.readTextTCP(clientSocket)
		filename = Lib.extractFilename(filenameRequest)
		fileSize = Lib.check_File_Exists(filename)
		
		if fileSize == 0:
			Lib.writeTextTCP(str(fileSize), clientSocket)
			clientSocket.close()
			print('File does not exist')
		else:
			Lib.writeTextTCP(str(fileSize), clientSocket)
			sendFile(filename, fileSize, clientSocket)
			clientSocket.close()
			print('Sent filesize to client')

	serverSocket.close()


def sendFile(fileName,  fileSize,  conn):
	file =  open(fileName, "rb")
	
	sentBytes = 0
	while sentBytes < fileSize:
		print(sentBytes)
		chunk = file.read(BUFSIZE)
		conn.send(chunk)
		sentBytes += len(chunk)
	file.close()
    
if __name__ == "__main__":
   main(sys.argv[1:])
