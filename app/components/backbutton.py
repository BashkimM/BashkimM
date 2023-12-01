from components.sprites_interface import ImageSprite


class BackButton(ImageSprite):
    file_name = "Home.png"
    name = "BackButton"

    def __init__(self, bx, by):
        ImageSprite.__init__(self, self.file_name, bx, by)
