# El cliente sera aquel que envie la peticion

# Libreria necesaria para la coneccion
import socket

# Configura el cliente
host = '127.0.0.1'  # Dirección IP del servidor
port = 12345       # Puerto del servidor

# Crea un socket de cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
client_socket.connect((host, port))
print(f"Conexión establecida con {host}:{port}")

# Envía y recibe datos
while True:
    message = input("Mensaje al servidor: ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f"Servidor dice: {data}")

# Cierra la conexión
client_socket.close()
