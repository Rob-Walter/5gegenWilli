import pygame
import pygame.freetype
import pygame_gui
import globals
import gui_elements
from board import Board
from player import Player
from database_controller import DB_Controller
import customEvents

pygame.freetype.init()


WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bauernschach")

BOARD_WIDTH, BOARD_HEIGHT = 600, 600

globals.setStartingPoints((WIDTH - BOARD_WIDTH) / 2, (HEIGHT - BOARD_HEIGHT) / 2)

board = Board( BOARD_WIDTH, BOARD_HEIGHT)

playerWhite = Player("white")
playerBlack = Player("black")

currentTurnPlayer = playerBlack

FPS = 60

ORANGE = (235, 180, 52)

#GUI Manager
#jeweils ein Manager für eine "Seite"
gui_manager = pygame_gui.UIManager((1200, 800), 'theme.json')
test = gui_elements.createTextfeld((0,0),'tergrtergrfdtttergrfdtttergrfdtttergrfdttte<br>rgrfdtttergrfdtttergrfdtttergrfdtttergrfdttfdt',globals.textboxTypes['WARN'], gui_manager)
#print(globals.textboxTypes['WARN'])

def switchCurrentTurnPlayer():
    global currentTurnPlayer
    if(currentTurnPlayer == playerWhite):
        currentTurnPlayer = playerBlack
    else:
        currentTurnPlayer = playerWhite

def draw_window():
    WIN.fill(ORANGE)
    WIN.blit(board.draw(),(globals.boardStartingPointX, globals.boardStartingPointY))
    gui_manager.draw_ui(WIN)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        time_delta = clock.tick(FPS)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEMOTION:
                board.moveMouse(event, currentTurnPlayer)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.mousePressed(event, currentTurnPlayer)
            elif event.type == pygame.MOUSEBUTTONUP:
                board.mouseReleased(event, currentTurnPlayer)
            elif event.type == pygame.USEREVENT:
                if hasattr(event, 'user_type'):
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED: 
                        if event.ui_element == test:
                            entered_text = text
                if hasattr(event, 'customType'):
                    if event.customType == customEvents.PLAYERMOVED:
                        switchCurrentTurnPlayer()
                    elif event.customType == customEvents.PLAYERWIN:
                        if event.winner == "white":
                            print("Weiß gewinnt")
                        if event.winner == "black":
                            print("Black gewinnt")

        
            gui_manager.process_events(event)
        gui_manager.update(time_delta)        
        draw_window()
        

    pygame.quit()

if __name__ == "__main__":
    main() 