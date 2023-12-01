from components.sprites_interface import ImageSprite


class PlayAgainButton(ImageSprite):
    file_name = "PlayAgainButton.png"
    name = "PlayAgain"

    def __init__(self, bx, by):
        ImageSprite.__init__(self, self.file_name, bx, by)
