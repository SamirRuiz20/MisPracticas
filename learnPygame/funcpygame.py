import pygame
import sys

from pygame.key import get_pressed

pygame.init()




PANTALLA = pygame.display.set_mode((800, 600))


rect1 = pygame.Rect(450, 50, 100, 50)

rect2 = pygame.Rect(200, 50, 150, 100)



while True :

    pygame.time.Clock().tick(10)
    
    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN :

            pass 

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] :
        rect1.inflate_ip(1, 1)

    elif key[pygame.K_DOWN] :
        rect1.inflate_ip(-1, -1) 
        

    PANTALLA.fill('black')

    pygame.draw.rect(PANTALLA, 'red', rect1, width=0) 
    pygame.draw.rect(PANTALLA, 'blue', rect2, width=0)


    

    pygame.display.flip()