import pygame
import globals
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
        self.isHovered = False

    def addPawn(self,pawn : Pawn):
        self.pawn = pawn

    def removePawn(self):
        self.pawn = None

    def getPawn(self):
        return self.pawn

    def getPosition(self):
        return (self.x,self.y)

    def isCurrentlyHovered(self):
        return self.isHovered

    def checkMouseHover(self, event, currentTurnPlayer):
        if(self.pawn != None):
            if(self.surface.get_rect(topleft=((globals.boardStartingPointX + self.x),(globals.boardStartingPointY + self.y))).collidepoint(event.pos) and self.pawn.getTeam() == currentTurnPlayer.getTeam()):
                self.isHovered = True
            else:
                self.isHovered = False

    def draw(self):
        pygame.draw.rect(self.surface,self.color,pygame.Rect(0,0,self.width,self.height))
        if (self.isHovered == True):
            pygame.draw.rect(self.surface,globals.fieldHighLightColor,pygame.Rect(0,0,self.width,self.height), 3)
        if(self.pawn != None):
            self.surface.blit(self.pawn.draw(),(self.width / 2 - self.pawn.getSize()[0] / 2, self.height / 2 - self.pawn.getSize()[1] / 2))
        return self.surface
