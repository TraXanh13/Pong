import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up main window
screenWidth = 1200
screenHeight = 700
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #updating the window
    pygame.display.flip()
    clock.tick(60)