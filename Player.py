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

class Player(pygame.sprite.Sprite):
    
    #define constants
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y
        
        self.image = pygame.Surface([x,y])
        self.image.fill(Pong.BLACK)
        self.image.set_colorkey(Pong.BLACK)

        pygame.draw.rect(self.image, Pong.WHITE , [0, 0, self.x, self.y])
        
        
        self.rect = self.image.get_rect()

       


    #get mouse cordinates
    def getCords(self):
        self.rect.y = pygame.mouse.get_pos()[1] - (Pong.PLAYER_HEIGHT / 2)

    def move (self):
        self.getCords()
    
    #AI needs to move to where ball will be
    def AImove(self, ball):
        pass