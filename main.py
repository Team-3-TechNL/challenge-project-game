import pygame, sys
import player


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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.playerX_speed = 7
            if event.key == pygame.K_LEFT:
                player.playerX_speed = -7
            if event.key == pygame.K_UP:
                player.jumping = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.playerX_speed = 0
            if event.key == pygame.K_LEFT:
                player.playerX_speed = 0

    screen.fill("grey")

    draw_rects()
    player.collisions()
    player.jump()
    player.animate()

    clock.tick(60)
    pygame.display.flip()
