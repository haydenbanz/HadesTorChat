import socket
import threading
import os

clients = []
usernames = {}

def broadcast(message, client_socket):
    """Send a message to all clients except the sender."""
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error sending message to {client}: {e}")

def handle_client(client_socket):
    """Handle communication with a connected client."""
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))  # Print message to the server console
                broadcast(message, client_socket)
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    # Remove the client from the list and notify others
    if client_socket in clients:
        clients.remove(client_socket)
        username = usernames.pop(client_socket, "Unknown User")
        print(f"{username} has disconnected.")
        broadcast(f"{username} has left the chat.".encode('utf-8'), client_socket)
        client_socket.close()

def server():
    """Start the chat server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))  # Adjust the address if needed
    server_socket.listen()
    print("Server started on 127.0.0.1:5000")

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)

        # Automatically generate and save a username
        username = f"User{len(clients)}"
        usernames[client_socket] = username
        print(f"{username} has connected from {address}.")
        
        # Notify others that a new user has joined
        broadcast(f"{username} has joined the chat.".encode('utf-8'), client_socket)

        # Start a new thread to handle the client's communication
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    server()
