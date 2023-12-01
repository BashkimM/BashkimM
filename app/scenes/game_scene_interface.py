class IGameScene:
    """
    Interface Klasse der Szenen:
    Die Methode render kümmert sich um das Zeichnen des Bildschirms, während die Methode handle_events die Ereignisse verarbeitet, 
    die an die Szene übergeben werden.
        """

    # jede Szene muss einen Verweis auf den Szenenmanager haben
    def __init__(self):
        self.manager = None

    def handle_events(self, events):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def render(self, screen):
        raise NotImplementedError
