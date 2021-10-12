import pygame



#Tamaño de pantalla
ANCHO = 600
ALTO = 600

#FPS
FPS = 30

# Paleta de colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE= (0,255,0)
AZUL = (0,0,255)
H_50D2FE = (94,210,254)
GREEN = (0, 255, 0) 
RANDOM = (0, 255, 255)

class Jugador(pygame.sprite.Sprite) :


    # Sprite del jugador
    def __init__(self, color, speed= 1, dire= 'Y', size= (ANCHO // 2, ALTO // 2) ) :

        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.Surface((30, 200))
        self.speed = speed 
        self.direc = dire
        self.image.fill(color)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = size 



    def update(self):
        # Actualiza esto cada vuelta de bucle.
        if self.direc == 'Y' :
            
            self.rect.y += self.speed
            if self.rect.top > ALTO:
                self.rect.bottom = 0

        else :
        
            self.rect.x += self.speed
            if self.rect.left > ANCHO :
                self.rect.right = 0



# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()

#Grupo de sprites, instanciación del objeto jugador.
jugador = Jugador((255, 0, 0), 18)
jugador2 = Jugador(GREEN, 18, 'X')
jugador3 = Jugador(AZUL, 18, 'Y', (ANCHO // 4, ALTO // 2)) 
jugador4 = Jugador(RANDOM, 18, 'Y', (ANCHO - ANCHO // 4, ALTO // 2))   
sprites = pygame.sprite.Group(jugador, jugador2, jugador3, jugador4) 




# Bucle de juego
ejecutando = True
while ejecutando:

    # Es lo que especifica la velocidad del bucle de juego
    clock.tick(FPS)
    # Eventos
    for event in pygame.event.get():
        # Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False

    # Actualización de sprites


    # Fondo de pantalla, dibujo de sprites y formas geométricas.
    pantalla.fill(NEGRO)
    sprites.draw(pantalla)
    sprites.update()
    pygame.draw.line(pantalla, H_50D2FE, (300, 0), (300, 600), 5)
    pygame.draw.line(pantalla, AZUL, (0, 300), (600, 300), 5)
    # Actualiza el contenido de la pantalla.
    pygame.display.flip()

pygame.quit()