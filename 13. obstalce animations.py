import pygame
from random import randint
from sys import exit


#Add Score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}',False,'white')
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    return current_time

#Obstacles movement 
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 341:
                    screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []
    
# Collisions
def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

# Player animation
def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

pygame.init()

#display surface - window the player is going to see in the end						
screen = pygame.display.set_mode((800, 400))

#Set title
pygame.display.set_caption('Group D: Final Project')

#Font setup
test_font = pygame.font.Font('assets/fonts/Pixeltype.ttf', 50)  # None uses default font

#Set FPS
clock = pygame.time.Clock()

#game active
game_active = False
start_time = 0
score = 0

#Add background
background_surface = pygame.image.load("assets/Background/bg.jpg")

#Add snail
snail_frame_1 = pygame.image.load("assets/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("assets/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

#Add fly
fly_frame1 = pygame.image.load('assets/fly/aa1.png').convert_alpha()
fly_frame2 = pygame.image.load('assets/fly/aa2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

#Obstacles
obstacle_rect_list = []

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)



#Add player + Player Scale + Player movement
player_walk1 = pygame.image.load("assets/mario/mario1.png").convert_alpha()
player_walk2 = pygame.image.load("assets/mario/mario2.png").convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_jump = pygame.image.load("assets/mario/mario3.png").convert_alpha()
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(topright = (80,328))
player_gravity = 0
x = 55
y = 55

#Game over logo
logo = pygame.image.load('assets/Background/logo.png').convert_alpha()
logo_rect = logo.get_rect(center = (590,250))
game_name = test_font.render('Thank you for playing with Group D', False, 'white')
game_name_rect = game_name.get_rect(center = (400,30))
game_message = test_font.render("Press space to play", False, 'white')
game_message_rect = game_message.get_rect(center = (400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            #Add keyboard input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 328:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 328:
                    game_active = True
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if game_active:
            #Obstacle timer
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 341)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 210)))
            
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]





    if game_active:
        #Set background_surface
        screen.blit(background_surface, (0,0))
        
        #Score
        #set text
        # pygame.draw.rect(screen, 'Pink', score_rect)
        score = display_score()

        #Set player_surface
        #Change player size
        # newImage = pygame.transform.scale(player_surface, (x,y))
        original_midbottom = player_rect.midbottom 
        player_surface_scaled = pygame.transform.scale(player_surface, (x, y))
        player_rect = player_surface_scaled.get_rect(midbottom=original_midbottom)  # Update rect
        
        #Add Player gravity
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 349:
            player_rect.bottom = 349
        player_animation()
        screen.blit(player_surface_scaled, player_rect)
        
        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        # if snail_rect.colliderect(player_rect):
        #     game_active = False
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        #Game over screen
        screen.fill((50,174,226))
        logo_scaled = pygame.transform.scale(logo, (200, 100))
        screen.blit(logo_scaled, logo_rect)
        screen.blit(game_name, game_name_rect)
        obstacle_rect_list.clear()

        #Display score
        score_message = test_font.render(f'Your Score: {score}', False, 'white')
        score_message_rect = score_message.get_rect(center=(400, 300))
       
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)