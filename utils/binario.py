def toBin ( msg : str ) -> str:
    cat = ''

    for i in msg:
        cat += bin ( ord ( i ) ) [ 2:: ]

    return cat

def prueba():
    print ( 'prueba' )

if __name__ == '__main__':
    print ( 'Archivo binario.py' )
    print ( toBin ( 'Hola' ) )