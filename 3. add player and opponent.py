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

#Add player
player_surface = pygame.image.load("assets/Background/mario1.png").convert_alpha()

#Player Scale
x = 50
y = 50

#Play postion
player_x_pos = 600

#insert snail
snail_surface = pygame.image.load("assets/snail/snail1.png")
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    
    #Set background_surface
    screen.blit(background_surface, (0,0))
    
    #Set player_surface
    #Change player size
    newImage = pygame.transform.scale(player_surface, (x,y))
    screen.blit(newImage, (player_x_pos,300))

    #Set snail
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800

    screen.blit(snail_surface, (snail_x_pos,300))

    pygame.display.update()
    clock.tick(60)