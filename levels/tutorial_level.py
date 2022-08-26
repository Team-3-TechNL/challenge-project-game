import pygame
import player, level_load, enemies, animations, SFX
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

offset = 0

# Define enemy rects
knight_1 = level_load.knight_idle_L1.get_rect()

# Define spike rects
spike1 = level_load.spike.get_rect()
spike2 = spike1.copy()
spike3 = spike1.copy()
spike4 = spike1.copy()
spike5 = spike1.copy()
spike6 = spike1.copy()
spike7 = spike1.copy()
spike8 = spike1.copy()
spike9 = spike1.copy()
spike10 = spike1.copy()
spike11 = spike1.copy()
spike12 = spike1.copy()
spike13 = spike1.copy()
spike14 = spike1.copy()
spike15 = spike1.copy()
spike16 = spike1.copy()
spike17 = spike1.copy()
spike18 = spike1.copy()
spike19 = spike1.copy()
spike20 = spike1.copy()
spike21 = spike1.copy()
spike22 = spike1.copy()
spike23 = spike1.copy()
spike24 = spike1.copy()
spike25 = spike1.copy()
spike26 = spike1.copy()
spike27 = spike1.copy()
spike28 = spike1.copy()
spike29 = spike1.copy()
spike30 = spike1.copy()
spike31 = spike1.copy()
spike32 = spike1.copy()
spike33 = spike1.copy()
spike34 = spike1.copy()
spike35 = spike1.copy()
spike36 = spike1.copy()
spike37 = spike1.copy()
spike38 = spike1.copy()
spike39 = spike1.copy()
spike40 = spike1.copy()
spike41 = spike1.copy()

spikes = [spike1, spike2, spike3, spike4, spike5, spike6, spike7, spike8, spike9, spike10, spike11, spike12, spike13, spike14, spike15, spike16, spike17, spike18, spike19, spike20, spike21, spike22, spike23, spike24, spike25, spike26, spike27, spike28, spike29, spike30, spike31, spike32, spike33, spike34, spike35, spike36, spike37, spike38, spike39, spike40, spike41]

# Define one block rects
block1 = level_load.one_block.get_rect()
block2 = block1.copy()
block3 = block1.copy()
block4 = block1.copy()
block5 = block1.copy()
block6 = block1.copy()
block7 = block1.copy()
block8 = block1.copy()

# Define platform rects
light_plat1 = level_load.big_platform_LIGHT.get_rect()
light_plat2 = light_plat1.copy()
light_plat3 = light_plat1.copy()
light_plat4 = light_plat1.copy()

dark_plat1 = level_load.big_platform_DARK.get_rect()
dark_plat2 = dark_plat1.copy()

light_plat_5 = level_load.ground_platform_LIGHT.get_rect()

platforms = [light_plat1, light_plat2, light_plat3, light_plat4, light_plat_5, dark_plat1, dark_plat2, block1, block2, block3, block4, block5, block6, block7, block8]

# Define goal rect
key = level_load.key.get_rect()


