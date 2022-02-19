# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
  serverSocket.bind((HOST, port))
  serverSocket.listen(1)
  #Fill in start

  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
    # conn, addr = s.accept()

    try:

      try:
        message = (connectionSocket.recv(4096)).decode("utf-8")

    # Extract the filename from the given message
        filename = (message.split()[1]).split('/')[1]
        # filename = 'helloworld.html'

        # filename = message.split('/')[1]
        f = open(filename[0:])
        outputdata = f.read()
        outputdata = 'HTTP/1.1 200 OK\r\n'+ outputdata

        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        response = 'HTTP/1.1 404 Not Found\r\n'
        # connectionSocket.send(response.encode())
        # connectionSocket.close()

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
  # webServer(8080)
