from components.sprites_interface import ImageSprite


class PlayButton(ImageSprite):
    file_name = "PlayButton.png"
    name = "PlayButton"

    def __init__(self, bx, by):
        ImageSprite.__init__(self, self.file_name, bx, by)
