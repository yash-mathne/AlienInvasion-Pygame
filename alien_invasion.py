import pygame
from pygame.locals import *
from pygame.sprite import Group
from settings import Settings
from settings import Score
import game_functions as gf
from ship import Ship
from aliens import Aliens


def run_game():

    pygame.init()

    ai_settings = Settings()
    FPS = ai_settings.fps
    fpsclock = pygame.time.Clock()
    score = Score()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion!')

    # instantiating the ship object and two missile groups
    ship = Ship(screen)
    missiles1_fired = Group()
    missiles2_fired = Group()

    pygame.time.set_timer(USEREVENT + 1, 5000)

    # blitting the first alien to the screen,
    # and adding it to the curaliens group
    newalien = Aliens(screen)
    Aliens.curaliens.add(newalien)
    for alien in Aliens.curaliens:
        alien.blitme()

    # main game loop
    while True:
        gf.check_events(ship, missiles1_fired, missiles2_fired,
                        ai_settings, screen, Aliens.curaliens, score)
        gf.update_screen(ai_settings, screen, ship, missiles1_fired,
                         missiles2_fired, Aliens.curaliens, score)
        fpsclock.tick(FPS)


run_game()
