import pygame
import player, level_load
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

offset = 0

def load_level():
    global offset

    screen.blit(level_load.tutorial_bg, (offset, 0))

    #GROUND
    for x in range(16):
        #ground
        screen.blit(level_load.ground_platform_LIGHT, (0 + (390 * x) + offset, 640))

        #SPIKES
        screen.blit(level_load.spike, (850 + offset,570))
        screen.blit(level_load.spike, (785 + offset,570))
        screen.blit(level_load.spike, (720 + offset,570))
        screen.blit(level_load.spike, (655 + offset,570))

        screen.blit(level_load.spike, (1200 + offset,570))
        screen.blit(level_load.spike, (1265 + offset,570))
        screen.blit(level_load.spike, (65+1265 + offset,570))
        screen.blit(level_load.spike, (65+65+1265 + offset,570))
        screen.blit(level_load.spike, (65+65+65+1265 + offset,570))
        screen.blit(level_load.spike, (65+65+65+65+1265 + offset,570))
        screen.blit(level_load.spike, (65+65+65+65+65+1265 + offset,570))
        screen.blit(level_load.spike, (65+65+65+65+65+65+1265 + offset,570))
        screen.blit(level_load.spike, (65+65+65+65+65+65+65+1265 + offset,570))

        screen.blit(level_load.spike, (65+65+65+65+65+65+65+65+65+65+65+1265 + offset,370))
        screen.blit(level_load.spike, (65+65+65+65+65+65+65+65+65+65+65+65+1265 + offset,370))


        screen.blit(level_load.spike, (2330 + offset,500+70))
        screen.blit(level_load.spike, (2330+70+70 + offset,500+70))
        screen.blit(level_load.spike, (2330+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (2330+70+70+70+70+70+70 + offset,500+70))

        screen.blit(level_load.spike, (2330+70+70+70+70+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (2330+70+70+70+70+70+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (2330+70+70+70+70+70+70+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (2330+70+70+70+70+70+70+70+70+70+70+70 + offset,500+70))

        screen.blit(level_load.spike, (3350 + offset,500+70))
        screen.blit(level_load.spike, (3350+140+70 + offset,500+70))

        screen.blit(level_load.spike, (4300 + offset,500+70))
        screen.blit(level_load.spike, (4300+70 + offset,500+70))
        screen.blit(level_load.spike, (4300+70+70 + offset,500+70))
        screen.blit(level_load.spike, (4300+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (4300+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (4300+70+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (4300+70+70+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (4300+70+70+70+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (4300+70+70+70+70+70+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (4300+70+70+70+70+70+70+70+70+70 + offset,500+70))

        screen.blit(level_load.spike, (5360 + offset,500+70))
        screen.blit(level_load.spike, (5360+70 + offset,500+70))
        screen.blit(level_load.spike, (5360+70+70 + offset,500+70))
        screen.blit(level_load.spike, (5360+70+70+70 + offset,500+70))
        screen.blit(level_load.spike, (5360+70+70+70+70 + offset,500+70))

        #SINGLE BLOCK
        screen.blit(level_load.one_block, (1655-65-65-65 + offset,370))
        screen.blit(level_load.one_block, (1655-65-65 + offset,370))
        screen.blit(level_load.one_block, (1655-65 + offset,370))
        screen.blit(level_load.one_block, (2400 + offset,500))
        screen.blit(level_load.one_block, (2400+70+70 + offset,500-70-35))
        screen.blit(level_load.one_block, (2400+70+70+70+70 + offset,500-70-35-70-35))
        screen.blit(level_load.one_block, (3740 + offset,500+70))
        screen.blit(level_load.one_block, (4500 + offset,420))
        screen.blit(level_load.one_block, (4750 + offset,420))


        #PLATFORMS
        screen.blit(level_load.big_platform_LIGHT, (320 + offset,510))
        screen.blit(level_load.big_platform_DARK, (850 + offset,410))
        screen.blit(level_load.big_platform_DARK, (2400+70+70+70+70+70+70 + offset,500-70-35-70-35-70-35))
        screen.blit(level_load.big_platform_LIGHT, (3900 + offset,500-70))
        screen.blit(level_load.big_platform_LIGHT, (5000 + offset,500-70))
        screen.blit(level_load.big_platform_LIGHT, (5600 + offset,400))
        #DECOR
        screen.blit(level_load.sign, (50 + offset,565))

        #KEY
        screen.blit(level_load.key,(5900 + offset,290))

        #GROUND BLOCK
        screen.blit(level_load.ground_platform_LIGHT, (200+820+820 + offset,430))

    # Sidescrolling
    if player.player.x > 600 and player.right:
        offset -= 7
        player.player.x = 600

    if offset > -7:
        if player.player.x < 1 and player.left:
            offset += 7
            player.player.x = 1
    else:
        if player.player.x < 600 and player.left:
            offset += 7
            player.player.x = 600

    if offset < -4800:
        offset = -4800
    if offset > 0:
        offset = 0
