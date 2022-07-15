import pygame

class Platform(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/platform.png')
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def generate(self):
        pass

    def update(self) -> None:
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())