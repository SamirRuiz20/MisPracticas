''' CREACION DE UN MODULO PARA CREAR MENUS CON PYGAME '''

import pygame
import sys
from random import choice

from pygame import image
from pygame.mouse import get_pos




#COLORES
BLANCO = 255, 255, 255
NEGRO = 0, 0, 0
ROJO = 255, 0, 0
VERDE = 0, 255, 0
AZUL = 0, 0, 255



def cnf_merge(parametros, kw, cnf) :
    

    for key in kw.items() :

            if key[0] not  in parametros :
                
                raise KeyError(f'Parametro {key[0]} No Valido ')

            else :

                cnf[key[0]] = key[1]

    if not(type(cnf['x']) is int and type(cnf['y']) is int) :

        raise ValueError(f'Error -> tipo de x e y deberia ser <int>!!')

    if not(cnf['label']) and not(cnf['image']) :

        raise ValueError(f'Error -> Deberia pasarse un texto o imagen!!')

    return cnf




class Widget :


    def __init__(self, surface, cnf, kw, *args) -> None:

        
        self.parametros = args
        self.cnf = cnf

        self.surface = surface
        self.cnf = cnf_merge(self.parametros, kw, self.cnf)  

        if self.cnf['move'] == 'Y' :

            mover = choice(['UP', 'DOWN'])

        elif self.cnf['move'] == 'X' :

            mover = choice(['LEFT', 'RIGHT'])

        else :

            mover = None

        self.mover = mover
        self.desplazar = -8 if self.mover in ('UP', 'LEFT', None) else 8
        self.focus = False


    



class Label(Widget) :


    def __init__(self, surface= None, **kw) -> None :


        self.cnf = {
            'label' : None, 'image' : None, 'bg' : NEGRO, 'bd' : 0, 'bordercolor' : NEGRO,
            'activebordercolor' : None, 'font' : None, 'fg' : None, 'move' : None,
            'x' : None, 'y' : None, 'ipadx' : 1
        }

        self.parametros = [
            'label', 'image', 'bg', 'fg', 'font', 'bd', 'bordercolor', 'activebordercolor', 'x', 'y', 'move', 'ipadx'
        ]

        super().__init__(surface, self.cnf, kw, *self.parametros) 
        



    
    #DIBUJA EL LABEL CON LOS VALORES CLAVE-VALOR DADOS
    def draw(self) :

        if self.cnf['move'] == 'Y' :

            self.animacion('Y') 

        elif self.cnf['move'] == 'X' :

            self.animacion('X')
        


        if self.cnf['image'] :

            collag = self.cnf['image']
            size = self.cnf['image'].get_rect()
            width, height = size.width, size.height
            rect = size

        elif self.cnf['label'] :

            font = pygame.font.SysFont(*self.cnf['font']) 
            texto = f"{self.cnf['ipadx']*' '}{self.cnf['label']}{self.cnf['ipadx']*' '}"
            collag = font.render(texto, True, self.cnf['fg']) 
            rect = collag.get_rect()
            width, height = rect.width, rect.height

            

        if self.cnf['bg'] :
            rect = pygame.draw.rect(self.surface, self.cnf['bg'], (self.cnf['x'] - self.cnf['bd'], self.cnf['y'] - self.cnf['bd'], width + (self.cnf['bd']*2), height + (self.cnf['bd']*2)), 0, 30 )

        else :
            rect = pygame.Rect(self.cnf['x'] - self.cnf['bd'], self.cnf['y'] - self.cnf['bd'], width + (self.cnf['bd']*2), height + (self.cnf['bd']*2)) 

        if self.cnf['bd'] > 0 :
            pygame.draw.rect(self.surface, self.cnf['bordercolor'], (self.cnf['x'] - self.cnf['bd'], self.cnf['y'] - self.cnf['bd'], width + (self.cnf['bd']*2), height + (self.cnf['bd']*2)), self.cnf['bd'], 30 )
        

        self.surface.blit(collag, (self.cnf['x'], self.cnf['y']))

        return rect


    

    def animacion(self, mover= None) :

        if mover == 'Y' :
            if self.mover == 'UP' :

                self.cnf['y'] = self.cnf['y'] - 1
                self.desplazar += 1
                if int(self.desplazar) == 8 :
                    self.mover = 'DOWN'


            else :

                self.cnf['y'] = self.cnf['y'] + 1
                self.desplazar -= 1
                if int(self.desplazar) == -8 :
                    self.mover = 'UP'


        elif mover == 'X' :
            if self.mover == 'LEFT' :

                self.cnf['x'] = self.cnf['x'] - 1
                self.desplazar += 1
                if int(self.desplazar) == 8 :
                    self.mover = 'RIGHT'


            else :

                self.cnf['x'] = self.cnf['x'] + 1
                self.desplazar -= 1
                if int(self.desplazar) == -8 :
                    self.mover = 'LEFT'






