import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = {}

message_count = 0
lock = threading.Lock()


def log_chat(username, message):
    with open("chat_log.txt", "a") as file:
        timestamp = datetime.now().strftime("%H:%M:%S")
        file.write(f"{timestamp},{username},{message}\n")


def broadcast(message, sender):
    global message_count

    with lock:
        message_count += 1

    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                pass


def handle_client(client):
    username = usernames[client]

    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            log_chat(username, message)

            broadcast(f"[{username}] {message}", client)

        except:
            break

    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp},DISCONNECTED,{username}")

    clients.remove(client)
    del usernames[client]

    client.close()


def receive():

    print("=" * 45)
    print(" Multi Client Chat Server Started ")
    print("=" * 45)
    print(f"Listening on Port {PORT}\n")

    while True:

        client, address = server.accept()

        username = client.recv(1024).decode()

        usernames[client] = username
        clients.append(client)

        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"{timestamp},CONNECTED,{username},{address[0]}")

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


receive()

