#——————————————————————————-
# Name: UDPPingerServer.py
# Purpose:Lab 2: UDP Pinger
# For: Computer Networks
# Author: Gabriel SB Fernandez
# Created: 4/01/2024
#——————————————————————————-
# UDPPingerServer.py
# We will need the following module to generate randomized lost packets import random
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets

serverSocket = socket(AF_INET, SOCK_DGRAM)	# Assign IP address and port number to socket
serverSocket.bind(('127.0.0.1', 12000))
print("UDP Server Started IP Address: 127.0.01 and Port: 12000")
			
while True:
	
	rand = random.randint(0, 10) # Generate random number in the range of 0 to 10
	message, address = serverSocket.recvfrom(1024) # Receive the client packet along with the address it is coming from
	message = message.upper() # Capitalize the message from the client

	if rand < 4: # If rand is less is than 4, we consider the packet lost and do not respond
		continue
	serverSocket.sendto(message, address) # Otherwise, the server responds
