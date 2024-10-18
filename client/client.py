import socket
import threading
import tkinter as tk
import random
import os
import socks  # PySocks for Tor connection

# Function to generate and save a username
def get_username():
    if os.path.exists('username.txt'):
        with open('username.txt', 'r') as f:
            return f.read().strip()
    else:
        username = f"User{random.randint(1000, 9999)}"
        with open('username.txt', 'w') as f:
            f.write(username)
        return username

username = get_username()

# Function to receive messages from the server
def receive_messages(client_socket, msg_list):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            msg_list.insert(tk.END, message)  # Display message in the GUI
        except Exception as e:
            print(f"Error receiving message: {e}")
            status_label.config(text="Disconnected", fg="red")  # Change status to red
            break

# Function to send messages to the server
def send_message(event=None):
    message = f"{username}: {my_msg.get()}"
    my_msg.set("")  # Clear input field
    client_socket.send(bytes(message, "utf-8"))
    msg_list.insert(tk.END, message)  # Display sent message in GUI

# Function to handle closing the application
def on_closing(event=None):
    client_socket.close()
    top.quit()

# Connect to the Tor network
client_socket = socks.socksocket()
client_socket.set_proxy(socks.SOCKS5, '127.0.0.1', 9050)

# Setting up the Tkinter GUI
top = tk.Tk()
top.title("Tor Chat")

# Display connection status
status_label = tk.Label(top, text="Connecting...", fg="orange", font=("Helvetica", 12))
status_label.pack()

messages_frame = tk.Frame(top)
my_msg = tk.StringVar()  # To send messages
my_msg.set("Type your message here...")
scrollbar = tk.Scrollbar(messages_frame)  # To see past messages

msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tk.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send_message)  # Send message on pressing Enter
entry_field.pack()
send_button = tk.Button(top, text="Send", command=send_message)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)  # Handle window close

# Connect to the provided Tor hidden service address
try:
    client_socket.connect(('YOUR_ONION_URL', 5000))
    status_label.config(text="Connected", fg="green")  # Change status to green when connected
except Exception as e:
    status_label.config(text="Failed to connect", fg="red")  # Change status to red if connection fails
    print(f"Failed to connect to the server: {e}")
    exit()

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket, msg_list))
receive_thread.start()

tk.mainloop()
