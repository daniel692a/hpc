import socket
import threading

def handle_client(client_socket:socket.socket)->None:
    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break

        response = f"Mensaje Recibido: {msg}"
        client_socket.send(response.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('SERVER_IP', SERVER_PORT))
server.listen()

print("Servidor escuchando:)")

while True:
    client_socket, client_address = server.accept()
    print(f"Conexión aceptada de: {client_address}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket))
    client_handler.start()
