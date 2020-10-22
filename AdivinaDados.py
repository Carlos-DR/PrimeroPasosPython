import random
class Dado:
    def gen(self):
        nr = random.randint(0,10)
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
