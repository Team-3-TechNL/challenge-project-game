import pygame, sys
import animations

pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Movement Test")


# Jump Settings
jumping = False
gravity = 1
jump_height = 30  # CHANGE THIS VARIABLE TO CHANGE JUMP HEIGHT
playerY_speed = jump_height
playerX_speed = 0



# Rect Objects
floor = pygame.Rect(1, screen_height, screen_width, 1)

player = animations.crowned_walking_frames[0].get_rect()
# Initial position
player.bottomleft = (0, screen_height-1)


def animate():
    global player
    animations.frame_time += 1 # increases every 1/60 of a second
    if animations.frame_time > 60:
        animations.frame_time = 0 # resets every second

    if animations.frame_time % 3 == 0:  # player moving at 20 FPS (60 / 3 = 20)
        # detects key presses
        if keys[pygame.K_RIGHT]:
            animations.active_king += 1
        if keys[pygame.K_LEFT]:
            animations.active_king -= 1
        # changes between right/left
        if animations.active_king >= 8:
            animations.active_king = 0
        if animations.active_king <= -8:
            animations.active_king = -1

    # places frames onto player object
    screen.blit(animations.crowned_walking_frames[animations.active_king], player)


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

    keys = pygame.key.get_pressed()


    player.x += playerX_speed

    screen.fill("grey")

    draw_rects()
    collisions()
    jump()
    animate()

    clock.tick(60)
    pygame.display.flip()
