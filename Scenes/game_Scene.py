import pygame
import pygame.freetype
import pygame_gui
import Scenes.mainmenue_scene
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

    def __init__(self, isLoaded, loadData = None) -> None:
        super().__init__()
        if not isLoaded:
            globals.unsetGameNumber()
        self.BOARD_WIDTH, self.BOARD_HEIGHT = 600, 600

        globals.setStartingPoints((globals.screenWidth - self.BOARD_WIDTH) / 2, (globals.screenHeight - self.BOARD_HEIGHT) / 2)

        self.board = Board( self.BOARD_WIDTH, self.BOARD_HEIGHT, isLoaded, loadData)

        self.playerWhite = Player("white")
        self.playerBlack = Player("black")
        self.playerWhiteMovable = True
        self.playerBlackMovable = True

        # if isLoaded:
        #     if loadData[0][5] == "white":
        #         self.currentTurnPlayer = self.playerWhite
        #     else:
        #         self.currentTurnPlayer = self.playerBlack
        # else:
        #     self.currentTurnPlayer = self.playerWhite
        self.currentTurnPlayer = self.playerWhite

        #GUI Manager
        self.game_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
        self.save_game_button = gui_elements.createButton((0,300),'SAVE','ACCEPT', self.game_manager)
        self.back_game_button = gui_elements.createButton((0,350),'BACK','ACCEPT', self.game_manager)
        self.rules_game_button = gui_elements.createButton((0,400),'RULES','ACCEPT', self.game_manager)
        self.exit_game_button = gui_elements.createButton((0,450),'EXIT','ACCEPT', self.game_manager)


    def switchCurrentTurnPlayer(self):
        if self.currentTurnPlayer == self.playerBlack and self.playerWhiteMovable or not self.playerBlackMovable:
            self.currentTurnPlayer = self.playerWhite

        elif self.currentTurnPlayer == self.playerWhite and self.playerBlackMovable or not self.playerWhiteMovable:
            self.currentTurnPlayer = self.playerBlack
            result = minmax.minimax(self.board,None,None, 3, True)
            print("RESULT: ", result)
            self.board.move(result[2],result[3])
            self.board.checkForWinOrDraw()
            self.switchCurrentTurnPlayer()    

    
    def render(self, screen):
        screen.blit(self.board.draw(),(globals.boardStartingPointX, globals.boardStartingPointY))
        self.game_manager.draw_ui(screen)

    def update(self, timeDelta):
        self.game_manager.update(timeDelta) 

    def savegame(self):
        dbcontroller = DB_Controller()
        dbcontroller.savefilegame(globals.user['id'],self.board, self.currentTurnPlayer.getTeam())

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
                        elif event.ui_element == self.back_game_button:
                            print('back')
                            self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                        elif event.ui_element == self.rules_game_button:
                            print('rules')
                        elif event.ui_element == self.exit_game_button:
                            print('exit')
                            pygame.quit()
                if hasattr(event, 'customType'):
                    if event.customType == customEvents.PLAYERMOVED:
                        self.switchCurrentTurnPlayer()
                    elif event.customType == customEvents.PLAYERWIN:
                        if event.winner == "white":
                            print("Weiß gewinnt")
                            self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                        if event.winner == "black":
                            print("Black gewinnt")
                            self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                    elif event.customType == customEvents.DRAW:
                        print("Unentschieden")
                        self.manager.goTo(Scenes.mainmenue_scene.MainMenueScene())
                    elif event.customType == customEvents.IMMOBILIZED:
                        if event.immobilzedPlayer == "white":
                            self.playerWhiteMovable = False
                        if event.immobilzedPlayer == "black":
                            self.playerBlackMovable = False
            self.game_manager.process_events(event)

