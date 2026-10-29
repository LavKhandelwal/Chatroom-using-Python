import socket
import threading

# ===========================
# COMMON VARIABLES
# ===========================
HOST = '127.0.0.1'  # Localhost IP for both server and clients
PORT = 12345         # Port for communication

# ===========================
# SERVER FUNCTIONALITY
# ===========================
clients = []  # List of connected clients
nicknames = []  # List of client nicknames


def broadcast(message):
    """Broadcast a message to all connected clients."""
    for client in clients:
        client.send(message)


def handle_client(client):
    """Handle messages from a specific client."""
    while True:
        try:
            # Receive and broadcast messages from the client
            message = client.recv(1024)
            broadcast(message)
        except:
            # Handle client disconnection
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive_connections(server):
    """Accept and manage new client connections."""
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('Name to be displayed: '.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the chatroom!'.encode('utf-8'))

        # Start a thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


def start_server():
    """Start the chatroom server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Server is listening...")
    receive_connections(server)


# ===========================
# CLIENT FUNCTIONALITY
# ===========================
def receive_messages(client):
    """Receive messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred! Connection closed.")
            client.close()
            break


def send_messages(client, nickname):
    """Send messages to the server."""
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))


def start_client():
    """Start a chatroom client."""
    nickname = input("Enter your nickname: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Start threads to receive and send messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    write_thread = threading.Thread(target=send_messages, args=(client, nickname))
    write_thread.start()


# ===========================
# MAIN EXECUTION LOGIC
# ===========================
if __name__ == "__main__":
    mode = input("Enter 'server' to start the server or 'client' to join the chat: ").strip().lower()

    if mode == 'server':
        start_server()
    elif mode == 'client':
        start_client()
    else:
        print("Invalid mode! Please enter 'server' or 'client'.")