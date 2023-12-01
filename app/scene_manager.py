from scenes.game_scene_interface import IGameScene
from scenes.scenes_enum import ScenesEnum


class SceneManager:
    """
    Der Szenenmanager ist verantwortlich für die Verwaltung der Szenen. Das Erzeugen der Instanzen erwartet eine Scene
    als Parameter, die IGameScene implementiert. Damit wird sichergestellt, dass die Scene auf jeden Fall die
    drei Methoden des Game Loops implementiert: handle_events, update und render.
    Der SzenenManager ist inspiriert von:
    https://nicolasivanhoe.wordpress.com/2014/03/10/game-scene-manager-in-python-pygame/
    https://stackoverflow.com/a/14727074/8784614
    """

    def __init__(self, scene: IGameScene):
        self.scenes = {}
        self.scene = scene
        self.scene.manager = self

    def register_scene(self, scene: IGameScene, name: ScenesEnum):
        self.scenes[name] = scene
        self.scene.manager = self

    def change_scene(self, scene: IGameScene):
        self.scene = scene
        self.scene.manager = self
