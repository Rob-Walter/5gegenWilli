import pygame
import os

class Pawn:

    WIDTH, HEIGHT = 50 ,50

    def __init__(self,team,x : int,y : int):
        self.team = team
        self.width = self.WIDTH
        self.height = self.HEIGHT
        self.x = x
        self.y = y

        if(team == "white"):
            self.sprite = pygame.image.load(os.path.join("assets", "pawn_white.png"))
        elif(team == "black"):
            self.sprite = pygame.image.load(os.path.join("assets", "pawn_black.png"))

        self.sprite = pygame.transform.scale(self.sprite, self.getSize())

    def getSize(self):
        return (self.width, self.height)

    def getTeam(self):
        return self.team
        
    def draw(self):
        return self.sprite