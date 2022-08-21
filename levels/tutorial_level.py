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

    if player.player.x > 1000 and player.right:
        offset -= 7
        player.player.x = 1000
    if offset < -4800:
        offset = -4800
