import socket
import threading

HOST = input("Server IP : ")
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter Username : ")

client.send(username.encode())


def receive():

    while True:

        try:

            message = client.recv(1024).decode()

            print(message)

        except:

            break


def write():

    while True:

        message = input()

        client.send(message.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

write()