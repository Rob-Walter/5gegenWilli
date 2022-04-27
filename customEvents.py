import pygame

PLAYERMOVED = 1
PLAYERWIN = 2

playerMoved = pygame.event.Event(pygame.USEREVENT, {"customType":PLAYERMOVED})

def createWinEvent(winner):
    return pygame.event.Event(pygame.USEREVENT, {"customType":PLAYERWIN, "winner":winner})