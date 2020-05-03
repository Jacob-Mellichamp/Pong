import Pong
import Ball
import Player



def main():
    #user is playing game
    Playing = True

    while Playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Playing = False
    



            
    pygame.quit()