from socket import *

# Server details
serverName = "127.0.0.1"
serverPort = 12000

# Create a UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get the file name from the user
sentence = input("\nEnter file name: ")

# Send the file name to the server
clientSocket.sendto(sentence.encode("utf-8"), (serverName, serverPort))

# Receive the file contents from the server
filecontents, serverAddress = clientSocket.recvfrom(2048)

# Display the server's reply
print('\nReply from Server:\n')
print(filecontents.decode("utf-8"))

# Close the client socket
clientSocket.close()
