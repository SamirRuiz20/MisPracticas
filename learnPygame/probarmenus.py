import pygame
import sys
import menu


pygame.init()


PANTALLA = pygame.display.set_mode((800, 600))

img = pygame.image.load(r'learnPygame\IMAGENES\bg.png').convert()
img2 = pygame.image.load(r'learnPygame\IMAGENES\pelota.png').convert()

print(dir(img.get_rect()))

menu1 = menu.Menu(PANTALLA)
menu2 = menu.Menu(PANTALLA)
menu3 = menu.Menu(PANTALLA)
menu4 = menu.Menu(PANTALLA)

def funcion() :

    print('HA presionado CLICK') 


while True :

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()
            sys.exit()

    PANTALLA.blit(pygame.transform.scale(img, (PANTALLA.get_rect().width, PANTALLA.get_rect().height)), (0, 0))

    menu1.add(label= '  Menu  ', bd= 10, bordercolor= (0, 0, 255) , fg= (255, 0, 0), x= 50, y= 50, font= ('Verdana', 30), bg= None)
    menu2.add(label= ' Jugar ', bd= 5, bordercolor= (0, 255, 0) , fg= (255, 0, 0), x= 100, y= 150, font= ('Verdana', 20), bg= None, command= funcion)
    menu3.add(label= '  Niveles  ', bd= 5, bordercolor= (0, 0, 255) , fg= (255, 0, 0), x= 90, y= 220, font= ('Verdana', 20), bg= None)
    menu4.add(label= '  Ajustes  ', bd= 5, bordercolor= (0, 0, 255) , fg= (255, 0, 0), x= 90, y= 300, font= ('Verdana', 20), bg= None)


    pygame.display.flip() 