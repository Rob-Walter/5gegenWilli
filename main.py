import pygame
import globals
from board import Board
from player import Player
from database_controller import DB_Controller
import customEvents

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

def switchCurrentTurnPlayer():
    global currentTurnPlayer
    if(currentTurnPlayer == playerWhite):
        currentTurnPlayer = playerBlack
    else:
        currentTurnPlayer = playerWhite

def draw_window():
    WIN.fill(ORANGE)
    WIN.blit(board.draw(),(globals.boardStartingPointX, globals.boardStartingPointY))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
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
                if event.customType == customEvents.PLAYERMOVED:
                    switchCurrentTurnPlayer()
                elif event.customType == customEvents.PLAYERWIN:
                    if event.winner == "white":
                        print("Weiß gewinnt")
                    if event.winner == "black":
                        print("Black gewinnt")
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main() 