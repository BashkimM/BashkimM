from pygame import font

import config
import utility


class InGameScoreboard:
    def __init__(self, score, highscore):
        self._score = score
        self._highscore = highscore

    def update(self):
        self.set_highscore(utility.get_persistent_highscore())

    def render(self, screen):
        """
        Der aktuelle Spielstand und Highscore werden über dem Spielfeld(Grid) dargestellt
        """
        text = font.SysFont(config.FONT, 30)

        current_score = text.render(str(self.get_score()), True, config.BLACK)
        current_score_text = text.render("Score:", True, config.BLACK)
        highscore_text = text.render("HighScore:", True, config.BLACK)
        highscore = text.render(str(self.get_highscore()), True, config.BLACK)

        score_left_boundary = config.DISPLAY_WIDTH - highscore.get_width() - 50
        text_left_boundary = config.DISPLAY_WIDTH - 200

        screen.blit(highscore_text,
                    (text_left_boundary - highscore_text.get_width(),
                     config.DISPLAY_MARGIN_Y - highscore_text.get_height() + 8)
                    )

        screen.blit(highscore,
                    (score_left_boundary, config.DISPLAY_MARGIN_Y - highscore_text.get_height() + 8)
                    )

        screen.blit(current_score_text,
                    (text_left_boundary - current_score_text.get_width(), config.DISPLAY_MARGIN_Y + 8)
                    )
        screen.blit(current_score,
                    (score_left_boundary, config.DISPLAY_MARGIN_Y + 8)
                    )

    def get_score(self):
        return self._score

    def set_score(self, new_score):
        self._score = new_score

    def get_highscore(self):
        return self._highscore

    def set_highscore(self, new_highscore):
        self._highscore = new_highscore
