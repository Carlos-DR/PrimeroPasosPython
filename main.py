import random

salir = 0

while salir != 1:
    print('¿A que quieres jugar?')
    print(' ')
    print('1. Adivina los dados')
    print('2. Piedra, papel y tijera')
    print('3. Tres en raya')
    print('4. Snake')
    print('5. Buscaminas')
    print('0. SALIR')
    opcion = int(input('Escriba el número de una opción: '))

    if opcion < 0 or opcion > 5:
        print(' ')
        print('Esa opción no existe >:[')
        print(' ')

    if opcion == 0:
        print('Hasta luego')
        salir = 1

    if opcion == 1:
        print('ADIVINA LOS DADOS')

        class Dado:
            def gen(self):
                nr = random.randint(0, 10)
                return nr

        dado1 = Dado()
        dado2 = Dado()

        d1 = dado1.gen()
        d2 = dado2.gen()

        suma = d1 + d2

        print('Averigua la suma de 2 dados (Puede ser entre 0 y 20)')
        print('Tienes 5 intentos')
        numero = float(input('Inserte un número entre 0 y 20: '))

        win = 5
        while win > 1:
            print('INTENTOS RESTANTES:', win - 1)
            if suma == numero:
                print('Enhorabuena, has acertado :D')
                win = 0
            elif suma > numero:
                print('Te has quedado corto, prueba otra vez')
                numero = float(input('Inserte un número entre 0 y 20: '))
                win = win - 1
            else:
                print('Te has pasado, prueba otra vez')
                numero = float(input('Inserte un número entre 0 y 20: '))
                win = win - 1

    if opcion == 2:
        print('PIEDRA PAPEL Y TIJERA')
        Juego = ['Piedra', 'Papel', 'Tijera']

        Bot = random.randint(0, 2)

        print('¿Que quieres sacar?')
        print('0. Piedra')
        print('1. Papel')
        print('2. Tijera')

        jugador = int(input('---> '))

        game = 0

        while game == 0:

            if Bot == jugador:
                print('Has elegido:', Juego[jugador])
                print('Bot ha sacado:', Juego[Bot])
                print('Tu también has sacado', Juego[jugador])
                print('Empate! Intentalo de nuevo')
                game = 1

            elif (Bot == 0 and jugador == 1) or (Bot == 1 and jugador == 2) or (Bot == 2 and jugador == 0):
                print('Has elegido:', Juego[jugador])
                print('Bot ha sacado:', Juego[Bot])
                print(Juego[jugador], 'gana a', Juego[Bot])
                print('Has ganado!!')
                game = 1

            elif (Bot == 0 and jugador == 2) or (Bot == 1 and jugador == 0) or (Bot == 2 and jugador == 1):
                print('Has elegido:', Juego[jugador])
                print('Bot ha sacado:', Juego[Bot])
                print(Juego[Bot], 'gana a', Juego[jugador])
                print('Has perdido :(')
                game = 1

            else:
                print('Bot ha sacado:', Juego[Bot])
                print('Ha dao un caske')
                game = 1

    if opcion == 3:
        print('TRES EN RAYA')
        print(' ')
        print('EN DESARROLLO')

    if opcion == 4:
        print('SNAKE')
        print(' ')
        print('EN DESARROLLO')

    if opcion == 5:
        print('BUSCAMINAS')
        print(' ')
        print('EN DESARROLLO')
