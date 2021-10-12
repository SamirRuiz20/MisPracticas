import pygame
from pygame.draw import circle
import sys

celuleGrid = [(30, 30), (300, 30), (570, 30), (123, 122), (300, 122), (477, 122), (214, 215), (300, 215), (386, 215), 
        (30, 300), (123, 300), (214, 300), (386, 300), (477, 300), (570, 300), (214, 385), (300, 385), (386, 385), (123, 478), (300, 478), (477, 478), (30, 570),
        (300, 570), (570, 570)]

pygame.init()

pygame.display.set_caption("Alexiu Adrian - Nine men's morris")

ecran = pygame.display.set_mode(size=(600, 600))

background_image = pygame.image.load(r"IMAGENES\background.png").convert()

ecran.blit(background_image, [0, 0])

pygame.draw.circle(ecran, (0, 0, 0), (30, 30), 10, 5)

pygame.draw.circle(ecran, (0, 0, 0), (300, 30), 10)

pygame.draw.circle(ecran, (0, 0, 0), (570, 30), 10)


pygame.draw.circle(ecran, (0, 0, 0), (123, 122), 10)

pygame.draw.circle(ecran, (0, 0, 0), (300, 122), 10)

pygame.draw.circle(ecran, (0, 0, 0), (477, 122), 10)


pygame.draw.circle(ecran, (0, 0, 0), (214, 215), 10)

pygame.draw.circle(ecran, (0, 0, 0), (300, 215), 10)

pygame.draw.circle(ecran, (0, 0, 0), (386, 215), 10)


pygame.draw.circle(ecran, (0, 0, 0), (30, 300), 10)

pygame.draw.circle(ecran, (0, 0, 0), (123, 300), 10)

pygame.draw.circle(ecran, (0, 0, 0), (214, 300), 10)

pygame.draw.circle(ecran, (0, 0, 0), (386, 300), 10)

pygame.draw.circle(ecran, (0, 0, 0), (477, 300), 10)

pygame.draw.circle(ecran, (0, 0, 0), (570, 300), 10)


pygame.draw.circle(ecran, (0, 0, 0), (214, 385), 10)

pygame.draw.circle(ecran, (0, 0, 0), (300, 385), 10)

pygame.draw.circle(ecran, (0, 0, 0), (386, 385), 10)


pygame.draw.circle(ecran, (0, 0, 0), (123, 478), 10)

pygame.draw.circle(ecran, (0, 0, 0), (300, 478), 10)

pygame.draw.circle(ecran, (0, 0, 0), (477, 478), 10)


pygame.draw.circle(ecran, (0, 0, 0), (30, 570), 10)

pygame.draw.circle(ecran, (0, 0, 0), (300, 570), 10)

pygame.draw.circle(ecran, (0, 0, 0), (570, 570), 10)

pygame.display.flip()

while True:

    ecran.blit(background_image, [0, 0])

    pygame.draw.circle(ecran, (0, 0, 0), (30, 30), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (300, 30), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (570, 30), 10)


    pygame.draw.circle(ecran, (0, 0, 0), (123, 122), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (300, 122), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (477, 122), 10)


    pygame.draw.circle(ecran, (0, 0, 0), (214, 215), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (300, 215), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (386, 215), 10)


    pygame.draw.circle(ecran, (0, 0, 0), (30, 300), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (123, 300), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (214, 300), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (386, 300), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (477, 300), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (570, 300), 10)


    pygame.draw.circle(ecran, (0, 0, 0), (214, 385), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (300, 385), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (386, 385), 10)


    pygame.draw.circle(ecran, (0, 0, 0), (123, 478), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (300, 478), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (477, 478), 10)


    pygame.draw.circle(ecran, (0, 0, 0), (30, 570), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (300, 570), 10)

    pygame.draw.circle(ecran, (0, 0, 0), (570, 570), 10)

    def is_in_circle(point, center):
        print()
        for line in range(center[1] - 10, center[1] + 10):
            for column in range(center[0] - 10, center[0] + 10):
                if column == point[0] and line == point[1]:
                    return True
        
        return False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # inchide fereastra
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
    
            pos = pygame.mouse.get_pos()
            for position in celuleGrid:
                if is_in_circle(pos, position):
                    
                    print((position[1], position[0]))
                    pygame.draw.circle(ecran, (255, 255, 255), (position[0], position[1]), 25)

            pygame.display.flip()