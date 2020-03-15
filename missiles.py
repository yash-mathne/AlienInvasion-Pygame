import pygame
from pygame.sprite import Sprite


class Missile(Sprite):
    """
    Base class for the two kinds of missiles the ship can fire
    """

    def __init__(self, ai_settings, screen, ship):
        super(Missile, self).__init__()
        self.screen = screen

    def update(self):
        self.rect.y -= self.speed

    def draw_missile(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Mi1(Missile):
    """
    Class for type1 killer missiles1_fired
    """

    def __init__(self, ai_settings, screen, ship):
        super(Mi1, self).__init__(ai_settings, screen, ship)

        self.rect = pygame.Rect(
            ship.rect.x + 40, ship.rect.y - 75, ai_settings.mi1_width, ai_settings.mi1_height)
        self.color = ai_settings.mi1_color
        self.speed = ai_settings.mi1_speed


class Mi2(Missile):
    """
    Class for type2 life extending missiles
    """

    def __init__(self, ai_settings, screen, ship):
        super(Mi2, self).__init__(ai_settings, screen, ship)

        self.rect = pygame.Rect(
            ship.rect.x + 35, ship.rect.y - 80, ai_settings.mi2_width, ai_settings.mi2_height)
        self.color = ai_settings.mi2_color
        self.speed = ai_settings.mi2_speed
