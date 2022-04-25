import pygame
from board import Board

WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bauernschach")

BOARD_WIDTH, BOARD_HEIGHT = 600, 600

BOARD_STARTINGPOINTX = ((WIDTH - BOARD_WIDTH) / 2)
BOARD_STARTINGPOINTY = (HEIGHT - BOARD_HEIGHT) / 2


board = Board(WIN, BOARD_WIDTH, BOARD_HEIGHT, BOARD_STARTINGPOINTX, BOARD_STARTINGPOINTY)

FPS = 60

ORANGE = (235, 180, 52)

def draw_window():
    WIN.fill(ORANGE)
    board.draw()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main() 