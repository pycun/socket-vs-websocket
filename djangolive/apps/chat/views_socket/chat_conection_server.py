# El servidor siempre esta escuchando

# Libreria necesaria para la coneccion
import socket

# Configura el servidor
host = '127.0.0.1'  # Dirección IP del servidor
port = 12345       # Puerto en el que escucha el servidor

# Crea un socket de servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# "AF_INET" especifica la familia de direcciones de Internet que se utilizará
# "SOCK_STREAM" especifica el tipo de socket de flujo orientado a conexión que se creará para la comunicación. 

# Vincula el socket a la dirección y puerto especificados
server_socket.bind((host, port))

# Escucha conexiones entrantes
server_socket.listen(1)
print(f"Servidor escuchando en {host}:{port}")

# Acepta una conexión entrante
client_socket, client_address = server_socket.accept()
print(f"Conexión entrante desde {client_address}")

# Recibe y envía datos
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break  # Si no hay datos, la conexión se ha cerrado

    print(f"Cliente dice: {data}")
    response = input("Responder: ")
    client_socket.send(response.encode())

# Cierra la conexión
client_socket.close()
server_socket.close()
