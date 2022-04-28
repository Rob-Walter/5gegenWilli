import pygame
import pygame.freetype
import pygame_gui
import globals
import gui_elements
from board import Board
from player import Player
from database_controller import DB_Controller
import customEvents
from Scenes.scene import Scene
import minmax

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
        self.save_game_button = gui_elements.createButton((0,0),'SAVE GAME','ACCEPT', self.gui_manager)


    def switchCurrentTurnPlayer(self):
        if(self.currentTurnPlayer == self.playerWhite):
            self.currentTurnPlayer = self.playerBlack
            print(minmax.minimax(self.board, 4, "black"))
        else:
            self.currentTurnPlayer = self.playerWhite

    
    def render(self, screen):
        screen.blit(self.board.draw(),(globals.boardStartingPointX, globals.boardStartingPointY))
        self.gui_manager.draw_ui(screen)

    def update(self, timeDelta):
        self.gui_manager.update(timeDelta) 

    def savegame(self):
        dbcontroller = DB_Controller()
        dbcontroller.savefilegame(globals.user['id'],self.board)

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
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.save_game_button:
                            print('save game')
                            self.savegame()
                if hasattr(event, 'customType'):
                    if event.customType == customEvents.PLAYERMOVED:
                        self.switchCurrentTurnPlayer()
                    elif event.customType == customEvents.PLAYERWIN:
                        if event.winner == "white":
                            print("Weiß gewinnt")
                        if event.winner == "black":
                            print("Black gewinnt")
            self.gui_manager.process_events(event)

