import pygame
import animations, levels.tutorial_level, level_load, player
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

knight_1 = level_load.knight_idle_L1.get_rect()
knight_1.bottomleft = (2870, 205)

k1_dead = False
k1_hurtbox = pygame.Rect(0, 0, 70, 156)


knight_2 = level_load.knight_idle_L1.get_rect()
knight_2.bottomleft = (5627, 318)

k2_dead = False
k2_hurtbox = pygame.Rect(0, 0, 70, 156)

sword_swing = False



def enemy_setup():
    global knight_1, sword_swing, k1_dead, k2_dead


    # KNIGHT 1

    if knight_1.colliderect(player.hurtbox):
        k1_dead = True
    else:
        if level_load.level == 1:
           knight_1.bottomleft = (2900 + levels.tutorial_level.offset, 205)

    # animations
    if k1_dead:
        knight_1.y = 800
        screen.blit(level_load.knight_idle_L1, knight_1)
    elif not sword_swing:
        if animations.idle_frame == 0:
            screen.blit(level_load.knight_idle_L1, knight_1)
        elif animations.idle_frame == 1:
            screen.blit(level_load.knight_idle_L2, knight_1)

    elif sword_swing:
        # sword attack
        if animations.frame_time % 4 == 0:
            animations.enemy_action_frame += 1
            if animations.enemy_action_frame >= 6:
                animations.enemy_action_frame = 0
                sword_swing = False

        k1_hurtbox.bottomright = knight_1.bottomleft
        if player.player.colliderect(k1_hurtbox):
            if player.invincibility_time <= 0:
                player.health -=1
                player.invincibility_time = 120

        screen.blit(animations.knight_swinging_sword_frames[animations.enemy_action_frame], knight_1)


    # KNIGHT 2

    if knight_2.colliderect(player.hurtbox):
        k2_dead = True
    else:
        if level_load.level == 1:
           knight_2.bottomleft = (5627 + levels.tutorial_level.offset, 370)

    # animations
    if k2_dead:
        knight_2.y = 800
        screen.blit(level_load.knight_idle_L1, knight_2)
    elif not sword_swing:
        if animations.idle_frame == 0:
            screen.blit(level_load.knight_idle_L1, knight_2)
        elif animations.idle_frame == 1:
            screen.blit(level_load.knight_idle_L2, knight_2)

    elif sword_swing:
        # sword attack
        if animations.frame_time % 4 == 0:
            animations.enemy_action_frame += 1
            if animations.enemy_action_frame >= 6:
                animations.enemy_action_frame = 0
                sword_swing = False

        k2_hurtbox.bottomright = knight_2.bottomleft
        if player.player.colliderect(k2_hurtbox):
            if player.invincibility_time <= 0:
                player.health -=1
                player.invincibility_time = 120

        screen.blit(animations.knight_swinging_sword_frames[animations.enemy_action_frame], knight_2)