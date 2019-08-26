import pygame
from settings import Settings
import game_function as gf
from bird import Bird
from pygame.sprite import Group
from button import Button
from score import Scoreboard


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Flying Bird")

    bird = Bird(ai_settings, screen)
    mountains = Group()

    button = Button(ai_settings, screen, "PLAY")

    # 创建计分板
    sb = Scoreboard(ai_settings, screen)

    while True:

        gf.check_events(bird, button, ai_settings, mountains)

        if ai_settings.state:
            bird.update_bird()
            mountains.update(ai_settings)
            gf.update_mountains(bird, mountains, ai_settings)
            gf.built_mountains(mountains, ai_settings, screen)

        gf.update_screen(ai_settings, screen, bird, mountains, button, sb)


run_game()