

import random
import sys
from random import choice
import pygame
from pygame import mixer


# ========================----------- CLASE BALL ------------==================================
class Ball :


    nivel = 'one'

    def __init__(self,surface, color, size, radio) -> None :

        '''
        Metodo Que Inicializa Los Atributos Del Objeto Ball Al Instanciarse Un Objeto De Este Tipo ...
        '''

        self.surface = surface
        self.color = color
        self.x, self.y = size
        self.radio = radio
        self.state = 'quiet'
        self.speed_x = 0
        self.speed_y = 0
        self.show()


    def show(self) -> None :

        '''
        Metodo Que Dibuja El Objeto Ball En La Pantalla En Sus Coordenadas Dadas ...
        '''

        self.ball = pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radio) 



    def mover(self) :

        '''
        Metodo Que Realiza El Movimiento Del Objeto Ball ...
        '''

        self.x += self.speed_x
        self.y += self.speed_y



    #!SIN TERMINAR POR ERRORES
    def fisica_ball(self, raqueta1, raqueta2) -> None :

        top_ball = False
        bottom_ball = False
        bottom_ball_down = False
        top_ball_down = False
        bottom_left_ball = False
        bottom_right_ball = False
        top_left_ball = False
        top_right_ball = False

        if self.ball.colliderect(raqueta1) :

            self.speed_x = 13 

            if raqueta1.rect.left < self.x and self.x + self.ball.width < raqueta1.rect.right : #todo - comprueba si la pelota esta en el centro del top o bottom de la raqueta 

                self.speed_x = choice([2, -2]) 

                if self.ball.bottom - 1 == raqueta1.rect.top : #todo - la pelota colisiono con el bottom de la raqueta

                    self.speed_y = -10
                    bottom_ball = True

                else :                                       #todo - la pelota colisiono con el top de la raqueta

                    top_ball_down = True
                    self.speed_y = 10


            elif self.x < raqueta1.rect.x + raqueta1.rect.width // 2 : #todo - la pelota colisiono con la esquina izquierda de la raqueta

                self.speed_x = -2

                if self.ball.bottom - 1 == raqueta1.rect.top : #todo - del bottom de la raqueta

                    self.speed_y = -10
                    bottom_left_ball = True

                else :                                         #todo - del top de la raqueta

                    top_left_ball = True
                    self.speed_y = 10

            
            elif self.x > raqueta1.rect.width // 2 and (self.ball.bottom -1 == raqueta1.rect.top or self.ball.top +1 == raqueta1.rect.bottom ) : #todo - la pelota colisiono con la esquina derecha de la raqueta


                self.speed_x = -2

                if self.ball.bottom - 1 == raqueta1.rect.top : 

                    self.speed_y = -10
                    bottom_right_ball = True

                else :

                    top_right_ball = True
                    self.speed_y = 10


            elif raqueta1.move_direction == 'Up' :

                self.speed_y = choice([-3, -4, -5])

            elif raqueta1.move_direction == 'Down' :

                self.speed_y = choice([3, 4, 5])

            else :

                pass
            
            sound_ball.play()



        elif self.ball.colliderect(raqueta2) :
            
            self.speed_x = -13

            if raqueta2.rect.left < self.x and self.x + self.ball.width < raqueta2.rect.right :


                self.speed_x = choice([2, -2]) 

                if self.ball.bottom - 1 == raqueta2.rect.top  : 

                    self.speed_y = -10
                    bottom_ball = True

                else :

                    top_ball_down = True
                    self.speed_y = 10 

            
            elif self.x < raqueta2.rect.x + raqueta2.rect.width // 2 and self.ball.right > raqueta2.rect.left + 6 : #todo - la pelota colisiono con la esquina izquierda de la raqueta
                
                self.speed_x = -2

                if self.ball.bottom - 1 == raqueta2.rect.top : #todo - del bottom de la raqueta

                    self.speed_y = -10
                    bottom_left_ball = True

                else :                                         #todo - del top de la raqueta

                    top_left_ball = True
                    self.speed_y = 10

            
            elif self.x > raqueta2.rect.width // 2 and (self.ball.bottom -1 == raqueta2.rect.top or self.ball.top +1 == raqueta2.rect.bottom ) : #todo - la pelota colisiono con la esquina derecha de la raqueta
                

                self.speed_x = -2

                if self.ball.bottom - 1 == raqueta2.rect.top : 

                    self.speed_y = -10
                    bottom_right_ball = True

                else :

                    top_right_ball = True
                    self.speed_y = 10

                


            elif raqueta2.move_direction == 'Up' :

                self.speed_y = choice([-3, -4, -5])

            elif raqueta2.move_direction == 'Down' :

                self.speed_y = choice([3, 4, 5])

            else :

                pass

            sound_ball.play()

        
        if self.ball.top - 26 <= 0 :
            
            self.speed_x = 13 if str(self.speed_x)[0] != '-' else -13
            self.speed_y = 4
            sound_ball.play()
            top_ball = True
            top_left_ball = True
            top_right_ball = True 

        elif self.y + self.ball.height >= ALTO :

            self.speed_x = 13 if str(self.speed_x)[0] != '-' else -13
            self.speed_y = -4
            bottom_ball_down = True
            bottom_left_ball = True 
            bottom_right_ball = True
            sound_ball.play() 

        if (top_ball and bottom_ball) or (top_ball_down and bottom_ball_down) :

            self.speed_x = -50
            self.speed_y = 0
            print('-------------------------------------')

        elif (bottom_left_ball and top_left_ball) :

            self.speed_x = -50
            self.speed_y = 0

        elif (bottom_right_ball and top_right_ball) :

            self.speed_x = 50
            self.speed_y = 0





    def colisiones(self, *raquetas) :

        '''
        Metodo Que Comprueba Las Colisiones Del Objeto Ball ...
        '''

        if Ball.nivel == 'two' or Ball.nivel == 'three' :

            if self.ball.colliderect(raquetas[2]) :
                
                
                if raquetas[2].rect.top + 10 > self.ball.bottom >= raquetas[2].rect.top and self.ball.right - 3 >= raquetas[2].rect.left and self.ball.left + 3 <= raquetas[2].rect.right :

                    self.speed_y *= - 1

                elif raquetas[2].rect.bottom - 10 < self.ball.top <= raquetas[2].rect.bottom and self.ball.right - 3 >= raquetas[2].rect.left and self.ball.left + 3 <= raquetas[2].rect.right :

                    self.speed_y *= - 1

                else :

                    self.speed_x *= -1
                    
                sound_ball.play() 


            elif self.ball.colliderect(raquetas[3]) :

                

                if raquetas[3].rect.top + 10 > self.ball.bottom >= raquetas[3].rect.top and self.ball.right - 3 >= raquetas[3].rect.left and self.ball.left + 3 <= raquetas[3].rect.right :

                    self.speed_y *= - 1

                elif raquetas[3].rect.bottom - 10 < self.ball.top <= raquetas[3].rect.bottom and self.ball.right - 3 >= raquetas[3].rect.left and self.ball.left + 3 <= raquetas[3].rect.right :

                    self.speed_y *= - 1

                else :

                    self.speed_x *= -1

                sound_ball.play() 



        if self.ball.colliderect(raquetas[0]) :

            self.speed_x = 13

            if raquetas[0].move_direction == 'Up' :

                self.speed_y = choice([-3, -4, -5]) 

            elif raquetas[0].move_direction == 'Down' :

                self.speed_y = choice([3, 4, 5]) 

            else :

                self.speed_y = 0
            sound_ball.play() 

        
        elif self.ball.colliderect(raquetas[1]) :

            self.speed_x = -13

            if raquetas[1].move_direction == 'Up' :

                self.speed_y = choice([-3, -4, -5]) 

            elif raquetas[1].move_direction == 'Down' :

                self.speed_y = choice([3, 4, 5])

            else :

                self.speed_y = 0
            sound_ball.play()


        if self.y - 25 <= 0 :

            self.speed_y = choice([3, 4, 5])
            sound_ball.play()

        
        elif self.y + self.ball.height >= ALTO :

            self.speed_y = choice([-3, -4, -5])
            sound_ball.play()





