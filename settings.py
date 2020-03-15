class Settings():
    """
    A class to store all settings for alien invasion
    """

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (56, 45, 44)
        self.fps = 120
        self.score_color = (212, 175, 55)
        # missile1 settings
        self.mi1_height = 50
        self.mi1_width = 20
        self.mi1_color = (255, 0, 0)
        self.mi1_speed = 200 / self.fps
        # missile2 settings
        self.mi2_height = 60
        self.mi2_width = 30
        self.mi2_color = (0, 200, 0)
        self.mi2_speed = 400 / self.fps


class Score():
    """
    A class for maintaining a simple scoreboard
    """

    scorectr = 0

    def update_score(self, value):
        Score.scorectr += value
