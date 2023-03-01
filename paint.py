import pygame

# pygame.init()
(width, height) = (1000, 800)

screen = pygame.display.set_mode((width, height))

pygame.display.flip()

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        x,y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255,255,255), (x,y) ,20)
        pygame.display.update()
        

# pygame.update();