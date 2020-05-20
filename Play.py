import pygame
import Pong
import random

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")



def check_score():
    if Pong.player1.getScore() >= Pong.MAX_SCORE:
        return True
    elif Pong.player2.getScore() >= Pong.MAX_SCORE:
        return True
    
    return False

def display_score():
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(Pong.player1.getScore()), 1, Pong.WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(Pong.player2.getScore()), 1, Pong.WHITE)
    screen.blit(text, (420,10))
    


#user is playing the game
Playing = True

#variable to control fps (how fast screen updates)
fps = pygame.time.Clock()

while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False

    num = random.randint(0, 1)
    if num == 0 :
        action = 'U'
    else:
        action = 'D' 


    state, reward, ai_win, debug = Pong.testAI.step(action)

    #checking bounds for ball (making it bounce)
    Pong.ball.check_bounds()
    
    #checking for collision between player paddles and ball
    if pygame.sprite.collide_mask(Pong.ball, Pong.player1):
        Pong.ball.bounce(Pong.player1.rect.y)
    elif pygame.sprite.collide_mask(Pong.ball, Pong.player2):
        Pong.ball.bounce(Pong.player2.rect.y)
        
    #refresh background after every frame
    screen.fill(Pong.BLACK)
    #draw net
    pygame.draw.line(screen, Pong.WHITE, (350,500), (350, 0), 5)

    display_score()

    #drawing sprites
    Pong.sprites_list.draw(screen)

    #ai movement
    Pong.player1.AImove()

    #player movement
    #Pong.player2.move()
    #Pong.player1.move()

    #moving ball
    Pong.ball.move(Pong.BALL_SPEED)
    #updating screen
    pygame.display.flip()
    #limiting fps to 60
    fps.tick(60)

    if check_score():
        Playing = False



pygame.quit()