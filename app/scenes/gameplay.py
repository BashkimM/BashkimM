import pygame

import config
import game_engine
from components.in_game_scoreboard import InGameScoreboard
from components.logo import Logo
from components.number_tile import NumberTile
from scenes.game_scene_interface import IGameScene
from scenes.gameover import GameOverScene
from score_tracker import ScoreTracker


class GamePlayScene(IGameScene):
    """
    Die Klasse GamePlayScene stellt den Mittelpunkt des Spiels dar.
    """

    def __init__(self):
        self._tiles = []  # 2-dimensionale Darstellung der einzelnen Zahlen auf dem Spielfeld.

        self._sprites = [
            Logo(config.DISPLAY_MARGIN_X, config.DISPLAY_MARGIN_Y, 0.5),
        ]

        # Wir initialisieren die Game-Engine und starten das Spielfeld mit der Standard-Größe aus der Config.
        self._game = game_engine.GameEngine()
        self._game.start_game(config.DEFAULT_GRID_SIZE)

        # Wird auf True gesetzt, wenn die Spielfeld-Tiles erstellt wurden.
        self._grid_drawn = False

        # Observer für die Punkteerfassung
        self.score_tracker = ScoreTracker()

        self._game.add_observer(self.score_tracker)
        self._sprites.append(InGameScoreboard(self.score_tracker.get_score(), self.score_tracker.get_highscore()))

    def handle_events(self, events):

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._game.update('left')
                elif event.key == pygame.K_RIGHT:
                    self._game.update('right')
                elif event.key == pygame.K_UP:
                    self._game.update('up')
                elif event.key == pygame.K_DOWN:
                    self._game.update('down')
                # eigentlich nur für die Entwicklung hier drin, jedoch auch nützlich für die Präsentation
                elif event.key == pygame.K_q:
                    self._game.game_over = True

    def update(self):
        """
        Iteriert über jedes Element in der Liste und ruft die Update-Methode return auf.
        """

        # wenn die Game-Engine das Ende des Spiels erkannt hat, setzen wir das Spiel zurück und wechseln zur
        # GameOver Scene, dabei übergeben wir den Score.
        if self._game.game_over:
            # current_score wird erstellt, da reset_game den Punktestand zurücksetzt
            current_score = self.score_tracker.get_score()
            self._game.reset_game()
            self.manager.change_scene(GameOverScene(current_score))

        # Wenn die Spielfeld-Tiles noch nicht erstellt wurden, erstellen wir sie. Die Kacheln bewegen sich nicht,
        # sondern ändern ihren Wert und ihre Farbe.
        if not self._grid_drawn:
            self.setup_grid_tiles()
            self._grid_drawn = True

        self.update_number_tiles(self._game.grid)

        self._sprites[1].set_score(self.score_tracker.get_score())

        for sprite in self._sprites:
            sprite.update()

    def render(self, screen):
        """
        Einfärben des Bildschirms und zeichnen des Spielfelds.
        Das Spielfeld wird durch ein gefärbtes Rechteck dargestellt. Auf dieses Rechteck werden die Kacheln
        gezeichnet, die wiederum die Werte beinhalten.
        """
        screen.fill(config.GREY)

        # Das Hintergrundobjekt
        background_surface = pygame.Surface((config.GAME_BOARD_HEIGHT, config.GAME_BOARD_WIDTH), pygame.SRCALPHA, 32)

        background = pygame.rect.Rect(0, 0, config.GAME_BOARD_WIDTH, config.GAME_BOARD_HEIGHT)
        background = pygame.draw.rect(background_surface, config.BURLYWOOD, background, border_radius=10)

        background.center = config.DISPLAY_WIDTH / 2, config.DISPLAY_HEIGHT / 2 + config.GAME_BOARD_MARGIN_TOP

        for sprite in self._sprites:
            sprite.render(screen)

        self.render_number_tiles(background_surface)

        screen.blit(background_surface, background)

    def setup_grid_tiles(self):
        """
        Erstellt die Kacheln, die das Spielfeld darstellen. Dafür wird das aktuelle Grid aus der Game-Engine verwendet.
        Die Kacheln werden erstmalig aufgebaut und daher werden die NumberTiles instanziiert.
        """
        self._tiles = [[NumberTile(i, j) for j in range(len(self._game.grid[i]))] for i in range(len(self._game.grid))]

        for i in range(len(self._game.grid)):
            for j in range(len(self._game.grid[i])):
                self._tiles[i][j] = NumberTile(j, i, self._game.grid[i][j])

    def update_number_tiles(self, grid):
        """
        Für jede Kachel wird der entsprechende Wert des Grids geholt und in der Kachel gesetzt. Auf dieser Grundlage
        wird dann beim Aufruf der Methode "render" der Text und die Farbe gesetzt.
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tile = self._tiles[i][j]
                tile.set_text(str(grid[i][j]))

    def render_number_tiles(self, background_surface):
        """
        Ruft für jede Kachel die Methode "render" auf.
        """
        for i in range(len(self._tiles)):
            for j in range(len(self._tiles[i])):
                self._tiles[i][j].render(background_surface)
