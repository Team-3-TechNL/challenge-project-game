import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 700))

# load sprite sheets
crowned_king_walking = pygame.image.load('images/Sprite Sheets/king_walk_test.png').convert()
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


crowned_walking_frames = sprite_init(crowned_king_walking, 1, 8, 2)
active_king = 0
frame_time = 0
