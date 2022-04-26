from numbers import Number
from field import Field
from pawn import Pawn
import pygame

class Board:

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))
        self.rows = 6
        self.columns = 6
        self.fieldArray2D = []
        for columnIndex in range(0,self.columns):
            column = []
            for rowIndex in range(0,self.rows):
                if(columnIndex % 2 == 0):
                    if (rowIndex % 2 == 0):
                        fieldColor = self.WHITE
                    else:
                        fieldColor = self.BLACK          
                else:
                    if (rowIndex % 2 == 0):
                        fieldColor = self.BLACK
                    else:
                        fieldColor = self.WHITE
                column.append(Field(((self.width / self.rows) * rowIndex), ((self.height / self.columns) * columnIndex),(self.width / self.rows),(self.height / self.columns),fieldColor))
            self.fieldArray2D.append(column)
        self.initializeNewGame()

    def get2dArray(self):
        return self.fieldArray2D

    def initializeNewGame(self):
        whitePlayerColumn = self.fieldArray2D[0]
        for field in whitePlayerColumn:
            field.addPawn(Pawn("white", field.getPosition()[0],field.getPosition()[1]))
        
        blackPlayerColumn = self.fieldArray2D[self.columns - 1]
        for field in blackPlayerColumn:
            field.addPawn(Pawn("black", field.getPosition()[0],field.getPosition()[1]))

    def moveMouse(self, event, currentTurnPlayer):
        for column in self.fieldArray2D:
            for field in column:
                field.checkMouseHover(event, currentTurnPlayer)

    def mousePressed(self, event):
        for column in self.fieldArray2D:
            for field in column:
                if(field.isHovered()):
                    return

    def draw(self):
        for columnIndex,column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):  
                self.surface.blit(field.draw(), field.getPosition())
        return self.surface
