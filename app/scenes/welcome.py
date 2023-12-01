import pygame

import config
from components.highscores import Highscore
from components.logo import Logo
from components.playbutton import PlayButton
from scenes.game_scene_interface import IGameScene
from scenes.scenes_enum import ScenesEnum


class WelcomeScene(IGameScene):
    """
    Diese Szene zeigt den Startbildschirm an. Hier kann der Spieler auf den Play- oder Highscorebutton klicken,
    um zur jeweiligen Szene zu gelangen.
    """

    def __init__(self):

        # Sprites die nur optischen Charakter haben
        self._presentationals = pygame.sprite.Group(
            Logo(config.DISPLAY_WIDTH / 2 - (239 / 2), 100),
        )

        # Sprites, mit denen interagiert werden kann
        self._buttons = pygame.sprite.Group(
            PlayButton(config.DISPLAY_WIDTH / 4 * 1, config.DISPLAY_HEIGHT / 2),
            Highscore(config.DISPLAY_WIDTH / 4 * 3, config.DISPLAY_HEIGHT / 2),

        )

    def handle_events(self, events):
        for event in events:
            # Drücken der primären Maustaste, führt zur Überpfrüfung jedes Sprite der Gruppe Button, 
            # ob die Koordinaten des Mauszeigers auf dem Feld liegen. Liegt der Mauszeiger auf dem Feld "PlayButton",
            # wechseln wir zur GameScene (index 1 in der Liste scenes).
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self._buttons.sprites():
                    if button.rect.collidepoint(event.pos):
                        if button.name == "PlayButton":
                            self.manager.change_scene(self.manager.scenes[ScenesEnum.GAMEPLAY])
                        if button.name == "Highscore":
                            self.manager.change_scene(self.manager.scenes[ScenesEnum.HIGHSCORE])

            # Die Funktion mit der Leertaste ist grundsätzlich für die Entwicklung gedacht gewesen, aber auch für
            # Vielspieler praktisch
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.manager.change_scene(self.manager.scenes[ScenesEnum.GAMEPLAY])

    def update(self):
        """
        In der Update-Methode dieser Scene passiert nichts.
        """
        pass

    def render(self, screen):
        """
        Einfärben des Bildschirms und zeichnen der Spritegruppen auf den Bildschirm.
        """
        screen.fill(config.GREY)

        self._presentationals.draw(screen)
        self._buttons.draw(screen)
