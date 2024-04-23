#——————————————————————————-
# Name: UDPPingerServer.py
# Purpose:Lab 2: UDP Pinger
# For: Computer Networks
# Author: Gabriel SB Fernandez
# Created: 4/01/2024
#——————————————————————————-
# UDPPingerClient.py
import socket
import time # Import time library

while True:
        print("\n Chose an option to run UDP Pinger Client") # User menu to show that program is running
        print("1. Enter any key to ping to UDP server")
        print("2. Enter 0 to end program")

        option = input ("Enter your option: ")
        if option == '0':
            print("Ending program...") #Kills infinte loop of program
            break 

        print("Starting Ping...\n")

        mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP Socket for the client
        serverAddress = ('127.0.0.1', 12000) # Set IP address and Port number of Socket
        mysocket.settimeout(1) # Timeout value of 1 second

        try: # Infinite loop to send messages to the server
             for i in range(1, 11): #Starts at 1 and progresses to 10
                start = time.time() # Start time send message to server
                message = 'Ping ' + str(i) + " " + time.ctime(start) #Ping sequence_number time
                try:
                    sent = mysocket.sendto(message.encode("utf-8"), serverAddress)
                    print("Sent: " + message)
                    data, server = mysocket.recvfrom(4096)  # Maximum data received 4096 bytes
                    print("Received: " + str(data))
                    end = time.time();
                    elapsed = end - start
                    print("Time: " + str(elapsed * 1000) + " Milliseconds\n")
                except socket.timeout:
                    print("#" + str(i) + " Requested timed out\n")
        finally:
            print("Ping finished, closing socket")
            mysocket.close()
