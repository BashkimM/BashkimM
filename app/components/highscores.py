from components.sprites_interface import ImageSprite


class Highscore(ImageSprite):
    file_name = "Highscore.png"
    name = "Highscore"

    def __init__(self, bx, by):
        ImageSprite.__init__(self, self.file_name, bx, by)
