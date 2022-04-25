from numbers import Number
import pygame

class Board:

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    def __init__(self, surface, width: Number, height: Number, startingPointX:Number, startingPointY:Number) -> None:
        self.field = "field"
        self.surface = surface
        self.width = width
        self.height = height
        self.startingPointX = startingPointX
        self.startingPointY = startingPointY
        self.rows = 6
        self.columns = 6
        self.fieldArray2D = []
        for columns in range(0,self.columns):
            column = []
            for rows in range(0,self.rows):
                column.append(self.field)
            self.fieldArray2D.append(column)
    
    def draw(self):
        for columnIndex,column in enumerate(self.fieldArray2D):
            for rowIndex, field in enumerate(column):  
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
                    
                pygame.draw.rect(self.surface, fieldColor, pygame.Rect(((self.width / self.rows) * rowIndex) + self.startingPointX, ((self.height / self.columns) * columnIndex) + self.startingPointY, self.width / self.rows, self.height / self.columns ) )
