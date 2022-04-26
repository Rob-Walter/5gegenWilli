import pygame

PLAYERMOVED = 1

playerMoved = pygame.event.Event(pygame.USEREVENT, customType=PLAYERMOVED)