n = 0

prueba1 = 'Hola'
prueba2 = 'Adios'
prueba3 = 'que tal'

tablero = 'Hola'

while n < 4:
    variable = 'prueba' + str(n)
    print(variable)
    n = n +1

    if tablero == variable:
        print('Funciona', variable)