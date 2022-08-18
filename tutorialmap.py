import pygame
from pygame.locals import *

pygame.init()

#screen size
screen_width = 1125
screen_height = 416
block_height = 65
block_width = 65


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Medieval Game")

#map images############################################################################

one_block_img = pygame.image.load(r'C:\Users\arthu\Downloads\img\1block.png')
one_block = pygame.transform.scale(one_block_img, (block_width, block_height))

sign_img = pygame.image.load(r"C:\Users\arthu\Downloads\img\sign1.png")
sign = pygame.transform.scale(sign_img, (block_width, block_height))

key_img = pygame.image.load(r"C:\Users\arthu\Downloads\img\Key.png")
key = pygame.transform.scale(key_img, (block_width, block_height/2))

big_platform_DARK_img = pygame.image.load(r"C:\Users\arthu\Downloads\img\big_platform_DARK.png")
big_platform_DARK = pygame.transform.scale(big_platform_DARK_img, (block_width*6 , block_height*4))

big_platform_LIGHT_img = pygame.image.load(r"C:\Users\arthu\Downloads\img\big_platform_LIGHT.png")
big_platform_LIGHT = pygame.transform.scale(big_platform_LIGHT_img, (block_width*6 , block_height*4))

forest_background = pygame.image.load(r"C:\Users\arthu\Downloads\img\blur_forest_BACKGROUND.png")

ground_platform_DARK_img = pygame.image.load(r"C:\Users\arthu\Downloads\img\ground_platform_DARK.png")
groudn_platform_DARK = pygame.transform.scale(ground_platform_DARK_img, (block_width*6 , block_height))

ground_platform_LIGHT_img = pygame.image.load(r"C:\Users\arthu\Downloads\img\ground_platform_LIGHT.png")
ground_platform_LIGHT = pygame.transform.scale(ground_platform_LIGHT_img, (block_width*6 , block_height))

spike_img = pygame.image.load(r"C:\Users\arthu\Downloads\img\spike1.png")
spike = pygame.transform.scale(spike_img, (block_width, block_height))

###################################################################################


run = True
while run:

    #BACKGROUND
    screen.blit(forest_background, (0,0))
    #SPIKES
    screen.blit(spike, (850,320))
    screen.blit(spike, (785,320))
    screen.blit(spike, (720,320))
    screen.blit(spike, (655,320))
    #PLATFORMS
    screen.blit(big_platform_LIGHT, (350,250))
    screen.blit(big_platform_DARK, (850,180))
    #DECOR
    screen.blit(sign, (90,305))
    screen.blit(key, (1030,130))
    #GROUND
    screen.blit(ground_platform_LIGHT, (0,370))
    screen.blit(ground_platform_LIGHT, (390,370))
    screen.blit(ground_platform_LIGHT, (780,370))

    #quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()