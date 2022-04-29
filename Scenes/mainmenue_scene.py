import Scenes.leaderboard_scene
from Scenes.savedGamesScene import SavedGamesScene
import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
import Scenes.game_Scene
from database_controller import DB_Controller

class MainMenueScene(Scene):
    #GUI Manager
    def __init__(self):
        self.username = ""
        self.password = ""
        
        self.mainmenue_manager = pygame_gui.UIManager((1200, 800), 'theme.json')

        self.new_game_button = gui_elements.createButton((0,300),'NEW GAME','ACCEPT', self.mainmenue_manager)
        self.load_game_button = gui_elements.createButton((0,350),'LOAD GAME','ACCEPT', self.mainmenue_manager)
        self.leaderboard_button = gui_elements.createButton((0,400),'LEADERBOARD','ACCEPT', self.mainmenue_manager)
        self.exit_button = gui_elements.createButton((0,450),'EXIT','ACCEPT', self.mainmenue_manager)

    def login(self):
        dbcontroller = DB_Controller()
        return dbcontroller.checkifplayerexistinDB(self.username, self.password)

    def loadSavedGames(self):
        dbcontroller = DB_Controller()
        print(dbcontroller.loadSavedGames(globals.user["id"]))

    def update(self, time_delta):
        self.mainmenue_manager.update(time_delta)

    def render(self, screen):
        self.mainmenue_manager.draw_ui(screen)

    def handleEvents(self, events):
        for event in events:
            self.mainmenue_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.new_game_button:
                            print('new game')
                            self.manager.goTo(Scenes.game_Scene.GameScene(False))
                        elif event.ui_element == self.load_game_button:
                            self.manager.goTo(SavedGamesScene())
                        elif event.ui_element == self.leaderboard_button:
                            print('leaderboard')
                            self.manager.goTo(Scenes.leaderboard_scene.LeaderboardScene())
                        elif event.ui_element == self.exit_button:
                            print('exit')
                            pygame.quit()