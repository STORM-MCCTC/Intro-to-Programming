import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

       
        #game code
        pygame.draw.circle
        
        pygame.display.update()
        clock.tick(60)