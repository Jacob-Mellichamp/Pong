"""
The player class will contain functionality for the "players" or 
oposing rectangles in the game.

The Player class will contain the attributes:
- x (int)
- y (int)

The Player class will contain the methods:
- draw (self)
- move (self)


"""
import Pong


class Player:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def draw(self):
        pass
    def move (self):
