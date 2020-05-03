"""
The Ball class will contain all information related to ball movement
and ball location.

The Ball class will contain the attributes:
- x (int)
- y (int)
- velocity (int)

The Player class will contain the methods:
- draw (self)
- move (self)
- check (self)

"""
import pygame
import Pong
from random import randint
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        #create ball sprite
        self.image = pygame.Surface([x,y])
        #getting rectangle object
        self.rect = self.image.get_rect()
        #generating velocity
        self.velocity = [randint(-8,8), randint(-8,8)]
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, Pong.WHITE , [0, 0, self.x, self.y])

    def move(self, speed):
        self.rect.x += self.velocity[0] * speed
        self.rect.y += self.velocity[1] * speed
    
    def draw(self, screen, spawnX, spawnY):
        pass
        #pygame.draw.rect(screen, self.color, [spawnX, spawnY, self.x, self.y])

    def check_bounds(self):
        if self.rect.x >= 690:
            #flip the velocity (change direction)
            self.velocity[0] = -self.velocity[0]
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]

        if self.rect.y >= 490:
            self.velocity[1] = -self.velocity[1]
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        #self.velocity[1] = randint(-8,8)
    