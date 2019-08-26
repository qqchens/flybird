import pygame

class Bird():

    def __init__(self, ai_settings, screen):
        '''创建小鸟'''
        self.image = pygame.image.load("images/bird_flying.bmp")

        self.ai_settings = ai_settings
        self.screen = screen

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + 300

        self.speed = ai_settings.bird_speed
        self.direct = ai_settings.bird_direct

    def blitme(self):
        '''在指定位置绘制小鸟'''
        self.screen.blit(self.image, self.rect)

    def update_bird(self):

        if self.rect.y < 0:
            self.rect.y += 1
        elif self.rect.bottom > self.screen_rect.bottom:
            self.rect.y -= 1
        else:
            self.rect.y += float(self.speed * self.direct)

    def reset(self, ai_settings):
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + 300

        self.speed = ai_settings.bird_speed
        self.direct = ai_settings.bird_direct