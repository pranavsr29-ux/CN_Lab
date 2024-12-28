from socket import *
serverName = '127.0.0.1'  # IP address of the server (localhost)
serverPort = 12000         # Port number on which the server is listening
clientSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket (IPv4, TCP)

clientSocket.connect((serverName, serverPort))  # Connect to the server

# Input the file name from the user
sentence = input("\nEnter file name: ")

# Send the file name to the server
clientSocket.send(sentence.encode())

# Receive the file contents from the server
filecontents = clientSocket.recv(1024).decode()

# Print the contents received from the server
print('\nFrom Server:\n')
print(filecontents)

# Close the socket
clientSocket.close()
