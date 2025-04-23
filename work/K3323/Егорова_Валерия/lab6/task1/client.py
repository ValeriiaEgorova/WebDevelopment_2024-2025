import socket

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT)) 

client_socket.send("Hello, server".encode())

response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

client_socket.close()