# =====================----------- CLASE RAQUETA QUE HEREDA DE LA CLASE Sprite DEL MODULO pygame.sprite------------==========================
class Raqueta(pygame.sprite.Sprite) :

    nivel = 'one'


    def __init__(self, posx, posy, color, side= 'right', width= 20, height= 100, objectball= None) :

        super().__init__()
        self.image = pygame.Surface((width, height)) 
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy) 
        self.move_direction = 'Center'
        self.state = side
        self.ball = objectball
        


    def update(self) :

        keys = pygame.key.get_pressed()

        if self.state == 'right' :

            if keys[pygame.K_w] :
                
                self.move_direction = 'Up'
                self.rect.y -= 15

                if self.rect.top - 25 <= 0 :

                    self.rect.top = 10

            if keys[pygame.K_s] :

                self.move_direction = 'Down' 
                self.rect.y += 15

                if self.rect.bottom + 10 >= ALTO :

                    self.rect.bottom = ALTO - 10



        elif self.state == 'left' :

            self.move_IA(self.ball)

        
        elif self.state == 'static' :

            pass



    def move_IA(self, ball) :
        
        alcanze = ball.x >= ANCHO // 2 - 50 

        if ball.y < self.rect.y + self.rect.height // 2 and alcanze :  

            if self.rect.top - 25 <= 0 :

                    self.rect.top = 10

            else :

                self.rect.y -= 8
                self.move_direction = 'Up'

        elif ball.y > self.rect.y + self.rect.height // 2 and alcanze :


            if self.rect.bottom + 10 >= ALTO :

                self.rect.bottom = ALTO - 10

            else :

                self.rect.y += 8
                self.move_direction = 'Down'

        else :

            pass





