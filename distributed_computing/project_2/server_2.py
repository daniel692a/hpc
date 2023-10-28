import socket 

HOST = '224.0.0.12'
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) 
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32) 
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1) 
sock.bind((HOST, PORT)) 
mreq = socket.inet_aton(HOST) + socket.inet_aton('0.0.0.0') 
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq) 

while True: 
    data, addr = sock.recvfrom(1024) 
    print(f"Mensaje recibido del cliente: {data.decode('utf-8')}")