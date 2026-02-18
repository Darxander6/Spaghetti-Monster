# Example file showing a basic pygame "game loop"
import pygame
# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.transform.scale(pygame.image.load("space.png"),(800,600))
screen.blit(background, (0, 0))
clock = pygame.time.Clock()
running = True
Monster = pygame.transform.scale(pygame.image.load("frame_7.png"),(100,100))
x=400
y=300
frameCounter = 0
prev_mouse_pos = pygame.mouse.get_pos()
Movingwidth = 200
Movinghieght = 200
hieght=100
width=100
movingxadd = 0
movingyadd = 0
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                Movingwidth += 20
                Movinghieght += 20
                hieght += 10
                width += 10
                
                movingyadd -= 5
                movingxadd -= 5
            elif event.button == 3:  # Right mouse button
                Movingwidth -= 20
                Movinghieght -= 20
                hieght -= 10
                width -= 10
                
                movingyadd += 5
                movingxadd+= 5
       
        
    
    current_mouse_pos = pygame.mouse.get_pos()
    Mouse_moving = current_mouse_pos != prev_mouse_pos
    prev_mouse_pos = current_mouse_pos
    frame = pygame.image.load("frame_15.png").convert_alpha()
    
    screen.blit(background, (0, 0))
    if Mouse_moving:
        frameCounter = (frameCounter + 1) % 20
        Monster = pygame.transform.scale(pygame.image.load(f"frame_{frameCounter}.png"),(Movingwidth,Movinghieght))
        screen.blit(Monster, (x-50+movingxadd, y-50+movingyadd))
    else:
        Monster = pygame.transform.scale(pygame.image.load("Monster.png"),(width,hieght))
        screen.blit(Monster, (x, y))





        
    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()