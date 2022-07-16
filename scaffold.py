import pygame
import random
import coordchoices

class Platform(pygame.sprite.Sprite):

    def __init__(self, y):
        super().__init__()
        self.image = pygame.image.load('assets/platform4.png')
        self.x = 0
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 20)

    def generate(self):
        self.rect.centerx = random.choice(coordchoices.xchoices)
        self.x = self.rect.centerx

    def update(self) -> None:
        self.rect = pygame.Rect(self.x, self.y, 50, 20)