class Button(Label, Widget) :


    def __init__(self, surface=None, **kw) -> None:
        
        self.cnf = {
            'label' : None, 'image' : None, 'bg' : NEGRO, 'bd' : 0, 'bordercolor' : NEGRO,
            'activebordercolor' : None, 'font' : None, 'fg' : None, 'move' : None,
            'x' : None, 'y' : None, 'move_click' : False, 'side_bg_bottom' : None, 'command' : None, 'ipadx' : 1
        }


        self.parametros = [
            'label', 'image', 'bg', 'fg', 'font', 'bd', 'bordercolor', 'activebordercolor', 'x', 'y', 'move' ,'move_click', 'side_bg_bottom', 'command' ,'ipadx'
        ]
        
        Widget.__init__(self, surface, self.cnf, kw, *self.parametros)

        self.click = False
        self.focus = False
        self.elevar = 10 # atributo que servira para elvar el segundo boton para mostrar un efecto 3d





    def draw(self) :


        rect = super().draw()

        self.on_click(rect) 




    
    def on_click(self, rect) :

        pos = pygame.mouse.get_pos()

        if rect.collidepoint(pos) :

            click = pygame.mouse.get_pressed()[0]

            if click :

                self.click = True

            else :

                if self.click :

                    print('HA DADO CLICK DERECHO')
                    self.click = False

        else :

            self.click = False








class CheckButton(Label) :


    def __init__(self, surface=None, **kw) -> None:

        self.cnf = None
        self.parametros = [
            
        ]
        
        Widget.__init__(self ,surface, 0, 0, 0)











class Menu :

    list_menus = {

    }

    
    def __init__(self, screen= None) -> None:
        
        self.screen = screen
        self.crear_menus = True
        self.cont = 0
    

    def add_label(self, **kwargs) :

        if self.crear_menus :
            index = len(Menu.list_menus) 
            menu = Label(self.screen, **kwargs)          
            Menu.list_menus[index] = menu

        else :
            Menu.list_menus[len(Menu.list_menus) - (len(Menu.list_menus) - self.cont)].draw()    
            self.cont += 1
            if self.cont == len(Menu.list_menus) :
                self.cont = 0

    
    def add_button(self, **kwargs) :

        if self.crear_menus :
            index = len(Menu.list_menus) 
            menu = Button(self.screen, **kwargs)         
            Menu.list_menus[index] = menu

        else :
            Menu.list_menus[len(Menu.list_menus) - (len(Menu.list_menus) - self.cont)].draw()    
            self.cont += 1
            if self.cont == len(Menu.list_menus) :
                self.cont = 0

    
    def update(self) :

        self.crear_menus = False








def test() :

    pygame.init()


    PANTALLA = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Probando Modulo Menu') 

    img = pygame.image.load(r'learnPygame\IMAGENES\bg.png').convert()
    img2 = pygame.transform.scale(pygame.image.load(r'learnPygame\IMAGENES\arrow.png').convert(), (80, 150))

    #print(dir(img.get_rect()))

    menu1 = Menu(PANTALLA)

    def funcion() :

        print('HA presionado CLICK') 

    reloj = pygame.time.Clock()


    while True :

        
        reloj.tick(60)

        for event in pygame.event.get() :

            if event.type == pygame.QUIT :

                pygame.quit()
                sys.exit()

        PANTALLA.blit(pygame.transform.scale(img, (PANTALLA.get_rect().width, PANTALLA.get_rect().height)), (0, 0))

        menu1.add_label(label= 'Menu', bd= 0 , fg= (255, 0, 0), x= 50, y= 50, font= ('Verdana', 30), bg= None, move= 'Y') 
        menu1.add_label(move= 'X', label= 'Jugar', bd= 5, bordercolor= (0, 255, 0) , fg= (255, 0, 0), x= 100, y= 150, font= (None, 40), bg= None)
        menu1.add_label(label= 'Niveles', bd= 5, bordercolor= 'orange' , fg= (255, 0, 0), x= 90, y= 220, font= ('Verdana', 80), bg= (0, 255, 255))
        menu1.add_label(move= 'X', label= 'Jugar',bg= (0, 255, 255), bd= 5, bordercolor= (0, 0, 255) , fg= (255, 0, 0), x= 50, y= 320, font= ('Verdana', 50), ipadx= 2)
        menu1.add_label(move= 'Y', label= 'Logros',bg= 'yellow', bd= 5, bordercolor= (0, 255, 0) , fg= (255, 0, 0), x= 350, y= 320, font= ('Courier new', 35))
        menu1.add_button(label= 'Jugar', x= 350, y= 420, bd= 0, fg= 'red', move= None, font= (None ,100), bg= 'yellow', bordercolor= 'white', ipadx= 3)   

        #Menu.list_menus.clear() 
        menu1.update() 
        pygame.display.flip() 






if __name__ == '__main__' :

    test() 
