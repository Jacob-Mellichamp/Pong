"""
This file holds constants for the game.
These options can be changed to customize the experience

"""
import pygame
from Ball import Ball
from Player import Player


#initializing pygame
pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#game options
BALL_SPEED = 5
AI_SPEED = 5

#player options
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 70

#ball options
BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_MIDDLE_POINT = BALL_HEIGHT // 2

#paddle sections 
top_of_paddle = PLAYER_HEIGHT // 3
bottom_of_paddle = PLAYER_HEIGHT
middle_of_paddle = bottom_of_paddle - top_of_paddle  

#create ball
ball = Ball(WHITE, BALL_WIDTH, BALL_HEIGHT)
ball.rect.x = 345
ball.rect.y = 195

#create player 1
player1 = Player(PLAYER_WIDTH, PLAYER_HEIGHT)
player1.rect.x = 20
player1.rect.y = 250
#create player 2
player2 = Player(PLAYER_WIDTH, PLAYER_HEIGHT)
player2.rect.x = 670
player2.rect.y = 250

#sprite list
sprites_list = pygame.sprite.Group()
sprites_list.add(ball)
sprites_list.add(player1)
sprites_list.add(player2)

