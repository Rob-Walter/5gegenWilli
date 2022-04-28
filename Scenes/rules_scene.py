from Scenes.mainmenue_scene import MainMenueScene
import globals
import pygame
import pygame_gui
import gui_elements
from Scenes.scene import Scene
from database_controller import DB_Controller




class RulesScene(Scene):
    #GUI Manager
    #Rules Manager
    def __init__(self):
        self.rules_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        
        self.rules_label = gui_elements.createTextfeld((300,200),"Bauernschach ist eine Variante des <br>Schachs nur mit Bauern und auf einem <br> 6x6 Feld. Schwarze sowie weiße <br>Figuren stehen dabei an der <br>gegenüberliegenden Grundlinie. Die Farbe weiß <br>beginnt den Zug, danach folgen die <br>schwarzen Figuren. Zwei Züge sind erlaubt: <br>Ein Bauer darf nach vorne <br>ziehen wenn das vordere Feld frei ist. <br>Es muss dabei in die Richtung <br>der gegnerischen Grundlinie bewegen. Schlagen darf <br>der Bauer in Richtung der <br>gegnerischen Grundlinie durch diagonales Ziehen<br>in Richtung der gegnerischen Grundlinie, <br>aber auch nur wenn auf diesem <br>Feld ein gegnerischer Bauer steht. <br>Der “geschlagene” Bauer wird vom <br>Spielbrett genommen. Gewonnen hat man das <br>Spiel wenn man einen eigenen <br>Bauern auf die gegnerische Grundlinie platziert. <br>Die Farbe die dies erreicht, ist der Sieger. <br>Wenn ein Spieler weder Züge oder Figuren <br>hat zählt das Spiel für ihn verloren. <br>In dieser Variante des <br>Bauernschachs gibt es kein Unentschieden",globals.textboxTypes['RULES'], self.rules_manager)

    def update(self, time_delta):
        self.rules_manager.update(time_delta)

    def render(self, screen):
        self.rules_manager.draw_ui(screen)

    def handleEvents(self, events):
        for event in events:
            self.rules_manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.login_button:
                            self.username = self.username_input.get_text()
                            self.password = self.password_input.get_text()
                            if self.login():
                                self.manager.goTo(MainMenueScene())
                            else:
                                print('fehler ist aufgetreten')
                    #if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        #if event.ui_element == self.username_input:
                            #username = self.username_input.get_text()
                            #print('text:', username)