import pygame
from pygame.locals import *

pygame.init()

#screen size
screen_width = 6000
screen_height = 700
block_height = 70
block_width = 70


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Medieval Game")

#map images############################################################################

one_block_img = pygame.image.load('images/Tiles/1block.png')
one_block = pygame.transform.scale(one_block_img, (block_width, block_height))

sign_img = pygame.image.load("images/Tiles/sign1.png")
sign = pygame.transform.scale(sign_img, (block_width, block_height))

key_img = pygame.image.load("images/Tiles/Key.png")
key = pygame.transform.scale(key_img, (block_width, block_height/2))

big_platform_DARK_img = pygame.image.load("images/Tiles/big_platform_DARK.png")
big_platform_DARK = pygame.transform.scale(big_platform_DARK_img, (block_width*6 , block_height*4))

big_platform_LIGHT_img = pygame.image.load("images/Tiles/big_platform_LIGHT.png")
big_platform_LIGHT = pygame.transform.scale(big_platform_LIGHT_img, (block_width*6 , block_height*4))

forest_background = pygame.image.load("images/Backgrounds/length_5_bg.png")

ground_platform_DARK_img = pygame.image.load("images/Tiles/ground_platform_DARK.png")
groudn_platform_DARK = pygame.transform.scale(ground_platform_DARK_img, (block_width*6 , block_height))

ground_platform_LIGHT_img = pygame.image.load("images/Tiles/ground_platform_LIGHT.png")
ground_platform_LIGHT = pygame.transform.scale(ground_platform_LIGHT_img, (block_width*6 , block_height))

spike_img = pygame.image.load("images/Tiles/spike1.png")
spike = pygame.transform.scale(spike_img, (block_width, block_height))

###################################################################################


run = True
while run:

    #BACKGROUND
    screen.blit(forest_background, (0,0))

    #SPIKES
    screen.blit(spike, (850,570))
    screen.blit(spike, (785,570))
    screen.blit(spike, (720,570))
    screen.blit(spike, (655,570))

    screen.blit(spike, (1200,570))
    screen.blit(spike, (1265,570))
    screen.blit(spike, (65+1265,570))
    screen.blit(spike, (65+65+1265,570))
    screen.blit(spike, (65+65+65+1265,570))
    screen.blit(spike, (65+65+65+65+1265,570))
    screen.blit(spike, (65+65+65+65+65+1265,570))
    screen.blit(spike, (65+65+65+65+65+65+1265,570))
    screen.blit(spike, (65+65+65+65+65+65+65+1265,570))

    screen.blit(spike, (65+65+65+65+65+65+65+65+65+65+65+1265,370))
    screen.blit(spike, (65+65+65+65+65+65+65+65+65+65+65+65+1265,370))


    screen.blit(spike, (2330,500+70))
    screen.blit(spike, (2330+70+70,500+70))
    screen.blit(spike, (2330+70+70+70+70,500+70))
    screen.blit(spike, (2330+70+70+70+70+70+70,500+70))

    screen.blit(spike, (2330+70+70+70+70+70+70+70+70,500+70+35))
    screen.blit(spike, (2330+70+70+70+70+70+70+70+70+70,500+70+35))
    screen.blit(spike, (2330+70+70+70+70+70+70+70+70+70+70,500+70+35))
    screen.blit(spike, (2330+70+70+70+70+70+70+70+70+70+70+70,500+70+35))

    screen.blit(spike, (3350,500+70))
    screen.blit(spike, (3350+140+70,500+70))

    screen.blit(spike, (4300,500+70))
    screen.blit(spike, (4300+70,500+70))
    screen.blit(spike, (4300+70+70,500+70))
    screen.blit(spike, (4300+70+70+70,500+70))
    screen.blit(spike, (4300+70+70+70+70,500+70))
    screen.blit(spike, (4300+70+70+70+70+70,500+70))
    screen.blit(spike, (4300+70+70+70+70+70+70,500+70))
    screen.blit(spike, (4300+70+70+70+70+70+70+70,500+70))
    screen.blit(spike, (4300+70+70+70+70+70+70+70+70,500+70))
    screen.blit(spike, (4300+70+70+70+70+70+70+70+70+70,500+70))

    screen.blit(spike, (5360,500+70))
    screen.blit(spike, (5360+70,500+70))
    screen.blit(spike, (5360+70+70,500+70))
    screen.blit(spike, (5360+70+70+70,500+70))
    screen.blit(spike, (5360+70+70+70+70,500+70))

    #SINGLE BLOCK
    screen.blit(one_block, (1655-65-65,370))
    screen.blit(one_block, (1655-65,370))
    screen.blit(one_block, (2400,500))
    screen.blit(one_block, (2400+70+70,500-70-35))
    screen.blit(one_block, (2400+70+70+70+70,500-70-35-70-35))
    screen.blit(one_block, (3740,500+70))
    screen.blit(one_block, (4500,420))
    screen.blit(one_block, (4750,420))


    #PLATFORMS
    screen.blit(big_platform_LIGHT, (320,510))
    screen.blit(big_platform_DARK, (850,410))
    screen.blit(big_platform_DARK, (2400+70+70+70+70+70+70,500-70-35-70-35-70-35))
    screen.blit(big_platform_LIGHT, (3900,500-70))
    screen.blit(big_platform_LIGHT, (5000,500-70))
    screen.blit(big_platform_LIGHT, (5600,350))
    #DECOR
    screen.blit(sign, (50,565))

    #KEY
    screen.blit(key,(5900,290))

    #GROUND
    screen.blit(ground_platform_LIGHT, (0,630))
    screen.blit(ground_platform_LIGHT, (410,630))
    screen.blit(ground_platform_LIGHT, (820,630))
    screen.blit(ground_platform_LIGHT, (410+820,630))
    screen.blit(ground_platform_LIGHT, (820+820,630))
    screen.blit(ground_platform_LIGHT, (410+820+820,630))
    screen.blit(ground_platform_LIGHT, (200+820+820,430))
    screen.blit(ground_platform_LIGHT, (410+410+820+820,630))
    screen.blit(ground_platform_LIGHT, (410+410+820+820+410+310,630))
    screen.blit(ground_platform_LIGHT, (410+410+820+820+410+310+410,630))
    screen.blit(ground_platform_LIGHT, (410+410+410+820+820+410+310+410,630))
    screen.blit(ground_platform_LIGHT, (410+410+410+820+820+410+310+410,630))
    screen.blit(ground_platform_LIGHT, (410+410+410+410+820+820+410+310+410,630))
    screen.blit(ground_platform_LIGHT, (410+410+410+410+410+820+820+410+310+410,630))
    screen.blit(ground_platform_LIGHT, (410+410+410+410+410+410+820+820+410+310+410,630))
    screen.blit(ground_platform_LIGHT, (410+410+410+410+410+410+410+820+820+410+310+410,630))

    #quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
