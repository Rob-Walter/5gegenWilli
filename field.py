import pawn
class Field:
        def __init__(self,value : pawn,x : int,y : int ,color):
            self.value = value
            self.x = x
            self.y = y
            self.color = color
        def addPawn(self,pawn : pawn):
            self.value = pawn
        def removePawn(self):
            self.value = None
