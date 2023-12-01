from pygame import sprite

from observers import IObserver
from utility import get_persistent_highscore


class ScoreTracker(IObserver, sprite.Sprite):
    def __init__(self):
        self._score: int = 0
        self._highscore: int = get_persistent_highscore()

    def update(self, payload):
        """
        Addiert die in der game_engine generierten Punktegewinne.
        """
        if "latestScore" in payload:
            self._score += payload["latestScore"]

        # Wenn der aktuelle Score größer als der Highscore ist, wird dieser aktualisiert
        if self._score > self._highscore:
            self._highscore = self._score

        if "resetScore" in payload:
            self._score = 0

    def get_score(self):
        return self._score

    def get_highscore(self):
        return self._highscore

    def set_highscore(self, highscore):
        self._highscore = highscore
