import pygame

pygame.mixer.init()
jump_sound = pygame.mixer.Sound("sounds/mixkit-player-jumping-in-a-video-game-2043.wav")
pygame.mixer.Sound.set_volume(jump_sound, 0.2)

sword_slash = pygame.mixer.Sound("sounds/mixkit-sword-slash-swoosh-1476.wav")
pygame.mixer.Sound.set_volume(sword_slash, 0.2)

win = pygame.mixer.Sound("sounds/mixkit-medieval-orchestra-announcement-694.wav")
pygame.mixer.Sound.set_volume(win, 0.2)

hurt = pygame.mixer.Sound("sounds/350926__cabled-mess__hurt-c-07.wav")
pygame.mixer.Sound.set_volume(hurt, 0.2)

alert = pygame.mixer.Sound("sounds/alert.wav")
pygame.mixer.Sound.set_volume(alert, 0.2)

open = pygame.mixer.Sound("sounds/mixkit-old-medieval-door-lock-187.wav")
pygame.mixer.Sound.set_volume(open, 0.2)

draw_sword = pygame.mixer.Sound("sounds/mixkit-metal-hit-woosh-1485.wav")
pygame.mixer.Sound.set_volume(draw_sword, 0.2)
