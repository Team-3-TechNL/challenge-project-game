import pygame
import animations
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

player = animations.crowned_walking_frames[0].get_rect()

# Initial position
player.bottomleft = (0, 654)


# Movement Settings
left = False
right = False
run_once = False

# Jump Settings
jumping = False
gravity = 1
jump_height = 20  # CHANGE THIS VARIABLE TO CHANGE JUMP HEIGHT
playerY_speed = jump_height
playerX_speed = 0

# Animation Settings
holding_sword = False
swinging_sword = False


def collisions():
    global playerY_speed, playerX_speed
    player.x += playerX_speed

    if player.left < 0:
        player.left = 0
    if player.right > 1200:
        player.right = 1200


def animate():
    global player, playerX_speed, holding_sword, swinging_sword, left, right

    keys = pygame.key.get_pressed()

    animations.frame_time += 1 # increases every 1/60 of a second
    if animations.frame_time > 60:
        animations.frame_time = 0 # resets every second

    if animations.frame_time % 4 == 0:  # player moving at 15 FPS (60 / 4 = 15)
        # detects key presses
        if keys[pygame.K_RIGHT]:
            animations.active_king += 1
        if keys[pygame.K_LEFT]:
            animations.active_king -= 1
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            playerX_speed = 0

        if keys[pygame.K_SPACE]:
            holding_sword = True
        if keys[pygame.K_f]:
            holding_sword = False


        # changes between right/left
        if animations.active_king >= 8:
            animations.active_king = 0
        if 0 <= animations.active_king < 8:
            right = True
            left = False
        if animations.active_king <= -8:
            animations.active_king = -1
        if -8 < animations.active_king <= -1:
            left = True
            right = False

        if swinging_sword:
            if right:
                if animations.action_frame >= 6:
                    animations.action_frame = 0
                    swinging_sword = False
            if left:
                global run_once
                if not run_once:
                    animations.action_frame = 7
                    run_once = True
                if animations.action_frame >= 13:
                    animations.action_frame = 7
                    swinging_sword = False

            animations.action_frame += 1


    # places frames onto player object
    if swinging_sword and right:
        screen.blit(animations.king_swinging_sword_frames[animations.action_frame], player)
    elif swinging_sword and left:
        screen.blit(animations.king_swinging_sword_frames[animations.action_frame], (player.x - 77, player.y))

    elif holding_sword:
        screen.blit(animations.king_walking_sword_frames[animations.active_king], player)
    else:
        screen.blit(animations.king_walking_frames[animations.active_king], player)


def jump():
    global jumping, playerY_speed, gravity
    if jumping:
        player.y -= playerY_speed
        playerY_speed -= gravity

        if playerY_speed < -jump_height:
            jumping = False
            playerY_speed = jump_height


def sword_attack():
    global swinging_sword

