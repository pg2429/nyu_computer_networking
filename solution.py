from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    mailserver = (mailserver,port) #Fill in start #Fill in end
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    recv = clientSocket.recv(1024).decode()

    #print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')
    # else:
    #     print ("THIS IS FINE0")

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)

    # Send MAIL FROM command and handle server response.
    mailFrom = 'MAIL FROM:<pg2429@nyu.edu\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)

    # Send RCPT TO command and handle server response.
    rcptTo = 'RCPT TO:<pg2429@nyu.edu>\r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)

    # Send DATA command and handle server response.
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)

    # Send message data.
    clientSocket.send((msg+endmsg).encode())
    recv5 = clientSocket.recv(1024).decode()
    # print(recv5)


    # Message ends with a single period, send message end and handle server response.
    # clientSocket.send(endmsg.encode())
    # recv6 = clientSocket.recv(1024).decode()
    # print(recv6)

    # Send QUIT command and handle server response.
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv7 = clientSocket.recv(1024).decode()
    # print(recv7)

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
