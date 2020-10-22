import random
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