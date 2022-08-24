import pygame
import animations
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))


def spawn_enemy(type, posx, posy):
    enemy = pygame.Rect((posx, posy), (36, 54))
