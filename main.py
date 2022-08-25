import pygame, sys

import enemies
import level_load
import player, levels.tutorial_level

# bg = pygame.image.load("images/Backgrounds/length_5_bg.png")

pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Movement Test")

# Rect Objects
floor = pygame.Rect(1, screen_height, screen_width, 1)


def draw_rects():
    pygame.draw.rect(screen, "black", floor)
    # screen.blit(bg, (0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.playerX_speed = 7
                player.right = True

            if event.key == pygame.K_LEFT:
                player.playerX_speed = -7
                player.left = True

            if event.key == pygame.K_UP:
                player.jumping = True

            if event.key == pygame.K_z:
                if player.holding_sword:
                    player.swinging_sword = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.playerX_speed = 0
                player.right = False

            if event.key == pygame.K_LEFT:
                player.playerX_speed = 0
                player.left = False

    screen.fill("grey")

    if level_load.level == 1:
        levels.tutorial_level.load_level()

    draw_rects()

    player.collisions()
    player.jump()
    player.animate()
    player.sword_attack()

    clock.tick(60)
    pygame.display.flip()
