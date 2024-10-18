import socket
import threading
import random
import os
import socks  # PySocks for Tor connection
from PyQt5 import QtCore, QtGui, QtWidgets

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
def receive_messages(client_socket, text_area):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            
            # Assuming message format is 'username: message'
            if ':' in message:
                user, msg = message.split(':', 1)
                formatted_message = f"<span style='color: green; font-weight: bold;'>{user}:</span> <span style='color: white;'>{msg}</span>"
            else:
                formatted_message = message

            text_area.append(formatted_message)  # Append the formatted message to the text area
        except Exception as e:
            text_area.append(f"<span style='color: red;'>Error receiving message: {e}</span>")
            break

# Function to send messages to the server
def send_message(client_socket, input_field, text_area):
    message = f"{username}: {input_field.text()}"
    input_field.clear()  # Clear the input field after sending

    try:
        client_socket.send(bytes(message, "utf-8"))

        # Format the message: username in one color, message in another
        formatted_message = f"<span style='color: blue; font-weight: bold;'>You:</span> <span style='color: lightgray;'>{message.split(':', 1)[1]}</span>"
        text_area.append(formatted_message)
    except Exception as e:
        text_area.append(f"<span style='color: red;'>Error sending message: {e}</span>")

# PyQt5 window class
class ChatWindow(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super().__init__()

        self.client_socket = client_socket
        self.setWindowTitle("Tor Chat - Hades")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  # Remove title bar and keep on top
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Translucent background
        self.setGeometry(100, 100, 300, 200)

        # Set up the layout
        self.layout = QtWidgets.QVBoxLayout()

        # Black transparent background for the entire window
        self.setStyleSheet("background: rgba(0, 0, 0, 150);")  # Black with 150/255 transparency

        # Set font size to 9
        font = QtGui.QFont()
        font.setPointSize(9)
        self.setFont(font)  # Apply the font globally to the window

        # Status label
        self.status_label = QtWidgets.QLabel("Connecting Hades Tor Chat..", self)
        self.status_label.setStyleSheet("color: orange; background: transparent;")
        self.layout.addWidget(self.status_label)

        # Chat area
        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setStyleSheet("background: rgba(0, 0, 0, 100); color: white; border: 1px solid white;")  # Black transparent background
        self.layout.addWidget(self.text_area)

        # Input area
        self.input_field = QtWidgets.QLineEdit(self)
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.setStyleSheet("background: rgba(0, 0, 0, 100); color: white; border: 1px solid white;")  # Black transparent background
        self.input_field.returnPressed.connect(self.handle_send_message)
        self.layout.addWidget(self.input_field)

        # Send button
        self.send_button = QtWidgets.QPushButton("Send", self)
        self.send_button.setStyleSheet("background: rgba(0, 0, 0, 100); color: white; border: 1px solid white;")  # Black transparent background
        self.send_button.clicked.connect(self.handle_send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

        # Connect to the Tor network
        self.connect_to_server()

        # Enable window dragging
        self.oldPos = self.pos()

    def handle_send_message(self):
        send_message(self.client_socket, self.input_field, self.text_area)

    def connect_to_server(self):
        try:
            self.client_socket.connect(('YOUR_ONION_URL', 5000))
            self.status_label.setText("Connected Hades Tor Chat")
            self.status_label.setStyleSheet("color: green; background: transparent;")

            # Start a thread to receive messages
            receive_thread = threading.Thread(target=receive_messages, args=(self.client_socket, self.text_area))
            receive_thread.start()

        except Exception as e:
            self.status_label.setText("Failed to connect")
            self.status_label.setStyleSheet("color: red; background: transparent;")
            self.text_area.append(f"Failed to connect to the server: {e}")

    # Handling window drag
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

# Main function to run the app
def main():
    # Connect to the Tor network
    client_socket = socks.socksocket()
    client_socket.set_proxy(socks.SOCKS5, '127.0.0.1', 9050)

    # Create the PyQt5 application
    app = QtWidgets.QApplication([])

    # Create and show the chat window
    window = ChatWindow(client_socket)
    window.show()

    # Run the application
    app.exec_()

if __name__ == "__main__":
    main()
