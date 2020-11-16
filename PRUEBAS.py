import pygame

pygame.init()   # Iniciamos con init para crear la pantalla
dis = pygame.display.set_mode((400, 300))   # dis será la variable que mostrará la pantalla, con el tamaño en píxeles, ancho y alto

pygame.display.set_caption('Snake, aprendiendo') #Nombre de la ventana

blue = (0,0,255)
red = (255,0,0)

game_over = False
while not game_over:    #bucle para la pantalla
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        pygame.draw.rect(dis, blue,  [200,150, 10, 10]) #Creamos la serpiente, marcamos la posición donde aparece (200x150) y los píxseles de grande (10x10)
        pygame.display.update()
pygame.quit()
quit()