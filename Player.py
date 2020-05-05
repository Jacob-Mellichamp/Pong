"""
The player class will contain functionality for the "players" or 
oposing rectangles in the game.

The Player class will contain the attributes:
- x (int)
- y (int)

The Player class will contain the methods:
- move (self)


"""
import pygame
import Pong

class Player(pygame.sprite.Sprite):
    
    #define constants
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y

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
        self.rect.y = pygame.mouse.get_pos()[1] - (Pong.PLAYER_HEIGHT / 2)

        
    def move (self):
        self.getCords()
 
    #AI will calculate where ball will be
    def AIprediect(self, ball):
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

    #AI will move towards the predicted location
    def AImove(self, coordy):
        
        if(self.rect.y + Pong.AI_SPEED < 700):
            if(self.rect.y - Pong.PLAYER_HEIGHT + Pong.AI_SPEED > 0):
            
                if(self.rect.y < coordy):
                    self.rect.y = self.rect.y + Pong.AI_SPEED
                

                if(self.rect.y > coordy):
                    self.rect.y = self.rect.y - Pong.AI_SPEED
    