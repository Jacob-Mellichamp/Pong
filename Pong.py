import pygame
from Ball import Ball
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

PLAYER1_START = (20, 250)
PLAYER2_START = (670, 250)


#sprite list
sprites_list = pygame.sprite.Group()
sprites_list.add(ball)


#user is playing game
# Playing = True

# fps = pygame.time.Clock()

# while Playing:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             Playing = False


#     #checking bounds for ball (making it bounce)
#     if ball.rect.x >= 690:
#         #flip the velocity (change direction)
#         ball.velocity[0] = -ball.velocity[0]
#     if ball.rect.x <= 0:
#         ball.velocity[0] = -ball.velocity[0]

#     if ball.rect.y >= 490:
#         ball.velocity[1] = -ball.velocity[1]
#     if ball.rect.y <= 0:
#         ball.velocity[1] = -ball.velocity[1]
    
#     #refresh background after every frame
#     screen.fill(BLACK)
#     #draw net 
#     pygame.draw.line(screen, WHITE, (350,500), (350, 0), 5)

    
#     ball.move(BALL_SPEED)
#     ball.draw(screen, ball.rect.x, ball.rect.y)
#     pygame.display.flip()


#     fps.tick(60)
    



            
# pygame.quit()
