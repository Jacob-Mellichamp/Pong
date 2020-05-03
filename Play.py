import pygame
import Pong

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")


#draw net 
pygame.draw.line(screen, Pong.WHITE, (350,500), (350, 0), 5)
pygame.display.flip()


#user is playing game
Playing = True

#variable to control fps (how fast screen updates)
fps = pygame.time.Clock()

while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False

    #checking bounds for ball (making it bounce)
    Pong.ball.check_bounds()
    
    #checking for collision between player paddles and ball
    if pygame.sprite.collide_mask(Pong.ball, Pong.player1) or pygame.sprite.collide_mask(Pong.ball, Pong.player2):
        Pong.ball.bounce()
    
    #refresh background after every frame
    screen.fill(Pong.BLACK)
    #draw net 
    pygame.draw.line(screen, Pong.WHITE, (350,500), (350, 0), 5)

    
    #drawing sprites
    Pong.sprites_list.draw(screen)
    #moving player
    Pong.player1.move()

    #ai movement
    goto_y = Pong.player1.AIprediect(Pong.ball)
    Pong.player1.AImove(goto_y)
    Pong.player2.move()
    
    #moving ball
    Pong.ball.move(Pong.BALL_SPEED)
    #updating screen
    pygame.display.flip()
    #limiting fps to 60
    fps.tick(60)


pygame.quit()