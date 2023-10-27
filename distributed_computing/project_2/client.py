import socket
from datetime import datetime

def send_msg(msg:str)->None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(coordinate_address)
        client_socket.send(msg.encode())
        response = client_socket.recv(1024).decode()
        print(response)

message = input("Introduzca mensaje a enviar a los servidores: ")
hour = datetime.now().strftime('%H:%M:%S')
msg = f"{msg}, Time:{hour}"
send_msg(message)

