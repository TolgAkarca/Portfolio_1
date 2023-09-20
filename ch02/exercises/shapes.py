import pygame
pygame.init()
while True:
    for event in pygame.event.get():
        pass
    screen = pygame.display.set_mode()
    screen.fill('lightblue')
    pygame.draw.circle(screen, 'red ', (800,100), 50)
    pygame.draw.circle(screen, 'white', (800,250), 100)
    pygame.draw.circle(screen, 'red', (800,500), 150)
    pygame.display.flip()
    pygame.time.wait(200)
    break

