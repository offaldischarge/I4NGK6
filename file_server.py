import sys
import socket
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind((HOST, PORT))
	serverSocket.listen(1)
	print 'The server is ready to receive'
	
	while (True):
		(clientSocket, addr) = serverSocket.accept()
		filenameRequest = Lib.readTextTCP(clientSocket)
		filename = Lib.extractFilename(filenameRequest)
		fileSize = Lib.check_File_Exists(filename)
		if fileSize == 0:
			Lib.writeTextTCP(str(fileSize), clientSocket)
			print 'File does not exist'
		else:
			Lib.writeTextTCP(str(fileSize), clientSocket)
			print 'Sent filesize to client'
		sendFile(filename, fileSize, clientSocket)

def sendFile(fileName,  fileSize,  conn):
	
	totalsent = 0
	while totalsent < BUFSIZE
		sent = conn.send()
    
if __name__ == "__main__":
   main(sys.argv[1:])
