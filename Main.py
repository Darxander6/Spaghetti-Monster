# Example file showing a basic pygame "game loop"
import pygame
from PIL import Image
# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.transform.scale(pygame.image.load("space.png"),(800,600))
screen.blit(background, (0, 0))
clock = pygame.time.Clock()
running = True
Monster = pygame.transform.scale(pygame.image.load("monster.png"),(100,100))
x=400
y=300
frameCounter = 0

frames = [pygame.image.load(f"frame_{i}.png").convert_alpha() for i in range(20)]
prev_mouse_pos = pygame.mouse.get_pos()
while running:
    Mouse_moving = False
    
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
    current_mouse_pos = pygame.mouse.get_pos()
    Mouse_moving = current_mouse_pos != prev_mouse_pos
    prev_mouse_pos = current_mouse_pos
    frame = pygame.image.load("Monster.png").convert_alpha()
    screen.blit(background, (0, 0))
    screen.blit(frame, (x, y))
  
      
    #if Mouse_moving:
        #frameCounter = (frameCounter + 1) % 20
        #frame = frames[frameCounter]
     #screen.blit(frame, (x, y))
     #print("Mouse is moving")

        
    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()