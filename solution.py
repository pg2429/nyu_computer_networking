# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(('127.0.0.1', port))
  #Fill in start

  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket, '127.0.0.1:13331/helloworld.html' #Fill in start      #Fill in end
    try:

      try:
        message = addr #Fill in start    #Fill in end
        filename = message.split('/')[1]
        f = open(filename[0:])
        outputdata = f.read()
        outputdata = 'HTTP/1.1 200 OK\r\n'+ outputdata

        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        response = 'HTTP/1.1 404 Page not found\r\n'
        connectionSocket.send(response.encode())
        connectionSocket.close()

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
  # webServer(8080)
