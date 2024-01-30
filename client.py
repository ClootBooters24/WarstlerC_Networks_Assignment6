import socket

host = 'localhost'
port = 8080

# Create a socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect((host, port))

# Function to display the menu
def displayMenu():
    # Display the menu
    print("\nMenu:")
    print("Deposit")
    print("Withdraw")
    print("Balance")
    print("Exit")

# Main client logic
while True:
    displayMenu()

    # Get user input
    choice = input("Enter your choice: ")

    if choice == 'Deposit' or choice == 'deposit':
        # Deposit money
        amount = int(input("Enter the amount to deposit: "))
        clientSocket.send(f"deposit {amount}".encode('utf-8'))
        print(clientSocket.recv(1024).decode('utf-8'))
        
    elif choice == 'Withdraw' or choice == 'withdraw':
        # Withdraw money
        amount = int(input("Enter the amount to withdraw: "))
        clientSocket.send(f"withdraw {amount}".encode('utf-8'))
        print(clientSocket.recv(1024).decode('utf-8'))
        
    elif choice == 'Balance' or choice == 'balance':
        # Check balance
        clientSocket.send("balance".encode('utf-8'))
        balance = clientSocket.recv(1024).decode('utf-8')
        print(f"Account Balance: ${balance}")
        
    elif choice == 'Exit' or choice == 'exit':
        # Exit
        clientSocket.close()
        break
    
    else:
        print("Invalid choice. Please enter a valid choice.")