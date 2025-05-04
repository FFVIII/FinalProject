import pygame
from random import randint, choice
from sys import exit
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.transform.scale(pygame.image.load("assets/mario/mario1.png").convert_alpha(),(55, 55))
        player_walk2 = pygame.transform.scale(pygame.image.load("assets/mario/mario2.png").convert_alpha(),(55, 55))
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.transform.scale(pygame.image.load("assets/mario/mario3.png").convert_alpha(),(55,55,))

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(topright = (100,330))
        self.gravity = 0

    #Add Player input
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 330:
            self.gravity = -20

    #Add Play gravity
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 349:
            self.rect.bottom = 349

    #Add animation state
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly_frame1 = pygame.transform.scale(pygame.image.load('assets/fly/aa1.png').convert_alpha(), (45,45))
            fly_frame2 = pygame.transform.scale(pygame.image.load('assets/fly/aa2.png').convert_alpha(), (45,45))
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load("assets/snail/snail1.png").convert_alpha()
            snail_frame_2 = pygame.image.load("assets/snail/snail2.png").convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 341

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomright = (random.randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= 8
        self.destory()

    def destory(self):
        if self.rect.x <= -100:
            self.kill()

# #Add Score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}',False,'white')
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    return current_time

# #Obstacles movement 
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 7

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

def collisions_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True

pygame.init()

#display surface - window the player is going to see in the end						
screen = pygame.display.set_mode((800, 400))

#Set title
pygame.display.set_caption('Group D: Final Project')

#Font setup
test_font = pygame.font.Font('assets/fonts/Pixeltype.ttf', 50)  

#Set FPS
clock = pygame.time.Clock()

#game active
game_active = False
start_time = 0
score = 0

#OOP
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Add background
background_surface = pygame.image.load("assets/Background/bg.jpg")

# Add snail
snail_frame_1 = pygame.image.load("assets/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("assets/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

# Add fly
fly_frame1 = pygame.image.load('assets/fly/aa1.png').convert_alpha()
fly_frame2 = pygame.image.load('assets/fly/aa2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

#Game over logo
logo = pygame.image.load('assets/Background/logo.png').convert_alpha()
logo_rect = logo.get_rect(center = (590,250))
game_name = test_font.render('Group D Project', False, 'white')
game_name_rect = game_name.get_rect(center = (400,50))
game_message = test_font.render("Press space to play", False, 'white')
game_message_rect = game_message.get_rect(center = (400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_active:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            #Obstacle timer
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','snail', 'snail', 'snail'])))
            else: 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if not game_active:
                        game_active = True
                        start_time = int(pygame.time.get_ticks() / 1000)
              
    if game_active:
        #Set background_surface
        screen.blit(background_surface, (0,0))
        
        #Score
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #collision
        game_active = collisions_sprite()
     
    else:
        #Game over screen
        screen.fill((50,174,226))
        logo_scaled = pygame.transform.scale(logo, (200, 100))
        screen.blit(logo_scaled, logo_rect)
        screen.blit(game_name, game_name_rect)

        #Display score
        score_message = test_font.render(f'Your Score: {score}', False, 'white')
        score_message_rect = score_message.get_rect(center=(400, 300))
       
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)