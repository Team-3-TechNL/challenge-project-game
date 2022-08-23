import pygame
import player
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

block_height = 70
block_width = 70

# Tiles
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

forest_background = pygame.image.load("images/Tiles/blur_forest_BACKGROUND.png")

ground_platform_DARK_img = pygame.image.load("images/Tiles/ground_platform_DARK.png")
groudn_platform_DARK = pygame.transform.scale(ground_platform_DARK_img, (block_width*6 , block_height))

ground_platform_LIGHT_img = pygame.image.load("images/Tiles/ground_platform_LIGHT.png")
ground_platform_LIGHT = pygame.transform.scale(ground_platform_LIGHT_img, (block_width*6 , block_height))

spike_img = pygame.image.load("images/Tiles/spike1.png")
spike = pygame.transform.scale(spike_img, (block_width, block_height))

# Tutorial Level
tutorial_bg = pygame.image.load("images/Backgrounds/length_5_bg.png")

