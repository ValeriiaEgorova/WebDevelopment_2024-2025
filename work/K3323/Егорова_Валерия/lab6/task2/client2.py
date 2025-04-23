import socket

HOST = "127.0.0.1"
PORT = 12345

base = input("Введите основание параллелограмма: ")
height = input("Введите высоту параллелограмма: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = f"{base},{height}"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

client_socket.close()

