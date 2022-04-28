from Scenes.game_Scene import GameScene
from Scenes.login_scene import LoginScene
from Scenes.registration_scene import RegistrationScene
from Scenes.mainmenue_scene import MainMenueScene
from Scenes.rules_scene import RulesScene

class SceneManager(object):
    def __init__(self) -> None:
        self.goTo(RulesScene())

    def goTo(self,scene):
        self.scene = scene
        self.scene.manager = self