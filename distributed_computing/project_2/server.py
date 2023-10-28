import socket
import threading

HOST = '127.0.0.1'
PORT = 6664

def handle_client(client_socket:socket.socket)->None:
    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break
        file = open('./logger.txt.txt', "w")
        response = f"Hola cliente, soy el servidor: {HOST}\nHe recibido el siguiente mensaje: {msg}"
        file.write(msg+'\n')
        print("Respuesta guardada en logger")
        client_socket.send(response.encode())
        file.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Servidor escuchando en: {(HOST, PORT)}")

while True:
    client_socket, client_address = server.accept()
    print(f"Conexión aceptada de: {client_address}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
