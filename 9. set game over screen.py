import pygame
from sys import exit

#Add Score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}',False,'white')
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)

pygame.init()

#display surface - window the player is going to see in the end						
screen = pygame.display.set_mode((800, 400))

#Set title
pygame.display.set_caption('Group D: Final Project')

# Font setup
test_font = pygame.font.Font(None, 50)  # None uses default font

#Set FPS
clock = pygame.time.Clock()

#game active
game_active = False
start_time = 0

#Add background
background_surface = pygame.image.load("assets/Background/bg.jpg")


#Add snail
snail_surface = pygame.image.load("assets/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(topright = (600,305))

#Add player + Player Scale
player_surface = pygame.image.load("assets/mario/mario1.png").convert_alpha()
player_rect = player_surface.get_rect(topright = (80,327))
player_gravity = 0
x = 55
y = 55

#Game over logo
logo = pygame.image.load('assets/Background/logo.png').convert_alpha()
logo_rect = logo.get_rect(center = (590,250))
game_name = test_font.render('Thank you play with Group D', False, 'white')
game_name_rect = game_name.get_rect(center = (400,300))
game_message = test_font.render("Press space to play", False, 'white')
game_message_rect = game_message.get_rect(center = (400, 30))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            #Add keyboard input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 348:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 348:
                    game_active = True
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        #Set background_surface
        screen.blit(background_surface, (0,0))
        
        #Score
        #set text
        # pygame.draw.rect(screen, 'Pink', score_rect)
        display_score()

        #Set player_surface
        #Change player size
        # newImage = pygame.transform.scale(player_surface, (x,y))
        original_midbottom = player_rect.midbottom 
        player_surface_scaled = pygame.transform.scale(player_surface, (x, y))
        player_rect = player_surface_scaled.get_rect(midbottom=original_midbottom)  # Update rect
        
        #Add Player gravity
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 348:
            player_rect.bottom = 348

        screen.blit(player_surface_scaled, player_rect)

        #Set snail
        snail_rect.x -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        #Game over screen
        screen.fill((50,174,226))
        logo_scaled = pygame.transform.scale(logo, (200, 100))
        screen.blit(logo_scaled, logo_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_message, game_message_rect)

    pygame.display.update()
    clock.tick(60)