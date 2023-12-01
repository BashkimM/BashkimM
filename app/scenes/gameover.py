import pygame

import config
from components.gameover import GameOverSprite
from components.playagainbutton import PlayAgainButton
from scenes.game_scene_interface import IGameScene
from scenes.scenes_enum import ScenesEnum
from utility import draw_text, write_highscore_to_file, check_input_char


class GameOverScene(IGameScene):
    """
    Sobald das Spiel beendet ist wird diese Scene aufgerufen. Sie fordert den Spieler auf einen Namen einzugeben,
    um seinen Highscore in die Highscoreliste einzutragen.
    """

    def __init__(self, last_score=0):
        self._highscore_submitted = False
        self._last_score = last_score
        self._user_name = ""
        self._images = pygame.sprite.Group(
            GameOverSprite(config.DISPLAY_WIDTH / 2, 100),
        )
        self._buttons = pygame.sprite.Group(
            PlayAgainButton(config.DISPLAY_WIDTH / 2, 400)
        )

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self._buttons:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "PlayAgain":
                                self.manager.change_scene(self.manager.scenes[ScenesEnum.GAMEPLAY])
            if event.type == pygame.KEYDOWN:
                if not self._highscore_submitted:
                    self.handle_name_input_events(event)

    def update(self):
        pass

    def render(self, screen):
        screen.fill(config.GREY)
        self._images.draw(screen)
        self._buttons.draw(screen)
        self.create_input_dialogue(screen)

    def create_input_dialogue(self, scr):
        # Legt die Größe der Eingabefelder fest
        widget_width = 400
        widget_height = 200

        # Erstellt die Felder für die Eingabe
        widget_surface = pygame.Surface((widget_width, widget_height), pygame.SRCALPHA, 32)
        text_surface = pygame.Surface((widget_width, 30))
        text_surface.fill(config.WHITE)

        # Fordert den Spieler auf, seinen Namen einzugeben
        draw_text("Enter your name and press", 75, 10, widget_surface, size=22)
        draw_text("return to submit highscore.", 79, 30, widget_surface, size=22)
        draw_text("'Play Again' won't save your score", 35, 140, widget_surface, size=22)

        # Stellt das Eingabfeld dar
        text_input = pygame.font.Font(None, 30).render(self._user_name, True, (0, 0, 0), (255, 255, 255))
        text_surface.blit(text_input, (5, 5))
        widget_surface.blit(text_surface, (10, 60))
        scr.blit(widget_surface,
                 (config.DISPLAY_WIDTH / 2 - widget_width / 2, config.DISPLAY_WIDTH / 2 - widget_height))

    def handle_name_input_events(self, e):
        """
        Verarbeitet die Nutzereingaben der Namenseingabe
        """
        # Nur alphanumerisch und leertaste wird akzeptiert
        if check_input_char(e):
            # fügt das Zeichen der Benutzereingabe hinzu
            self._user_name += chr(e.key)
        # Rückstelltaste = löschen
        if e.key == pygame.K_BACKSPACE:
            self._user_name = self._user_name[:-1]
        # Abspeichern bei Enter
        if e.key == pygame.K_RETURN:
            if self._user_name != "" and self._highscore_submitted is False:
                player_name = self._user_name
                player_score = str(self._last_score)
                self._user_name = "Submitted! Thank you."
                try:
                    write_highscore_to_file(player_name, player_score)
                    self._highscore_submitted = True

                    # Den letzten Highscore in der HighScoreSzene zur Verfügung stellen
                    self.manager.scenes[ScenesEnum.HIGHSCORE].set_last_score(self._last_score)
                    self.manager.change_scene(self.manager.scenes[ScenesEnum.HIGHSCORE])
                except:
                    self._user_name = "Sorry, there was an error."
