class Settings():

    def __init__(self):

        self.background_color = (255, 255, 255)
        self.screen_width = 1200
        self.screen_height = 600

        self.bird_speed = 1
        self.bird_direct = 1

        self.mountains_width = 100
        self.mountains_speed = 1
        self.mountains_color = (20, 20, 20)
        self.mountains_previous = 0
        self.change_limit = 300

        self.button_width = 200
        self.button_height = 50

        self.score = 0
        self.score_up = 1

        self.state = False

    def reset(self):
        self.bird_speed = 1
        self.bird_direct = 1
        self.mountains_speed = 1
        self.mountains_previous = 0
        self.change_limit = 200
        self.score = 0