#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont(None, 50)

def draw_text(text, font, color, surface, x, y):
    textobj = pygame.transform.rotate(font.render(text, 1, color, 'red'), 0)
    textrect = textobj.get_rect()
    
    textrect.topleft = (x, y)
    
    return textrect, textobj

click = False


def main_menu():

    while True:

        screen.fill((0,0,0))
        
        
        
        r, obj = draw_text('Menu Principal', font, (0, 0, 255), screen, 20, 20)

        #surface = pygame.Surface(( r.width, r.height)) 
        #surface.fill((0, 255, 0))

        #screen.blit(surface, (20, 20))
        screen.blit(obj, r) 

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                print('45')
                #game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()