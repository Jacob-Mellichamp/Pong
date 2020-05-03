import pygame
import Ball
import Pong
import Player






# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")


#draw net 
pygame.draw.line(screen, Pong.WHITE, (350,500), (350, 0), 5)
pygame.display.flip()


#user is playing game
Playing = True

player1 = Player.Player(Pong.PLAYER1_START[0], Pong.PLAYER1_START[1])
player2 = Player.Player(Pong.PLAYER2_START[0], Pong.PLAYER2_START[1])
while Playing:
    # draw rect
    player1.draw(screen)
    player2.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
    pygame.display.update()


pygame.quit()