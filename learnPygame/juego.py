

import pygame
#from pygame.locals import *
import sys

pygame.init()

PANTALLA = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Mi Primer Juego")


BLANCO = 255, 255, 255
NEGRO = 0, 0, 0
ROJO = 255, 0, 0
AZUL = 0, 0, 255
VERDE = 0, 255, 0

HC74225 = 199, 66, 37
H61CD35 = 97, 205, 53

PANTALLA.fill(BLANCO)


rectangulo1 = pygame.draw.rect(PANTALLA, ROJO, (100, 50, 100, 50))

pygame.draw.line(PANTALLA, VERDE, (100, 104), (199, 104), 10)

pygame.draw.circle(PANTALLA, NEGRO, (122, 250), 20, 0)

pygame.draw.ellipse(PANTALLA, H61CD35, (100, 200, 40, 80), 10)

puntos = [(100, 300), (100, 100)]

pygame.draw.polygon(PANTALLA, AZUL, puntos, 8)

while True :


    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()
            sys.exit()


    pygame.display.update()