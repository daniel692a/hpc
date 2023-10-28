import socket

HOST = '224.0.1.1'
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
while True:
    mensaje = input("Introduzca un mensaje para enviar a los servidores: ")
    sock.sendto(mensaje.encode('utf-8'), (HOST, PORT))