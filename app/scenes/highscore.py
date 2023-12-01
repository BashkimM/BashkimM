import pygame

import config
from components.backbutton import BackButton
from components.highscores import Highscore
from components.playagainbutton import PlayAgainButton
from scenes.game_scene_interface import IGameScene
from scenes.scenes_enum import ScenesEnum
from utility import draw_text, build_highscore_list


class HighscoreScene(IGameScene):
    def __init__(self):
        self._last_score = 0

        # Laden der Bilder und Buttons der Szene
        self._images = pygame.sprite.Group(
            Highscore(config.DISPLAY_WIDTH / 2, 50),
        )
        self._buttons = pygame.sprite.Group(
            PlayAgainButton(config.DISPLAY_WIDTH / 2 + 130, 550),
            BackButton(config.DISPLAY_WIDTH / 2 - 130, 550)
        )

    # Darstellung der Elemente auf dem Bildschirm
    def render(self, screen):
        screen.fill(config.GREY)
        self._images.draw(screen)
        self._buttons.draw(screen)
        self.highscore_board(screen, self._last_score)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self._buttons:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "PlayAgain":
                                # startet ein neues Spiel
                                self.manager.change_scene(self.manager.scenes[ScenesEnum.GAMEPLAY])
                            if button.name == "BackButton":
                                # Sprung zum Welcome Screen
                                self.manager.change_scene(self.manager.scenes[ScenesEnum.WELCOME])
            if event.type == pygame.KEYDOWN:
                # zur intuitiven Bedienung backspace = zurück
                if event.key == pygame.K_BACKSPACE:
                    self.manager.change_scene(self.manager.scenes[ScenesEnum.GAMEPLAY])

    def update(self):
        pass

    def highscore_board(self, screen, last_score):
        # Die Highscore Liste wird geladen
        highscore = build_highscore_list()

        line_height = 40
        list_position_y = 100
        name_left = 300

        # Maximal 10 Einträge der Highscore-Liste ausgeben, aber nur so viele Iterationen zulassen, wie es Einträge gibt
        for i in range(min(len(highscore), 10)):

            if highscore[i][1] == 0:
                continue

            color = config.BLACK
            # wenn der letzte Score nicht 0 ist, und in der top10 liegt,
            # wird die betreffende Zeile farblich hervorgehoben
            if not last_score == 0 and highscore[i][1] == last_score:
                color = config.GREEN

            draw_text(f"{str(i + 1)}:", name_left - 100, list_position_y + i * line_height, screen, size=40,
                      color=color)
            draw_text(f"{str(highscore[i][0])}", name_left - 40, list_position_y + i * line_height, screen, size=40,
                      color=color)
            draw_text(f"{str(highscore[i][1])}", name_left + 270, list_position_y + i * line_height, screen, size=40,
                      color=color)

    def set_last_score(self, last_score):
        self._last_score = last_score
