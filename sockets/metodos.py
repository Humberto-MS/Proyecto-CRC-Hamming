def crc(message, generator, crc_code='0000'):
	if int(crc_code) == 0 : # if there isnt a crc_code and is the first xor module
		crc_code = ''
		for i in range(len(generator) -1):
			crc_code = crc_code + '0'

	# add the crc_code to the binary message
	message = message + crc_code

	# convert divisors to lists for better management.
	message = list(message)
	generator = list(generator)

	for i in range(len(message) - len(crc_code)):
		if message[i] == '1': # if is a 1 bit
			for j in range(len(generator)):
				message[i+j] = str((int(message[i+j])+int(generator[j]))%2) # mod 2 division

	return ''.join(message[-len(crc_code):])

def distancia_hamming(str1, str2):
    if len(str1) == len(str2):
        return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def corregir_mensaje(mensaje_recibido, errores):
    mensaje_corregido = list(mensaje_recibido)
    
    for error_pos in errores:
        mensaje_corregido[error_pos] = '0' if mensaje_corregido[error_pos] == '1' else '1'
    
    return ''.join(mensaje_corregido)

def detectar_errores(mensaje_original, mensaje_recibido):
    if len(mensaje_original) == len(mensaje_recibido):
        errores = [i for i, (c1, c2) in enumerate(zip(mensaje_original, mensaje_recibido)) if c1 != c2]
        return errores    