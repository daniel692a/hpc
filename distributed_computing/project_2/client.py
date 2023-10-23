import socket



def send_msg(msg:str)->None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(coordinate_address)
        client_socket.send(msg.encode())
        response = client_socket.recv(1024).decode()
        print(response)

message = input("Introduzca mensaje a enviar a los servidores: ")
send_msg(message)

