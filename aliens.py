import pygame
import random
import threading
from pygame.sprite import Sprite
from pygame.sprite import Group


class Aliens(Sprite):

    curaliens = Group()

    def __init__(self, screen):
        super(Aliens, self).__init__()

        self.screen = screen
        # returns a surface representing the ship
        self.image = pygame.image.load('images/alien1.bmp')
        # get_rect is used to get access to a surface's rect attribute
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # randomly spawn in any location int the top two rows
        self.rect.x = (random.randint(1, 8) - 1) * 100
        self.rect.y = (random.randint(1, 2) - 1) * 100

        # call the delete function after 8 seconds of creation unless
        # extendlife function is called
        self.x = threading.Timer(4.0, self.__del__)
        self.x.start()

    def __del__(self):
        Aliens.curaliens.remove(self)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def extendlife(self):
        # cancel the previously running timer and start a new timer for 5 secs
        self.x.cancel()
        # change the appearance of the alien
        self.image = pygame.image.load('images/alien2.bmp')
        self.x = threading.Timer(2.0, self.__del__)
        self.x.start()
