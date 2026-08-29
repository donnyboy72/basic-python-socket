import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.2.176.197"
ADDR = (SERVER, PORT) #creates a tuple with the IP address and port number

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a socket object

client.connect((ADDR))

def send(msg):
    message = msg.encode(FORMAT) #encodes the message to bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) #sends the length of the message to the server
    client.send(message) #sends the message to the server
    print(client.recv(2048).decode(FORMAT))

user_input = input("Enter your message: ")
while user_input.lower() != "disconnect" and user_input.lower() != "exit":
    send(user_input)
    user_input = input("Enter your message: ")

send(DISCONNECT_MESSAGE)

