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
import pygame





class Player:
    
    #define constants
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.top = y
        self.bottom = Pong.PLAYER_HEIGHT
        self.side1 = x
        self.side2 = Pong.PLAYER_WIDTH


    #get mouse cordinates
    def getCords(self):
        self.top = pygame.mouse.get_pos()[1] - (Pong.PLAYER_HEIGHT / 2)
    #draw  the current position of 
    def draw(self, screen):
        pygame.draw.rect(screen, Pong.WHITE , [self.side1, self.top, self.side2, self.bottom] )
        
    def move (self):
        self.getCords()
    
    #AI needs to move to where ball will be
    def AImove(self, ball):
        pass