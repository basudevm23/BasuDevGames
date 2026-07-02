import pygame

# trying to create a scoring system
# i switched off three statements for the auto completes here in vscode
# and also switched off music which disturbed me 

pygame.init()
screen = pygame.display.set_mode((600, 600))

font = pygame.font.Font('freesansbold.ttf', 20)
score = 0
timer = pygame.time.Clock()
framerate = 60

pygame.display.set_caption("Bouncy Ball Game")
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

black = (0, 0, 0)
white = (255, 255, 255)



pos_x = 500
pos_y = 30

pos_x_update = 8
pos_y_update = 9

my_fucking_colour = (69, 69, 69)

def update_ball_position():

    global pos_x
    global pos_y, pos_x_update, pos_y_update
    global score

    if  pos_x_update > 0:
        if pos_x < 580:
            pos_x = pos_x + pos_x_update

        else:
            pos_x_update = -1*pos_x_update
            score = score +1
    elif pos_x_update < 0:
        if pos_x > 20:
            pos_x = pos_x + pos_x_update
        else:
            pos_x_update = -1*pos_x_update
            score = score + 1

    if  pos_y_update > 0:
        if pos_y < 580:
            pos_y = pos_y + pos_y_update

        else:
            pos_y_update = -1*pos_y_update
            score = score+2
    elif pos_y_update < 0:
        if pos_y > 20:
            pos_y = pos_y + pos_y_update
        else:
            pos_y_update = -1*pos_y_update 
            score = score + 2         
       
running = True
    
while running:
    timer.tick(framerate)
    update_ball_position()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    screen.fill(blue)

    pygame.draw.circle(screen, red, (pos_x, pos_y), 30, 5)
    pygame.draw.circle(screen, green, (pos_x, pos_y), 15)
    
    display_counter = font.render("Score: "+ str(score), True, white, black)
    screen.blit(display_counter, (10, 10))

    pygame.display.flip() ### for putting it onto the screen

pygame.quit()


