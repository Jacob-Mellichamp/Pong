import pygame
pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#user is playing game
Playing = True

while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False

            
pygame.quit()