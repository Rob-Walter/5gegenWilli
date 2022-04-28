import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
from Scenes.login_scene import LoginScene
from database_controller import DB_Controller




class RegistrationScene(Scene):
    #GUI Manager
    def __init__(self):
        self.username = ""
        self.password = ""
        
        self.registration_manager = pygame_gui.UIManager((1200, 800), 'theme.json')

        self.login_label = gui_elements.createTextfeld((0,0),'Username',globals.textboxTypes['INFO'], self.registration_manager)
        self.username_input = gui_elements.createInput((0,50),globals.inputTypes['NORMAL'], self.registration_manager)

        self.password_label = gui_elements.createTextfeld((0,150),'Password',globals.textboxTypes['INFO'], self.registration_manager)
        self.password_input = gui_elements.createInput((0,200),globals.inputTypes['PASSWORD'], self.registration_manager)

        self.registration_button = gui_elements.createButton((0,260),'registrieren','ACCEPT', self.registration_manager)

    def update(self, time_delta):
        self.registration_manager.update(time_delta)

    def render(self, screen):
        self.registration_manager.draw_ui(screen)

    def handleEvents(self, events):
        dbcontroller = DB_Controller()
        for event in events:
            self.registration_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.registration_button:
                            self.username = self.username_input.get_text()
                            self.password = self.password_input.get_text()
                            if len(self.username) >= 3 and len(self.password)  >= 3:
                                if dbcontroller.insertnewplayer(self.username, self.password):
                                    #bitte weiterleiten auf login_scene
                                    self.manager.goTo(LoginScene())
                            else:
                                print('bitte längere Eingabe machen')
                    elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        if event.ui_element == self.username_input:
                            username = self.username_input.get_text()
                            print('text:', username)