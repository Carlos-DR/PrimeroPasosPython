import random

salir = 0

while salir != 1:
    print('¿A que quieres jugar?')
    print(' ')
    print('1. Adivina los dados')
    print('2. Piedra, papel y tijera')
    print('3. Tres en raya (2 jugadores)')
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
            print('INTENTOS RESTANTES:', win - 1, '\n')
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
        # Implementación del juego Tic-Tac-Toe para dos jugadores en Python.

        '''' Haremos el tablero usando diccionario.
             en qué teclas estará la ubicación (es decir, arriba a la izquierda, a la mitad a la derecha, etc.)
             e inicialmente sus valores serán un espacio vacío y luego, después de cada movimiento
             cambiaremos el valor de acuerdo con la elección de movimiento del jugador. '''

        theBoard = {'7': ' ', '8': ' ', '9': ' ',
                    '4': ' ', '5': ' ', '6': ' ',
                    '1': ' ', '2': ' ', '3': ' '}

        board_keys = []

        for key in theBoard:
            board_keys.append(key)

        ''' Tendremos que imprimir el tablero actualizado después de cada movimiento en el juego y
             así haremos una función en la que definiremos la función printBoard
             para que podamos imprimir fácilmente el tablero cada vez llamando a esta función. '''


        def printBoard(board):
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('-+-+-')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('-+-+-')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])


        # Ahora escribiremos la función principal que tiene toda la funcionalidad del juego..
        def game():
            turn = 'X'
            count = 0

            for i in range(10):
                printBoard(theBoard)
                print("Es tu turno," + turn + ".¿Donde quieres marcar?")

                move = input()

                if theBoard[move] == ' ':
                    theBoard[move] = turn
                    count += 1
                else:
                    print("Ya hay una marca en ese lugar.\n¿Donde quieres marcar?")
                    continue

                # Ahora comprobaremos si el jugador X u O ha ganado, por cada movimiento después de 5 movimientos..
                if count >= 5:
                    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # tres en raya horizontal arriba
                        printBoard(theBoard)
                        print("\nFin del juego.\n")
                        print(" **** " + turn + " gana. ****")
                        break
                    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # tres en raya horizontal en medio
                        printBoard(theBoard)
                        print("\nFin del juego.\n")
                        print(" **** " + turn + " gana. ****")
                        break
                    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # tres en raya horizontal abajo
                        printBoard(theBoard)
                        print("\nFin del juego.\n")
                        print(" **** " + turn + " gana. ****")
                        break
                    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # tres en raya vertical izquierdo
                        printBoard(theBoard)
                        print("\nFin del juego.\n")
                        print(" **** " + turn + " gana. ****")
                        break
                    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # tres en raya vertical en medio
                        printBoard(theBoard)
                        print("\nFin del juego.\n")
                        print(" **** " + turn + " gana. ****")
                        break
                    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # tres en raya vertical derecho
                        printBoard(theBoard)
                        print("\nFin del juego.\n")
                        print(" **** " + turn + " gana. ****")
                        break
                    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal 1
                        printBoard(theBoard)
                        print("\nFin del juego.\n")
                        print(" **** " + turn + " gana. ****")
                        break
                    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal 2
                        printBoard(theBoard)
                        print("\nFin del juego.\n")
                        print(" **** " + turn + " gana. ****")
                        break

                        # Si ni X ni O ganan y el tablero está lleno, declararemos el resultado como 'empate'.
                if count == 9:
                    print("\nFin del juego.\n")
                    print("EMPATE!!")

                # Cambiamos de jugador después de cada movimiento.
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

                    # Preguntamos si quieres reiniciar el juego o no.
            restart = input("¿Quieres jugar otra vez?(s/n)")
            if restart == "s" or restart == "S":
                for key in board_keys:
                    theBoard[key] = " "
                game()


        if __name__ == "__main__":
            game()

    if opcion == 4:
        print('SNAKE')
        print(' ')
        print('EN DESARROLLO')

    if opcion == 5:
        print('BUSCAMINAS')
        print(' ')
        print('EN DESARROLLO')
