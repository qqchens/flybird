import pygame.font


class Button():

    def __init__(self ,ai_settings, screen, content):
        '''初始化按钮属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.ai_settings = ai_settings

        # 设置按钮的尺寸和其他属性
        self.width, self.height = ai_settings.button_width, ai_settings.button_height
        self.button_color = (0, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.content = content

        self.preg_msg()

    def preg_msg(self):
        '''将msg渲染为图像，并使其在按钮上居中'''
        self.msg_image = self.font.render(self.content, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)