import pygame
import pygame.freetype
import pygame_gui
import globals
import gui_elements
from board import Board
from player import Player
from database_controller import DB_Controller
import customEvents
from scene import Scene

pygame.freetype.init()

class GameScene(Scene):

    def __init__(self) -> None:
        super().__init__()
    
        self.BOARD_WIDTH, self.BOARD_HEIGHT = 600, 600

        globals.setStartingPoints((globals.screenWidth - self.BOARD_WIDTH) / 2, (globals.screenHeight - self.BOARD_HEIGHT) / 2)

        self.board = Board( self.BOARD_WIDTH, self.BOARD_HEIGHT)

        self.playerWhite = Player("white")
        self.playerBlack = Player("black")

        self.currentTurnPlayer = self.playerWhite

        #GUI Manager
        self.gui_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        self.test = gui_elements.createTextfeld((0,0),'tergrtergrfdtttergrfdtttergrfdtttergrfdttte<br>rgrfdtttergrfdtttergrfdtttergrfdtttergrfdttfdt',globals.textboxTypes['WARN'], self.gui_manager)


    def switchCurrentTurnPlayer(self):
        if(self.currentTurnPlayer == self.playerWhite):
            self.currentTurnPlayer = self.playerBlack
        else:
            self.currentTurnPlayer = self.playerWhite


    def render(self, screen):
        screen.blit(self.board.draw(),(globals.boardStartingPointX, globals.boardStartingPointY))
        self.gui_manager.draw_ui(screen)

    def update(self, timeDelta):
        self.gui_manager.update(timeDelta) 

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                    self.board.moveMouse(event, self.currentTurnPlayer)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.board.mousePressed(event, self.currentTurnPlayer)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.board.mouseReleased(event, self.currentTurnPlayer)
            elif event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        if event.ui_element == self.test:
                            entered_text = self.text
                if hasattr(event, 'customType'):
                    if event.customType == customEvents.PLAYERMOVED:
                        self.switchCurrentTurnPlayer()
                    elif event.customType == customEvents.PLAYERWIN:
                        if event.winner == "white":
                            print("Weiß gewinnt")
                        if event.winner == "black":
                            print("Black gewinnt")
            self.gui_manager.process_events(event)
