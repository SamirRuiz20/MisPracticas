
import pygame
#from pygame.locals import *
import sys
import time


pygame.init()

W, H = 1000, 600

PANTALLA = pygame.display.set_mode((W, H))


#CONTROL DE FPS
fps = 40
RELOJ = pygame.time.Clock()


#ICONO DE LA VENTANA
pygame.display.set_caption("EXTERMINATOR")

icono = pygame.image.load(r"IMAGENES\icono.png")

pygame.display.set_icon(icono)


#FONDO DE LA PANTALLA
fondo = pygame.image.load(r"IMAGENES\ciudad.png")


loadimage = pygame.image.load


#PERSONAJE DEL JUEGO EN ESTADO QUIETO A LA DERECHA Y A LA IZQUIERDA
quieto = [
    
    loadimage(r"IMAGENES\SPRITES\idle1.png"),
    loadimage(r"IMAGENES\SPRITES\idle2.png")

]




runLEFT = [

    loadimage(r"IMAGENES\SPRITES\run1-izq.png"),
    loadimage(r"IMAGENES\SPRITES\run2-izq.png"),
    loadimage(r"IMAGENES\SPRITES\run3-izq.png"),
    loadimage(r"IMAGENES\SPRITES\run4-izq.png"),
    loadimage(r"IMAGENES\SPRITES\run5-izq.png"),
    loadimage(r"IMAGENES\SPRITES\run6-izq.png")

]


runRIGHT = [

    loadimage(r"IMAGENES\SPRITES\run1.png"),
    loadimage(r"IMAGENES\SPRITES\run2.png"),
    loadimage(r"IMAGENES\SPRITES\run3.png"),
    loadimage(r"IMAGENES\SPRITES\run4.png"),
    loadimage(r"IMAGENES\SPRITES\run5.png"),
    loadimage(r"IMAGENES\SPRITES\run6.png")

]


salta = [
    loadimage(r"IMAGENES\SPRITES\jump1.png"),
    loadimage(r"IMAGENES\SPRITES\jump2.png")
]



#VARIABLES
x = 0
px = 20
py = 200
ancho = 40
velocidad = 10


#VARIABLES SALTO
salto = False
#ALTURA DEL SALTO
cuentasalto= 10

#VARIABLES DE DIRECCION
left = False
right = False
brujula = "RIGHT"

#PASOS
cuentapasos = 0



#MOVIMIENTO
def loadPantalla() :

    global cuentapasos
    global x
    
    
    if px >= W // 2 :

        #fondo en movimiento
        x_relativa = x % fondo.get_rect().width
        PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
        
        
        if x_relativa < W :

            PANTALLA.blit(fondo, (x_relativa, 0))

        x -= 5

    
    


    else :

        PANTALLA.blit(fondo, (0, 0))

        

    #contador de pasos
    if cuentapasos + 1 >= 6 :
        cuentapasos = 0

    #mover a la izquierda 
    if left :
        PANTALLA.blit(runLEFT[cuentapasos], (px, py))
        cuentapasos += 1

        #mover a la derecha
    elif right :
        PANTALLA.blit(runRIGHT[cuentapasos], (px, py))
        cuentapasos += 1

    elif salto + 1 >= 2 :
        cuentapasos = 0
        PANTALLA.blit(salta[cuentapasos], (px, py))

    else :
        PANTALLA.blit(quieto[1], (px, py)) if brujula == "LEFT" else PANTALLA.blit(quieto[0], (px, py))

    #ACTUALIZA LA VENTANA
    pygame.display.update()





#PALETA DE COLORES
BLANCO = 255, 255, 255
NEGRO = 0, 0, 0
ROJO = 255, 0, 0
AZUL = 0, 0, 255
VERDE = 0, 255, 0

HC74225 = 199, 66, 37
H61CD35 = 97, 205, 53


#COLOR DE PANTALLA
PANTALLA.blit(fondo, (0, 0))


clave = False

while True :


    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()
            sys.exit()

    #OPCION TECLA PULSADA
    keys = pygame.key.get_pressed()

    #TECLA A - MOVIMIENTO A LA IZQUIERDA
    if keys[pygame.K_a] and px > velocidad :
        
        
        brujula = "LEFT"
        px -= velocidad
        left = True
        right = False

    elif keys[pygame.K_d] and px < 760 :


        brujula = "RIGHT"
        px += velocidad
        left = False
        right = True
        

    else :

        left = False
        right = False
        cuentapasos = 0



    #TECLA W MOVER HACIA ARRIBA
    if keys[pygame.K_w] and py > 100 :

        py -= velocidad

    elif keys[pygame.K_s] and py < 300 and not(salto) :

        py += velocidad



    #TECLA ESPACIO PARA SALTAR
    if not(salto) :

        if keys[pygame.K_SPACE] :
            
            salto = True
            left = right = False
            cuentapasos = 0
            fps = 50

    else :

        if cuentasalto >= -10 :
          
            py -= (cuentasalto * abs(cuentasalto)) * 0.5
            cuentasalto -= 1

        else :
            
            cuentasalto = 10
            salto = False 
            fps = 40



    #LLAMAR A LA FUNCION DE ACTUALIZACION DE LA PANTALLA
    loadPantalla() 
    
  
    

    pygame.display.update() 
    RELOJ.tick(fps)

   
    
