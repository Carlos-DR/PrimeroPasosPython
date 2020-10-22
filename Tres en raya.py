import random

print('Tres en raya')
print('Elige con que quieres jugar X o O')

tablero = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}

tictactoc1 = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': 'X', '2': 'X', '3': 'X'}
tictactoc2 = {'7': ' ', '8': ' ', '9': ' ', '4': 'X', '5': 'X', '6': 'X', '1': ' ', '2': ' ', '3': ' '}
tictactoc3 = {'7': 'X', '8': 'X', '9': 'X', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
tictactoc4 = {'7': 'X', '8': ' ', '9': ' ', '4': 'X', '5': ' ', '6': ' ', '1': 'X', '2': ' ', '3': ' '}
tictactoc5 = {'7': ' ', '8': 'X', '9': ' ', '4': ' ', '5': 'X', '6': ' ', '1': ' ', '2': 'X', '3': ' '}
tictactoc6 = {'7': ' ', '8': ' ', '9': 'X', '4': ' ', '5': ' ', '6': 'X', '1': ' ', '2': ' ', '3': 'X'}
tictactoc7 = {'7': ' ', '8': ' ', '9': 'X', '4': ' ', '5': 'X', '6': ' ', '1': 'X', '2': ' ', '3': ' '}
tictactoc8 = {'7': 'X', '8': ' ', '9': ' ', '4': ' ', '5': 'X', '6': ' ', '1': ' ', '2': ' ', '3': 'X'}

tictactoc9 = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': 'O', '2': 'O', '3': 'O'}
tictactoc10 = {'7': ' ', '8': ' ', '9': ' ', '4': 'O', '5': 'O', '6': 'O', '1': ' ', '2': ' ', '3': ' '}
tictactoc11 = {'7': 'O', '8': 'O', '9': 'O', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
tictactoc12 = {'7': 'O', '8': ' ', '9': ' ', '4': 'O', '5': ' ', '6': ' ', '1': 'O', '2': ' ', '3': ' '}
tictactoc13 = {'7': ' ', '8': 'O', '9': ' ', '4': ' ', '5': 'O', '6': ' ', '1': ' ', '2': 'O', '3': ' '}
tictactoc14 = {'7': ' ', '8': ' ', '9': 'O', '4': ' ', '5': ' ', '6': 'O', '1': ' ', '2': ' ', '3': 'O'}
tictactoc15 = {'7': ' ', '8': ' ', '9': 'O', '4': ' ', '5': 'O', '6': ' ', '1': 'O', '2': ' ', '3': ' '}
tictactoc16 = {'7': 'O', '8': ' ', '9': ' ', '4': ' ', '5': 'O', '6': ' ', '1': ' ', '2': ' ', '3': 'O'}

jugador = input()
jugador = jugador.upper()
bot = 'A'

fin = 0
win = 0
array = []

while fin == 0:

    if jugador == 'X':
        bot = 'O'
        fin = 1
    if jugador == 'O':
        bot = 'X'
        fin = 1
    elif jugador != 'X' and jugador != 'O':
        print('Por favor, introduzca un valor válido (X o O)')
        jugador = input()
        jugador = jugador.upper()


def imprimirtablero(tab):
    print('+---+---+---+')
    print('| ' + tab['7'] + ' | ' + tab['8'] + ' | ' + tab['9'] + ' |')
    print('+---+---+---+')
    print('| ' + tab['4'] + ' | ' + tab['5'] + ' | ' + tab['6'] + ' |')
    print('+---+---+---+')
    print('| ' + tab['1'] + ' | ' + tab['2'] + ' | ' + tab['3'] + ' |')
    print('+---+---+---+')


def comprobarposicion():
    # Posición del X
    if tablero == variable:
        return True
    if tablero == tictactoc2:
        return True
    if tablero == tictactoc3:
        return True
    if tablero == tictactoc4:
        return True
    if tablero == tictactoc5:
        return True
    if tablero == tictactoc6:
        return True
    if tablero == tictactoc7:
        return True
    if tablero == tictactoc8:
        return True

    # Posición del O
    if tablero == tictactoc9:
        return True
    if tablero == tictactoc10:
        return True
    if tablero == tictactoc11:
        return True
    if tablero == tictactoc12:
        return True
    if tablero == tictactoc13:
        return True
    if tablero == tictactoc14:
        return True
    if tablero == tictactoc15:
        return True
    if tablero == tictactoc16:
        return True
    else:
        return False


while not comprobarposicion():
    print('¿Donde quieres marcar?')
    imprimirtablero(tablero)
    print(tablero)
    marca = input()

    if marca in array:
        print('Por favor, marque en una casilla en blanco')

    if marca not in array:
        array.append(marca)
        tablero[marca] = jugador
        numbot = str(random.randint(1, 9))
        print(numbot)

        if len(array) != 9:
            bucle = 1

            while bucle == 1:
                
                if numbot in array:
                    numbot = str(random.randint(1, 9))
                    print('nuevo numbot', numbot)

                if numbot not in array:
                    array.append(numbot)
                    tablero[numbot] = bot
                    imprimirtablero(tablero)
                    bucle = 0

                else:
                    print('Ha dado un caske')

        elif len(array) == 9:
            imprimirtablero(tablero)
            print('Fin')
            comprobarposicion()

    elif len(array) == 9:
        imprimirtablero(tablero)
        print('Fin')
        comprobarposicion()
