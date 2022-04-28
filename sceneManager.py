from Scenes.gameScene import GameScene
from Scenes.login_scene import LoginScene
from Scenes.registration_scene import RegistrationScene

class SceneManager(object):
    def __init__(self) -> None:
        self.goTo(RegistrationScene())

    def goTo(self,scene):
        self.scene = scene
        self.scene.manager = self