import pygame
from Ball import Ball
from Player import Player


#initializing pygame
pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#game options
BALL_SPEED = 1
AI_SPEED = 5

#player options
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 70

#create ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#player options
PLAYER1_START = (20, 250)
PLAYER2_START = (670, 250)
player1 = Player(PLAYER1_START[0], PLAYER1_START[1])
player2 = Player(PLAYER2_START[0], PLAYER2_START[1])

#sprite list
# sprites_list = pygame.sprite.Group()
# sprites_list.add(ball)