class Button :


    def __init__(self, image, x, y) -> None:
        

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.topleft = (x, y)
        self.accion = False


    def show(self) :

        PANTALLA.blit(self.image, (self.rect.x, self.rect.y))


    def check(self) :

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) :

            clicks = pygame.mouse.get_pressed()

            if clicks[0] and not(self.accion) :

                print('HA PRESIONADO CLICK') 
                self.accion = True

            elif not clicks[0] :

                self.accion = False







#FUNCION QUE MANEJARA LOS EVENTOS DE MOUSE Y TECLADO EN EL BUCLE PRINCIPAL DEL JUEGO
def eventos_keyboard(ball, jugar) :


    for event in pygame.event.get() :

            if event.type == pygame.QUIT :

                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN :

                if event.key == pygame.K_SPACE and not(jugar) :

                    ball.speed_x = random.choice([13, -13])
                    ball.speed_y = 0
                    jugar = True
                
                if event.key == pygame.K_RETURN :

                    pass




#FUNCION DE DIBUJO
def draw_objets(point1, point2, raquetas, ball) :

    PANTALLA.fill((0, 0, 0))

    pygame.draw.line(PANTALLA, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO), 5)
    pygame.draw.rect(PANTALLA, (0, 180, 0), (0, 0, ANCHO, ALTO), 10, 20)

    raquetas.draw(PANTALLA)
    raquetas.update() 

    ball.mover() 
    ball.show()
    score(PANTALLA, str(point1), (255, 255, 255), ANCHO // 4, ALTO // 8)
    score(PANTALLA, str(point2), (255, 255, 255), ANCHO - ANCHO // 4, ALTO // 8)




#FUNCION QUE SERVIRA PARA SABER SI LA PELOTA HA SALIDO DE LA PANTALLA
def ball_out(ball, point1, point2) :

    if ball.x > ANCHO  :

        point1 += 1
        return True, point1, point2
        
    elif ball.x < 0 :

        point2 += 1
        return True, point1, point2
    
    return 0, point1, point2




# ---------------- FUNCION PARA MOSTRAR PUNTUACION -------------------
def score(pantalla, texto,color, x, y) :

    tipo_letra = pygame.font.SysFont('Courier', 50, True ,True )
    superficie = tipo_letra.render(texto, True, color) 
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie,rectangulo)









#PALETA DE COLORES
BLANCO = 255, 255, 255

# ------------------------ ESTRUCTURA BASICA DE PYGAME --------------------------------------
pygame.init()

SIZE = ANCHO, ALTO = 800, 500
PANTALLA = pygame.display.set_mode(SIZE)
RELOJ = pygame.time.Clock() 
#--------------------------------------------------------------------------------------------

# ----------------------------- CONFIGURACION DE SONIDOS ------------------------------------
mixer.init()
sound_ball = mixer.Sound(r'learnPygame\sounds\sound_ball2.mp3')  
# -------------------------------------------------------------------------------------------



def menu() :

    img_detener = pygame.transform.scale(pygame.image.load(r'learnPygame\IMAGENES\detener.png').convert(), (80, 80))

    img_play = pygame.transform.scale(pygame.image.load(r'learnPygame\IMAGENES\play.png').convert(), (80, 80))
    btn1 = Button(img_detener, ANCHO // 4, ALTO // 2)
    btn2 = Button(img_play, ANCHO - ANCHO // 4, ALTO // 2)

    while True :


        for event in pygame.event.get() :

            if event.type == pygame.QUIT :

                pygame.quit()
                sys.exit()

        PANTALLA.fill((0, 0, 0))
        btn1.show()
        btn2.show()
        btn1.check()
        btn2.check()

        pygame.display.flip() 






def level_one(point_player1 = 0,
    point_player2 = 0) :

    ball = Ball(PANTALLA, (255, 255, 255), (ANCHO // 2, ALTO // 2), 15)
    pygame.draw.line(PANTALLA, (255, 255, 255), (ANCHO // 2, 0), (ANCHO // 2, ALTO), 3) 
    
    raqueta1 = Raqueta(30, ALTO // 2, BLANCO, 'right', 20, 100, ball) 
    raqueta2 = Raqueta(ANCHO - 30, ALTO // 2, BLANCO, 'left', 20, 100, ball)     
    raquetas = pygame.sprite.Group(raqueta1, raqueta2) 
    
    jugar = False
    

    while True :

        RELOJ.tick(60)
        #--------------------------

        eventos_keyboard(ball, jugar) 

        #----------------------------- COLISIONES DELA PELOTA --------------------------
        ball.colisiones(raqueta1, raqueta2) 

        # ------------------------------------ DIBUJOS ---------------------------------------------------

        draw_objets(point_player1, point_player2, raquetas, ball)

        # --------------------------------------------------------------------------------------------

        # ------------ PELOTA FUERA DE RANGO ----------------------
        out = ball_out(ball, point_player1, point_player2)

        if out :
            break
    

        pygame.display.flip()  

    level_one(point_player1, point_player2)






def level_two(point_player1 = 0,
    point_player2 = 0) :

    ball = Ball(PANTALLA, (255, 255, 255), (ANCHO // 2, ALTO // 2), 15)
    Ball.nivel = 'two'
    pygame.draw.line(PANTALLA, (255, 255, 255), (ANCHO // 2, 0), (ANCHO // 2, ALTO), 3) 
    
    raqueta1 = Raqueta(30, ALTO // 2, BLANCO, 'right', 20, 100, ball) 
    raqueta2 = Raqueta(ANCHO - 30, ALTO // 2, BLANCO, 'left', 20, 100, ball)
    raqueta3 = Raqueta(ANCHO // 2 - 50, ALTO // 4, BLANCO, 'static', 20, 50, ball) 
    raqueta4 = Raqueta(ANCHO // 2 + 50,ALTO - ALTO // 4, BLANCO, 'static', 20, 50, ball)
    Raqueta.nivel = 'two' 
    raquetas = pygame.sprite.Group(raqueta1, raqueta2, raqueta3, raqueta4)   
    jugar = False
    

    while True :

        RELOJ.tick(60)
        #--------------------------

        eventos_keyboard(ball, jugar) 

        #----------------------------- COLISIONES DELA PELOTA --------------------------
        ball.colisiones(raqueta1, raqueta2, raqueta3, raqueta4)  

        # ------------------------------------ DIBUJOS ---------------------------------------------------

        draw_objets(point_player1, point_player2, raquetas, ball)

        # --------------------------------------------------------------------------------------------

        # ------------ PELOTA FUERA DE RANGO ----------------------
        out, point_player1, point_player2 = ball_out(ball, point_player1, point_player2)

        if out :
            break
    

        pygame.display.flip()  

    level_two(point_player1, point_player2)





if __name__ == '__main__' :

    menu()

    vueltas = 5

    while vueltas > 0 :

        level_two() 
