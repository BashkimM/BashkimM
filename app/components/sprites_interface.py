import os

import pygame as pg
from pygame import sprite


class ImageSprite(sprite.Sprite):
    """
    Superklasse für die Sprites. Wir brauchen den Pfad zum Bilderordner nur einmal zu definieren. Die Subklassen brauchen
    nur noch den Dateinamen und die anfänglichen Koordinaten zu setzen.
    """

    # Das Verzeichnis dieser Datei
    component_folder = os.path.dirname(__file__)
    # Der erste Teil des Split ist der Pfad ohne den aktuellen Ordner, also der Ordner, "app"
    app_folder = os.path.split(component_folder)[0]
    # Zusammenfügen des Pfades zu den Bildern
    graphic_folder = os.path.join(app_folder, "graphic")

    def __init__(self, image_file, bx, by):
        sprite.Sprite.__init__(self)
        # Der Pfad zum Bild wird im init zusammengefügt.
        self.image = pg.image.load(os.path.join(self.graphic_folder, image_file))
        self._bx = bx
        self._by = by
        self.rect = self.image.get_rect()
        # Wir verwenden rect.center, da hauptsächlich zentrierte Bilder verwendet werden.
        self.rect.center = (self._bx, self._by)

    def render(self, screen):
        screen.blit(self.image, self.rect)
