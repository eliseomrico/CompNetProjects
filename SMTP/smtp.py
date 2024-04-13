from socket import *
import ssl
import base64
import sys


def get_server_response(error_code,clientSocket):
    recv = clientSocket.recv(1024).decode()
    if recv[:3] != str(error_code):
        print(f'{error_code} reply not received from server.')
        print(f'--> Received Error Code: {recv[:3]} instead')
        print(recv)
        sys.exit (0)
    print(f'Server responded successfully: {recv}')
def close_server_connection(clientSocket):
    clientSocket.sendall('QUIT\r\n'.encode())
    get_server_response(221,clientSocket)
    clientSocket.close()

def main():

    server_address = "smtp.gmail.com"
    sender_email="eliseomrico@gmail.com"
    sender_password = "czzx fmuv prrd smvb"
    server_port = 587


    # Declare and initalize client socket
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((server_address,server_port))
    get_server_response(220,clientSocket)


    # Send HELO command and print server response.
    tlsComman = 'HELO Alice\r\n'
    clientSocket.sendall(tlsComman.encode ())
    get_server_response(250,clientSocket)
    

    # # TSL handshake
    tlsComman = 'STARTTLS \r\n'
    clientSocket.sendall(tlsComman.encode())
    get_server_response(220,clientSocket)
    

    # Wrap client socket for TLS
    context = ssl.create_default_context()
    clientSocket = context.wrap_socket(clientSocket, server_hostname=server_address)


    # Base64 encode the username and password
    encoded_user = base64.b64encode(sender_email.encode()).decode()
    encoded_password = base64.b64encode(sender_password.encode()).decode()


    # Send AUTH LOGIN command with encoded username
    clientSocket.send(f'AUTH LOGIN {encoded_user}\r\n'.encode())
    response = clientSocket.recv(1024).decode()


    # Send encoded password
    clientSocket.send(f'{encoded_password}\r\n'.encode())
    response = clientSocket.recv(1024).decode()
    print(response)
  

    # Send Mail From Command
    clientSocket.sendall(('MAIL FROM: <eliseomrico@gmail.com>\r\n').encode())
    get_server_response(250,clientSocket)


    # Send Recepient to command
    clientSocket.sendall(('RCPT TO: <personal.mr4@gmail.com>\r\n').encode())
    get_server_response(250,clientSocket)


    # Send DATA
    clientSocket.send(('DATA\r\n').encode())
    get_server_response(354,clientSocket) 


    # Subject
    clientSocket.sendall(('Subject: Testing\r\n').encode())


    # Body
    clientSocket.sendall(('\r\nThis is the body of the test email\r\n.\r\n').encode())
    print("Body finished")


    # End Message
    clientSocket.sendall(('\r\n.\r\n').encode())
    print("Message Ended")

    # close_server_connection
    close_server_connection(clientSocket)

if __name__=='__main__':
    main()