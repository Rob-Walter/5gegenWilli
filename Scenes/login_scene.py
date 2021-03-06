from Scenes.mainmenue_scene import MainMenueScene
from Scenes.start_scene import StartScene
import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
from database_controller import DB_Controller




class LoginScene(Scene):
    #GUI Manager
    #Login Manager
    def __init__(self):
        self.username = ""
        self.password = ""
        
        self.login_manager = pygame_gui.UIManager((1200, 800), 'theme.json')

        self.login_label = gui_elements.createTextfeld((500,200),'USERNAME',globals.textboxTypes['INFO'], self.login_manager)
        self.username_input = gui_elements.createInput((500,250),globals.inputTypes['NORMAL'], self.login_manager)

        self.password_label = gui_elements.createTextfeld((500,320),'PASSWORD',globals.textboxTypes['INFO'], self.login_manager)
        self.password_input = gui_elements.createInput((500,370),globals.inputTypes['PASSWORD'], self.login_manager)

        self.login_button = gui_elements.createButton((500,480),'LOGIN',globals.buttonTypes['ACCEPT'], self.login_manager)

        self.back_button = gui_elements.createButton((500,530),'BACK',globals.buttonTypes['ACCEPT'], self.login_manager)

    def login(self):
        dbcontroller = DB_Controller()
        return dbcontroller.checkifplayerexistinDB(self.username, self.password)

    def update(self, time_delta):
        self.login_manager.update(time_delta)

    def render(self, screen):
        self.login_manager.draw_ui(screen)

    def handleEvents(self, events):
        for event in events:
            self.login_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.login_button:
                            self.username = self.username_input.get_text()
                            self.password = self.password_input.get_text()
                            if self.login():
                                self.manager.goTo(MainMenueScene())
                            else:
                                print('Spieler nicht gefunden')
                        elif event.ui_element == self.back_button:
                            print('back')
                            self.manager.goTo(StartScene())
                    #if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        #if event.ui_element == self.username_input:
                            #username = self.username_input.get_text()
                            #print('text:', username)