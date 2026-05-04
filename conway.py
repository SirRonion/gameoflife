import numpy as np
import pygame

from sprites import Wall

dirs = [
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0]
]

def get_count(state, x, y):
    count = 0
    for dir in dirs:
        row = y + dir[0]
        col = x + dir[1]

        if row < 0 or row >= len(state):
            continue

        if col < 0 or col >= len(state[0]):
            continue
        
        if state[row, col] == 1:
            count += 1

    return count


def play_round(state):
    out = np.zeros((len(state), len(state[0])), dtype=int)

    for y, row in enumerate(state):
        for x in range(len(row)):
            count = get_count(state, x, y)

            if state[y, x] == 1:
                if count == 2 or count == 3:
                    out[y, x] = 1
            else:
                if count == 3:
                    out[y, x] = 1
                
    return out

def create_map(state, shrink_factor=0.8):
    all_sprites = pygame.sprite.Group()

    sw, sh = pygame.display.get_surface().get_size()
    
    rows = len(state)
    cols = len(state[0]) if rows > 0 else 0

    slot_w = sw // cols
    slot_h = sh // rows

    tw = int(slot_w * shrink_factor)
    th = int(slot_h * shrink_factor)

    offset_x = (slot_w - tw) // 2
    offset_y = (slot_h - th) // 2

    for r, row in enumerate(state):
        for c, cell in enumerate(row):
            if cell == 1:
                x = (c * slot_w) + offset_x
                y = (r * slot_h) + offset_y

                wall = Wall(x, y, tw, th)
                all_sprites.add(wall)

    return all_sprites
