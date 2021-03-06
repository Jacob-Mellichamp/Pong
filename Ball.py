"""
The Ball class will contain all information related to ball movement
and ball location.

The Ball class will contain the attributes:
- x (int)
- y (int)
- color (Vector3)

The ball class will contain the methods:
- move (self, speed)
- check_bounds (self)
- calcSlope (self)
- bounce (self, player_y)
- respawn(self)


"""
import pygame
import random
import Pong

#list of possible starting directions (-1=left, 1=right)
starting_direction = [-1, 1]

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        #create ball sprite
        self.image = pygame.Surface([x,y])
        self.image.fill(Pong.BLACK)
        self.image.set_colorkey(Pong.BLACK)

        #getting rectangle object
        self.rect = self.image.get_rect()
        
        #generating velocity
        self.velocity = [random.choice(starting_direction), random.randint(-5,5)] 
        
        pygame.draw.rect(self.image, self.color , [0, 0, self.x, self.y])

    #return slope of current state of ball
    def calcSlope(self):
        return self.velocity[1] / self.velocity[0]
        
    def move(self, speed):
        self.rect.x += self.velocity[0] * speed
        self.rect.y += self.velocity[1]

    #function to make the ball bounce when hitting edges of screen
    def check_bounds(self):
        if self.rect.x >= 690:
            Pong.player1.addPoint()
            self.respawn()
        if self.rect.x <= 0:
            Pong.player2.addPoint()
            self.respawn()
        #flip the velocity (change direction)
        if self.rect.y >= 490:
            self.velocity[1] = -self.velocity[1]
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

    #function to determine how the ball bounces off the paddles
    def bounce(self, player_y):
        #getting the 3 different segmented ranges of the paddle
        top_range  = player_y + Pong.top_of_paddle
        middle_range = player_y + Pong.middle_of_paddle
        lower_range = player_y + Pong.bottom_of_paddle

        #getting the ball's middle point
        ball_y = self.rect.y + Pong.BALL_MIDDLE_POINT

        #changing directions
        self.velocity[0] = -self.velocity[0]

        if ball_y >= player_y and ball_y <= top_range:
            self.velocity[1] = random.randint(-5, -1)
        elif ball_y >= top_range and ball_y <= middle_range:
            self.velocity[1] = 0
        elif ball_y >= middle_range and ball_y <= lower_range:
            self.velocity[1] = random.randint(1, 5)

    def respawn(self):
        #respawning ball after score
        self.rect.x = 345
        self.rect.y = 195
        self.velocity = [random.choice(starting_direction), random.randint(-5,5)]
    
