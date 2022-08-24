
import pygame
from pygame.locals import *

pygame.init()

#screen size
screen_width = 1200
screen_height = 4200
block_height = 70
block_width = 70


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Medieval Game")

#map images############################################################################

background = pygame.image.load('images/Backgrounds/level2_bg.png')

###################################################################################


run = True
while run:

    #BACKGROUND
    screen.blit(background, (0,0))

    #quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()