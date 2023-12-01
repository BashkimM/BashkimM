class Subject:
    """
    Die Abstrakte Klasse ist Gegenstand des Observer Pattern.
    """

    def __init__(self):
        """
        Der Konstruktor der Klasse.
        """
        self.observers = []

    def add_observer(self, observer):
        """
        Fügt der Observer-Liste einen Observer hinzu.
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        Entfernt einen Observer aus der Observer-Liste.
        """
        self.observers.remove(observer)

    def notify(self, payload):
        """
        Benachrichtigt alle Observer:param payload:
        """
        for observer in self.observers:
            observer.update(payload)


class IObserver:
    """
    Die Abstrakte-Klasse ist der Observer des Observer Pattern.
    """

    def update(self, payload):
        """
        Die Methode update wird aufgerufen, wenn das Subjekt benachrichtigt wird.
        """
        raise NotImplementedError
