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
background_surface = pygame.image.load("assets/Background/bg.jpg")

#Add snail
snail_surface = pygame.image.load("assets/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(topright = (600,305))

#Add player
player_surface = pygame.image.load("assets/Background/mario1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,301))

#Player Scale
x = 60
y = 60

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
    screen.blit(newImage, player_rect)

    #Set snail
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    pygame.display.update()
    clock.tick(60)