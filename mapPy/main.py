# Example file showing a basic pygame "game loop"
import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    map = pygame.image.load("assets/world-map.png")
    scaledMap = pygame.transform.scale(map, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(scaledMap, (0, 0))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
