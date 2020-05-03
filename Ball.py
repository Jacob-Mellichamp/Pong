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
from random import randint
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, x, y):
        #calling the sprite constructor
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

    def move(self, speed):
        self.rect.x += self.velocity[0] * speed
        self.rect.y += self.velocity[1] * speed
    
    def draw(self, screen, spawnX, spawnY):
         pygame.draw.rect(screen, self.color, [spawnX, spawnY, self.x, self.y])

    def check_if_hit(self):
        pass
