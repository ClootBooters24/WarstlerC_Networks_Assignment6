import socket

host = 'localhost'
port = 8080

accountBalance = 100

# Create a socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
serverSocket.bind((host, port))

# Listen for incoming connections
serverSocket.listen()

print(f"Server listening on {host}:{port}")

# Function to handle client requests
def handleClient(clientSocket):
    global accountBalance

    while True:
        # Receive data from the client
        request = clientSocket.recv(1024).decode('utf-8')

        if not request:
            break

        # Process client requests
        if request == 'balance':
            # Send the current account balance to the client
            clientSocket.send(str(accountBalance).encode('utf-8'))
            
        elif request.startswith('withdraw'):
            # Process withdrawal request
            while True:
                try:
                    amount = int(request.split()[1])
                    break
                except ValueError:
                    clientSocket.send("Invalid amount".encode('utf-8'))
            
            if amount > accountBalance:
                clientSocket.send("Insufficient funds".encode('utf-8'))
            
            elif amount < 0:
                clientSocket.send("Invalid amount".encode('utf-8'))
            
            else:
                accountBalance -= amount
                clientSocket.send("Withdrawal successful".encode('utf-8'))
                
        elif request.startswith('deposit'):
            # Process deposit request
            while True:
                try:
                    amount = int(request.split()[1])
                    break
                except ValueError:
                    clientSocket.send("Invalid amount".encode('utf-8'))
                                
            if amount < 0:
                clientSocket.send("Invalid amount".encode('utf-8'))
            
            else:
                accountBalance += amount
                clientSocket.send("Deposit successful".encode('utf-8'))
            
        else:
            clientSocket.send("Invalid command".encode('utf-8'))

    # Close the connection
    clientSocket.close()

# Accept and handle connections
while True:
    clientSocket, clientAddress = serverSocket.accept()
    print(f"Connection from {clientAddress}")
    handleClient(clientSocket)