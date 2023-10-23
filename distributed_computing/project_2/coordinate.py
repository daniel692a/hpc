import threading
import socket
from typing import List, Tuple

server_addresses:List[Tuple] = [ ('IP_1', PORT_1), ('IP_2', PORT_2) ]

def route_msg(msg:str, server_address:str)->str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect(server_address)
        server_socket.send(msg.encode())
        response = server_socket.recv(1024).decode()
    return response

def handle_client(client_socket:socket.socket)->None:
    while True:
        msg = client_socket.recv(1024).decode()

        if not msg:
            break
        
        client_ip, client_port = client_socket.getpeername()
        msg_with_metadata = f"Message: {msg}, Address: {client_ip}:{client_port}"

        responses = []
        for server_address in server_addresses:
            response = route_msg(msg_with_metadata, server_address)
            responses.append(response)
        
        client_socket.send("\n".join(responses).encode())

coordinate_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
coordinate_server.bind(('IP_COORDINATE', PORT_COORDINATE))
coordinate_server.listen(4)

print("El servidor coordinador está escuchando")

while True:
    client_s, client_a = coordinate_server.accept()
    print("Conexión Aceptada")
    client_handler = threading.Thread(target=handle_client, args = (client_s,))
    client_handler.start()