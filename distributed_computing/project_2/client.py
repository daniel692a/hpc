import socket
from datetime import datetime

def send_msg(msg:str)->None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('127.0.0.1', 6664))
        client_socket.send(msg.encode())
        response = client_socket.recv(1024).decode()
        print(response)

message = input("Introduzca mensaje a enviar a los servidores: ")
hour = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
msg = f"{message}, Time:{hour}"
send_msg(msg)