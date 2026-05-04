import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((255, 255, 255)) # white sqaure
        self.rect = self.image.get_rect(topleft=(x, y))
