import pygame, random
from os.path import isfile, join

pygame.init()
pygame.display.set_caption("Platformer")

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.y = 300
        self.speed = 8
        self.image = pygame.image.load('assets/Background/Onepunch.png')
        self.image = pygame.transform.scale(self.image, (100, 20))
        self.rect = self.image.get_rect(center=(x, 300))

    def update(self):
        x, _ = pygame.mouse.get_pos()
        self.x = x
        self.rect.center = (self.x, self.y)

#screen size
WIDTH, HEIGHT= 1000, 800
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodge the Blocks!')
clock = pygame.time.Clock()

paddle_group = pygame.sprite.Group()
paddle = Paddle(WIDTH / 2)
paddle_group.add(paddle)

#background
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

#draw background
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

def main(window):

    clock = pygame.time.Clock()

    #background
    background, bg_image = get_background("Blue.png")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #draw
        paddle_group.draw(window)
        pygame.display.update()

        #update
        paddle_group.update()

        #call draw function
        draw(window, background, bg_image)

    pygame.quit()

if __name__ == "__main__":
    main(window)
