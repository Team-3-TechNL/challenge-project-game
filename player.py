import pygame
import animations
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

player = animations.crowned_walking_frames[0].get_rect()
# Initial position
player.bottomleft = (0, screen_height-1)


# Movement Settings
left = False
right = False


# Jump Settings
jumping = False
gravity = 1
jump_height = 30  # CHANGE THIS VARIABLE TO CHANGE JUMP HEIGHT
playerY_speed = jump_height
playerX_speed = 0


def collisions():
    global playerY_speed, playerX_speed
    player.x += playerX_speed

    if player.left < 0:
        player.left = 0
    if player.right > 1200:
        player.right = 1200


def animate():
    global player, playerX_speed
    keys = pygame.key.get_pressed()

    animations.frame_time += 1 # increases every 1/60 of a second
    if animations.frame_time > 60:
        animations.frame_time = 0 # resets every second

    if animations.frame_time % 3 == 0:  # player moving at 20 FPS (60 / 3 = 20)
        # detects key presses
        if keys[pygame.K_RIGHT]:
            animations.active_king += 1
        if keys[pygame.K_LEFT]:
            animations.active_king -= 1
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            playerX_speed = 0

        # changes between right/left
        if animations.active_king >= 8:
            animations.active_king = 0
        if animations.active_king <= -8:
            animations.active_king = -1

    # places frames onto player object
    screen.blit(animations.crowned_walking_frames[animations.active_king], player)


def jump():
    global jumping, playerY_speed, gravity
    if jumping:
        player.y -= playerY_speed
        playerY_speed -= gravity

        if playerY_speed < -jump_height:
            jumping = False
            playerY_speed = jump_height