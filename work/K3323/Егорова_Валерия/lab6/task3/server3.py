import socket

HOST = '127.0.0.1'
PORT = 8080

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

response = "HTTP/1.1 200 OK\n"
response += "Content-Type: text/html\n"
response += f"Content-Length: {len(html_content.encode())}\n"
response += "\n"
response += html_content

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Сервер запущен на http://{HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Клиент подключен: {addr}")

    request = conn.recv(1024).decode()
    print(f"Запрос клиента:\n{request}")

    conn.send(response.encode())
    conn.close()

