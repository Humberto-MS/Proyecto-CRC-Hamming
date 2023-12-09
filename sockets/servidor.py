import socket
import os
#pyside
server = socket.socket ( 
            socket.AF_INET, 
            socket.SOCK_STREAM ) #TCP/IP
          # socket.SOCK_DGRAM    #UDP/IP

host = "127.0.0.1"
port = 12345
buffer_size = 1024

server.bind ( ( host, port ) )
server.listen ( 1 )
print ( f"Escuchando en { host }:{ port }" )

conn, addr = server.accept()
conn.send ( b"Conectado" )
# ( connection, address )

print ( f"Conexión establecida con { addr }" )

while True:
    data = conn.recv ( buffer_size )
    data = data.decode();
    print ( f"Mensaje: { data }" )

    if data.lower() == "quit":
        conn.close()
        break

    msg = f"RECIBIDO: { data }"
    conn.send ( msg.encode() )

print ( 'Saliendo...' )
server.close()