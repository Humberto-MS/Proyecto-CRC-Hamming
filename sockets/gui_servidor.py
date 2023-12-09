import socket, random
from tkinter import Tk, Label, Button
from threading import Thread
from metodos import crc, distancia_hamming, detectar_errores, corregir_mensaje

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def obtener_ip():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.connect(("8.8.8.8",80))
        ip = server.getsockname()[0]
        server.close()
        return ip
    except socket.error:
        return "127.0.0.1"

def start_server():
    global server_thread
    server_thread = Thread(target=run_server)
    server_thread.start()

def run_server():
    info = [obtener_ip(), 12345]
    host = info[0]
    port = info[1]

    global buffer_size
    buffer_size = 1024

    server.bind((host, port))
    server.listen(1)
    status.config(text=f"Escuchando en {host}:{port}")

    global conn
    conn, addr = server.accept()
    conn.send(b"Conectado")
    status.config(text=f"Conexión establecida con {addr}")

    if ( status.cget("text") != "Detenido" ):
        while True:
            recibir_datos()

            msg, crc_code, prj, polinomio = data.split(' ')
            msg_original = msg

            msg_original_invertido = ''.join(reversed(msg_original))

            rnd = random.randint ( 0, 100 )
            msg = list(msg)

            if ( rnd <= int(prj) ):
                rand = random.randint ( 1, len(msg)-1 )

                for _ in range(rand):
                    nA = random.randint ( 0, len(msg)-1 )
                    if ( msg [ nA ] == '1' ): msg [ nA ] = '0'
                    if ( msg [ nA ] == '0' ): msg [ nA ] = '1'
            
            msg = ''.join(msg)
            mensaje.config(text=f"{msg} {crc_code}")    

            res = crc ( msg, polinomio, crc_code )
            res = int(res)

            if ( res != 0 ):
                msg_invertido = ''.join(reversed(msg))
                cant_errores = distancia_hamming(msg_original,msg) 
                posiciones = detectar_errores(msg_original_invertido,msg_invertido) 
                msg_corregido = ''.join(reversed(corregir_mensaje(msg_invertido,posiciones)))

                error.config(text="SI")
                cantidad.config(text=f"{cant_errores}")

                posiciones = ', '.join(map(str,posiciones))
                posicion.config(text=f"{posiciones}")

                mensaje_corregido.config(text=f"{msg_corregido}")

            else: error.config(text="NO")

            conn.send(msg.encode())
    else:
        status.config(text='Saliendo...')
        conn.close()
        server.close()

def recibir_datos():
    global data
    data = conn.recv(buffer_size)
    data = data.decode()

def limpiar():
    mensaje.config(text="---")
    error.config(text="---")
    cantidad.config(text="---")
    posicion.config(text="---")
    mensaje_corregido.config(text="---")

root = Tk()
root.title("Servidor")
root.geometry("800x490")

start_button = Button(root, text="Iniciar Servidor", command=start_server)
start_button.pack(pady=10)

status_label = Label(root, text="Estado:")
status_label.pack(pady=10)

status = Label(root, text="---")
status.pack()

label_mensaje = Label(root, text="Mensaje Recibido:")
label_mensaje.pack(pady=10)

mensaje = Label(root, text="---")
mensaje.pack()

error_label = Label(root, text="¿Hubo errores?")
error_label.pack(pady=10)

error = Label(root, text="---")
error.pack()

cantidad_label = Label(root, text="Cantidad de Errores:")
cantidad_label.pack(pady=10)

cantidad = Label(root,text="---")
cantidad.pack()

posicion_label = Label(root, text="Posiciones de los Errores:")
posicion_label.pack(pady=10)

posicion = Label(root, text="---")
posicion.pack()

mensaje_corregido_label = Label(root, text="Mensaje Corregido:")
mensaje_corregido_label.pack(pady=10)

mensaje_corregido = Label(root, text="---")
mensaje_corregido.pack()

boton_borrar = Button(root,text="Limpiar Campos",command=limpiar)
boton_borrar.pack(pady=20)

root.mainloop()
