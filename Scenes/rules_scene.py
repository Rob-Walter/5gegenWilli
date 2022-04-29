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

        self.back_button = gui_elements.createButton((0,350),'BACK','ACCEPT', self.rules_manager)
        self.rules_label = gui_elements.createTextfeld((200,150),"Bauernschach ist eine Variante des Schachs nur mit Bauern und auf einem <br>6x6 Feld. Schwarze sowie weiße Figuren stehen dabei an der <br>gegenüberliegenden Grundlinie. Die Farbe weiß beginnt den Zug, danach folgen die <br>schwarzen Figuren. Zwei Züge sind erlaubt: Ein Bauer darf nach vorne <br>ziehen wenn das vordere Feld frei ist. Es muss dabei in die Richtung <br>der gegnerischen Grundlinie bewegen. Schlagen darf der Bauer in Richtung der <br>gegnerischen Grundlinie durch diagonales Ziehen in Richtung der gegnerischen Grundlinie, <br>aber auch nur wenn auf diesem Feld ein gegnerischer Bauer steht. <br>Der “geschlagene” Bauer wird vom Spielbrett genommen. Gewonnen hat man das <br>Spiel wenn man einen eigenen Bauern auf die gegnerische Grundlinie platziert. <br>Die Farbe die dies erreicht, ist der Sieger. Wenn ein Spieler weder Züge oder Figuren <br>hat zählt das Spiel für ihn verloren. In dieser Variante des <br>Bauernschachs gibt es kein Unentschieden.",globals.textboxTypes['RULES'], self.rules_manager)
        #kriege es nicht hin die scroll weg zu machen
    def update(self, time_delta):
        self.rules_manager.update(time_delta)

    def render(self, screen):
        self.rules_manager.draw_ui(screen)

    def handleEvents(self, events):
        for event in events:
            self.rules_manager.process_events(event)
            #if event.type == pygame.USEREVENT:
                #if hasattr(event, 'user_type'):
                    #if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    #if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        #if event.ui_element == self.username_input:
                            #username = self.username_input.get_text()
                            #print('text:', username)