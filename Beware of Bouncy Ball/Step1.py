import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Basudev is in the house, hi you!")
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

my_fucking_colour = (69, 69, 69)

running = True
counter = 0 
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(my_fucking_colour)

        pygame.draw.polygon(screen, red, ((100, 100), (200, 100), (150, 50), (69, 382)))

        pygame.display.flip() ### for putting it onto the screen

pygame.quit()


