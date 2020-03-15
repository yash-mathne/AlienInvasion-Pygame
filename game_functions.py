import sys
import pygame
import missiles
import time
import aliens
import settings
from pygame.locals import *


def check_events(ship, missiles1_fired, missiles2_fired, ai_settings, screen,
                 curaliens, score):
    """
    Check for user events and take appropriate actions
    """

    # iterate over all events that have occured
    # since last time .get() function was called
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # quit the game
            pygame.quit()
            sys.exit()

        if event.type == USEREVENT + 1:  # time to spawn a new alien
            newalien = aliens.Aliens(screen)
            curaliens.add(newalien)

        if event.type == pygame.KEYDOWN:  # to account for key press events

            # pressing q quits the game
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

            # move the ship left by 100 px ( a pressed )
            if event.key == pygame.K_a and ship.rect.x >= 100:
                ship.rect.x -= 100

            # move the shipe right by 100 px ( d pressed )
            elif event.key == pygame.K_d and ship.rect.x <= 600:
                ship.rect.x += 100

            # fire a type1 missile by pressing space
            elif event.key == pygame.K_SPACE:
                new_missile = missiles.Mi1(ai_settings, screen, ship)
                missiles1_fired.add(new_missile)

            # fire a type2 missile by pressing s
            elif event.key == pygame.K_s:
                new_missile = missiles.Mi2(ai_settings, screen, ship)
                missiles2_fired.add(new_missile)


def update_screen(ai_settings, screen, ship, missiles1_fired, missiles2_fired,
                  curaliens, score):
    """
    updates the screen after making all updates
    """

    # fill the background with specified colour in settings
    screen.fill(ai_settings.bg_color)

    # update already fired missiles
    missiles1_fired.update()
    missiles2_fired.update()

    # create a scoreboard in center of the screen
    font = pygame.font.SysFont("freesansbold", 50)
    scoreboard = font.render("SCORE:{0}".format(
        score.scorectr), True, ai_settings.score_color)
    scoreboard_rect = scoreboard.get_rect(center=screen.get_rect().center)
    screen.blit(scoreboard, scoreboard_rect)

    # remove missiles that have crossed the screen
    for mis1 in missiles1_fired.copy():
        if mis1.rect.bottom <= 0:
            missiles1_fired.remove(mis1)
    for mis2 in missiles2_fired.copy():
        if mis2.rect.bottom <= 0:
            missiles2_fired.remove(mis2)

    # remove the missile and alien which have collided
    collide1 = pygame.sprite.groupcollide(
        missiles1_fired, curaliens, True, True)
    collide2 = pygame.sprite.groupcollide(
        missiles2_fired, curaliens, True, False)

    settings.Score.update_score(score, len(collide1))

    # extend the life of aliens that were hits by misssile2
    for luckyaliens in collide2:
        for et in collide2[luckyaliens]:
            aliens.Aliens.extendlife(et)

    # draw the updated missiles to the screen
    for mis1 in missiles1_fired:
        mis1.draw_missile()
    for mis2 in missiles2_fired:
        mis2.draw_missile()

    # draw the ship onto the screen
    ship.blitme()

    # draw the currently alive aliens onto the screen
    for alien in curaliens:
        alien.blitme()

    # finally update the screen after making all changes
    pygame.display.update()
