import pygame

from config import DISPLAY_WIDTH, DISPLAY_HEIGHT, FPS
from scene_manager import SceneManager
from scenes.gameover import GameOverScene
from scenes.gameplay import GamePlayScene
from scenes.highscore import HighscoreScene
from scenes.scenes_enum import ScenesEnum
from scenes.welcome import WelcomeScene


# from app.scenes.Highscorescene import HighscoreScene


class Game:
    """
    Die Klasse Game ist die Hauptklasse des Spiels. Hauptverantwortlich hierin ist der SceneManager, über den wir
    die verschiedenen Spielbildschirme (Scenes) verwalten und ansteuern können.
    Der Scene Manager wird mit der "WelcomeScene" initialisiert. Alle Scenen implementieren das Interface "GameScene" und
    haben daher die drei Methoden handle_events(), update() und render().
    """

    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.scene_manager = SceneManager(WelcomeScene())
        self.setup_scenes()

    def run(self):
        """
        Die Methode run() wird aufgerufen, sobald das Spiel über die main.py gestartet wird. Sie beinhaltet den Game Loop
        aus den Vorlesungsunterlagen und ruft die Methoden handle_events(), update() und render() der aktuellen Szene auf.
        """
        while self.running:

            self.clock.tick(FPS)

            if pygame.event.get(pygame.QUIT):
                self.running = False

            self.scene_manager.scene.handle_events(pygame.event.get())

            self.scene_manager.scene.update()

            self.scene_manager.scene.render(self.screen)

            pygame.display.flip()

        pygame.quit()

    def setup_scenes(self):
        self.scene_manager.register_scene(WelcomeScene(), ScenesEnum.WELCOME)
        self.scene_manager.register_scene(GamePlayScene(), ScenesEnum.GAMEPLAY)
        self.scene_manager.register_scene(GameOverScene(), ScenesEnum.GAMEOVER)
        self.scene_manager.register_scene(HighscoreScene(), ScenesEnum.HIGHSCORE)


"""
Wir starten das Spiel nur, wenn es aus der main.py aufgerufen wird.
"""
if __name__ == '__main__':
    app = Game()
    app.run()
