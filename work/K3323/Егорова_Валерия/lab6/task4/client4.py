import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

nickname_prompt = client_socket.recv(1024).decode()
nickname = input(nickname_prompt)
client_socket.send(nickname.encode())

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Отключение от сервера")
            client_socket.close()
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input()
    if message.lower() == 'exit':
        client_socket.close()
        break
    client_socket.send(message.encode())

