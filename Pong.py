import pygame
#initializing pygame
pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#game options
BALL_SPEED = 5
AI_SPEED = 5
PLAYER_WIDTH = 5
PLAYER_HEIGHT = 50

PLAYER1_START = (10,250)
PLAYER2_START = (690, 250)


# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")


#draw net 
pygame.draw.line(screen, WHITE, (350,500), (350, 0), 5)
pygame.display.flip()

#user is playing game
Playing = True

while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
    



            
pygame.quit()