"""
The player class will contain functionality for the "players" or 
oposing rectangles in the game.

The Player class will contain the attributes:
- x (int)
- y (int)

The Player class will contain the methods:
- move (self)
- getCords(self)
- AImove(self)
- addPoint(self)
- getScore(self)


"""
import pygame
import Pong

#variables for the min and max movement ranges of paddles on screen (by pixels)
PADDLE_LOW = 0
PADDLE_HIGH = 430

class Player(pygame.sprite.Sprite):
    
    #define constants
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.score = 0

        #creating sprite
        self.image = pygame.Surface([x,y])
        self.image.fill(Pong.BLACK)
        self.image.set_colorkey(Pong.BLACK)

        #drawing sprite
        pygame.draw.rect(self.image, Pong.WHITE , [0, 0, self.x, self.y])
        
        #getting rect object
        self.rect = self.image.get_rect()

    #get mouse cordinates
    def getCords(self):

        #bounds check the mouse pointer
        cord = pygame.mouse.get_pos()[1] - (Pong.PLAYER_HEIGHT / 2)

        if(cord < PADDLE_LOW):
            cord = PADDLE_LOW
        
        if(cord > PADDLE_HIGH):
            cord = PADDLE_HIGH

        self.rect.y = cord
   
    def move (self):
        self.getCords()
 
    #AI will move towards the predicted location
    def AImove(self):
            
        if(self.rect.y < Pong.ball.rect.y):
            self.rect.y = self.rect.y + Pong.AI_SPEED
        
        if(self.rect.y > Pong.ball.rect.y):
            self.rect.y = self.rect.y - Pong.AI_SPEED

    def addPoint(self):
        self.score += 1
    
    def getScore(self):
        return self.score
    
    """
    Fun algorithm to predict exactly where ball will be
            slope = ball.calcSlope()
        predictedY = slope * (self.rect.x - ball.rect.x) + ball.rect.y
        
        updated_slope = slope
        updated_y = ball.rect.y
        updated_x = ball.rect.x

        #TODO: fix bug causing infinite loop
        #continue to calc until in bounds 
        while(predictedY > 700 or predictedY < 0):
            #if ball hits the top   
            if (predictedY > 700):
                updated_x = (700 - updated_y) + (updated_slope * updated_x) / updated_slope
                updated_slope = -updated_slope
                updated_y = 700
                predictedY = updated_slope * (self.rect.x - updated_x) + updated_y
            
            #if ball hits the bottom
            if(predictedY < 0):
                updated_x = (0 - updated_y) + (updated_slope * updated_x) / updated_slope
                updated_slope = -updated_slope
                updated_y = 0
                predictedY = updated_slope * (self.rect.x - updated_x) + updated_y
            
        return predictedY

        """