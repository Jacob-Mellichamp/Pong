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
        self.top = y
        self.bottom = Pong.PLAYER_HEIGHT
        self.side1 = x
        self.side2 = Pong.PLAYER_WIDTH

        self.image = pygame.Surface([x,y])
        self.image.fill(Pong.BLACK)
        self.image.set_colorkey(Pong.BLACK)

        pygame.draw.rect(self.image, Pong.WHITE , [0, 0, self.side2, self.bottom])
        
        
        self.rect = self.image.get_rect()

       


    #get mouse cordinates
    def getCords(self):
        self.rect.y = pygame.mouse.get_pos()[1] - (Pong.PLAYER_HEIGHT / 2)
        
    def move (self):
        self.getCords()

    # def check_if_hit(self, ball):
    #     ball_mask = ball.get_mask()
    #     player_mask = pygame.mask.from_surface(self.image)

    #     offset = (self.x - ball.x, self.top - ball.y)

    #     point = ball_mask.overlap(player_mask, offset)

    #     if point:
    #         return True
        
    #     return False
    
    #AI will calculate where ball will be
    def AIprediect(self, ball):
        slope = ball.calcSlope()
        predictedY = slope * (self.side1 - ball.rect.x) + ball.rect.y
        
        updated_slope = slope
        updated_y = ball.rect.y
        updated_x = ball.rect.x
        #continue to calc until in bounds
        while(predictedY > 700 or predictedY < 0):

            #if ball hits the top
            if (predictedY > 700):
                updated_x = (700 - updated_y) + (updated_slope * updated_x) / updated_slope
                updated_slope = -updated_slope
                updated_y = 700
                predictedY = updated_slope * (self.side1 - updated_x) + updated_y
            
            #if ball hits the bottom
            if(predictedY < 0):
                updated_x = (0 - updated_y) + (updated_slope * updated_x) / updated_slope
                updated_slope = -updated_slope
                updated_y = 0
                predictedY = updated_slope * (self.side1 - updated_x) + updated_y
            
        

        return predictedY

    #AI will move towards the predicted location
    def AImove(self, coordy):
        
        if(self.top < coordy):
            self.top = self.top + Pong.AI_SPEED
        

        if(self.top > coordy):
            self.top = self.top - Pong.AI_SPEED
        
    