import pygame
#from pygame.locals import *
import sys

pygame.init()

W, H = 1000, 600

PANTALLA = pygame.display.set_mode((W, H))
FPS = 60
RELOJ = pygame.time.Clock()


fondo = pygame.image.load(r"IMAGENES\ciudad.png")

pygame.display.set_caption("EXTERMINATOR")

icono = pygame.image.load(r"IMAGENES\icono.png")

pygame.display.set_icon(icono)

x = 0


BLANCO = 255, 255, 255
NEGRO = 0, 0, 0
ROJO = 255, 0, 0
AZUL = 0, 0, 255
VERDE = 0, 255, 0

HC74225 = 199, 66, 37
H61CD35 = 97, 205, 53

PANTALLA.fill(BLANCO)



while True :


    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()
            sys.exit()

    
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    
    if x_relativa < W :

        PANTALLA.blit(fondo, (x_relativa, 0))

    x -= 1

    pygame.display.update() 
    RELOJ.tick(FPS) 