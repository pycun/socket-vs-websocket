# El servidor siempre esta escuchando

# Libreria necesaria para la coneccion
import socket

HOST = "127.0.0.1"  # Dirección de interfaz (localhost)
PORT = 65432  # Puerto que se encuentra escuchando (Puertos sin privilegios > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Se vincula la conexion
    s.bind((HOST, PORT))
    # Se establece que el socket esta escuchando
    s.listen()
    # Se crea la conexion
    conn, addr = s.accept()
    with conn:
        # Se entra al contexto de la conexion
        print(f"Connected by {addr}")
        while True:
            # Se reciben los datos
            data = conn.recv(1024)
            # Si no hay datos se termina la conexion
            if not data:
                print("break")
                break
            # De lo contrario se responde a la conexion
            print("envio")
            conn.sendall(data)
