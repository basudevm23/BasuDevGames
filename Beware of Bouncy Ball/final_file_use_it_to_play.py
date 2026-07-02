import pygame
from random import randint

# Creating a PLayer Object and Defining Player Motion Control
# in computer screen, positive is in the bottom direction

# Initializing pygame over here
pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

font = pygame.font.Font('PixelifySans-Bold.ttf', 30)
fontnew = pygame.font.Font('PixelifySans-Bold.ttf', 40)
fonthehe = pygame.font.Font('PixelifySans-Bold.ttf', 28)
fontnewnew = pygame.font.Font('PixelifySans-Bold.ttf', 20)
score = 0
timer = pygame.time.Clock()
framerate = 60

pygame.display.set_caption("Beware of Bouncy Ball")

# Really wanted to go retro; wanted out pixels
background_raw = pygame.image.load("myimagegame.png").convert()
# scaling my background image which I got from the internet
background_setup = pygame.transform.scale(background_raw, ((WINDOW_WIDTH, WINDOW_HEIGHT))) 

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
orange = (255, 165, 0)

black = (0, 0, 0)
white = (255, 255, 255)
golden = (240, 220, 0)

# Initial postion of the player
player_x = 300
player_y = 500

# Dimensions of the player
player_height = 39
player_width = 39

# Speed and direction of the player
player_speed = 6
player_direction_x= 0
player_direction_y = 0

previous_score = 0
high_score = 0
# The following defines the postions of the villain (antagonist)
pos_x = 500
pos_y = 30
# Till the ball catches you, it is game on
gameover = False

# This is how the ball will move and have velocity
pos_x_update = 2
pos_y_update = 3

my_colour = (65, 65, 65)

# these for speed boosting functions, the boost is  out of the screen, till its time comes
speedx = -100
speedy = -100

speedboostavailable = False
last_when_grabbed = 0

def speed_boosting_function():
    global speedx
    global speedy
    global speedboostavailable 
    global score
    global player_speed
    global last_when_grabbed

    if score - last_when_grabbed > 6 and not speedboostavailable:
        speedx = randint(0, 450)
        speedy = randint(0, 450)
        speedboostavailable = True
        
def check_difficulty_function():
    global score
    global pos_x_update
    global pos_y_update
    x_mod = (score//12)
    y_mod = (score//13)

# Increase its speed as the difficulty rises
    if pos_x_update>0:
        pos_x_update = 2 + x_mod
    elif pos_x_update<0:
        pos_x_update = -2 - x_mod
        
    if pos_y_update >0:
        pos_y_update = 3 + y_mod
    elif pos_y_update<0:
        pos_y_update = -3 -y_mod

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
    # display_counter_final= fontnew.render("Go Home Baby..", True, my_colour, white)
    display_value_final = font.render("Your Score: " + str(score), True, white)
    # screen.blit(display_counter_final, (150, 300))
    display_restart = fontnewnew.render("To keep playing, hit your SPACEBAR!!", True,golden)
    current_time = pygame.time.get_ticks()
    if current_time//1000 % 2 ==0:
        screen.blit(display_restart, (130, 285))

    screen.blit(display_value_final, (210, 320))
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
    # Keep running, the loop keeps running
while running:
    timer.tick(framerate)
    update_ball_position()

    update_player_position()
    check_difficulty_function()

    speed_boosting_function()
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
                speedx = -100
                speedy = -100
                player_speed = 5
                speedboostavailable = False
                last_when_grabbed = 0                
                gameover = False

    # screen.fill(blue)
    screen.blit(background_setup, (0, 0))    
    pygame.draw.circle(screen, red, (pos_x, pos_y), 20, 5)
    ball = pygame.draw.circle(screen, green, (pos_x, pos_y), 15)
    player = pygame.draw.rect(screen, orange, [player_x, player_y, player_width, player_height])
    
    collision_happened(player.centerx, player.centery, ball.centerx, ball.centery)

    display_counter = fonthehe.render("Score: "+ str(score), True, white)
    screen.blit(display_counter, (10, 10))

    # display_counter_prev = fonthehe.render("Previous Score: "+ str(previous_score), True, white)
    # screen.blit(display_counter_prev, (10, 40))

    display_counter = fonthehe.render("High Score: "+ str(high_score), True, white)
    screen.blit(display_counter, (10, 45))

    if speedboostavailable:
        boost = pygame.draw.rect(screen, white, [speedx, speedy, 20, 20])
        if player.colliderect(boost):
            speedx = -100
            speedy = -100
            player_speed = player_speed + 1
            last_when_grabbed = score
            speedboostavailable = False

    speed_counter = font.render("Speed: "+ str(player_speed-4), True, white)
    screen.blit(speed_counter, (465, 20))

    pygame.display.flip() ### for putting it onto the screen

pygame.quit()


