import pygame
from sys import exit

pygame.init()

#display surface - window the player is going to see in the end						
screen = pygame.display.set_mode((800, 400))

#Set title
pygame.display.set_caption('Group D: Final Project')

#Set FPS
clock = pygame.time.Clock()

#Add background
background_surface = pygame.image.load("assets/Background/mountains-background-game-vector.jpg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    
    #set sky_surface
    screen.blit(background_surface, (0,0))

    pygame.display.update()
    clock.tick(60)