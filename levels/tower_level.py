import pygame
import random
import player, level_load, enemies, animations, SFX
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

offset = 0
enemyX = 2100
enemyY = 654

enemy_king = pygame.Rect(2100, 654, 36, 52)

def load_level():
    global offset, enemyX

    enemyX += offset

    enemy_king.bottomleft = (2100, 654)

    pygame.draw.rect(screen, "blue", enemy_king)

    if level_load.level == 2:
        screen.blit(level_load.boss_background, (offset, 0))

    if player.player.x > 600 and player.right and offset > -1200:
        offset -= 7
        player.player.x = 600
    if player.player.x > 600:
        if enemies.summoned:
            pygame.mixer.Sound.play(SFX.alert)
            enemies.summoned = False

    if player.health <= 0:
        player.player.bottomleft = (0, 664)
        offset = 0
        player.health = 3
        enemies.boss_hp = 300
        enemies.summoned = True

    if player.player.bottom > 664:
        player.player.bottom = 664
    # bossfight
    enemies.bossfight()