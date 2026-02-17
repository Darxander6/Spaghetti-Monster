# Example file showing a basic pygame "game loop"
import pygame
# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.transform.scale(pygame.image.load("space.png"),(800,600))
screen.blit(background, (0, 0))
clock = pygame.time.Clock()
running = True
Monster = pygame.transform.scale(pygame.image.load("monster.png"),(100,100))
Monster_Dancing = pygame.transform.scale(pygame.image.load("spaghetti_monster_dance.gif"),(100,100))
x=400
y=300
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_DOWN:
                y += 10
        if event.type == pygame.MOUSEMOTION:
            screen.blit(background, (0, 0))
            screen.blit(Monster_Dancing, (x, y))
        else:
            screen.blit(background, (0, 0))

            screen.blit(Monster, (x, y))
    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()