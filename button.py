import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, image: pygame.Surface):
        super().__init__()
        self.image = image
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
