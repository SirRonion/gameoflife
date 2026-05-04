import pygame
import numpy as np
from conway import *

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # size of the window you can adjust if you want, i think :)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Conway's game of life")

state = np.zeros((40, 50), dtype=int)
state[20, 25] = 1
state[20, 26] = 1
state[21, 25] = 1
state[21, 26] = 1
state[22, 23] = 1
state[22, 24] = 1
state[22, 25] = 1
state[23, 24] = 1

last_state = None
walls = pygame.sprite.Group()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("log: quiting game")
            running = False

    if not np.array_equal(state, last_state): # for some reason my editor is saying there's an error here even tho i there isn't cause it's on an if statement but whatever it's my problem i guess
        walls = create_map(state, 0.6) # here you can change the size of the tiles by using the offset param, 0.5 would be half the size of it's cell
        last_state = state.copy()

    state = play_round(state)

    screen.fill((30, 30, 30))
    walls.draw(screen)
    pygame.display.flip()

    clock.tick(30) # and here you can adjust the frame rate, the lower it is the slower the game of life runs duh, but the lower framerate saves some cpu power so that's on you

pygame.quit()
