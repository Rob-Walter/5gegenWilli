import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
import Scenes.game_Scene
#from Scenes.login_scene import LoginScene
import Scenes.start_scene
#from Scenes.registration_scene import RegistrationScene
from database_controller import DB_Controller

class StartScene(Scene):
    #GUI Manager
    def __init__(self):        
        self.startscene_manager = pygame_gui.UIManager((1200, 800), 'theme.json')

        self.login_button = gui_elements.createButton((500,350),'LOGIN','ACCEPT', self.startscene_manager)
        self.register_button = gui_elements.createButton((500,400),'REGISTER','ACCEPT', self.startscene_manager)
        self.exit_button = gui_elements.createButton((500,450),'EXIT','ACCEPT', self.startscene_manager)

        #self.a_label = gui_elements.createTextfeld((0,50),'F','HEADER', self.startscene_manager)
        #self.b_label = gui_elements.createTextfeld((40,50),'U','HEADER', self.startscene_manager)
        #self.c_label = gui_elements.createTextfeld((90,50),'E','HEADER', self.startscene_manager)
        #self.d_label = gui_elements.createTextfeld((130,50),'N','HEADER', self.startscene_manager)
        #self.e_label = gui_elements.createTextfeld((170,50),'F','HEADER', self.startscene_manager)

        #self.f_label = gui_elements.createTextfeld((210,50),'G','HEADER', self.startscene_manager)
        #self.g_label = gui_elements.createTextfeld((250,50),'E','HEADER', self.startscene_manager)
        #self.h_label = gui_elements.createTextfeld((290,50),'G','HEADER', self.startscene_manager)
        #self.j_label = gui_elements.createTextfeld((330,50),'E','HEADER', self.startscene_manager)
        #self.k_label = gui_elements.createTextfeld((370,50),'N','HEADER', self.startscene_manager)

        #self.l_label = gui_elements.createTextfeld((410,50),'W','HEADER', self.startscene_manager)
        #self.m_label = gui_elements.createTextfeld((450,50),'I','HEADER', self.startscene_manager)
        #self.n_label = gui_elements.createTextfeld((490,50),'L','HEADER', self.startscene_manager)
        #self.o_label = gui_elements.createTextfeld((530,50),'L','HEADER', self.startscene_manager)
        #self.p_label = gui_elements.createTextfeld((570,50),'I','HEADER', self.startscene_manager)

    def update(self, time_delta):
        self.startscene_manager.update(time_delta)

    def render(self, screen):
        self.startscene_manager.draw_ui(screen)
    
    def handleEvents(self, events):
        for event in events:
            self.startscene_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.login_button:
                            print('login')
                            self.manager.goTo(Scenes.login_scene.LoginScene())
                        elif event.ui_element == self.register_button:
                            print('register')
                            self.manager.goTo(Scenes.registration_scene.RegistrationScene())
                        elif event.ui_element == self.exit_button:
                            print('exit')
                            pygame.quit()