import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
from Scenes.game_Scene import GameScene
from database_controller import DB_Controller

class SavedGamesScene(Scene):
    #GUI Manager
    def __init__(self):

        self.ButtonListWithGameNumber = []
        self.savedGames_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        self.savedGames = self.loadSavedGames()
        self.createSaveGameEntry(self.savedGames)

    def createSaveGameEntry(self, data):
        if len(data) > 0:
            for entryIndex, entry in enumerate(data):
                positionY = entryIndex * 60
                dateTextBox =gui_elements.createTextfeld((0,positionY), entry[4], globals.textboxTypes['INFO'],self.savedGames_manager)
                loadEntryButton = gui_elements.createButton((260,positionY),"Spielstand laden",globals.buttonTypes["ACCEPT"],self.savedGames_manager)
                self.ButtonListWithGameNumber.append((loadEntryButton, entry[0]))
        else:
            textBox = gui_elements.createTextfeld((0,0), "Keine Spielstände vorhanden", globals.textboxTypes['INFO'],self.savedGames_manager)


    def loadSavedGames(self):
        dbcontroller = DB_Controller()
        return dbcontroller.loadSavedGames(globals.user["id"])

    def loadSaveGameAndInitiliaseGame(self,gameNumber):
        dbcontroller = DB_Controller()
        result = dbcontroller.loadSaveFileGame(globals.user["id"],gameNumber)
        self.manager.goTo(GameScene(True,result))

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
                        for entry in self.ButtonListWithGameNumber:
                            print("Entry: ",entry)
                            if event.ui_element == entry[0]:
                                print(entry[1])
                                self.loadSaveGameAndInitiliaseGame(entry[1])
                                
                     