from gameScene import GameScene

class SceneManager(object):
    def __init__(self) -> None:
        self.goTo(GameScene())

    def goTo(self,scene):
        self.scene = scene
        self.scene.manager = self