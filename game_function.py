import pygame
import sys
from mountains import Mountains


def update_screen(ai_settings, screen, bird, mountains, button, sb):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.background_color)

    bird.blitme()
    for mountain in mountains.sprites():
        mountain.draw_mountains()

    if not ai_settings.state:
        button.draw_button()

    sb.prep_score(ai_settings.score)
    sb.show_score()
    # ai_settings.score_up += 1

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_events(bird, action_button, ai_settings, mountains):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            onkey_change(event, bird, ai_settings)
        elif event.type == pygame.KEYUP:
            onkey_change(event, bird, ai_settings)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            restart_game(bird, action_button, ai_settings, mountains)


def restart_game(bird, action_button, ai_settings, mountains):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if action_button.rect.collidepoint(mouse_x, mouse_y) and ai_settings.state == False:
        ai_settings.reset()
        bird.reset(ai_settings)
        mountains.empty()
        ai_settings.state = True


def onkey_change(event, bird, ai_settings):

    if event.key == pygame.K_ESCAPE:
        sys.exit()

    if not ai_settings.state:
        return

    if event.key == pygame.K_SPACE:
        bird.direct *= -1
        if event.type == pygame.KEYDOWN:
            bird.image = pygame.image.load("images/bird_up.bmp")
        if event.type == pygame.KEYUP:
            bird.image = pygame.image.load("images/bird_flying.bmp")



def built_mountains(mountains, ai_settings, screen):

    if len(mountains) == 0:
        new_mountain = Mountains(ai_settings, screen, "top")
        mountains.add(new_mountain)
        new_mountain = Mountains(ai_settings, screen, "bottom")
        mountains.add(new_mountain)

    create_flag = True
    for mountain in mountains:
        if mountain.rect.right + 400 > mountain.screen_rect.right:
            create_flag = False

    if create_flag:
        new_mountain = Mountains(ai_settings, screen, "top")
        mountains.add(new_mountain)
        new_mountain = Mountains(ai_settings, screen, "bottom")
        mountains.add(new_mountain)


def update_mountains(bird, mountains, ai_settings):
    # 删除已消失的山
    for mountain in mountains.copy():
        if mountain.rect.right <= 0:
            mountains.remove(mountain)

    check_bird_mountains(bird, mountains, ai_settings)


def check_bird_mountains(bird, mountains, ai_settings):

    if pygame.sprite.spritecollideany(bird, mountains):
        ai_settings.state = False