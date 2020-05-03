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
    #draw  the current position of 
    def draw(self, screen):
        pass
        #pygame.draw.rect(screen, Pong.WHITE , [self.side1, self.top, self.side2, self.bottom])
        
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
    
    #AI needs to move to where ball will be
    def AImove(self, ball):
        pass