def load_level():
    global offset

    if level_load.level == 1:
        screen.blit(level_load.tutorial_bg, (offset, 0))




    #SPIKES
    screen.blit(level_load.spike, spike1)
    spike1.topleft = (850 + offset, 590)
    screen.blit(level_load.spike, spike2)
    spike2.topleft = (785 + offset, 590)
    screen.blit(level_load.spike, spike3)
    spike3.topleft = (720 + offset, 590)
    screen.blit(level_load.spike, spike4)
    spike4.topleft = (655 + offset, 590)

    screen.blit(level_load.spike, spike5)
    spike5.topleft = (1200 + offset, 590)
    screen.blit(level_load.spike, spike6)
    spike6.topleft = (1265 + offset, 590)
    screen.blit(level_load.spike, spike7)
    spike7.topleft = (65+1265 + offset, 590)
    screen.blit(level_load.spike, spike8)
    spike8.topleft = (65+65+1265 + offset, 590)
    screen.blit(level_load.spike, spike9)
    spike9.topleft = (65+65+65+1265 + offset, 590)
    screen.blit(level_load.spike, spike10)
    spike10.topleft = (65+65+65+1265 + offset, 590)
    screen.blit(level_load.spike, spike11)
    spike11.topleft = (65+65+65+65+1265 + offset, 590)
    screen.blit(level_load.spike, spike12)
    spike12.topleft = (65+65+65+65+65+1265 + offset, 590)
    screen.blit(level_load.spike, spike13)
    spike13.topleft = (65+65+65+65+65+65+1265 + offset, 590)
    screen.blit(level_load.spike, spike14)
    spike14.topleft = (65+65+65+65+65+65+65+1265 + offset, 590)

    screen.blit(level_load.spike, spike15)
    spike15.topleft = (65+65+65+65+65+65+65+65+65+65+65+1265 + offset, 370+20)
    screen.blit(level_load.spike, spike16)
    spike16.topleft = (65+65+65+65+65+65+65+65+65+65+65+65+1265 + offset, 370+20)

    screen.blit(level_load.spike, spike17)
    spike17.topleft = (2330 + offset, 500+70+20)
    screen.blit(level_load.spike, spike18)
    spike18.topleft = (2330+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike19)
    spike19.topleft = (2330+70+70+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike20)
    spike20.topleft = (2330+70+70+70+70+70+70 + offset, 500+70+20)

    screen.blit(level_load.spike, spike21)
    spike21.topleft = (2330+70+70+70+70+70+70+70+70 + offset, 500+70+35+20)
    screen.blit(level_load.spike, spike22)
    spike22.topleft = (2330+70+70+70+70+70+70+70+70+70 + offset, 500+70+35+20)
    screen.blit(level_load.spike, spike23)
    spike23.topleft = (2330+70+70+70+70+70+70+70+70+70+70 + offset, 500+70+35+20)
    screen.blit(level_load.spike, spike24)
    spike24.topleft = (2330+70+70+70+70+70+70+70+70+70+70+70 + offset, 500+70+35+20)

    screen.blit(level_load.spike, spike25)
    spike25.topleft = (3350 + offset, 500+70+20)
    screen.blit(level_load.spike, spike26)
    spike26.topleft = (3350+140+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike27)
    spike27.topleft = (4300 + offset, 500+70+20)
    screen.blit(level_load.spike, spike28)
    spike28.topleft = (4300+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike29)
    spike29.topleft = (4300+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike30)
    spike30.topleft = (4300+70+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike31)
    spike31.topleft = (4300+70+70+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike32)
    spike32.topleft = (4300+70+70+70+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike33)
    spike33.topleft = (4300+70+70+70+70+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike34)
    spike34.topleft = (4300+70+70+70+70+70+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike35)
    spike35.topleft = (4300+70+70+70+70+70+70+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike36)
    spike36.topleft = (4300+70+70+70+70+70+70+70+70+70 + offset, 500+70+20)

    screen.blit(level_load.spike, spike37)
    spike37.topleft = (5360 + offset, 500+70+20)
    screen.blit(level_load.spike, spike38)
    spike38.topleft = (5360+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike39)
    spike39.topleft = (5360+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike40)
    spike40.topleft = (5360+70+70+70 + offset, 500+70+20)
    screen.blit(level_load.spike, spike41)
    spike41.topleft = (5360+70+70+70+70 + offset, 500+70+20)

    # SINGLE BLOCKS
    screen.blit(level_load.one_block, block1)
    block1.topleft = (1655-65-65 + offset, 370+20)
    screen.blit(level_load.one_block, block2)
    block2.topleft = (1655-65 + offset, 370+20)
    screen.blit(level_load.one_block, block3)
    block3.topleft = (2400 + offset, 500+20)
    screen.blit(level_load.one_block, block4)
    block4.topleft = (2400+70+70 + offset, 500-70-35+20)
    screen.blit(level_load.one_block, block5)
    block5.topleft = (2400+70+70+70+70 + offset, 500-70-35-70-35+20)
    screen.blit(level_load.one_block, block6)
    block6.topleft = (3740 + offset, 500+70+20)
    screen.blit(level_load.one_block, block7)
    block7.topleft = (4500 + offset, 420+20)
    screen.blit(level_load.one_block, block8)
    block8.topleft = (4750 + offset, 420+20)

    # PLATFORMS
    screen.blit(level_load.big_platform_LIGHT, light_plat1)
    light_plat1.topleft = (320 + offset, 510+20)
    screen.blit(level_load.big_platform_LIGHT, light_plat2)
    light_plat2.topleft = (3900 + offset, 500-70+20)
    screen.blit(level_load.big_platform_LIGHT, light_plat3)
    light_plat3.topleft = (5000 + offset, 500-70+20)
    screen.blit(level_load.big_platform_LIGHT, light_plat4)
    light_plat4.topleft = (5600 + offset, 350+20)
    screen.blit(level_load.ground_platform_LIGHT, light_plat_5)
    light_plat_5.topleft = (200+820+820+offset, 430+20)


    screen.blit(level_load.big_platform_DARK, dark_plat1)
    dark_plat1.topleft = (850 + offset, 410+20)
    screen.blit(level_load.big_platform_DARK, dark_plat2)
    dark_plat2.topleft = (2400+70+70+70+70+70+70 + offset, 500-70-35-70-35-70-35+20)



    #GROUND
    for x in range(16):
        screen.blit(level_load.ground_platform_LIGHT, (0 + (390 * x) + offset, 654))

    # Sidescrolling
    if player.player.x > 600 and player.right and offset > -4800:
        offset -= 7
        player.player.x = 600

    if offset > -7:
        if player.player.x < 1 and player.left:
            offset += 7
            player.player.x = 1
    else:
        if player.player.x < 600 and player.left:
            offset += 7
            player.player.x = 600

    if offset < -4800:
        offset = -4800
    if offset > 0:
        offset = 0

    # Player Collisions
    # SPIKES
    if player.player.collidelist(spikes) != -1:
        if player.invincibility_time <= 0:
            player.health -=1
            pygame.mixer.Sound.play(SFX.hurt)
            player.invincibility_time = 120
    if player.invincibility_time != 0:
        player.invincibility_time -= 1

    # PLATFORMS
    if player.player.bottom > light_plat1.top and light_plat1.left < player.player.right and player.player.left < light_plat1.right:
        player.player.bottom = light_plat1.top

    if player.player.bottom > light_plat2.top and light_plat2.left < player.player.right and player.player.left < light_plat2.right:
        player.player.bottom = light_plat2.top

    if player.player.bottom > light_plat3.top and light_plat3.left < player.player.right and player.player.left < light_plat3.right:
        player.player.bottom = light_plat3.top

    if player.player.bottom > light_plat4.top and light_plat4.left < player.player.right and player.player.left < light_plat4.right:
        player.player.bottom = light_plat4.top

    if player.player.colliderect(light_plat_5):
        player.player.bottom = light_plat_5.top

    if player.player.bottom > dark_plat1.top and dark_plat1.left < player.player.right and player.player.left < dark_plat1.right:
        player.player.bottom = dark_plat1.top

    if player.player.bottom > dark_plat2.top and dark_plat2.left < player.player.right and player.player.left < dark_plat2.right:
        player.player.bottom = dark_plat2.top

    if player.player.colliderect(block1):
        player.player.bottom = block1.top

    if player.player.colliderect(block2):
        player.player.bottom = block2.top

    if player.player.colliderect(block3):
        player.player.bottom = block3.top

    if player.player.colliderect(block4):
        player.player.bottom = block4.top

    if player.player.colliderect(block5):
        player.player.bottom = block5.top

    if player.player.colliderect(block6):
        player.player.bottom = block6.top

    if player.player.colliderect(block7):
        player.player.bottom = block7.top

    if player.player.colliderect(block8):
        player.player.bottom = block8.top

    if player.player.collidelist(platforms) == -1 and not player.jumping or player.player.bottom < 654 and not player.jumping:
        player.player.y += 10

    # GOAL
    screen.blit(level_load.key, key)
    key.topleft = (5900 + offset, 290)

    if player.player.colliderect(key):
        if level_load.level == 1:
            player.player.bottomleft = (0, 664)
            player.health = 3
            pygame.mixer.Sound.play(SFX.open)
        level_load.level += 1


    # ENEMIES
    enemies.enemy_setup()


    # Player Health
    if player.health <= 0:
        offset = 0
        player.player.bottomleft = (0, 654)
        player.health = 3


    # FLOOR
    if level_load.level == 1:
        if player.player.bottom > 654:
            player.player.bottom = 654
