
from platform import platform
import pygame
from pygame.locals import *

pygame.init()

#READ THIS
#screen size
# add /2.5 for user friendly view
# delete any division for proper scale view

screen_width = 1200/2.5
screen_height = 4200/2.5
block_height = 70/2.5
block_width = 70/2.5

#READ THIS
#change to "1" for user friendly view
#change to "2.5" for proper scale view
scale_variable = 1



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Medieval Game")

#map images############################################################################

background_img = pygame.image.load('images/Backgrounds/level2_bg.png')
background = pygame.transform.scale(background_img, (screen_width, screen_height))

platform_img = pygame.image.load('images/Tiles/platform_lv2.png')
platform_block = pygame.transform.scale(platform_img, (block_width*6,block_height))

block_img = pygame.image.load('images/Tiles/block_lv2.png')
block = pygame.transform.scale(block_img, (block_width*1.8,block_height))

spike_img = pygame.image.load('images/Tiles/spike_lv2.png')
spike = pygame.transform.scale(spike_img, (block_width,block_height/1.15))

key_img = pygame.image.load('images/Tiles/key.png')
key = pygame.transform.scale(key_img, (block_width,block_height/2))

###################################################################################


run = True
while run:

    #BACKGROUND
    screen.blit(background, (0,0))

    #PLATFORM
    screen.blit(platform_block, (310*scale_variable,1637*scale_variable))
    screen.blit(platform_block, (348*scale_variable,1610*scale_variable))
    screen.blit(platform_block, (386*scale_variable,1583*scale_variable))

    screen.blit(platform_block, (65*scale_variable,1533*scale_variable))

    screen.blit(platform_block, (330*scale_variable,1360*scale_variable))

    screen.blit(platform_block, (230*scale_variable,1286*scale_variable))

    screen.blit(platform_block, (40*scale_variable,1260*scale_variable))

    screen.blit(platform_block, (95*scale_variable,1110*scale_variable))

    screen.blit(platform_block, (290*scale_variable,1083*scale_variable))

    screen.blit(platform_block, (150*scale_variable,980*scale_variable))

    screen.blit(platform_block, (400*scale_variable,740*scale_variable))

    screen.blit(platform_block, (440*scale_variable,712 *scale_variable))

    screen.blit(platform_block, (230*scale_variable,675*scale_variable))
    screen.blit(platform_block, (20*scale_variable,675*scale_variable))

    screen.blit(platform_block, (250*scale_variable,460*scale_variable))
    screen.blit(platform_block, (400*scale_variable,435*scale_variable))

    screen.blit(platform_block, (130*scale_variable,380*scale_variable))
    screen.blit(platform_block, (-30*scale_variable,350*scale_variable))

    screen.blit(platform_block, (150*scale_variable,50*scale_variable))
    screen.blit(platform_block, (-10*scale_variable,50*scale_variable))

    #BLOCK
    screen.blit(block, (270*scale_variable,1560*scale_variable))

    screen.blit(block, (00*scale_variable,1500*scale_variable))
    screen.blit(block, (80*scale_variable,1460*scale_variable))
    screen.blit(block, (160*scale_variable,1420*scale_variable))
    screen.blit(block, (240*scale_variable,1380*scale_variable))

    screen.blit(block, (430*scale_variable,1334*scale_variable))

    screen.blit(block, (200*scale_variable,1260*scale_variable))

    screen.blit(block, (0*scale_variable,1230*scale_variable))

    screen.blit(block, (80*scale_variable,1190*scale_variable))

    screen.blit(block, (0*scale_variable,1140*scale_variable))

    screen.blit(block, (430*scale_variable,1055*scale_variable))

    screen.blit(block, (350*scale_variable,1015*scale_variable))

    screen.blit(block, (65*scale_variable,960*scale_variable))

    screen.blit(block, (0*scale_variable,930*scale_variable))

    screen.blit(block, (80*scale_variable,885*scale_variable))
    screen.blit(block, (160*scale_variable,845*scale_variable))
    screen.blit(block, (240*scale_variable,805*scale_variable))
    screen.blit(block, (320*scale_variable,765*scale_variable))

    screen.blit(block, (0*scale_variable,647*scale_variable))
    screen.blit(block, (80*scale_variable,610*scale_variable))
    screen.blit(block, (0*scale_variable,560*scale_variable))
    screen.blit(block, (80*scale_variable,520*scale_variable))
    screen.blit(block, (160*scale_variable,480*scale_variable))

    screen.blit(block, (330*scale_variable,390*scale_variable))

    screen.blit(block, (0*scale_variable,322*scale_variable))
    screen.blit(block, (80*scale_variable,282*scale_variable))
    screen.blit(block, (160*scale_variable,242*scale_variable))
    screen.blit(block, (240*scale_variable,202*scale_variable))
    screen.blit(block, (320*scale_variable,162*scale_variable))
    screen.blit(block, (400*scale_variable,122*scale_variable))
    screen.blit(block, (320*scale_variable,75*scale_variable))
    
    #SPIKE
    screen.blit(spike, (165*scale_variable,1510*scale_variable))
    screen.blit(spike, (330*scale_variable,1264*scale_variable))
    screen.blit(spike, (160*scale_variable,1238*scale_variable))
    screen.blit(spike, (140*scale_variable,1086*scale_variable))
    screen.blit(spike, (330*scale_variable,652*scale_variable))
    screen.blit(spike, (290*scale_variable,437*scale_variable))
    screen.blit(spike, (250*scale_variable,27*scale_variable))

    #key
    screen.blit(key, (20*scale_variable,27*scale_variable))

    #quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
