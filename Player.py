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
    
    def __init__(self, x,y):
        # x = 30
        # y = 250
        self.x = x
        self.y = y
        self.top = y
        self.bottom = Pong.PLAYER_HEIGHT
        self.side1 = x
        self.side2 = Pong.PLAYER_WIDTH
        self.image = pygame.Surface([x,y])
        self.rect = self.image.get_rect()

    def draw(self, screen):
        pygame.draw.rect(screen, Pong.WHITE , [self.side1, self.top, self.side2, self.bottom] )
        
    def move (self):
        pass
