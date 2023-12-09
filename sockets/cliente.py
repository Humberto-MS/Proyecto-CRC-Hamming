import socket

cliente = socket.socket ( 
            socket.AF_INET, 
            socket.SOCK_STREAM ) #TCP/IP
          # socket.SOCK_DGRAM    #UDP/IP

host = "127.0.0.1"
port = 12345
buffer_size = 1024

cliente.connect ( ( host, port ) )

while True:
    msg = input ( "msg --> " )

    cliente.send ( msg.encode() )

    if msg.lower == "quit":
        cliente.close()
        break

    data = cliente.recv ( buffer_size )
    print ( f"RECIBIDO: { data.decode() }" )