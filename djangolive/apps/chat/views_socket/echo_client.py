# El cliente sera aquel que envie la peticion

import socket

HOST = "127.0.0.1"  # Dirección de interfaz (localhost)
PORT = 65432  # Puerto que se encuentra escuchando (Puertos sin privilegios > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Se conecta al servidor mediante el punto
    s.connect((HOST, PORT))
    # Se envia un mensaje
    s.sendall(b"Hello, world")
    # Se recibe la respuesta
    data = s.recv(1024)

print(f"Received {data!r}")