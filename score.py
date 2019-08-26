import pygame.font
from pygame.sprite import Group


class Scoreboard():

    def __init__(self, ai_settings, screen):
        '''初始化显示得分涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 显示得分信息时使用的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score(ai_settings.score)

    def prep_score(self, score):
        '''得分、等级转换为一副渲染的图像'''
        rounded_score = int(round(score,1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.background_color)

        # 将得分显示在屏幕左上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.screen_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)