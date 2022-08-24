import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 700))

# load sprite sheets
crowned_king_walking = pygame.image.load('images/Sprite Sheets/crowned_king_walking.png').convert()
king_walking = pygame.image.load('images/Sprite Sheets/king_walking.png').convert()
king_walking_sword = pygame.image.load('images/Sprite Sheets/king_walking_sword.png').convert()
king_swinging_sword = pygame.image.load('images/Sprite Sheets/king_sword_swing.png').convert()

hp3 = pygame.image.load('images/Sprite Sheets/3_hp.png')
hp3 = pygame.transform.scale(hp3, (150, 45))

hp2 = pygame.image.load('images/Sprite Sheets/2_hp.png')
hp2 = pygame.transform.scale(hp2, (150, 45))

hp1 = pygame.image.load('images/Sprite Sheets/1_hp.png')
hp1 = pygame.transform.scale(hp1, (150, 45))

hp0 = pygame.image.load('images/Sprite Sheets/0_hp.png')
hp0 = pygame.transform.scale(hp0, (150, 45))

black = (0, 0, 0)

# appends all frames from sprite sheet into list
def sprite_init(sheet, rows, columns, scale=1):
    sheet.set_colorkey(black)
    sprite = sheet.get_rect()
    img_width = sprite.w/columns
    img_height = sprite.h/rows

    frames = []
    # forwards
    for row in range(rows):
        for column in range(columns):
            rect = pygame.Rect(column * img_width, row * img_height, img_width, img_height)
            frames.append(pygame.transform.scale(sheet.subsurface(rect), (img_width * scale, img_height * scale)))

    # backwards
    for row in range(rows):
        for column in range(columns):
            rect = pygame.Rect(column * img_width, row * img_height, img_width, img_height)
            flipped_img = pygame.transform.flip(sheet.subsurface(rect), True, False)
            frames.append(pygame.transform.scale(flipped_img, (img_width * scale, img_height * scale)))

    return frames


crowned_walking_frames = sprite_init(crowned_king_walking, 1, 8, 3)
king_walking_frames = sprite_init(king_walking, 1, 8, 3)
king_walking_sword_frames = sprite_init(king_walking_sword, 1, 8, 3)
king_swinging_sword_frames = sprite_init(king_swinging_sword, 1, 7, 3)

active_king = 0
action_frame = 0
frame_time = 0
