from components.sprites_interface import ImageSprite


class GameOverSprite(ImageSprite):
    file_name = "GameOver.png"
    name = "GameOver"

    def __init__(self, bx, by):
        ImageSprite.__init__(self, self.file_name, bx, by)
