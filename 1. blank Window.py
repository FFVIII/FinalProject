import pygame
from sys import exit

pygame.init()

#display surface - window the player is going to see in the end						
screen = pygame.display.set_mode((800, 400))

#Set title
pygame.display.set_caption('Final Project')

#Set FPS
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

    pygame.display.update()
    clock.tick(60)