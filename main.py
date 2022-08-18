import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Movement Test")
walk_sprite_sheet = pygame.image.load('images/king_walk_test.png').convert_alpha()

# Jump Settings
jumping = False
gravity = 1
jump_height = 30  # CHANGE THIS VARIABLE TO CHANGE JUMP HEIGHT
playerY_speed = jump_height
playerX_speed = 0

player = walk_sprite_sheet.get_rect()

# Initial position
player.bottomleft = (0, screen_height-1)

# Rect Objects
floor = pygame.Rect(1, screen_height, screen_width, 1)


def draw_rects():
    pygame.draw.rect(screen, "black", floor)


def collisions():
    global playerY_speed
    if player.left < 0:
        player.left = 0
    if player.right > 1200:
        player.right = 1200
    if player.bottom > floor.top:
        player.bottom = floor.top


def jump():
    global jumping, playerY_speed, gravity
    if jumping:
        player.y -= playerY_speed
        playerY_speed -= gravity

        if playerY_speed < -jump_height:
            jumping = False
            playerY_speed = jump_height


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_speed = 7
            if event.key == pygame.K_LEFT:
                playerX_speed = -7
            if event.key == pygame.K_UP:
                jumping = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerX_speed = 0
            if event.key == pygame.K_LEFT:
                playerX_speed = 0

    player.x += playerX_speed

    screen.fill("black")

    screen.blit(walk_sprite_sheet, player)

    draw_rects()
    collisions()
    jump()


    clock.tick(60)
    pygame.display.flip()
