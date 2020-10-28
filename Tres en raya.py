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