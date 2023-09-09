# Example file showing a basic pygame "game loop"
import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_TITLE = "mapPy"

# pygame setup
pygame.init()
pygame.display.set_caption(f'Welcome to {GAME_TITLE}')
icon = pygame.image.load("assets/intro_ball.gif")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
running = True

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Window visual render happens here
    screen.fill("white")
    map = pygame.image.load("assets/world-map.png")
    scaledMap = pygame.transform.scale(map, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(scaledMap, (0, 0))
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
