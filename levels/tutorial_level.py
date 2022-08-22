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
        screen.blit(level_load.ground_platform_LIGHT, (0 + (390 * x) + offset, 654))

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