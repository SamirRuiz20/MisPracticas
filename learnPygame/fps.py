import pygame
import random as rnd



pygame.init()



PANTALLA = pygame.display.set_mode((800, 600))


rects = []

for i in range(50) :

    x = rnd.randint(1, 799)
    y = rnd.randint(1, 599)
    rects.append([x, y])

fps = 0
frames = 0
trans = 0
segundos  = 0

reloj = pygame.time.Clock()
font = pygame.font.SysFont(None, 70, bold=False, italic=False)


run = True

while run :

    time = reloj.tick(60)
    trans += time

    frames += 1
    if trans >= 1000 :

        fps = frames
        frames = 0
        trans = 0
        segundos += 1

    

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            run = False

    for c in rects :

        c[0] += 1
        c[1] += 2

        if c[0] >= 800 :

            c[0] = 0

        if c[1] >= 600 :

            c[1] = 0

    PANTALLA.fill('black')
    
    for c in rects :

        pygame.draw.rect(PANTALLA, 'green', (c[0], c[1], 10, 10), width=0)

    t1 = font.render(str(fps), True, 'red')
    t2 = font.render(str(segundos), True, 'red')
    PANTALLA.blit(t1, (10 ,10))
    PANTALLA.blit(t2, (200 ,10))

    
    pygame.display.flip() 


    