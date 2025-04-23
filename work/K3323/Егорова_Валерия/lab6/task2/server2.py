import socket

HOST = "127.0.0.1"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Сервер запущен. Ожидание клиента...")

conn, addr = server_socket.accept()
print(f"Клиент подключен: {addr}")

data = conn.recv(1024).decode()
print(f"Получено от клиента: {data}")

try:
    base, height = map(float, data.split(','))
    area = base * height
    result = f"Площадь параллелограмма: {area}"
except Exception as e:
    result = f"Ошибка: {str(e)}"

conn.send(result.encode())

conn.close()
server_socket.close()

