import socket

HOST = "127.0.0.1"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Сервер запущен, ожидает подключения...")

conn, addr = server_socket.accept()
print(f"Подключен клиент: {addr}")

data = conn.recv(1024).decode()
print(f"Сообщение от клиента: {data}")

conn.send("Hello, client".encode())

conn.close()
server_socket.close()

