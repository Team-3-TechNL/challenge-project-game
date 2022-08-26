import pygame, sys
from pygame import mixer
import enemies
import level_load
import player, levels.tutorial_level, levels.tower_level, SFX

# bg = pygame.image.load("images/Backgrounds/length_5_bg.png")

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Bring Back the KING")

# Rect Objects
floor = pygame.Rect(1, screen_height, screen_width, 1)



pygame.mixer.music.load("sounds/mixkit-suspense-mystery-bass-685.wav")
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if player.holding_sword:
                    player.playerX_speed = 5
                else:
                    player.playerX_speed = 7
                player.right = True

            if event.key == pygame.K_LEFT:
                if player.holding_sword:
                    player.playerX_speed = -5
                else:
                    player.playerX_speed = -7
                player.left = True

            if event.key == pygame.K_UP:
                if not player.jumping:
                    pygame.mixer.Sound.play(SFX.jump_sound)
                player.jumping = True

            if event.key == pygame.K_z:
                if player.holding_sword:
                    if not player.swinging_sword:
                        pygame.mixer.Sound.play(SFX.sword_slash)
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
    elif level_load.level >= 2:
        levels.tower_level.load_level()


    player.collisions()
    player.jump()
    player.animate()
    player.sword_attack()

    clock.tick(60)
    pygame.display.flip()
