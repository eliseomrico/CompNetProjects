#——————————————————————————-
# Name: UDPPingerServer.py & UDPPingerClient.py
# Purpose:Lab 2: UDP Pinger
# For: Computer Networks
# Author: Group 6: Gabriel SB Fernandez
# Created: 4/01/2024
#——————————————————————————-

A UDP Pinger using Python where packet drop rate is simulated to be 30% and client can ping server. The client asks the user to run ping or end program. Once the ping is started it sends 10 pings. The server will randomly capitalize the encapsulated data and send it back to the client.

To run the server: python UDPPingerServer.py
Example server output: 
	UDP Server Started IP Address: 127.0.01 and Port: 12000

to run the client: python UDPPingerClient.py
Example client output:

Chose an option to run UDP Pinger Client
1. Enter any key to ping to UDP server
2. Enter 0 to end program
Enter your option: 1
Starting Ping...

Sent: Ping 1 Tue Apr 23 04:01:32 2024
Received: b'PING 1 TUE APR 23 04:01:32 2024'
Time: 0.5323886871337891 Milliseconds

Sent: Ping 2 Tue Apr 23 04:01:32 2024
Received: b'PING 2 TUE APR 23 04:01:32 2024'
Time: 0.0 Milliseconds

Sent: Ping 3 Tue Apr 23 04:01:32 2024
Received: b'PING 3 TUE APR 23 04:01:32 2024'
Time: 0.2040863037109375 Milliseconds

Sent: Ping 4 Tue Apr 23 04:01:32 2024
#4 Requested timed out

Sent: Ping 5 Tue Apr 23 04:01:33 2024
#5 Requested timed out

Sent: Ping 6 Tue Apr 23 04:01:34 2024
Received: b'PING 6 TUE APR 23 04:01:34 2024'
Time: 4.662275314331055 Milliseconds

Sent: Ping 7 Tue Apr 23 04:01:34 2024
#7 Requested timed out

Sent: Ping 8 Tue Apr 23 04:01:35 2024
Received: b'PING 8 TUE APR 23 04:01:35 2024'
Time: 3.9200782775878906 Milliseconds

Sent: Ping 9 Tue Apr 23 04:01:35 2024
Received: b'PING 9 TUE APR 23 04:01:35 2024'
Time: 3.1175613403320312 Milliseconds

Sent: Ping 10 Tue Apr 23 04:01:35 2024
#10 Requested timed out

Ping finished, closing socket

 Chose an option to run UDP Pinger Client
1. Enter any key to ping to UDP server
2. Enter 0 to end program
Enter your option: 0
Ending program...

