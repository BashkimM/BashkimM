import pygame as pg
from pygame.sprite import Sprite

import config


class NumberTile(Sprite):
    def __init__(self, bx, by, text="0", ):
        Sprite.__init__(self)
        self._surface = pg.Surface((config.TILE_SIZE, config.TILE_SIZE), pg.SRCALPHA, 32)

        self._basic = pg.rect.Rect(0, 0, config.TILE_SIZE, config.TILE_SIZE)

        self.set_background_color(config.WHITE)

        self._tile_value = pg.font.SysFont("arial", 40)

        self._text: str = str(text)

        # position
        self.rect = self._surface.get_rect()

        self._bx = (config.GRID_GUTTER_WIDTH / 2) + bx * 100
        self._by = (config.GRID_GUTTER_WIDTH / 2) + by * 100

        self.rect.topleft = (self._bx, self._by)

    def update(self):
        pass

    def render(self, screen):
        # Kacheln werden farblich je nach Wert der Kachel gefärbt
        if self._text != "0":
            self.set_background_color(config.TILE_COLORS[self._text])
            # Berechnung, damit der Wert der Kachel mittig dargestellt wird.
            self._surface.blit(self._tile_value.render(self._text, True, config.BLACK),
                               (config.TILE_SIZE / 2 - self._tile_value.render(self._text, True,
                                                                               config.BLACK).get_width() / 2,
                                config.TILE_SIZE / 2 - self._tile_value.render(self._text, True,
                                                                               config.BLACK).get_height() / 2))
            screen.blit(self._surface, self.rect)
        # Wenn der Wert in der Kachel 0 ist, wird diese ausgegraut
        elif self._text == "0":
            self.set_background_color(config.BURLYWOOD_LIGHT)
            self._surface.blit(self._tile_value.render(self._text, True, config.BURLYWOOD_LIGHT),
                               (config.TILE_SIZE / 2, config.TILE_SIZE / 2))

            screen.blit(self._surface, self.rect)

    def set_background_color(self, color):
        pg.draw.rect(self._surface, color, self._basic, border_radius=10)

    def set_text(self, text):
        self._text = text
