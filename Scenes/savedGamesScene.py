import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
import Scenes.game_Scene
from database_controller import DB_Controller

class SavedGamesScene(Scene):
    #GUI Manager
    def __init__(self):

        self.savedGames_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        self.savedGames = self.loadSavedGames()
        self.createSaveGameEntry(self.savedGames)

    def createSaveGameEntry(self, data):
        if len(data) > 0:
            for entryIndex, entry in enumerate(data):
                dateTextBox =gui_elements.createTextfeld((0,0), entry[4], globals.textboxTypes['INFO'],self.savedGames_manager)
                loadEntry = gui_elements.createButton((260,0),"Spielstand laden",globals.buttonTypes["ACCEPT"],self.savedGames_manager)
        else:
            textBox = gui_elements.createTextfeld((0,0), "Keine Spielstände vorhanden", globals.textboxTypes['INFO'],self.savedGames_manager)


    def loadSavedGames(self):
        dbcontroller = DB_Controller()
        return dbcontroller.loadSavedGames(globals.user["id"])

    def update(self, time_delta):
        self.savedGames_manager.update(time_delta)

    def render(self, screen):
        self.savedGames_manager.draw_ui(screen)

    def handleEvents(self, events):
        for event in events:
            self.savedGames_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.new_game_button:
                            print('new game')
                            self.manager.goTo(Scenes.game_Scene.GameScene())
                        elif event.ui_element == self.load_game_button:
                            self.loadSavedGames()
                        elif event.ui_element == self.exit_button:
                            print('exit')