def obtener_ip():
#     try:
#         server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         server.connect(("8.8.8.8",80)) # Conecta a un servidor DNS (ni idea de q sea esto)
#         ip = server.getsockname()[0]
#         server.close()
#         return ip
#     except socket.error:
#         return "127.0.0.1"