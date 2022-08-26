import pygame
import animations, levels.tutorial_level, levels.tower_level, level_load, player, SFX

pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

knight = level_load.knight_idle_L1.get_rect()
knight.bottomleft = (2870, 205)

k_dead = False
k_hurtbox = pygame.Rect(0, 0, 70, 156)

sword_swing = False

pygame.mixer.init()

def enemy_setup():
    global knight, sword_swing, k_dead

    if knight.colliderect(player.hurtbox):
        k_dead = True
    else:
        if level_load.level == 1:
            knight.bottomleft = (5627 + levels.tutorial_level.offset, 370)

    # animations
    if k_dead:
        knight.y = 800
        screen.blit(level_load.knight_idle_L1, knight)
    elif not sword_swing:
        if animations.idle_frame == 0:
            screen.blit(level_load.knight_idle_L1, knight)
        elif animations.idle_frame == 1:
            screen.blit(level_load.knight_idle_L2, knight)

    elif sword_swing:
        # sword attack
        if animations.frame_time % 4 == 0:
            animations.enemy_action_frame += 1
            if animations.enemy_action_frame >= 6:
                animations.enemy_action_frame = 0
                sword_swing = False

        k_hurtbox.bottomright = knight.bottomleft
        if player.player.colliderect(k_hurtbox):
            if player.invincibility_time <= 0:
                player.health -= 1
                pygame.mixer.Sound.play(SFX.hurt)
                player.invincibility_time = 120



        screen.blit(animations.knight_swinging_sword_frames[animations.enemy_action_frame], knight)


bossking = animations.boss_swinging_sword_frames_L[0].get_rect()
bossking.bottomleft = (2870, 205)

boss_hp = 300
boss_dead = False
boss_hurtbox = pygame.Rect(0, 0, 100, 156)

leftside = False
rightside = True

boss_walktime = 0
boss_walking = True
boss_action = 0

playonce = True
playonce2 = True

summoned = True


def bossfight():
    global bossking, boss_hp, leftside, rightside, boss_walktime, boss_dead, sword_swing, boss_action, boss_walking, playonce, summoned

    if bossking.colliderect(player.hurtbox):
        boss_hp -= 1

    if levels.tower_level.offset > -1200:
        bossking.bottomleft = (1300, 664)

    if boss_hp <= 0:
        boss_dead = True
        if playonce:
            pygame.mixer.Sound.play(SFX.win)
            pygame.mixer.music.stop()
            playonce = False
    # movement
    if boss_dead:
        bossking.y = 800
        screen.blit(level_load.thanks, (0,0))
    elif levels.tower_level.offset <= 1200:
        if rightside:
            if bossking.left < 0:
                leftside = True
                rightside = False
            bossking.x -= 7
        elif leftside:
            if bossking.right > 1200:
                leftside = False
                rightside = True
            bossking.x += 7

    # animations
    if animations.frame_time % 4 == 0:
        if leftside:
            boss_walktime += 1
            if boss_walking:
                if boss_walktime >= 7:
                    boss_walktime = 0

        if rightside:
            boss_walktime -= 1
            if boss_walking:
                if boss_walktime <= -8:
                    boss_walktime = -1

        #sword_swing
        animations.enemy_action_frame += 1
        if animations.enemy_action_frame >= 6:
            animations.enemy_action_frame = 0
            sword_swing = False
            boss_walking = True

    if animations.frame_time % 60 == 0:
        sword_swing = True
        boss_walking = False

    # sword attack
    if boss_walking:
        screen.blit(animations.boss_walking_frames[boss_walktime], bossking)
        boss_hurtbox.y = 900
    elif sword_swing and rightside:
        screen.blit(animations.boss_swinging_sword_frames_L[animations.enemy_action_frame], (bossking.x - 77, bossking.y))
        boss_hurtbox.bottomright = bossking.bottomleft

    elif sword_swing and leftside:
        screen.blit(animations.boss_swinging_sword_frames_R[animations.enemy_action_frame], bossking)
        boss_hurtbox.midleft = bossking.center

    # player hitbox + i-frames
    if sword_swing:
        if player.player.colliderect(boss_hurtbox):
            if player.invincibility_time <= 0:
                player.health -= 1
                pygame.mixer.Sound.play(SFX.hurt)
                player.invincibility_time = 120
    player.invincibility_time -= 1
    if player.invincibility_time <= 0:
        player.invincibility_time = 0
