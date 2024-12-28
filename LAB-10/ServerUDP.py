from socket import *

# Server details
serverPort = 12000

# Create a UDP server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the server socket to the specified IP and port
serverSocket.bind(("127.0.0.1", serverPort))

print("The server is ready to receive")

while True:
    # Receive file name from the client
    sentence, clientAddress = serverSocket.recvfrom(2048)
    sentence = sentence.decode("utf-8")

    try:
        # Open the requested file in read mode
        with open(sentence, "r") as file:
            # Read the contents of the file
            contents = file.read(2048)
        
        # Send the file contents back to the client
        serverSocket.sendto(contents.encode("utf-8"), clientAddress)

        print(f"\nSent contents of {sentence}")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        error_message = f"Error: File '{sentence}' not found."
        serverSocket.sendto(error_message.encode("utf-8"), clientAddress)
        print(f"\nFile '{sentence}' not found. Error message sent to client.")
