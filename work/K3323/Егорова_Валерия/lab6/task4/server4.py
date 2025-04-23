import socket
import threading
HOST = '127.0.0.1'
PORT = 12345
clients = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print("Сервер запущен. Ожидаем подключения...")
def broadcast(message, sender_socket=None):
    for client in list(clients):
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                del clients[client]
def handle_client(client_socket):
    try:
        client_socket.send("Введите ваш ник: ".encode())
        nickname = client_socket.recv(1024).decode().strip()
        clients[client_socket] = nickname
        print(f"{nickname} подключился.")
        broadcast(f"{nickname} присоединился к чату.", client_socket)
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            formatted = f"{nickname}: {message.decode()}"
            print(formatted)
            broadcast(formatted, client_socket)
    except:
        pass
    finally:
        nickname = clients.get(client_socket, "Неизвестный")
        print(f"{nickname} отключился.")
        broadcast(f"{nickname} покинул чат.")
        clients.pop(client_socket, None)
        client_socket.close()
while True:
    client_socket, addr = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

