# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

img = pygame.image.load('TestGameIcon.png')
pygame.display.set_icon(img)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "green", player_pos2, 40)

    keys = pygame.key.get_pressed()

    # the controls for the red
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    # the controls for the green
    if keys[pygame.K_UP]:
        player_pos2.y-= 300 *dt
    if keys[pygame.K_LEFT]:
        player_pos2.x-= 300 *dt
    if keys[pygame.K_DOWN]:
        player_pos2.y+= 300 *dt
    if keys[pygame.K_RIGHT]:
        player_pos2.x+= 300 *dt



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120) / 1000

pygame.quit()

35
40 
29
11
4
4r+6p
16r + 24p
\
4 pinks
7 whites (printer paper?)
2 reds
