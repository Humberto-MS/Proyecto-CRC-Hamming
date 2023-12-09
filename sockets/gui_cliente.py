import socket
import tkinter as tk
from tkinter import Tk, Entry, Button, Label, ttk
from threading import Thread
from metodos import crc

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 1024
global status

def start_client():
    global client_thread
    client_thread = Thread(target=run_client)
    client_thread.start()

def run_client():
    host_servidor = '192.168.1.8'
    port_servidor = 12345    

    cliente.connect((host_servidor, port_servidor))
    status.config(text=f"Conectado a {host_servidor}:{port_servidor}")    

def enviar_mensaje():
    if ( status.cget("text") != "Cliente desconectado" ):
        prj = porcentaje.get() 
        msg = input_mensaje.get()
        msg = ''.join(format(ord(i), '08b') for i in msg)
        crc_code = crc ( msg, polinomio )
        label_binario.config(text=f"{msg}")
        mensaje = msg + ' ' + crc_code + ' ' + prj + ' ' + polinomio
        cliente.sendall(mensaje.encode())

def getOpcion(event):
    global polinomio
    opcion = cb_opcion.get()
    if opcion == 'x^3 + x^2 + 1':
        polinomio = '1101'
    elif opcion == 'x^4 + x + 1':
        polinomio = '10011'
    elif opcion == 'x^8 + x^2 + x + 1':
        polinomio = '100000111'
    elif opcion == 'x^10 + x^9 + x^5 + x^4 + x + 1':
        polinomio = '11000110011'
    elif opcion == 'x^12 + x^11 + x^3 + x^2 + x + 1':
        polinomio = '1100000001111'
    elif opcion == 'x^16 + x^12 + x^5 + 1':
        polinomio = '10001000000100001'
    elif opcion == 'x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1':
        polinomio = '100000100110000010001110110110111'
    elif opcion == 'x^64 + x^4 + x^3 + x + 1':
        polinomio = '10000000000000000000000000000000000000000000000000000000000011011'

root = Tk()
root.title("Cliente")
root.geometry("650x430")

start_button = Button(root, text="Conectar al Servidor", command=start_client)
start_button.pack(pady=10)

status_label = Label(root, text="Estado:")
status_label.pack(pady=10)

status = Label(root, text="---")
status.pack(pady=10)

n = tk.StringVar()
cb_opcion = ttk.Combobox ( root, width=90, textvariable=n )

cb_opcion [ 'values' ] = (
    '--Selecciona un Polinomio--',
    'x^3 + x^2 + 1',
    'x^4 + x + 1',
    'x^8 + x^2 + x + 1',
    'x^10 + x^9 + x^5 + x^4 + x + 1',
    'x^12 + x^11 + x^3 + x^2 + x + 1',
    'x^16 + x^12 + x^5 + 1',
    'x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1',
    'x^64 + x^4 + x^3 + x + 1'
)

cb_opcion.pack(pady=10)
cb_opcion.current(0)
cb_opcion.config(justify='center')
cb_opcion.bind("<<ComboboxSelected>>", getOpcion)

label_porcentaje = Label(root, text="Porcentaje de Error:")
label_porcentaje.pack(pady=10)

porcentaje = Entry(root, width=15)
porcentaje.pack(pady=10)
porcentaje.config(justify='center')

label_mensaje = Label(root, text="Mensaje a Enviar:")
label_mensaje.pack(pady=10)

input_mensaje = Entry(root, width=80)
input_mensaje.pack(pady=10)
input_mensaje.config(justify='center')

label_binario = Label(root, text="---")
label_binario.pack(pady=10)

boton_enviar = Button(root, text="Enviar Mensaje", command=enviar_mensaje)
boton_enviar.pack(pady=10)

root.mainloop()
