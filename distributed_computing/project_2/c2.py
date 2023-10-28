import socket 

SERVERS = ['127.0.0.1']
PORT = 6664

HOST = '127.0.0.1'
HOST_PORT = 6666
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, HOST_PORT))
    s.listen()
    print('Servidor escuchando en', (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            msg = conn.recv(1024)
            input()
            if not msg:
                break
            for server in SERVERS: 
                s.connect((server, PORT))
                s.sendall(msg.encode('utf-8')) 
                data = s.recv(1024) 
                print(f"Mensaje enviado al servidor {server}: {msg}") 
                print(f"Mensaje recibido del servidor {server}: {data.decode('utf-8')}")
                response = f"Mensaje recibido del servidor {server}: {data.decode('utf-8')}"
                s.sendall(response.encode('utf-8'))