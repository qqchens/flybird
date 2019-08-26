import pygame
from pygame.sprite import Sprite
import random

class Mountains(Sprite):

    def __init__(self, ai_settings, screen, position):

        # 在飞船所处的位置创建一个子弹类
        super(Mountains, self).__init__()  #or super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.color = ai_settings.mountains_color

        self.height = random.randint(0,500)
        while abs(ai_settings.mountains_previous - self.height) > ai_settings.change_limit:
            self.height = random.randint(0, 500)

        if position == "bottom":
            self.height = 400 - ai_settings.mountains_previous

        self.rect = pygame.Rect(0, 0, ai_settings.mountains_width,
                                self.height)

        self.rect.right = self.screen_rect.right
        if position == "top":
            ai_settings.mountains_previous = self.height
            self.rect.top = self.screen_rect.top
            ai_settings.score += ai_settings.score_up
        elif position == "bottom":
            self.rect.bottom = self.screen_rect.bottom



    def update(self, ai_settings):

        self.rect.x -= ai_settings.mountains_speed

    def draw_mountains(self):
        pygame.draw.rect(self.screen, self.color, self.rect)