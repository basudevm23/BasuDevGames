import pygame

# Creating a PLayer Object and Defining Player Motion Control
# in computer screen, negative is in the bottom direction

pygame.init()
screen = pygame.display.set_mode((600, 600))

font = pygame.font.Font('freesansbold.ttf', 20)
fontnew = pygame.font.Font('freesansbold.ttf', 40)
score = 0
timer = pygame.time.Clock()
framerate = 60

pygame.display.set_caption("Bouncy Ball Game")
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
orange = (255, 165, 0)

black = (0, 0, 0)
white = (255, 255, 255)

player_x = 300
player_y = 500

player_height = 20
player_width = 30

player_speed = 5
player_direction_x= 0
player_direction_y = 0
previous_score = 0
high_score = 0
pos_x = 500
pos_y = 30
gameover = False

pos_x_update = 8
pos_y_update = 9

my_fucking_colour = (69, 69, 69)

def collision_happened(player_x, player_y, ball_x, ball_y):
    

    if abs(player_x - ball_x) < 40 and abs(player_y - ball_y ) < 30:
        global player_direction_x 
        global player_direction_y
        global pos_x_update
        global pos_y_update
        player_direction_x  = 0
        player_direction_y = 0
        pos_x_update = 0
        pos_y_update = 0
        game_over_function()  
    

def game_over_function():
    global gameover
    display_counter_final= fontnew.render("Go Home Baby..", True, my_fucking_colour, white)
    display_value_final = font.render("Final Score: " + str(score), True, red, green)
    screen.blit(display_counter_final, (150, 300))
    display_restart = font.render("Click on space and enjoy", True, my_fucking_colour, green)
    screen.blit(display_restart, (60, 265))
    screen.blit(display_value_final, (240, 265))
    gameover=True

def update_player_position():
    global player_x, player_y
    if player_direction_x>0:
        if player_x < 600 - player_width:
            player_x = player_x + player_speed*player_direction_x
    if player_direction_x<0:
        if player_x > 0:
            player_x += player_speed*player_direction_x

    if player_direction_y>0:
        if player_y < 600 - player_height:
            player_y = player_y + player_speed*player_direction_y
    if player_direction_y<0:
        if player_y > 0:
            player_y += player_speed*player_direction_y
    

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

    update_player_position()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_direction_y = 1
                            
            if event.key== pygame.K_UP:
                player_direction_y= -1
            
            if event.key == pygame.K_LEFT:
                player_direction_x =-1
            
            if event.key == pygame.K_RIGHT:
                player_direction_x = 1
        # IF WE DONT DO THE FOLLOWING, THE AGENT WILL KEEP ON SLIDING
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_DOWN:
                player_direction_y = 0
                            
            if event.key== pygame.K_UP:
                player_direction_y= 0
            
            if event.key== pygame.K_LEFT:
                player_direction_x = 0
            
            if event.key== pygame.K_RIGHT:
                player_direction_x = 0
            if event.key == pygame.K_SPACE and gameover:
                pos_x = 500
                pos_y = 30
                pos_x_update = 8
                pos_y_update = 9
                player_x = 300
                player_y = 500
                previous_score = score
                if previous_score > high_score:
                    high_score = previous_score
                score = 0

                gameover = False


                

    screen.fill(blue)
    
    pygame.draw.circle(screen, red, (pos_x, pos_y), 20, 5)
    ball = pygame.draw.circle(screen, green, (pos_x, pos_y), 15)
    player = pygame.draw.rect(screen, orange, [player_x, player_y, player_width, player_height])

    
    collision_happened(player.centerx, player.centery, ball.centerx, ball.centery)

    display_counter = font.render("Score: "+ str(score), True, white, black)
    screen.blit(display_counter, (10, 10))

    display_counter_prev = font.render("Previous Score: "+ str(previous_score), True, white, black)
    screen.blit(display_counter_prev, (10, 20))

    display_counter = font.render("High Score: "+ str(high_score), True, white, black)
    screen.blit(display_counter, (10, 30))

    pygame.display.flip() ### for putting it onto the screen

pygame.quit()


