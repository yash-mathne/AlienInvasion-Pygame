import pygame


class Ship():
    """
    This class represents the ship object
    """

    def __init__(self, screen):
        self.screen = screen
        #  a surface representing the ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # initial position of the ship
        self.rect.x = 300
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
