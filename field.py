import pygame
from pygame import Surface
from pawn import Pawn

class Field:
    def __init__(self, x : int,y : int , width : int , height : int, color):
        self.pawn = None
        self.surface = Surface((width,height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def addPawn(self,pawn : Pawn):
        self.pawn = pawn

    def removePawn(self):
        self.pawn = None

    def getPosition(self):
        return (self.x,self.y)

    def draw(self):
        pygame.draw.rect(self.surface,self.color,pygame.Rect(0,0,self.width,self.height))
        if(self.pawn != None):
            self.surface.blit(self.pawn.draw(),(self.width / 2 - self.pawn.getSize()[0] / 2, self.height / 2 - self.pawn.getSize()[1] / 2))
        return self.surface
