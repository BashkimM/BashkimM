import pygame as pg

from components.sprites_interface import ImageSprite


class Logo(ImageSprite):
    file_name = "Logo.png"
    name = "Logo"

    def __init__(self, bx, by, scale=1):
        ImageSprite.__init__(self, self.file_name, bx, by)

        # Position von Oben Links in diesem Fall
        self.rect.topleft = (self._bx, self._by)

        # Skalierung der Logo, damit wir die gleiche Klasse nehmen können.
        if scale != 1:
            self.size = self.image.get_size()
            self.scaled_image = pg.transform.scale(self.image,
                                                   (int(self.size[0] * scale),
                                                    int(self.size[1] * scale)))
            self.image = self.scaled_image

            self.rect = self.image.get_rect()
            self.rect.center = (self._bx, self._by)
