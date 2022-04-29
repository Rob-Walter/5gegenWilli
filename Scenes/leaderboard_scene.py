from shelve import DbfilenameShelf
import Scenes.mainmenue_scene
import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
from database_controller import DB_Controller




class LeaderboardScene(Scene):
    #GUI Manager
    def __init__(self):
        self.leader_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        self.back_button = gui_elements.createButton((0,350),'BACK',globals.buttonTypes['ACCEPT'], self.leader_manager)
        #self.rules_label = gui_elements.createTextfeld((200,150),"text",globals.textboxTypes['RULES'], self.leader_manager)

        self.easy_button = gui_elements.createButton((300,50),'EASY',globals.buttonTypes['STRENGTH'], self.leader_manager)
        self.medium_button = gui_elements.createButton((450,50),'MEDIUM',globals.buttonTypes['STRENGTH'], self.leader_manager)
        self.hard_button = gui_elements.createButton((600,50),'HARD',globals.buttonTypes['STRENGTH'], self.leader_manager)

    def update(self, time_delta):
        self.leader_manager.update(time_delta)

    def render(self, screen):
        self.leader_manager.draw_ui(screen)

    def leaderboard(self, ki_strength):
        dbcontroller = DB_Controller()
        ausgabe = dbcontroller.getleaderboard(ki_strength)
        print(ausgabe)

    def handleEvents(self, events):
        

        for event in events:
            self.leader_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == self.back_button:
                                print('back')
                                self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                            elif event.ui_element == self.easy_button:
                                print('leaderboard for easy')
                                self.leaderboard('easy')
                            elif event.ui_element == self.medium_button:
                                print('leaderboard for medium')
                                self.leaderboard('medium')
                            elif event.ui_element == self.hard_button:
                                print('leaderboard for hard')
                                self.leaderboard('hard')
                    #if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        #if event.ui_element == self.username_input:
                            #username = self.username_input.get_text()
                            #print('text:', username)