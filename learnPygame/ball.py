import pygame
import sys
import os


pygame.init () # initialize pygame
pygame.mixer.init() 
size = ancho, alto = 640, 480 # establecer tamaño de ventana
screen = pygame.display.set_mode (size) # ventana de visualización
s1 = pygame.mixer.Sound(r'sounds\sound_ball2.mp3') 
color = (0, 0, 0) # establecer color
ball = pygame.image.load (r'IMAGENES\pelota.png') # cargar imagen
ballrect = ball.get_rect () # Obtener área rectangular
print(ballrect)
ball.fill((255, 255, 255))
clock = pygame.time.Clock()

velocidad = [5, 5] # Establecer los ejes de movimiento X e Y

while True: # loop sin fin para garantizar que la ventana siempre se muestre

        clock.tick(60) 

        for event in pygame.event.get (): # Iterar a través de todos los eventos
            if event.type == pygame.QUIT: # Salga si hace clic para cerrar la ventana
                sys.exit()

        if ballrect.left < 0 or ballrect.right >= ancho :
            
            
            velocidad[0] = -velocidad[0]
            s1.play() 
            #pygame.time.delay(1000)

        if ballrect.top < 0 or ballrect.bottom >= alto :

            
            velocidad[1] = -velocidad[1] 
            s1.play() 
            #pygame.time.delay(1000)   

        ballrect = ballrect.move (velocidad) # mover la pelota
        screen.fill (color) # color de relleno
        screen.blit (ball, ballrect) # dibuja la imagen en la ventana
        pygame.display.flip () # actualizar todas las pantallas

pygame.quit () # salir de pygame
